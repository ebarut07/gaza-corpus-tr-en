# Arşiv Erişim Testi Raporu
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** 6 kaynak (Al Jazeera EN/TR, BBC EN/TR, AA EN/TR)  
**Test Yöntemi:** robots.txt kontrolü + arama/arşiv URL testi + örnek içerik doğrulama

---

## ⚠️ PROJE İÇİN KRİTİK BULGULAR (Öne Çekilen)

Teste başlamadan önce iki kritik sorun tespit edildi:

1. **Al Jazeera Türkçe servisi mevcut değil.** `aljazeera.com.tr` İngilizce Türkiye haberlerine yönlendiriyor. `aljazeera.com/tr/` → 404. Sitemap'ta tek bir Türkçe URL yok.
2. **BBC'ye hiçbir programatik erişim sağlanamadı.** `www.bbc.com`, `www.bbc.co.uk`, `news.bbc.co.uk`, `bbc.com/sitemap.xml` — hepsi engelli. Geçici çözüm bölümüne bakın.

---

## 1. Al Jazeera English (aljazeera.com)

### robots.txt Durumu
- **URL:** `aljazeera.com/robots.txt` ✅ Erişildi
- `/search/` dizini → **Disallow**
- `/api` → **Disallow**
- **ÖNEMLİ:** `ClaudeBot` ve `Claude-Web` ajanları robots.txt'de açıkça **Disallow** edilmiş
- Crawl-delay: Belirtilmemiş
- 4 adet XML sitemap linki mevcut

### Arşiv/Arama URL Yapısı
| Yöntem | URL Formatı | Durum |
|--------|------------|-------|
| Arama sayfası | `/search/Gaza?sort=date&dateFrom=...` | ❌ JavaScript ile yükleniyor, içerik gelmiyor |
| Etiket sayfası | `/tag/israel-war-on-gaza/` | ✅ Kısmen çalışıyor (8-10 haber görünür) |
| **Günlük sitemap** | `/sitemap.xml?yyyy=2023&mm=10&dd=07` | ✅ **EN GÜÇLÜ YÖNTEM** |

### Sitemap Testi — Tarih Aralığı Doğrulaması
- **7 Ekim 2023:** 29 URL — Gaza haberlerini içeriyor ✅
- **7 Nisan 2024:** 41 URL — Gaza haberlerini içeriyor ✅
- Tarih aralığımızın (6 ay = ~180 gün) **tamamına erişim mümkün**

### URL Formatı
```
https://www.aljazeera.com/news/2023/10/7/sirens-warn-of-rockets-launched-towards-israel-from-gaza-news-reports
https://www.aljazeera.com/[seksiyon]/[yil]/[ay]/[gun]/[slug]
```
Seksiyon örnekleri: `news`, `features`, `opinions`, `gallery`, `liveblog`

### İçerik Testi
- 7 Ekim 2023 tarihli makale doğrudan URL ile açıldı ✅
- İçerik **statik HTML** olarak geliyor (JavaScript bekleme gerekmez)
- Başlık, metin, tarih bilgisi hepsi HTML içinde mevcut

### Sayfa Başına Sonuç
- Sitemap yöntemiyle: tüm günün URL'leri tek seferde (örn. 29-41 URL)
- Etiket sayfalarında: 8-10 görünen, "Show More" butonu ile artıyor

### Sayfalama
- Sitemap yöntemi: sayfa yok — her gün bir URL, 1 API isteği
- Etiket sayfaları: "Show More" butonu (JavaScript gerektirir)
- **Önerilen yöntem: Sitemap**

### Türkçe Durum
❌ **Al Jazeera Türkçe servisi yoktur.** Bu kaynak yalnızca İngilizce korpus için kullanılabilir. Proje tasarımında kaynak seçimi gözden geçirilmelidir.

---

## 2. Al Jazeera Türkçe (aljazeera.com.tr)

### Test Sonucu
| Test | Sonuç |
|------|-------|
| `aljazeera.com.tr` | → `aljazeera.com/where/turkey/` yönlendirmesi (301) |
| `aljazeera.com/tr/` | → 404 Hata |
| `aljazeera.com/where/turkey/` | İçerik İngilizce — Türkiye hakkında İngilizce haberler |
| Sitemap'ta Türkçe URL | Yok |
| Sayfada Türkçe dil seçeneği | Yok |

