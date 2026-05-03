"""Deduplication yardımcıları.

İki seviyeli kontrol:
    - URL hash: aynı URL'i iki kez fetch etme
    - Metin hash (SHA-256): aynı metin farklı URL'lerden gelse bile tek sayılır
"""
from __future__ import annotations

import hashlib


def url_hash(url: str) -> str:
    """URL için SHA-256 hex digest (kısa, 12 karakter)."""
    return hashlib.sha256(url.strip().encode("utf-8")).hexdigest()[:12]


def text_hash(text: str) -> str:
    """Tam metin için SHA-256 hex digest.

    Boşlukları normalize eder ki minor whitespace farkı yanılgıya yol açmasın.
    """
    normalized = " ".join(text.split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()
