"""Standart logging kurulumu.

Hem dosyaya (logs/scraping_YYYY-MM-DD.log) hem konsola log yazar.
Akademik şeffaflık için her hata, her başarı kaydedilir.
"""
from __future__ import annotations

import logging
import sys
from datetime import datetime, timezone
from pathlib import Path


def setup_logger(log_dir: Path, name: str = "gazze_korpus") -> logging.Logger:
    """Logger örneğini hazırlar ve döndürür.

    Args:
        log_dir: Log dosyalarının yazılacağı dizin.
        name: Logger adı (modüller arası paylaşım için sabit tutulur).

    Returns:
        Yapılandırılmış logging.Logger nesnesi.
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"scraping_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    # Windows cp1254 konsol Türkçe karakterleri kaldıramaz — stdout'u UTF-8'e çevir.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(fmt)
    logger.addHandler(stream_handler)

    logger.info("=" * 70)
    logger.info("Logger başlatıldı | Log dosyası: %s", log_file)
    logger.info("=" * 70)
    return logger
