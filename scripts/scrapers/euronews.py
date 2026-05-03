"""Euronews scraper.

Pilot raporu (Bölüm 2.2) bulguları:
    - Tag pagination çalışıyor (`/tag/<slug>?p=N`)
    - TR Oct 7-15 boşluğu `/tag/hamas` p=22-23 ile kapatılıyor
    - `/video/` URL'leri filtrelenmeli (metin az)
    - hreflang dil linki JS-rendered ama Python requests ile alınabilir
    - Slug dile çevriliyor (EN ve TR URL slug'ları farklı)

Strateji:
    1. Her dil için tag listesinden sayfa sayfa makale URL'leri topla
    2. /video/ URL'lerini ele
    3. Geçenleri fetch + parse + topic re-check + save
    4. Parse aşamasında hreflang meta tag'lerini de yakala (EN-TR eşleşmesi
       sonradan adım 2.4'te kullanılacak — şimdilik ekstra alan olarak loglanır)
"""
from __future__ import annotations

import logging
import re
from datetime import date, datetime
from typing import Iterable
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from scrapers.base import Article, BaseScraper
from utils.html_cleaner import extract_text, make_soup, strip_noise

logger = logging.getLogger("gazze_korpus")

DOMAINS = {
    "en": "https://www.euronews.com",
    "tr": "https://tr.euronews.com",
}

# Tag pagination kaynakları (pilot raporu Bölüm 2.2 + 7)
TAG_SOURCES = {
    "en": [
        ("israel-hamas-war", 90),  # ~86 sayfa pilot, +marj
        ("gaza", 50),
        ("palestine", 50),
    ],
    "tr": [
        ("gazze", 45),
        ("hamas", 30),     # özellikle p=22-23 Oct 7-15 boşluğu için
        ("filistin", 60),
        ("israil", 40),
    ],
}

# URL içinde geçerse atla
URL_BLOCKLIST = ("/video/", "/no-comment/", "/programmes/", "/live/")

# Makale URL formatı: /YYYY/MM/DD/slug
ARTICLE_URL_RE = re.compile(r"/(\d{4})/(\d{2})/(\d{2})/[a-z0-9-]+/?$", re.I)


