"""GAZZE KORPUSU — Ana scraping orchestrator.

Kullanım:
    python main.py                  # config.yaml'daki tüm kaynakları çalıştır
    python main.py --source aa      # sadece bir kaynak
    python main.py --test            # test_mode=true zorla
    python main.py --config X.yaml   # alternatif config

Çalıştırılan iş akışı:
    1. config.yaml + checkpoint yükle
    2. Aktif kaynakları sıraya koy (Sputnik → AA → Euronews)
    3. Her kaynağı kendi run() metoduyla çağır
    4. Sonunda özet bas
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

import yaml

# Paket olmayan flat layout — modülleri doğrudan ekle
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from scrapers.aa import AAScraper           # noqa: E402
from scrapers.base import BaseScraper        # noqa: E402
from scrapers.euronews import EuronewsScraper  # noqa: E402
from scrapers.sputnik import SputnikScraper    # noqa: E402
from utils.checkpoint import Checkpoint      # noqa: E402
from utils.logger import setup_logger        # noqa: E402
from utils.topic_filter import TopicFilter   # noqa: E402

# Registry: kaynak adı → scraper factory.
# "sputnik"    = anlatilaninotesi.com.tr (TR mirror) — Türkiye lokal Python ile çalışır.
# "sputnik_en" = sputnikglobe.com (EN) — Türkiye'den RTÜK SNI bloğu nedeniyle erişilemez,
#                yalnızca GitHub Actions Microsoft-hosted runner (Frankfurt) üzerinden çalışır.
SCRAPER_REGISTRY: dict[str, callable] = {
    "sputnik":    lambda **kw: SputnikScraper(langs=["tr"], **kw),
    "sputnik_en": lambda **kw: SputnikScraper(langs=["en"], **kw),
    "aa":         AAScraper,
    "euronews":   EuronewsScraper,
}

# Türkiye lokal'de çalıştırılması anlamsız olan kaynaklar.
# Bu kaynaklara erişim altyapı düzeyinde engellidir — uyarı verip atla.
LOCAL_BLOCKED = {
    "sputnik_en": (
        "Sputnik EN (sputnikglobe.com) Türkiye'den RTÜK SNI bloğu nedeniyle "
        "erişilemez. Bu kaynak yalnızca GitHub Actions üzerinden çekilir.\n"
        "  -> .github/workflows/scrape_sputnik_en.yml workflow'unu manuel "
        "tetikleyin (GitHub → Actions sekmesi → Run workflow)."
    ),
}


def load_config(path: Path) -> dict[str, Any]:
    """YAML config dosyasını yükle."""
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_path(base: Path, value: str) -> Path:
    """config'deki relative path'i mutlaklaştır."""
    p = Path(value)
    if not p.is_absolute():
        p = (base / p).resolve()
    return p


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gazze Korpusu scraping orchestrator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=SCRIPT_DIR / "config.yaml",
        help="config.yaml yolu",
    )
    parser.add_argument(
        "--source",
        action="append",
        help="Sadece belirtilen kaynak(lar) çalışsın (birden fazla için tekrar). "
             "Geçerli değerler: aa, sputnik (TR), sputnik_en (yalnız GitHub Actions), euronews",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="test_mode=true zorla (config'i ezer)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="test_mode=false zorla (tam scraping)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="JSON dosyası yazma — sadece doğrulama akışı",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)

    # CLI override'ları
    if args.test:
        config["runtime"]["test_mode"] = True
    if args.full:
        config["runtime"]["test_mode"] = False
    if args.dry_run:
        config["runtime"]["dry_run"] = True

    # Yolları çöz
    output_root = resolve_path(SCRIPT_DIR, config["paths"]["output_root"])
    log_dir = resolve_path(SCRIPT_DIR, config["paths"]["log_dir"])

    output_root.mkdir(parents=True, exist_ok=True)

    logger = setup_logger(log_dir)
    logger.info("Konfigürasyon: %s", args.config)
    logger.info("Çıktı dizini : %s", output_root)
    logger.info("Test modu    : %s", config["runtime"]["test_mode"])
    logger.info("Dry run      : %s", config["runtime"]["dry_run"])
    logger.info("Tarih araligi: %s -> %s",
                config["date_range"]["start"], config["date_range"]["end"])

    # Filtre & checkpoint
    topic_filter = TopicFilter(config["topic_keywords"])
    checkpoint = Checkpoint(output_root / "progress.json")

    # Hangi kaynaklar?
    if args.source:
        active = args.source
    else:
        active = config["sources"]

    # GitHub Actions modunda (env GITHUB_ACTIONS=true) lokal blokları atlama
    in_github_actions = os.environ.get("GITHUB_ACTIONS", "").lower() == "true"

    # Lokal'de bloklu kaynakları uyarı vererek listeden çıkar
    if not in_github_actions:
        filtered_active: list[str] = []
        for s in active:
            if s in LOCAL_BLOCKED:
                logger.warning("=" * 70)
                logger.warning("KAYNAK ATLANDI: %s", s)
                logger.warning(LOCAL_BLOCKED[s])
                logger.warning("=" * 70)
                continue
            filtered_active.append(s)
        active = filtered_active

    logger.info("Aktif kaynaklar: %s", ", ".join(active) if active else "(yok)")

    # Çalıştır
    totals: dict[str, int] = {}
    for source_name in active:
        scraper_factory = SCRAPER_REGISTRY.get(source_name)
        if scraper_factory is None:
            logger.warning("Bilinmeyen kaynak atlanıyor: %s", source_name)
            continue
        scraper = scraper_factory(
            config=config,
            checkpoint=checkpoint,
            topic_filter=topic_filter,
            output_root=output_root,
        )
        saved = scraper.run()
        totals[source_name] = saved

    # Özet
    logger.info("=" * 70)
    logger.info("ÖZET — bu çalıştırma")
    for src, n in totals.items():
        logger.info("  %-10s : %d haber kaydedildi", src, n)
    logger.info("ÖZET — kümülatif (tüm zamanlar)")
    for src, stats in checkpoint.summary().items():
        logger.info(
            "  %-10s : saved=%d  filtered=%d  failed=%d",
            src, stats["saved"], stats["filtered"], stats["failed"],
        )
    logger.info("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
