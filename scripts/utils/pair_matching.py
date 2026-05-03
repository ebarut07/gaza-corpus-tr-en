"""candidate_pair_id üretimi.

Adım 2.4'te asıl EN-TR eşleştirmesi cosine similarity + NER ile yapılacak.
Bu modül, scraping aşamasında her habere bir aday eşleşme kimliği atar:
aynı kaynak + tarih + benzer başlık → aynı candidate_pair_id.

Bu, korpusun tek geçişte hem scrape edilip hem de ön-eşleştirilmesini
sağlayan basit bir hash şemasıdır. Kesin değil — ön-katalogtur.
"""
from __future__ import annotations

import hashlib
import re

# Türkçe ve İngilizce için ortak stopword seti
_STOPWORDS = {
    # EN
    "the", "a", "an", "of", "in", "on", "at", "to", "for", "and", "or", "but",
    "by", "with", "from", "is", "are", "was", "were", "be", "been", "as",
    "that", "this", "it", "its", "his", "her", "their", "they", "he", "she",
    # TR
    "bir", "ve", "ile", "için", "de", "da", "den", "dan", "ki", "ya", "ya da",
    "ama", "ancak", "fakat", "olarak", "olan", "var", "yok", "bu", "şu", "o",
    "ne", "nasıl", "neden", "niçin", "kim", "hangi", "şey",
}


def normalize_title(title: str) -> str:
    """Başlığı eşleştirme amaçlı normalize eder.

    Lowercase, noktalama kaldır, stopword temizle, Türkçe diakritik koruyarak.
    """
    if not title:
        return ""
    text = title.lower()
    text = re.sub(r"[^\w\sçğıöşüâîû]", " ", text, flags=re.UNICODE)
    tokens = [t for t in text.split() if t and t not in _STOPWORDS and len(t) > 2]
    return " ".join(sorted(tokens))


def candidate_pair_id(source: str, date_iso: str, title: str) -> str:
    """Aynı kaynak+tarih+başlık-shape için stabil ID üretir.

    Args:
        source: 'aa', 'sputnik', 'euronews'.
        date_iso: 'YYYY-MM-DD'.
        title: Haber başlığı.

    Returns:
        '{source}_{date}_{6char_hex}' formatında ID.
    """
    normalized = normalize_title(title)
    digest = hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:6]
    return f"{source}_{date_iso}_{digest}"