class EuronewsScraper(BaseScraper):
    name = "euronews"

    def discover_urls(self) -> Iterable[tuple[str, str, str, str, str]]:
        """Her dilin tag sayfalarını dolaşıp makale URL'leri yield eder."""
        start = date.fromisoformat(self.config["date_range"]["start"])
        end = date.fromisoformat(self.config["date_range"]["end"])

        for lang in ("en", "tr"):
            yield from self._urls_for_lang(lang, start, end)

    def _urls_for_lang(
        self, lang: str, start: date, end: date
    ) -> Iterable[tuple[str, str, str, str, str]]:
        seen: set[str] = set()
        base = DOMAINS[lang]

        for tag_slug, max_pages in TAG_SOURCES[lang]:
            for page in range(1, max_pages + 1):
                tag_url = f"{base}/tag/{tag_slug}?p={page}"
                html = self.fetch(tag_url)
                if html is None:
                    logger.warning("[euronews] tag sayfası erişilemez: %s", tag_url)
                    break

                soup = make_soup(html)
                page_urls = self._extract_article_links(soup, base)

                if not page_urls:
                    # bu tag bitti
                    logger.info("[euronews] %s/%s p=%d boş → tag tamamlandı", lang, tag_slug, page)
                    break

                # Bu sayfadaki en eski tarih, başlangıç tarihinden öncesine geçti mi?
                stop_paginating = False
                yielded_in_page = 0

                for url, article_date in page_urls:
                    if url in seen:
                        continue
                    seen.add(url)

                    # tarih aralığı kontrolü
                    if article_date is not None:
                        if article_date < start or article_date > end:
                            if article_date < start:
                                # daha eski → bir sonraki sayfada da daha eski olur
                                stop_paginating = True
                            continue

                    date_iso = article_date.strftime("%Y-%m-%d") if article_date else ""
                    yield url, lang, f"tag:{tag_slug}", "", date_iso
                    yielded_in_page += 1

                if stop_paginating and yielded_in_page == 0:
                    logger.info(
                        "[euronews] %s/%s p=%d tüm haberler tarih aralığından eski — durdur",
                        lang, tag_slug, page,
                    )
                    break

    def _extract_article_links(
        self, soup: BeautifulSoup, base: str
    ) -> list[tuple[str, date | None]]:
        """Tag sayfasından (URL, tarih) listesi çıkarır."""
        results: list[tuple[str, date | None]] = []
        for anchor in soup.find_all("a", href=True):
            href = anchor["href"]
            if not href:
                continue
            if any(bl in href for bl in URL_BLOCKLIST):
                continue
            match = ARTICLE_URL_RE.search(href)
            if not match:
                continue
            full_url = urljoin(base, href).split("#")[0].rstrip("/")
            try:
                article_date = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            except ValueError:
                article_date = None
            results.append((full_url, article_date))
        return results

    # ------------------------------------------------------------------

    def parse(self, url: str, html: str, lang: str) -> Article | None:
        soup = make_soup(html)

        title = self._extract_title(soup)
        if not title:
            return None

        date_iso, date_full = self._extract_date(url, soup)
        author = self._extract_author(soup)
        tags = self._extract_tags(soup)
        body = self._extract_body(soup)
        if not body:
            return None

        # hreflang link'leri etiket olarak da kayıt et (sonra eşleştirmede kullanılacak)
        hreflang = self._extract_hreflang(soup)
        if hreflang:
            tags = list(tags) + [f"hreflang:{ln}={u}" for ln, u in hreflang.items()]

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
        h1 = soup.find("h1")
        if h1:
            text = h1.get_text(strip=True)
            if text:
                return text
        meta = soup.find("meta", property="og:title")
        if meta and meta.get("content"):
            return meta["content"].strip()
        return ""

    def _extract_date(self, url: str, soup: BeautifulSoup) -> tuple[str, str]:
        # URL'den /YYYY/MM/DD/
        m = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
        url_iso = ""
        if m:
            url_iso = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

        for prop in ("article:published_time", "og:article:published_time"):
            meta = soup.find("meta", property=prop)
            if meta and meta.get("content"):
                content = meta["content"]
                return url_iso or content[:10], content
        time_tag = soup.find("time")
        if time_tag and time_tag.get("datetime"):
            return url_iso or time_tag["datetime"][:10], time_tag["datetime"]
        return url_iso, url_iso

    def _extract_author(self, soup: BeautifulSoup) -> str:
        meta = soup.find("meta", attrs={"name": "author"})
        if meta and meta.get("content"):
            return meta["content"].strip()
        return ""

    def _extract_tags(self, soup: BeautifulSoup) -> list[str]:
        tags: list[str] = []
        meta = soup.find("meta", attrs={"name": "keywords"})
        if meta and meta.get("content"):
            tags.extend([t.strip() for t in meta["content"].split(",") if t.strip()])
        return tags[:30]

    def _extract_hreflang(self, soup: BeautifulSoup) -> dict[str, str]:
        """alternate hreflang link'lerini topla — EN-TR eşleştirme için."""
        result: dict[str, str] = {}
        for link in soup.find_all("link", rel="alternate"):
            lang = link.get("hreflang")
            href = link.get("href")
            if lang and href and lang in ("en", "tr", "x-default"):
                result[lang] = href
        return result

    def _extract_body(self, soup: BeautifulSoup) -> str:
        candidates = [
            ("div", {"class": re.compile("c-article-content|article__body|article-content", re.I)}),
            ("article", {}),
            ("main", {}),
        ]
        for tag, attrs in candidates:
            node = soup.find(tag, attrs=attrs) if attrs else soup.find(tag)
            if node:
                strip_noise(node, extra_substrings=("widget", "embed", "ad-"))
                text = extract_text(node)
                if text and len(text.split()) >= 50:
                    return text
        if soup.body:
            strip_noise(soup.body, extra_substrings=("widget", "embed", "ad-"))
            return extract_text(soup.body)
        return ""