### Sonuç
**❌ Al Jazeera Türkçe servisi mevcut değil.** Bu kaynak EN-TR paralel korpus için kullanılamaz.

---

## 3. BBC News English (bbc.com/news)

### robots.txt Durumu
- `www.bbc.com/robots.txt` → **Erişim engelli**
- `www.bbc.co.uk/robots.txt` → **Erişim engelli**

### Arşiv/Arama Testi
| Test Edilen URL | Sonuç |
|----------------|-------|
| `bbc.com/robots.txt` | ❌ Erişim engelli |
| `bbc.co.uk/robots.txt` | ❌ Erişim engelli |
| `bbc.com/news/topics/c2vdnvyttv8t` (Gaza konusu) | ❌ Erişim engelli |
| `bbc.com/sitemap.xml` | ❌ Erişim engelli |
| `news.bbc.co.uk/robots.txt` | ❌ Erişim engelli |

### URL Formatı (Genel Bilgi)
Bilinen BBC haber URL formatı (doğrudan test edilemedi):
```
bbc.com/news/world-middle-east-XXXXXXXX   (İngilizce)
bbc.com/turkce/haberler-XXXXXXXX          (Türkçe)
```

### Sonuç
**❌ BBC tüm programatik erişim yöntemlerine kapalı.** Bu, CloudFare veya IP bazlı bir engel olabilir. BBC doğrudan scraping için en sorunlu kaynak.

### Geçici Çözüm Önerileri
1. **Wayback Machine (archive.org):** `web.archive.org/web/20231007*/bbc.com/news/world-middle-east*` — arşivlenmiş sayfalar genellikle erişilebilir
2. **Manuel indirme:** BBC makalelerini tarayıcıdan "Farklı kaydet" ile HTML olarak kaydetmek
3. **BBC API (ContentAPI):** Akademik erişim için BBC'ye resmi başvuru (MediaWiki API benzeri)

---

## 4. BBC Türkçe (bbc.com/turkce)

### Test Sonucu
❌ `bbc.com` engeli nedeniyle `bbc.com/turkce` sayfasına da erişilemedi. BBC İngilizce ile aynı durum.

---

## 5. Anadolu Ajansı English (aa.com.tr/en)

