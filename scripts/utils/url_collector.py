"""URL keşif yardımcıları — GDELT API ve CommonCrawl wrapper'ları.

Pilot scraping'de doğrulanan iki yöntem (docs/00_metodoloji_master.md
Bölüm 4 ve pilot/00_pilot_scraping_raporu.md Bölüm 6):

    - GDELT Project API: aa.com.tr URL'lerinin tarih aralıklı keşfi
    - CommonCrawl CC-MAIN index: yedek URL havuzu
"""
from __future__ import annotations

import logging
import time
from datetime import date, datetime
from typing import Iterator

import requests

GDELT_ENDPOINT = "https://api.gdeltproject.org/api/v2/doc/doc"
COMMONCRAWL_INDEX = "https://index.commoncrawl.org"

logger = logging.getLogger("gazze_korpus")


def gdelt_search(
    domain: str,
    keywords: list[str],
    start_dt: date,
    end_dt: date,
    session: requests.Session,
    rate_delay: float = 3.0,
    max_records: int = 250,
) -> list[dict[str, str]]:
    """GDELT 2.0 Doc API üzerinden URL keşfi.

    Args:
        domain: Hedef domain (ör. 'aa.com.tr').
        keywords: Aranacak anahtar kelimeler (OR ile birleştirilir).
        start_dt: Başlangıç tarihi (dahil).
        end_dt: Bitiş tarihi (dahil).
        session: requests.Session örneği.
        rate_delay: API'ye saygılı bekleme süresi (saniye).
        max_records: Tek sorguda maksimum kayıt (GDELT üst sınırı 250).

    Returns:
        Her makale için {'url', 'title', 'seendate', 'language'} sözlükleri.
    """
    keyword_query = " OR ".join(keywords) if keywords else ""
    query_parts = [f"domain:{domain}"]
    if keyword_query:
        query_parts.append(f"({keyword_query})")
    query = " ".join(query_parts)

    params = {
        "query": query,
        "mode": "artlist",
        "format": "json",
        "maxrecords": str(max_records),
        "startdatetime": start_dt.strftime("%Y%m%d") + "000000",
        "enddatetime": end_dt.strftime("%Y%m%d") + "235959",
        "sort": "datedesc",
    }

    try:
        response = session.get(GDELT_ENDPOINT, params=params, timeout=30)
    except requests.RequestException as exc:
        logger.warning("GDELT istek hatası (%s → %s): %s", start_dt, end_dt, exc)
        return []

    time.sleep(rate_delay)

    if response.status_code == 429:
        logger.info("GDELT 429 — 30 saniye bekleyip tekrar deneniyor")
        time.sleep(30)
        return gdelt_search(domain, keywords, start_dt, end_dt, session, rate_delay, max_records)

    if response.status_code != 200:
        logger.warning(
            "GDELT non-200 (%s → %s): HTTP %d", start_dt, end_dt, response.status_code
        )
        return []

    try:
        data = response.json()
    except ValueError:
        logger.warning("GDELT JSON parse hatası (%s → %s)", start_dt, end_dt)
        return []

    articles = data.get("articles", []) or []
    return [
        {
            "url": a.get("url", ""),
            "title": a.get("title", ""),
            "seendate": a.get("seendate", ""),
            "language": a.get("language", ""),
        }
        for a in articles
        if a.get("url")
    ]


def daterange_blocks(start: date, end: date, block_days: int) -> Iterator[tuple[date, date]]:
    """Tarih aralığını N-günlük bloklara böler (GDELT için)."""
    from datetime import timedelta

    cursor = start
    while cursor <= end:
        block_end = min(cursor + timedelta(days=block_days - 1), end)
        yield cursor, block_end
        cursor = block_end + timedelta(days=1)


def parse_seendate(seendate: str) -> datetime | None:
    """GDELT seendate ('20231007T110000Z') → datetime."""
    if not seendate:
        return None
    try:
        return datetime.strptime(seendate, "%Y%m%dT%H%M%SZ")
    except ValueError:
        return None
