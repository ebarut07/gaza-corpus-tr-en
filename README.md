# Gazze Korpusu — Q1 Makale Projesi

**Proje Sahibi:** Dr. Evren Barut, Afyon Kocatepe Üniversitesi
**Alan:** Uygulamalı Dilbilim / Çeviribilim
**Durum:** Adım 2.3 Tam Scraping (devam ediyor)
**Son Güncelleme:** 3 Mayıs 2026
**GitHub:** https://github.com/ebarut07/gaza-corpus-tr-en (Public, MIT)

---

## Proje Özeti

Gazze savaşının ilk altı ayını (7 Ekim 2023 – 7 Nisan 2024) kapsayan, üç farklı devlet/üst-devlet medya kaynağından derlenen **Türkçe-İngilizce paralel haber korpusu** inşası projesi. Hedef: yaklaşık 1.500 EN-TR haber çifti.

**Kaynak üçlemesi:**
1. **Anadolu Ajansı (AA)** — Türkiye ulus-devlet medyası
2. **Sputnik** — Rusya devlet medyası (TR: anlatilaninotesi.com.tr)
3. **Euronews** — AB üst-devlet medyası (TR: tr.euronews.com)

**Teorik çerçeve:** Bielsa & Bassnett (2009), Baker (2006), Valdeón (2015)

**Hedef dergiler:**
- Makale 1 (bu proje): *Language Resources and Evaluation*, *Corpora*
- Makale 2: *Target*, *Perspectives*, *Translation Studies*
- Makale 3: *Machine Translation*, *Natural Language Engineering*

---

## Klasör Yapısı

```
C:\GazzeKorpus\
├── CLAUDE.md                       # Proje hafıza dosyası (Claude Code bağlamı)
├── README.md                       # Bu dosya
├── .github/workflows/
│   └── scrape_sputnik_en.yml       # GitHub Actions Sputnik EN workflow
├── docs/
│   ├── 00_metodoloji_master.md     # Master metodoloji (Bölüm 3.3 + 9.4: hibrit erişim)
│   └── 01_..._07_*.md              # 7 erişim test raporu
├── pilot/
│   └── 00_pilot_scraping_raporu.md # Pilot rapor + Bölüm 10 düzeltme
├── scripts/
│   ├── main.py                     # Lokal scraping orchestrator
│   ├── config.yaml                 # Scraping konfigürasyonu
│   ├── merge_github_artifacts.py   # GitHub Actions zip → lokal corpus birleştirici
│   ├── scrapers/                   # AA, Sputnik, Euronews scraper modülleri
│   ├── utils/                      # logger, checkpoint, html_cleaner, vb.
│   ├── README.md                   # Scraping aracı kullanım kılavuzu
│   ├── requirements.txt
│   └── LICENSE                     # MIT
└── corpus/                         # Çıktı: JSON dosyaları
    ├── aa/{en,tr}/
    ├── sputnik/{en,tr}/
    ├── euronews/{en,tr}/
    └── progress.json               # Checkpoint
```

---

## Süreç Aşamaları

| Adım | Görev | Durum |
|------|-------|-------|
| **1** | Araştırma tasarımı — kaynak seçimi kriterleri | ✅ Tamamlandı |
| **2.1** | Arşiv erişim testi — 8 rapor, 25+ kaynak, final tasarım | ✅ Tamamlandı |
| **2.2** | Pilot scraping — her kaynaktan 20-30 haber | ✅ Tamamlandı (3 May 2026 düzeltildi) |
| **2.3** | Tam scraping — 6 aylık dönem (hibrit: lokal + GitHub Actions) | 🚧 Devam ediyor |
| **2.4** | EN-TR eşleştirme (cosine similarity) | ⏳ Bekliyor |
| **2.5** | Örnekleme (%70 stratified + %30 event-based) | ⏳ Bekliyor |
| **2.6** | Manuel doğrulama — 50 haber alt-örneklem | ⏳ Bekliyor |
| **3** | Annotation şeması ve uygulama | ⏳ Bekliyor |
| **4** | Zenodo + GitHub korpus paketi | ⏳ Bekliyor |
| **5** | Makale yazımı ve Q1 submission | ⏳ Bekliyor |

---

## Erişim Mimarisi — Hibrit Yapı

| Kaynak | Erişim Aracı | Konum |
|--------|--------------|-------|
| AA EN+TR | Lokal Python | Türkiye, Afyonkarahisar |
| Euronews EN+TR | Lokal Python | Türkiye, Afyonkarahisar |
| Sputnik TR (anlatilaninotesi.com.tr) | Lokal Python | Türkiye, Afyonkarahisar |
| **Sputnik EN (sputnikglobe.com)** | **GitHub Actions** | **Frankfurt (Microsoft Azure)** |

**Neden hibrit?** Türkiye'den lokal Python ile sputnikglobe.com'a erişim, RTÜK'ün SNI-bazlı domain filtresi nedeniyle TCP düzeyinde engelli. Detay: `docs/00_metodoloji_master.md` Bölüm 3.3 ve `pilot/00_pilot_scraping_raporu.md` Bölüm 10.

---

## ⚙️ Lokal Scraping Nasıl Çalıştırılır?

```powershell
cd C:\GazzeKorpus\scripts
py -m pip install -r requirements.txt   # ilk kurulum
py main.py --test                        # her dilden 5 haber (~13 dk)
py main.py --full                        # tam scraping (~10-13 saat)
```

> Tam scraping checkpoint sistemi sayesinde kesilirse aynı yerden devam eder.
> Gece çalıştırmak idealdir (uyku Never, şarja takılı, Windows Update active hours dışı).

Detaylar: `scripts/README.md`