### robots.txt Durumu
- **URL:** `aa.com.tr/robots.txt` ✅ Erişildi
- `/api/` → **Disallow**
- `/search?*` → **Disallow** (arama URL'leri engelli)
- `/*?s=*` → **Disallow**
- `/*/p/preview/*` → **Disallow**
- Genel içerik (`/`) → **Allow**
- Crawl-delay: Belirtilmemiş

### Arşiv/Arama URL Yapısı
| Yöntem | URL | Durum |
|--------|-----|-------|
| Arama sayfası | `/en/search?q=Gaza&from=...` | ❌ İçerik gelmiyor (muhtemelen JS) |
| Arama (sorgu parametreli) | `/search?*` formatı | ❌ robots.txt'de Disallow |
| Sayfa numaralı pagination | `/en/middle-east/page/2` | ❌ 404 döndürüyor |
| **Kategori sayfası** | `/en/middle-east` | ✅ 20+ haber görünüyor |

### URL Formatı
```
https://www.aa.com.tr/en/middle-east/israeli-army-demolishes-christian-monastery/3924485
https://www.aa.com.tr/en/[kategori]/[haber-basligi-slug]/[haber-id]
```
Haber ID: Sıralı numara (Mayıs 2026'da ~3924000 civarı)

### İçerik Özellikleri
- Kategori sayfasında 20+ haber başlığı, başlık + tarih + URL hepsi HTML içinde ✅
- Tarih formatı: `01 May 2026` (gün ay yıl)
- "Load more" butonu mevcut (JavaScript gerektirir)
- **Eski haberlere erişim:** Belirsiz — kategori sayfaları sadece güncel içerik gösteriyor

### Eski İçeriğe Erişim Sorunu
Ekim 2023 tarihli haberlere erişim test edildi ancak AA'nın arşive yönelik tarih bazlı URL yapısı bulunamadı. Haber ID numaraları aracılığıyla doğrudan erişim teorik olarak mümkün (ID bilinirse), ancak sistematik arşiv erişimi için sitemap veya farklı yöntem araştırılması gerekiyor.

---

## 6. Anadolu Ajansı Türkçe (aa.com.tr/tr)

### Test Sonucu
| Test | Sonuç |
|------|-------|
| robots.txt | İngilizce ile aynı (tek robots.txt) |
| Kategori sayfası `/tr/gundem` | ✅ 15+ haber görünüyor |
| URL formatı | `/tr/gundem/[slug]/[id]` |
| Eski içerik erişimi | ❌ Test edilemedi |

### URL Formatı
```
https://www.aa.com.tr/tr/gundem/cumhurbaskani-yardimcisi-yilmaz-ermenistana-gidecek/3924838
https://www.aa.com.tr/tr/[kategori]/[slug]/[haber-id]
```

### İçerik Özellikleri
- 15+ haber başlığı statik HTML içinde görünüyor ✅
- Tarih bilgisi mevcut (02 Mayıs 2026 formatı)
- "Daha fazla" butonu JavaScript ile yükleme yapıyor
- EN ve TR URL'leri aynı haber ID'sini paylaşıyor olabilir (doğrulanması gerekiyor — önemli! Eşleştirme için kritik)

---

## GENEL DEĞERLENDİRME

### Kaynak Bazında Özet Tablo

| Kaynak | robots.txt | Arşiv Erişimi | HTML mi JS mi? | Öneri |
|--------|-----------|--------------|----------------|-------|
| Al Jazeera EN | ⚠️ ClaudeBot Disallow | ✅ Mükemmel (sitemap) | ✅ Statik HTML | **İlk öncelik** |
| Al Jazeera TR | — | ❌ Mevcut değil | — | **Kaynaktan çık** |
| BBC EN | ❌ Erişilemiyor | ❌ Tamamen engelli | — | **Manuel/Wayback** |
| BBC TR | ❌ Erişilemiyor | ❌ Tamamen engelli | — | **Manuel/Wayback** |
| AA EN | ✅ Temiz | ⚠️ Kategori sayfası (eski içerik belirsiz) | ⚠️ Kısmen JS | **İkinci öncelik** |
| AA TR | ✅ Temiz | ⚠️ Kategori sayfası (eski içerik belirsiz) | ⚠️ Kısmen JS | **İkinci öncelik** |

### En Kolay Scrape Edilecek Kaynak
**Al Jazeera English** — günlük sitemap sistemi sayesinde her gün ayrı bir API isteği yapılıyor, tüm 6 ay (180 gün) sistematik şekilde taranabilir, içerik statik HTML, URL formatı tahmin edilebilir. 7 Ekim 2023 – 7 Nisan 2024 arası doğrulandı.

**Dikkat:** Al Jazeera robots.txt'de ClaudeBot açıkça Disallow edilmiş. Scraper için `User-Agent` seçimi ve akademik erişim etiği gözden geçirilmeli.

### En Sorunlu Kaynak
**BBC (EN ve TR)** — programatik erişim tamamen engelli. Seçenekler: (1) Wayback Machine üzerinden arşiv erişimi, (2) academic API başvurusu, (3) manuel indirme.

### Proje Tasarımına Etki: Kaynak Revizyonu Gerekiyor

Mevcut tasarımdaki `Al Jazeera EN-TR` çifti **uygulanamaz** çünkü Al Jazeera'nın Türkçe servisi 2013'te kapatılmış ve şu an mevcut değil.

**Önerilen alternatif kaynak çiftleri:**

| Seçenek | EN Kaynak | TR Kaynak | Notlar |
|---------|-----------|-----------|--------|
| A | Al Jazeera EN | AA TR | İdeolojik çeşitlilik korunuyor |
| B | BBC EN | BBC TR | Aynı kurum — güçlü parallel, ama erişim sorunu |
| C | AA EN | AA TR | Aynı kurum — ID bazlı eşleştirme mümkün olabilir |
| D | Al Jazeera EN | BBC TR | Çapraz karşılaştırma |

---

## Sıradaki Adım (2.2 öncesi)

1. **Kaynak revizyonu kararı:** Al Jazeera TR yerine hangi TR kaynağı kullanılacak?
2. **BBC engeli çözümü:** Wayback Machine yöntemi test edilecek mi?
3. **AA eski içerik testi:** Ekim 2023 tarihli bir AA haberi bulunup ID numarasıyla doğrudan URL testi yapılacak
4. **AA EN-TR ID eşleşme testi:** Aynı haberin İngilizce ve Türkçe ID'lerinin birebir aynı olup olmadığı kontrol edilecek — evet ise eşleştirme çok kolaylaşır

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
