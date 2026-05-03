# Gazze Korpusu — Scraping Aracı

**Proje:** Gazze savaşı Türkçe-İngilizce paralel haber korpusu (7 Ekim 2023 – 7 Nisan 2024)
**Kaynaklar:** Anadolu Ajansı (AA), Sputnik, Euronews
**Yazar:** Dr. Evren Barut, Afyon Kocatepe Üniversitesi
**Lisans:** MIT

---

## TR — Hızlı Başlangıç

### Gereksinimler
- Python 3.10+ (test edildi: 3.14.4)
- Windows / macOS / Linux

### Kurulum (Windows)
```powershell
cd C:\GazzeKorpus\scripts
py -m pip install -r requirements.txt
```

> Not: Sistemde `python` komutu yoksa Windows Python Launcher (`py`) kullanın.
> Linux/macOS'te `python` veya `python3` komutu çalışır.

### Test çalıştırması (her kaynaktan 5 haber, ~1-2 dk)
```powershell
py main.py --test
```

### Tam çalıştırma (~5-6 saat, kesilirse kaldığı yerden devam)
```powershell
py main.py --full
```

### Sadece bir kaynak çalıştırma
```powershell
py main.py --source sputnik --test
py main.py --source aa --full
py main.py --source euronews --source aa --full
```

### Dry-run (JSON yazmadan akışı test et)
```powershell
py main.py --test --dry-run
```

### Konfigürasyon
Tüm parametreler `config.yaml` içindedir:
- `date_range`: tarih aralığı
- `sources`: aktif kaynaklar
- `runtime.test_mode` / `max_per_source_test`: test limiti
- `content.min_word_count`: min metin uzunluğu (varsayılan 200; navigasyon HTML elemek için)
- `topic_keywords`: dile göre konu filtresi anahtar kelimeleri
- `http.rate_limit_per_source`: kaynak başına saygı süresi (saniye)

### Çıktı yapısı
```
corpus/
├── aa/en/, aa/tr/             # JSON dosyaları: {tarih}_{hash}.json
├── sputnik/en/, sputnik/tr/
├── euronews/en/, euronews/tr/
├── progress.json              # Checkpoint (her 50 haberde güncellenir)
├── filtered_out.jsonl         # Konu/uzunluk filtresinden elenenler
└── failed_urls.jsonl          # Erişilemeyen URL'ler
```

### JSON şeması
```json
{
  "kaynak": "aa|sputnik|euronews",
  "dil": "en|tr",
  "url": "...",
  "tarih": "2023-10-07",
  "tarih_tam": "2023-10-07T11:00:00Z",
  "baslik": "...",
  "metin": "...",
  "yazar": "...",
  "etiketler": [...],
  "scraping_tarihi": "2026-05-03T...",
  "scraping_method": "gdelt|daily_archive|tag:hamas|...",
  "candidate_pair_id": "aa_2023-10-07_a3f9c1",
  "kelime_sayisi": 524,
  "metin_hash": "sha256..."
}
```

### Etik notu
Script, robots.txt'e saygı gösterir ve User-Agent string'inde akademik kimliği şeffaf biçimde
beyan eder. Her kaynak için `rate_limit_per_source` ile makul gecikme uygulanır.

---

## EN — Quick Start

### Requirements
- Python 3.10+ (tested: 3.14.4)

### Install
```bash
cd scripts
python -m pip install -r requirements.txt    # Windows: py -m pip install -r requirements.txt
```

### Test run (5 articles per source, ~1-2 min)
```bash
python main.py --test
```

### Full run (~5-6 hours; resumable on interruption)
```bash
python main.py --full
```

### Single source
```bash
python main.py --source sputnik --test
```

### Configuration
All parameters live in `config.yaml`:
- `date_range`, `sources`, `topic_keywords`
- `runtime.test_mode` toggles 5-articles-per-source mode
- `content.min_word_count` (default 200) filters out navigation-HTML stubs
- `http.rate_limit_per_source` per-source request delay in seconds

### Output
JSON files at `corpus/<source>/<lang>/{date}_{urlhash}.json` plus
`progress.json` (checkpoint), `filtered_out.jsonl`, `failed_urls.jsonl`.

### Ethical use
The scraper honours robots.txt and announces its academic identity transparently
in the User-Agent. A configurable per-source delay is applied to every request.

---

## Akademik Atıf / Citation
Eğer bu aracı veya korpusu kullanırsanız, makale yayınlandığında atıf bilgisi
buraya eklenecektir.

> Barut, E. (2026). *Gazze Korpusu: A Turkish-English Parallel News Corpus on
> the Gaza Conflict (7 October 2023 – 7 April 2024)* [Data set & software].
> Zenodo. (DOI eklenecek.)
