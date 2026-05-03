"""BaseScraper — tüm kaynak scraper'larının ortak temeli.

Sağladığı özellikler:
    - requests.Session() (cookie persistence, bot tespit riskini azaltır)
    - Retry decorator (exponential backoff: config.yaml'dan)
    - Rate limiting (per-source delay)
    - HTML temizleme + metin çıkarma
    - JSON yazımı (atomik write — kısmi dosya riski yok)
    - filtered_out.jsonl ve failed_urls.jsonl yazımı (akademik şeffaflık)
"""
from __future__ import annotations

import json
import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import requests
from tenacity import (
    RetryError,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from utils.checkpoint import Checkpoint
from utils.deduplication import text_hash, url_hash
from utils.html_cleaner import make_soup, word_count
from utils.pair_matching import candidate_pair_id
from utils.topic_filter import TopicFilter

logger = logging.getLogger("gazze_korpus")


@dataclass
class Article:
    """Tek haber için standart şema (config.yaml ile uyumlu)."""

    kaynak: str
    dil: str
    url: str
    tarih: str            # 'YYYY-MM-DD'
    tarih_tam: str        # ISO 8601
    baslik: str
    metin: str
    yazar: str = ""
    etiketler: list[str] = field(default_factory=list)
    scraping_tarihi: str = ""
    scraping_method: str = ""
    candidate_pair_id: str = ""
    kelime_sayisi: int = 0
    metin_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kaynak": self.kaynak,
            "dil": self.dil,
            "url": self.url,
            "tarih": self.tarih,
            "tarih_tam": self.tarih_tam,
            "baslik": self.baslik,
            "metin": self.metin,
            "yazar": self.yazar,
            "etiketler": self.etiketler,
            "scraping_tarihi": self.scraping_tarihi,
            "scraping_method": self.scraping_method,
            "candidate_pair_id": self.candidate_pair_id,
            "kelime_sayisi": self.kelime_sayisi,
            "metin_hash": self.metin_hash,
        }