---

## 🤖 GitHub Actions ile Sputnik EN Scraping

Sputnik EN için aşağıdaki adımları takip edin. Kod bilmenize gerek yok — hepsi web tarayıcısından yapılır.

### Adım 1 — Repo'yu GitHub'a yükle (sadece ilk kez)

**1a. Önkoşul: Windows Gezgini'nde gizli öğeleri göster**
- Windows Gezgini'ni açın → Üst menüden **"Görünüm" → "Göster" → "Gizli öğeler"** seçeneğini işaretleyin
- Bu yoksa `.github` klasörü görünmez (nokta ile başlayan klasörleri Windows varsayılan olarak saklar)

**1b. GitHub web arayüzünden yükle**

1. https://github.com/ebarut07/gaza-corpus-tr-en adresine girin
2. Sağ üstte **"Add file" → "Upload files"** butonuna tıklayın
3. Bilgisayarınızda `C:\GazzeKorpus\` klasörünü Windows Gezgini ile açın
4. **Şu klasör/dosyaları SEÇİP sürükleyip GitHub'a bırakın:**
   - `scripts/` klasörünün tamamı (alt klasörler dahil korunur)
   - `.github/` klasörünün tamamı (gizli olduğu için 1a adımı gerekli)
   - `docs/` klasörünün tamamı
   - `pilot/` klasörünün tamamı
   - `CLAUDE.md`
   - `README.md` (bu dosya)
5. **YÜKLEMEYİN** (zaten .gitignore'da):
   - `corpus/` klasörü (çok büyük, ham veri)
   - `scripts/logs/` (runtime log'ları)
   - `scripts/__pycache__/` ya da herhangi bir `__pycache__/` klasörü
   - `scripts/scrapers/__pycache__/`, `scripts/utils/__pycache__/`
   - `*.pyc` uzantılı dosyalar
   - `test.txt` (kullanılmayan dosya)
6. Aşağıda yeşil **"Commit changes"** butonuna basın
7. ~30 saniye bekleyin, dosyalar yüklenir

> **İpucu**: Windows Gezgini'nde Ctrl+A ile tüm klasörleri seçebilirsiniz, sonra Ctrl tıklayarak `corpus`, `__pycache__` (varsa) ve `test.txt`'i seçimden çıkarabilirsiniz. Kalanları sürükleyip bırakın.

> **Yüklenecek dosya tahmini**: ~30 dosya, toplam ~150 KB. GitHub web arayüzü 100 dosya/commit sınırının çok altında.

### Adım 2 — Workflow'u tetikle

1. Repo sayfasında üstteki **"Actions"** sekmesine tıklayın
2. Sol menüden **"Sputnik EN Scraping"** workflow'unu seçin
3. Sağ üstte **"Run workflow"** butonuna basın (mavi açılır menü açılır)
4. Parametreler için **varsayılanları kabul edin** (tam scraping):
   - `start_date`: 2023-10-07
   - `end_date`: 2024-04-07
   - `max_articles`: 0 (sınırsız)
5. Yeşil **"Run workflow"** butonuna basın
6. Workflow başlar — sayfayı yenileyin, listede yeni bir satır görünecek

### Adım 3 — Tamamlanmasını bekle (~1-2 saat)

- Çalışmakta olan workflow'a tıklayın → "scrape" job'unun ilerleyişini görürsünüz
- Tamamlanınca yeşil ✅ ya da kırmızı ❌ durum işareti görünür
- Sayfanın aşağısında **özet rapor** otomatik üretilir (kaç haber çekildi)

### Adım 4 — Çıktıyı indir

1. Tamamlanan workflow run sayfasında **en aşağıya** kayın
2. **"Artifacts"** kutusunda `sputnik-en-corpus-XXXXXX` adlı bir zip dosyası göreceksiniz
3. Zip dosyasının üzerine tıklayıp **bilgisayarınıza indirin**
4. İndirme klasörünüze (genelde `C:\Users\evren\Downloads\`) kaydedilir

### Adım 5 — Lokal corpus'a birleştir

```powershell
cd C:\GazzeKorpus
py scripts\merge_github_artifacts.py "C:\Users\evren\Downloads\sputnik-en-corpus-XXXXXX.zip"
```

Script çıktısı şöyle bir özet verir:
```
======================================================================
ÖZET
======================================================================
  Eklenen yeni haber       : 487
  Tekrar (zaten mevcut)    : 0
  Hedef klasördeki toplam  : 487
```

İlk önce **dry-run** ile ne olacağını görmek istiyorsanız:
```powershell
py scripts\merge_github_artifacts.py "...zip" --dry-run
```

### İleride yeniden scraping yapmak isterseniz

Adım 1'i atlayın — repo zaten GitHub'da. Adım 2'den başlayın. Eski sonuçlar lokal corpus'ta kalır; merge script tekrar gelen haberleri otomatik dedup eder.

---

## Akademik Atıf

> Barut, E. (2026). *Gazze Korpusu: A Turkish-English Parallel News Corpus on
> the Gaza Conflict (7 October 2023 – 7 April 2024)* [Data set & software].
> Zenodo. (DOI eklenecek.)

---

## Hızlı Başvuru

- **Master metodoloji:** `docs/00_metodoloji_master.md` (Bölüm 3.3 hibrit erişim, Bölüm 9.4 Q1-hazır EN paragraf)
- **Pilot raporu + 3 May düzeltmesi:** `pilot/00_pilot_scraping_raporu.md` Bölüm 10
- **Proje bağlamı:** `CLAUDE.md` — araştırma sorusu, korpus tasarımı, hibrit erişim notları
- **Scraping aracı dökümanı:** `scripts/README.md`
