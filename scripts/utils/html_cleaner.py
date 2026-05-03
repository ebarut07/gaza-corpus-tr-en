"""HTML temizleme ve metin çıkarma yardımcıları.

BeautifulSoup ile reklam, navigasyon, footer, script ve style elementlerini
soyup okunabilir gövde metnini döndürür.
"""
from __future__ import annotations

import re
from typing import Iterable

from bs4 import BeautifulSoup, Tag

# Tüm kaynaklarda silinmesi gereken yapısal elementler
DEFAULT_STRIP_TAGS: tuple[str, ...] = (
    "script",
    "style",
    "noscript",
    "nav",
    "header",
    "footer",
    "aside",
    "form",
    "button",
    "iframe",
    "svg",
    "figure",  # tipik olarak resim/caption — gövde metni değil
)

# Reklam, "ilgili haber", paylaş, sosyal medya kalıpları (class/id substring)
DEFAULT_STRIP_SUBSTRINGS: tuple[str, ...] = (
    "advert",
    "social",
    "share",
    "newsletter",
    "subscribe",
    "related",
    "recommend",
    "promo",
    "cookie",
    "comment",
    "sidebar",
    "breadcrumb",
    "tag-list",
    "author-box",
    "byline",
    "copyright",
)


def make_soup(html: str) -> BeautifulSoup:
    """HTML metninden BeautifulSoup nesnesi üretir (lxml parser)."""
    return BeautifulSoup(html, "lxml")


def strip_noise(
    soup: BeautifulSoup,
    extra_tags: Iterable[str] = (),
    extra_substrings: Iterable[str] = (),
) -> BeautifulSoup:
    """Yapısal gürültüyü (script, nav, reklam, vb.) kaldırır.

    Args:
        soup: BeautifulSoup nesnesi (in-place modifiye edilir).
        extra_tags: Kaynak-spesifik ek silinecek tag adları.
        extra_substrings: class/id'sinde geçerse silinecek substring'ler.

    Returns:
        Aynı soup nesnesi (chain için).
    """
    for tag_name in (*DEFAULT_STRIP_TAGS, *extra_tags):
        for element in soup.find_all(tag_name):
            element.decompose()

    substrings = (*DEFAULT_STRIP_SUBSTRINGS, *extra_substrings)
    for element in soup.find_all(True):
        if not isinstance(element, Tag):
            continue
        # bs4 + Python 3.14 edge case: bazı node'larda attrs None olabilir
        attrs = getattr(element, "attrs", None) or {}
        classes = attrs.get("class") or []
        if isinstance(classes, str):
            classes = [classes]
        element_id = attrs.get("id") or ""
        identifiers = (" ".join(classes) + " " + element_id).lower()
        if any(s in identifiers for s in substrings):
            element.decompose()

    return soup


def extract_text(node: Tag | BeautifulSoup) -> str:
    """Bir node altındaki tüm metni okunur biçimde toplar.

    Paragraflar arasında çift satır, fazlalık boşlukları temizler.
    """
    parts: list[str] = []
    for paragraph in node.find_all(["p", "h2", "h3", "h4", "li"]):
        text = paragraph.get_text(separator=" ", strip=True)
        if text and len(text.split()) >= 3:  # tek-iki kelimelik nav linkleri ele
            parts.append(text)

    if not parts:
        # fallback: tüm metin
        text = node.get_text(separator="\n", strip=True)
        parts = [line.strip() for line in text.split("\n") if line.strip()]

    body = "\n\n".join(parts)
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def word_count(text: str) -> int:
    """Boşlukla ayrılmış kelime sayısı."""
    return len(text.split()) if text else 0