class BaseScraper(ABC):
    """Tüm kaynak scraper'larının soyut temeli."""

    name: str = ""  # alt sınıf override eder ('aa', 'sputnik', 'euronews')

    def __init__(
        self,
        config: dict[str, Any],
        checkpoint: Checkpoint,
        topic_filter: TopicFilter,
        output_root: Path,
    ) -> None:
        self.config = config
        self.checkpoint = checkpoint
        self.topic_filter = topic_filter
        self.output_root = output_root

        http_cfg = config["http"]
        self.user_agent = http_cfg["user_agent"]
        self.timeout = http_cfg["timeout_seconds"]
        self.retry_attempts = http_cfg["retry_attempts"]
        self.backoff = http_cfg["retry_backoff_seconds"]
        self.rate_delay = http_cfg["rate_limit_per_source"][self.name]

        # Kaynak-spesifik override desteği (config.yaml > source_options).
        # Akademik gerekçe: editoryal stillere göre kalibrasyon (bkz. metodoloji).
        src_opts = config.get("source_options", {}).get(self.name, {})
        self.min_word_count = src_opts.get(
            "min_word_count", config["content"]["min_word_count"]
        )
        self.max_word_count = src_opts.get(
            "max_word_count", config["content"]["max_word_count"]
        )

        self.dry_run: bool = config["runtime"]["dry_run"]
        self.test_mode: bool = config["runtime"]["test_mode"]
        if self.test_mode:
            self.max_articles: int | None = config["runtime"]["max_per_source_test"]
        else:
            self.max_articles = config["runtime"]["max_per_source"]

        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": self.user_agent,
                "Accept-Language": "en;q=0.9,tr;q=0.9,*;q=0.5",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
        )

    # ------------------------------------------------------------------
    # HTTP layer
    # ------------------------------------------------------------------

    def fetch(self, url: str) -> str | None:
        """URL'i fetch eder. Retry başarısızsa None döner.

        Akademik şeffaflık: başarı/hata tüm log'a yazılır.
        """
        try:
            return self._fetch_with_retry(url)
        except RetryError as exc:
            inner = exc.last_attempt.exception() if exc.last_attempt else exc
            logger.error("FETCH FAIL [%s] %s | %s", self.name, url, inner)
            self._record_failure(url, str(inner))
            return None
        except requests.RequestException as exc:
            # tenacity reraise=True → orijinal istisna doğrudan geçebilir
            logger.error("FETCH FAIL [%s] %s | %s", self.name, url, exc)
            self._record_failure(url, str(exc))
            return None
        except Exception as exc:
            # son güvenlik ağı: scraper'ı tek bir URL çökerteme
            logger.exception("FETCH UNEXPECTED [%s] %s | %s", self.name, url, exc)
            self._record_failure(url, f"unexpected: {exc}")
            return None

    @retry(
        retry=retry_if_exception_type((requests.RequestException,)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=5, min=5, max=45),
        reraise=True,
    )
    def _fetch_with_retry(self, url: str) -> str:
        time.sleep(self.rate_delay)
        response = self.session.get(url, timeout=self.timeout)
        if response.status_code == 429:
            logger.warning("Rate-limited (429): %s — 30 sn bekleniyor", url)
            time.sleep(30)
            raise requests.RequestException("HTTP 429 — rate limited")
        if response.status_code >= 400:
            raise requests.RequestException(f"HTTP {response.status_code}")
        # encoding fallback
        if not response.encoding or response.encoding.lower() == "iso-8859-1":
            response.encoding = response.apparent_encoding or "utf-8"
        return response.text

    # ------------------------------------------------------------------
    # Article processing
    # ------------------------------------------------------------------

    def process_article(
        self,
        url: str,
        lang: str,
        scraping_method: str,
        seed_title: str = "",
        seed_date: str = "",
    ) -> Article | None:
        """Tek bir URL'i fetch + parse + filter + save akışından geçirir.

        Returns:
            Başarıyla kaydedilmişse Article; aksi halde None.
        """
        if self.checkpoint.is_processed(self.name, url):
            return None

        # Başlık-bazlı ön filtre (varsa)
        if seed_title:
            pre = self.topic_filter.matches(seed_title, lang)
            if not pre.matched:
                logger.info("[skip-title] %s | %s", self.name, url)
                self._record_filtered(url, lang, reason="title_no_keyword", title=seed_title)
                self.checkpoint.mark_processed(self.name, url, outcome="filtered")
                return None

        html = self.fetch(url)
        if html is None:
            self.checkpoint.mark_processed(self.name, url, outcome="failed")
            return None

        try:
            article = self.parse(url, html, lang)
        except Exception as exc:  # parse hatası loglanır, akış kırılmaz
            logger.exception("PARSE FAIL [%s] %s | %s", self.name, url, exc)
            self._record_failure(url, f"parse error: {exc}")
            self.checkpoint.mark_processed(self.name, url, outcome="failed")
            return None

        if article is None:
            logger.info("[empty] %s | %s", self.name, url)
            self._record_failure(url, "parser returned None")
            self.checkpoint.mark_processed(self.name, url, outcome="failed")
            return None

        # Metin uzunluğu kontrolü
        wc = word_count(article.metin)
        article.kelime_sayisi = wc
        if wc < self.min_word_count:
            logger.info("[skip-short %dw] %s | %s", wc, self.name, url)
            self._record_filtered(url, lang, reason=f"text_too_short ({wc}w)", title=article.baslik)
            self.checkpoint.mark_processed(self.name, url, outcome="filtered")
            return None
        if wc > self.max_word_count:
            logger.info("[skip-long %dw] %s | %s", wc, self.name, url)
            self._record_filtered(url, lang, reason=f"text_too_long ({wc}w)", title=article.baslik)
            self.checkpoint.mark_processed(self.name, url, outcome="filtered")
            return None

        # Metin-bazlı kesin konu filtresi (başlık + ilk 1000 kelime)
        body_sample = " ".join(article.metin.split()[:1000])
        topic = self.topic_filter.matches_any([article.baslik, body_sample], lang)
        if not topic.matched:
            logger.info("[skip-offtopic] %s | %s", self.name, url)
            self._record_filtered(url, lang, reason="text_no_keyword", title=article.baslik)
            self.checkpoint.mark_processed(self.name, url, outcome="filtered")
            return None

        # Metadata tamamla
        # Tarih fallback: parser çıkaramadıysa GDELT/discover'dan gelen seed_date kullan.
        # Bu özellikle AA için önemli — tüm AA URL'leri GDELT'ten seedate ile gelir.
        if not article.tarih and seed_date:
            article.tarih = seed_date[:10]
        if not article.tarih_tam and seed_date:
            article.tarih_tam = seed_date

        article.scraping_tarihi = datetime.now(timezone.utc).isoformat()
        article.scraping_method = scraping_method
        article.candidate_pair_id = candidate_pair_id(self.name, article.tarih, article.baslik)
        article.metin_hash = text_hash(article.metin)

        # Kaydet
        if not self.dry_run:
            self._save_article(article)

        self.checkpoint.mark_processed(self.name, url, outcome="saved")
        logger.info(
            "[saved %s/%s %dw] %s | %s",
            self.name,
            lang,
            wc,
            article.baslik[:60],
            url,
        )
        return article

    # ------------------------------------------------------------------
    # I/O
    # ------------------------------------------------------------------

    def _save_article(self, article: Article) -> None:
        """JSON dosyasını {tarih}_{sira}.json formatında yazar (atomik)."""
        # sputnik_en de fiziksel olarak sputnik/en/ klasörüne yazılır
        physical_source = "sputnik" if self.name == "sputnik_en" else self.name
        out_dir = self.output_root / physical_source / article.dil
        out_dir.mkdir(parents=True, exist_ok=True)

        # benzersiz dosya adı: tarih + URL hash (sıra hesabı race condition yapmaz)
        fname = f"{article.tarih}_{url_hash(article.url)}.json"
        path = out_dir / fname

        tmp = path.with_suffix(".json.tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(article.to_dict(), f, ensure_ascii=False, indent=2)
        tmp.replace(path)

    def _record_filtered(self, url: str, lang: str, reason: str, title: str = "") -> None:
        """Filtrelenmiş URL'leri ayrı log'a yaz (akademik şeffaflık)."""
        path = self.output_root / "filtered_out.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "kaynak": self.name,
            "dil": lang,
            "url": url,
            "baslik": title,
            "sebep": reason,
            "tarih": datetime.now(timezone.utc).isoformat(),
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _record_failure(self, url: str, error: str) -> None:
        """Erişilemeyen URL'leri ayrı log'a yaz."""
        path = self.output_root / "failed_urls.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "kaynak": self.name,
            "url": url,
            "hata": error,
            "tarih": datetime.now(timezone.utc).isoformat(),
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------------
    # Parsing — alt sınıflar implement eder
    # ------------------------------------------------------------------

    @abstractmethod
    def parse(self, url: str, html: str, lang: str) -> Article | None:
        """HTML'den Article nesnesi üretir. Başarısızsa None döner."""

    @abstractmethod
    def discover_urls(self) -> Iterable[tuple[str, str, str, str, str]]:
        """URL keşfi — yield (url, lang, scraping_method, seed_title, seed_date_iso)."""

    def expected_langs(self) -> list[str]:
        """Bu scraper'ın hangi dillerde haber çekebileceğini bildir.

        Test mode'da per-language sayım için kullanılır. Alt sınıflar
        (örn. SputnikScraper TR-only veya EN-only) override edebilir.
        """
        return ["en", "tr"]

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self) -> int:
        """Discovery → process döngüsü. Başarıyla kaydedilen sayıyı döner.

        Test mode'da per-language sayım yapılır:
        her dil için max_per_source_test (config'deki) kadar haber çekilir.
        Tam scraping'de max_per_source toplam üst sınırdır (genelde None).
        """
        logger.info(
            ">>> %s scraper başlıyor (test_mode=%s, langs=%s)",
            self.name, self.test_mode, self.expected_langs(),
        )
        saved_per_lang: dict[str, int] = {}
        expected = set(self.expected_langs())

        # Cap mantığı:
        # - Test mode: max_articles = per-language cap (her dil için ayrı sınır)
        # - Tam scraping: max_articles = toplam cap (genelde None = sınırsız)
        per_lang_cap = self.max_articles if self.test_mode else None
        total_cap = self.max_articles if not self.test_mode else None

        try:
            for url, lang, method, seed_title, seed_date in self.discover_urls():
                # Toplam üst sınır (tam scraping'de manuel limit konursa)
                total_saved = sum(saved_per_lang.values())
                if total_cap is not None and total_saved >= total_cap:
                    logger.info(
                        "[%s] toplam max_per_source (%d) doldu — durdur",
                        self.name, total_cap,
                    )
                    break

                # Per-language cap (test mode)
                if per_lang_cap is not None:
                    if saved_per_lang.get(lang, 0) >= per_lang_cap:
                        # Bu dil dolu — tüm beklenen diller dolduysa kes
                        if all(saved_per_lang.get(l, 0) >= per_lang_cap for l in expected):
                            logger.info(
                                "[%s] tüm dillerde per-lang cap (%d) doldu — durdur",
                                self.name, per_lang_cap,
                            )
                            break
                        # Aksi halde bu URL'i atla, başka dil URL'leri için devam et
                        continue

                article = self.process_article(url, lang, method, seed_title, seed_date)
                if article is not None:
                    saved_per_lang[lang] = saved_per_lang.get(lang, 0) + 1
                    total_saved = sum(saved_per_lang.values())
                    if total_saved % 50 == 0:
                        self.checkpoint.save()
                        logger.info(
                            "[%s] checkpoint kaydedildi (toplam=%d, %s)",
                            self.name, total_saved, dict(saved_per_lang),
                        )
        finally:
            self.checkpoint.save()

        total_saved = sum(saved_per_lang.values())
        logger.info(
            "<<< %s scraper bitti — bu çalıştırmada %d haber (%s)",
            self.name, total_saved, dict(saved_per_lang),
        )
        return total_saved

    # Yardımcı: alt sınıflar tarih ayrıştırması için
    @staticmethod
    def date_iso(value: str | datetime) -> str:
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d")
        return value[:10]
