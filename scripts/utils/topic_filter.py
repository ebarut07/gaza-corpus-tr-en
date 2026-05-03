"""Konu filtresi — askeri + insani + diplomasi kapsamı için keyword tabanlı.

İki aşama:
    1. Başlık-bazlı (hızlı) — Sputnik arşiv listesinden ön eleme.
    2. Metin-bazlı (kesin) — fetch sonrası metin üzerinde doğrulama.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class TopicFilterResult:
    """Filtre sonucu ve hangi keyword'lerin eşleştiği bilgisi."""

    matched: bool
    matched_keywords: list[str]


class TopicFilter:
    """Çok-dilli keyword kapsayıcısı."""

    def __init__(self, keywords_by_lang: dict[str, list[str]]) -> None:
        self._keywords: dict[str, list[str]] = {
            lang: [k.lower() for k in kws] for lang, kws in keywords_by_lang.items()
        }

    def keywords_for(self, lang: str) -> list[str]:
        """Belirli dil için keyword listesi (lowercase)."""
        return self._keywords.get(lang, [])

    def matches(self, text: str, lang: str) -> TopicFilterResult:
        """Metinde dil-uygun keyword'lerden en az birini arar.

        Args:
            text: Aranacak metin (başlık ya da gövde).
            lang: 'en' veya 'tr'.

        Returns:
            TopicFilterResult — matched=True ise eşleşen keyword listesi dolu.
        """
        if not text:
            return TopicFilterResult(False, [])
        normalized = text.lower()
        matched = [k for k in self.keywords_for(lang) if k in normalized]
        return TopicFilterResult(matched=bool(matched), matched_keywords=matched)

    def matches_any(self, fragments: Iterable[str], lang: str) -> TopicFilterResult:
        """Birden fazla metin parçasında (başlık + özet) ortak arama."""
        all_matched: list[str] = []
        for fragment in fragments:
            result = self.matches(fragment or "", lang)
            all_matched.extend(result.matched_keywords)
        # tekrarları kaldır, sırayı koru
        seen: set[str] = set()
        unique = [k for k in all_matched if not (k in seen or seen.add(k))]
        return TopicFilterResult(matched=bool(unique), matched_keywords=unique)
