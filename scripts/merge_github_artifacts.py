"""GitHub Actions Artifact Birleştirici.

GitHub Actions üzerinde çalışan Sputnik EN scraping workflow'unun ürettiği
ZIP artifact'ini açar ve içindeki JSON dosyalarını lokal corpus klasörüne
(`corpus/sputnik/en/`) kopyalar. Mevcut dosyalar varsa metin hash'i ile
deduplication yapar.

Kullanım:
    py scripts/merge_github_artifacts.py PATH/sputnik-en-corpus-12345.zip

    # Dry-run (kopyalama yapmadan ne olacağını göster):
    py scripts/merge_github_artifacts.py PATH/...zip --dry-run

    # Farklı hedef:
    py scripts/merge_github_artifacts.py PATH/...zip --target /custom/corpus/path
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TARGET = (SCRIPT_DIR.parent / "corpus").resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="GitHub Actions Sputnik EN artifact'ini lokal korpusa entegre eder",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("zip_path", type=Path, help="GitHub'dan indirilen .zip dosyasının yolu")
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help="Hedef corpus dizini (varsayılan: <repo>/corpus)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dosyaları kopyalama, sadece ne olacağını listele",
    )
    return parser.parse_args()


def find_jsons(root: Path) -> list[Path]:
    """ZIP içinden çıkmış klasörde sputnik/en altındaki tüm JSON'ları bul."""
    candidates: list[Path] = []

    # Workflow çıktısı: corpus_github/sputnik/en/*.json
    # Olası varyasyonlar: corpus/sputnik/en/, doğrudan sputnik/en/
    for pattern in (
        "**/sputnik/en/*.json",
        "**/sputnik_en/*.json",
    ):
        for p in root.glob(pattern):
            if p.is_file() and p.name not in ("progress.json",):
                candidates.append(p)

    # Yinelenen path'leri kaldır
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in candidates:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            unique.append(p)
    return unique


def article_hash(json_path: Path) -> str:
    """JSON içindeki metin_hash alanını döndürür (yoksa boş)."""
    try:
        with json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("metin_hash", "")
    except (OSError, json.JSONDecodeError):
        return ""


def existing_hashes(target_dir: Path) -> set[str]:
    """Hedef klasördeki mevcut tüm dosyaların metin_hash'lerini topla."""
    hashes: set[str] = set()
    if not target_dir.exists():
        return hashes
    for p in target_dir.glob("*.json"):
        h = article_hash(p)
        if h:
            hashes.add(h)
    return hashes


def merge_logs(extracted_root: Path, target_root: Path, dry_run: bool) -> None:
    """GitHub log'larını lokal log klasörüne kopyala (üzerine yazmaz, suffix ekler)."""
    log_dir_target = SCRIPT_DIR / "logs"
    for log_pattern in ("**/scripts/logs/*.log", "**/logs/*.log"):
        for log_file in extracted_root.glob(log_pattern):
            if not log_file.is_file():
                continue
            dest = log_dir_target / f"github_actions_{log_file.name}"
            if dry_run:
                print(f"  [dry-run] LOG kopyalanacak: {log_file.name} -> {dest}")
                continue
            log_dir_target.mkdir(parents=True, exist_ok=True)
            shutil.copy2(log_file, dest)
            print(f"  [log] {log_file.name} -> {dest}")


def main() -> int:
    args = parse_args()

    if not args.zip_path.exists():
        print(f"HATA: ZIP dosyası bulunamadı: {args.zip_path}", file=sys.stderr)
        return 1

    if not zipfile.is_zipfile(args.zip_path):
        print(f"HATA: Geçerli bir ZIP dosyası değil: {args.zip_path}", file=sys.stderr)
        return 1

    target_dir = args.target / "sputnik" / "en"
    target_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("GitHub Actions Artifact Birleştirici")
    print("=" * 70)
    print(f"ZIP    : {args.zip_path}")
    print(f"Hedef  : {target_dir}")
    print(f"Dry-run: {args.dry_run}")
    print()

    with tempfile.TemporaryDirectory(prefix="gazze_artifact_") as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(args.zip_path, "r") as zf:
            zf.extractall(tmp_path)
        print(f"ZIP açıldı (geçici klasör): {tmp_path}")

        json_files = find_jsons(tmp_path)
        print(f"Bulunan JSON dosyası: {len(json_files)}")

        if not json_files:
            print("UYARI: ZIP içinde sputnik/en/*.json bulunamadı.")
            print("ZIP içeriği:")
            for p in tmp_path.rglob("*"):
                if p.is_file():
                    print(f"  {p.relative_to(tmp_path)}")
            return 2

        existing = existing_hashes(target_dir)
        print(f"Hedefteki mevcut benzersiz haber sayısı: {len(existing)}")

        added = 0
        duplicate = 0
        skipped_empty = 0

        for src in json_files:
            h = article_hash(src)
            if not h:
                skipped_empty += 1
                if args.dry_run:
                    print(f"  [dry-run] BOŞ HASH atlanacak: {src.name}")
                continue
            if h in existing:
                duplicate += 1
                continue

            dest = target_dir / src.name
            # İsim çakışması: numaralı suffix ekle
            if dest.exists() and not args.dry_run:
                base = dest.stem
                ext = dest.suffix
                idx = 1
                while dest.exists():
                    dest = target_dir / f"{base}_{idx}{ext}"
                    idx += 1

            if args.dry_run:
                print(f"  [dry-run] EKLENECEK: {src.name} -> {dest.name}")
            else:
                shutil.copy2(src, dest)
            existing.add(h)
            added += 1

        print()
        merge_logs(tmp_path, args.target, args.dry_run)

    print()
    print("=" * 70)
    print("ÖZET")
    print("=" * 70)
    print(f"  Eklenen yeni haber       : {added}")
    print(f"  Tekrar (zaten mevcut)    : {duplicate}")
    print(f"  Boş hash (atlandı)       : {skipped_empty}")
    print(f"  Hedef klasördeki toplam  : {len(list(target_dir.glob('*.json')))}")
    if args.dry_run:
        print()
        print("Bu bir dry-run idi — gerçek kopyalama yapılmadı.")
        print("Onayladıysanız --dry-run bayrağını kaldırıp tekrar çalıştırın.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
