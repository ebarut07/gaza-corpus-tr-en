"""Checkpoint yönetimi.

progress.json dosyasında her kaynak için işlenmiş URL setlerini ve
sayaçları saklar. Script kesilirse aynı yerden devam edebilmesini sağlar.
"""
from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Checkpoint:
    """Per-source checkpoint state'i tutar ve diske yazar.

    progress.json formatı:
        {
            "aa":       {"processed_urls": [...], "saved_count": N, "last_update": ISO},
            "sputnik":  {...},
            "euronews": {...}
        }
    """

    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.Lock()
        self._state: dict[str, dict[str, Any]] = self._load()

    def _load(self) -> dict[str, dict[str, Any]]:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _ensure_source(self, source: str) -> None:
        if source not in self._state:
            self._state[source] = {
                "processed_urls": [],
                "saved_count": 0,
                "filtered_count": 0,
                "failed_count": 0,
                "last_update": None,
            }

    def is_processed(self, source: str, url: str) -> bool:
        """URL'in daha önce işlenip işlenmediğini kontrol eder."""
        self._ensure_source(source)
        return url in self._state[source]["processed_urls"]

    def mark_processed(
        self,
        source: str,
        url: str,
        outcome: str = "saved",
    ) -> None:
        """URL'i işlenmiş olarak işaretler.

        Args:
            source: Kaynak adı (aa, sputnik, euronews).
            url: İşlenmiş URL.
            outcome: 'saved', 'filtered', veya 'failed'.
        """
        with self._lock:
            self._ensure_source(source)
            if url not in self._state[source]["processed_urls"]:
                self._state[source]["processed_urls"].append(url)
            counter_key = f"{outcome}_count"
            if counter_key in self._state[source]:
                self._state[source][counter_key] += 1
            self._state[source]["last_update"] = datetime.now(timezone.utc).isoformat()

    def saved_count(self, source: str) -> int:
        """Kaynaktan başarıyla kaydedilen haber sayısı."""
        self._ensure_source(source)
        return self._state[source]["saved_count"]

    def save(self) -> None:
        """State'i diske yazar."""
        with self._lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8") as f:
                json.dump(self._state, f, ensure_ascii=False, indent=2)

    def summary(self) -> dict[str, dict[str, int]]:
        """Konsola basmak için özet."""
        return {
            source: {
                "saved": data["saved_count"],
                "filtered": data["filtered_count"],
                "failed": data["failed_count"],
            }
            for source, data in self._state.items()
        }
