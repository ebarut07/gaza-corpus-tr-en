"""Sputnik scraper.

Kaynak yapısı (pilot/00_pilot_scraping_raporu.md Bölüm 2.1'de doğrulandı):
    - EN: sputnikglobe.com/YYYYMMDD/        — günlük arşiv listesi
    - TR: anlatilaninotesi.com.tr/YYYYMMDD/ — günlük arşiv listesi
    - İçerik statik HTML

Strateji:
    1. Tarih aralığındaki her gün için arşiv sayfasını fetch et
    2. Sayfadaki tüm article linklerini topla
    3. Linkin metnindeki/başlığındaki keyword'lere göre ön ele
    4. Geçenler fetch + parse + topic re-check + save
"""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import Iterable
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from scrapers.base import Article, BaseScraper
from utils.html_cleaner import extract_text, make_soup, strip_noise

logger = logging.getLogger("gazze_korpus")

DOMAINS = {
    "en": "https://sputnikglobe.com",
    "tr": "https://anlatilaninotesi.com.tr",
}


class SputnikScraper(BaseScraper):
    """Sputnik scraper.

    Dil seçimi:
        - Türkiye lokal Python erişimi: yalnızca TR (anlatilaninotesi.com.tr).
        - GitHub Actions Microsoft-hosted runner (TR dışı IP): EN
          (sputnikglobe.com — Türkiye'de RTÜK SNI bloğu vardır).

    Hangi dil(ler)in işleneceği `langs` constructor parametresi ile belirlenir;
    main.py registry'de iki ayrı kaynak adı altında kayıtlı:
        - "sputnik"    -> SputnikScraper(langs=["tr"])     # lokal default
        - "sputnik_en" -> SputnikScraper(langs=["en"])     # GitHub Actions
    """

    name = "sputnik"

    def __init__(self, *args, langs: list[str] | None = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.langs = list(langs) if langs else ["tr"]
        # Birden fazla "sputnik" kaynağı aynı oturumda farklı dillerle
        # çalışırsa checkpoint'in karışmaması için isim ekini ayarla:
        if self.langs == ["en"]:
            self.name = "sputnik_en"

    def expected_langs(self) -> list[str]:
        """Sputnik tek dil modu (TR lokal veya EN GitHub Actions)."""
        return list(self.langs)

    def discover_urls(self) -> Iterable[tuple[str, str, str, str, str]]:
        """Yalnızca self.langs içindeki diller için günlük arşiv yield eder."""
        start = date.fromisoformat(self.config["date_range"]["start"])
        end = date.fromisoformat(self.config["date_range"]["end"])

        cursor = start
        while cursor <= end:
            for lang in self.langs:
                yield from self._urls_for_day(cursor, lang)
            cursor += timedelta(days=1)

    def _urls_for_day(
        self, day: date, lang: str
    ) -> Iterable[tuple[str, str, str, str, str]]:
        """Tek gün için arşiv sayfasından makale linklerini yield eder."""
        archive_url = f"{DOMAINS[lang]}/{day.strftime('%Y%m%d')}/"
        html = self.fetch(archive_url)
        if html is None:
            logger.warning("[sputnik] arşiv erişilemez: %s", archive_url)
            return

        soup = make_soup(html)
        seen: set[str] = set()
        date_iso = day.strftime("%Y-%m-%d")

        for anchor in soup.find_all("a", href=True):
            href = anchor["href"]
            if not href:
                continue
            full_url = urljoin(DOMAINS[lang], href)

            # Yalnızca o günün makaleleri (URL'de /YYYYMMDD/ var)
            day_segment = f"/{day.strftime('%Y%m%d')}/"
            if day_segment not in full_url:
                continue
            # Arşiv kök URL'si (sonu /YYYYMMDD/) makale değil
            if full_url.rstrip("/").endswith(day.strftime("%Y%m%d")):
                continue
            # Aynı URL iki kez listelenmesin
            if full_url in seen:
                continue
            seen.add(full_url)

            # Anchor metni başlık adayı (varsa)
            title_text = anchor.get_text(strip=True) or ""

            yield full_url, lang, "daily_archive", title_text, date_iso

    # ------------------------------------------------------------------

    def parse(self, url: str, html: str, lang: str) -> Article | None:
        """Sputnik makale HTML'inden Article üretir."""
        soup = make_soup(html)

        # 1. Başlık
        title = self._extract_title(soup)
        if not title:
            return None

        # 2. Tarih (URL'den /YYYYMMDD/)
        date_iso, date_full = self._extract_date(url, soup)

        # 3. Yazar (varsa)
        author = self._extract_author(soup)

        # 4. Etiketler (varsa)
        tags = self._extract_tags(soup)

        # 5. Gövde
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
        # Önce <h1>, sonra og:title meta
        h1 = soup.find("h1")
        if h1:
            text = h1.get_text(strip=True)
            if text:
                return text
        meta = soup.find("meta", property="og:title")
        if meta and meta.get("content"):
            return meta["content"].strip()
        if soup.title:
            return soup.title.get_text(strip=True)
        return ""

    def _extract_date(self, url: str, soup: BeautifulSoup) -> tuple[str, str]:
        # URL'den /YYYYMMDD/
        import re

        m = re.search(r"/(\d{4})(\d{2})(\d{2})/", url)
        if m:
            y, mo, d = m.groups()
            iso_date = f"{y}-{mo}-{d}"
        else:
            iso_date = ""

        # Tam timestamp: meta tag
        for prop in ("article:published_time", "og:article:published_time"):
            meta = soup.find("meta", property=prop)
            if meta and meta.get("content"):
                return iso_date or meta["content"][:10], meta["content"]

        return iso_date, iso_date

    def _extract_author(self, soup: BeautifulSoup) -> str:
        meta = soup.find("meta", attrs={"name": "author"})
        if meta and meta.get("content"):
            return meta["content"].strip()
        # alternatif: byline class
        byline = soup.find(class_=lambda c: c and "author" in c.lower())
        if byline:
            return byline.get_text(strip=True)[:200]
        return ""

    def _extract_tags(self, soup: BeautifulSoup) -> list[str]:
        tags: list[str] = []
        meta = soup.find("meta", attrs={"name": "keywords"})
        if meta and meta.get("content"):
            tags.extend([t.strip() for t in meta["content"].split(",") if t.strip()])
        return tags[:30]  # üst sınır

    def _extract_body(self, soup: BeautifulSoup) -> str:
        # Sputnik makale gövdesi tipik olarak <div class="article__text"> içinde
        candidates = [
            ("div", {"class": lambda c: c and "article__text" in " ".join(c if isinstance(c, list) else [c])}),
            ("div", {"class": lambda c: c and "article__body" in " ".join(c if isinstance(c, list) else [c])}),
            ("article", {}),
            ("main", {}),
        ]
        for tag, attrs in candidates:
            node = soup.find(tag, attrs=attrs) if attrs else soup.find(tag)
            if node:
                strip_noise(node)
                text = extract_text(node)
                if text and len(text.split()) >= 50:
                    return text
        # Son çare: tüm body
        if soup.body:
            strip_noise(soup.body)
            return extract_text(soup.body)
        return ""
