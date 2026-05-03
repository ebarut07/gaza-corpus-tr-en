"""Anadolu Ajansı (AA) scraper.

Pilot raporu (Bölüm 6) yöntemi:
    1. GDELT API ile 7 günlük bloklar halinde URL keşfi
       query: domain:aa.com.tr + topic_keyword
    2. Çekilen URL'leri doğrudan AA'dan fetch et
    3. Path çeşitliliği: /tr/dunya/, /tr/politika/, /tr/ortadogu/, /en/middle-east/...
    4. Min. 200 kelime (BaseScraper'da uygulanıyor) — kısa breaking news nav-HTML sorunu
"""
from __future__ import annotations

import logging
import re
from datetime import date
from typing import Iterable

from bs4 import BeautifulSoup

from scrapers.base import Article, BaseScraper
from utils.html_cleaner import extract_text, make_soup, strip_noise
from utils.url_collector import daterange_blocks, gdelt_search, parse_seendate

logger = logging.getLogger("gazze_korpus")

GDELT_BLOCK_DAYS = 7
GDELT_KEYWORDS_EN = ["gaza", "hamas", "israel", "palestine", "rafah"]
GDELT_KEYWORDS_TR = ["gazze", "hamas", "israil", "filistin", "refah"]


class AAScraper(BaseScraper):
    name = "aa"

    def discover_urls(self) -> Iterable[tuple[str, str, str, str, str]]:
        """GDELT API üzerinden URL keşfi (7 günlük bloklar)."""
        start = date.fromisoformat(self.config["date_range"]["start"])
        end = date.fromisoformat(self.config["date_range"]["end"])
        gdelt_delay = self.config["http"]["gdelt_rate_limit"]

        for block_start, block_end in daterange_blocks(start, end, GDELT_BLOCK_DAYS):
            # EN sorgusu
            en_results = gdelt_search(
                domain="aa.com.tr",
                keywords=GDELT_KEYWORDS_EN,
                start_dt=block_start,
                end_dt=block_end,
                session=self.session,
                rate_delay=gdelt_delay,
            )
            for record in en_results:
                url = record["url"]
                lang = self._classify_lang(url, record.get("language", ""))
                if lang != "en":
                    continue
                seen_dt = parse_seendate(record.get("seendate", ""))
                date_iso = seen_dt.strftime("%Y-%m-%d") if seen_dt else ""
                yield url, "en", "gdelt", record.get("title", ""), date_iso

            # TR sorgusu
            tr_results = gdelt_search(
                domain="aa.com.tr",
                keywords=GDELT_KEYWORDS_TR,
                start_dt=block_start,
                end_dt=block_end,
                session=self.session,
                rate_delay=gdelt_delay,
            )
            for record in tr_results:
                url = record["url"]
                lang = self._classify_lang(url, record.get("language", ""))
                if lang != "tr":
                    continue
                seen_dt = parse_seendate(record.get("seendate", ""))
                date_iso = seen_dt.strftime("%Y-%m-%d") if seen_dt else ""
                yield url, "tr", "gdelt", record.get("title", ""), date_iso

    @staticmethod
    def _classify_lang(url: str, gdelt_lang: str) -> str:
        """URL path'inden veya GDELT'in dil tahmininden dil belirler."""
        if "/en/" in url or "aa.com.tr/en" in url:
            return "en"
        if "/tr/" in url or url.startswith("https://www.aa.com.tr/tr"):
            return "tr"
        # GDELT bazen language alanını döndürür
        gl = (gdelt_lang or "").lower()
        if "turkish" in gl:
            return "tr"
        if "english" in gl:
            return "en"
        return "unknown"

    # ------------------------------------------------------------------

    def parse(self, url: str, html: str, lang: str) -> Article | None:
        """AA makale HTML'inden Article üretir."""
        soup = make_soup(html)

        title = self._extract_title(soup)
        if not title:
            return None

        date_iso, date_full = self._extract_date(soup)
        author = self._extract_author(soup)
        tags = self._extract_tags(soup)
        body = self._extract_body(soup)
        if not body:
            return None

        return Article(
            kaynak=self.name,
            dil=lang,
            url=url,
            tarih=date_iso,
            tarih_tam=date_full,
            baslik=title,
            metin=body,
            yazar=author,
            etiketler=tags,
        )

    # ---- parser yardımcıları ----

    def _extract_title(self, soup: BeautifulSoup) -> str:
        # AA: önce h1.detay-baslik, sonra og:title
        h1 = soup.find("h1", class_=re.compile("detay-baslik|title", re.I))
        if h1:
            text = h1.get_text(strip=True)
            if text:
                return text
        h1 = soup.find("h1")
        if h1:
            text = h1.get_text(strip=True)
            if text:
                return text
        meta = soup.find("meta", property="og:title")
        if meta and meta.get("content"):
            return meta["content"].strip()
        return ""

    def _extract_date(self, soup: BeautifulSoup) -> tuple[str, str]:
        # AA özelliği: published_time YOK, modified_time mevcut.
        # modified_time published_time ile pratik olarak aynıdır (kısa süre farkı).
        for prop in (
            "article:published_time",
            "og:article:published_time",
            "article:modified_time",       # AA gerçekte bunu kullanıyor
            "og:article:modified_time",
        ):
            meta = soup.find("meta", property=prop)
            if meta and meta.get("content"):
                content = meta["content"]
                return content[:10], content
        time_tag = soup.find("time")
        if time_tag and time_tag.get("datetime"):
            content = time_tag["datetime"]
            return content[:10], content
        return "", ""

    def _extract_author(self, soup: BeautifulSoup) -> str:
        # AA muhabir adı
        author_meta = soup.find("meta", attrs={"name": "author"})
        if author_meta and author_meta.get("content"):
            return author_meta["content"].strip()
        muhabir = soup.find(class_=re.compile("muhabir|author", re.I))
        if muhabir:
            return muhabir.get_text(strip=True)[:200]
        return ""

    def _extract_tags(self, soup: BeautifulSoup) -> list[str]:
        tags: list[str] = []
        meta = soup.find("meta", attrs={"name": "keywords"})
        if meta and meta.get("content"):
            tags.extend([t.strip() for t in meta["content"].split(",") if t.strip()])
        return tags[:30]

    def _extract_body(self, soup: BeautifulSoup) -> str:
        # AA Tailwind tabanlı yeni tasarım kullanıyor: gerçek gövde paragrafları
        # `embed-responsive prose ...` class'lı div içindedir. Eski selector'lar
        # (detay-icerik vb.) ya yok ya yanlış div'i (medya slider) seçiyor.
        candidates = [
            # Yeni AA tasarımı (2024+) — birincil hedef
            ("div", {"class": re.compile(r"\bembed-responsive\b.*\bprose\b", re.I)}),
            ("div", {"class": re.compile(r"\bprose\b", re.I)}),
            # Eski AA varyasyonları (yedek)
            ("div", {"class": re.compile("detay-icerik|detay-content|article-text", re.I)}),
            ("article", {}),
            ("main", {}),
        ]
        # AA için ek temizleme pattern'ları:
        # - "relatednews" / "related" → bg-relatedNewsBackground (alt haberler kutusu)
        # - "footer" / "newsletter" / "subscribe" → DEFAULT_STRIP_SUBSTRINGS'de mevcut
        aa_extras = ("etiket", "tag-", "ilgili", "relatednews", "more-news", "haber-listesi")
        for tag, attrs in candidates:
            node = soup.find(tag, attrs=attrs) if attrs else soup.find(tag)
            if node:
                strip_noise(node, extra_substrings=aa_extras)
                text = extract_text(node)
                if text and len(text.split()) >= 50:
                    return text
        if soup.body:
            strip_noise(soup.body, extra_substrings=aa_extras)
            return extract_text(soup.body)
        return ""
