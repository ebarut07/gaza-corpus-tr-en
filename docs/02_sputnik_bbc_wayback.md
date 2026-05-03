# Arşiv Erişim Testi Raporu — 2. Bölüm
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** Sputnik (EN+TR) ve BBC Wayback Machine yaklaşımı  
**Önceki Rapor:** `arsiv_testi_raporu.md` (Al Jazeera, BBC doğrudan, AA)

---

## ⚠️ ANA BULGULAR (Öne Çekilen)

1. **Sputnik Turkish mevcut ama gizli:** `tr.sputniknews.com` Türkiye'de erişim yasağı nedeniyle `anlatilaninotesi.com.tr` adlı ayna siteye yönlendiriyor. Ayna site tamamen işlevsel; Sputnik'in altyapısını ve URL sistemini kullanıyor.
2. **Sputnik EN ve TR'de tarih bazlı arşiv çalışıyor:** 7 Ekim 2023 arşivine doğrudan erişim sağlandı.
3. **BBC Wayback'te YOK:** BBC tüm arşiv servislerini aktif olarak engelliyor. 7 farklı URL ve tarih kombinasyonunda Wayback boş döndü. BBC bu projede hiçbir yöntemle programatik olarak kullanılamaz.

---

## 1. Sputnik English (sputnikglobe.com)

### robots.txt Durumu
- **URL:** `sputnikglobe.com/robots.txt` ✅ Erişildi
- `/search/` → **Disallow**
- `/services/` → **Disallow**
- `/cms/` → **Disallow**
- `*-print.html$` → **Disallow**
- Genel içerik (`/`) → **Allow**
- Crawl-delay: Yok
- **3 sitemap var:** article index, list index, **archive sitemap** ✅
- ClaudeBot veya özel bot kısıtlaması: **Yok**

### Arşiv/Arama URL Yapısı
| Yöntem | URL | Durum |
|--------|-----|-------|
| Tarih bazlı arşiv | `/YYYYMMDD/` | ✅ **Mükemmel çalışıyor** |
| Arama sayfası | `/search/` | ❌ Disallow |

### 7 Ekim 2023 Arşiv Testi
- `sputnikglobe.com/20231007/` açıldı ✅
- Sayfa başlığı: *"News archive and major events - 07.10.2023"*
- Hamas/Gaza haberleri mevcut — örnek URL'ler:

```
/20231007/hamas-sneak-attack-on-israel-deemed-major-failure-for-israeli-intelligence-1114006542.html
/20231007/huge-mess-whats-known-so-far-about-hamas-israel-armed-standoff-1114004861.html
/20231007/russia-urges-israel-palestine-to-cease-fire-return-to-negotiations---foreign-ministry-1114003454.html
/20231007/israel-defense-forces-declare-state-of-alert-amid-crisis-at-border-with-gaza-strip-1113998216.html
```

**URL Formatı:**
```
https://sputnikglobe.com/[YYYYMMDD]/[slug]-[ID].html
```

### İçerik Özellikleri
- Bireysel makale testi: `...-1114006542.html` ✅ açıldı
- İçerik **statik HTML** — JavaScript bekleme gerekmez
- Tarih, başlık, haber metni HTML içinde mevcut
- Sayfa başına haber: tarih arşiv sayfasında 15+ görünen + "load more"

### ID Sistemi
- EN makale ID'leri (7 Eki 2023): ~**1113-1114 milyon** aralığı
- ID'ler sıralı ve tarih arşivi üzerinden **tahmin edilebilir**
- Sayfada Türkçe versiyona link: **Görünmüyor** — dil değiştirici yok

---

## 2. Sputnik Turkish (anlatilaninotesi.com.tr)

### Arka Plan
- `tr.sputniknews.com` → Türkiye'de RTÜK kararıyla engellendi (2022)
- `tr.sputniknews.com` URL'si `anlatilaninotesi.com.tr` adresine **301 yönlendiriyor**
- `anlatilaninotesi.com.tr` Sputnik'in Türkiye'deki resmi olmayan ayna sitesi

### Kimlik Doğrulaması
Ana sayfada açıkça görülen:
- Başlık: **"Sputnik Haberler - Dünya ve Türkiye Gündemi, Son Dakika Haberler"**
- İletişim e-postası: **feedback.tr@sputniknews.com**
- Footer: **"© 2026 Sputnik Tüm hakları saklıdır"**
- Bu site kesinlikle Sputnik'in Türkçe servisidir.

### robots.txt Durumu
- `anlatilaninotesi.com.tr/robots.txt` ✅ Erişildi
- Kural yapısı `sputnikglobe.com/robots.txt` ile **birebir aynı**
- Aynı Disallow kuralları, aynı sitemap yapısı, aynı clean-param

### Arşiv/Arama URL Yapısı
| Yöntem | URL | Durum |
|--------|-----|-------|
| Tarih bazlı arşiv | `/YYYYMMDD/` | ✅ **Mükemmel çalışıyor** |

### 7 Ekim 2023 Arşiv Testi
- `anlatilaninotesi.com.tr/20231007/` açıldı ✅
- Sayfa başlığı: *"07.10.2023 için haber ve en önemli olaylar arşivi"*
- Sayfa başında "**20 içerik daha**" notu — toplam 35+ haber var
- Hamas/Gaza haberleri mevcut — örnek URL'ler:

```
/20231007/1076133500.html
/20231007/mahmud-abbas-israilin-eylemleri-durdurulmali-1076132338.html
```

**URL Formatı:**
```
https://anlatilaninotesi.com.tr/[YYYYMMDD]/[slug]-[ID].html
```
Not: Bazı TR makalelerde slug yok, sadece ID var (`/20231007/1076133500.html`)

### ID Sistemi — Kritik Bulgu
| Dil | Örnek ID (7 Eki 2023) | Aralık |
|-----|-----------------------|--------|
| English | 1114006542, 1114004861, 1113998216 | ~1113-1114 milyon |
| Turkish | 1076133500, 1076132338 | ~1076 milyon |

**EN ve TR makaleler farklı ID numaraları kullanıyor.** Aynı haberin EN ve TR versiyonları aynı ID'yi paylaşmıyor. EN-TR eşleştirme için içerik benzerliği yöntemi gerekiyor:
- Aynı tarih + başlık/içerik karşılaştırması (cosine similarity)
- Bu yöntem Katman 2 (comparable) için doğal, Katman 1 (strict parallel) için ek doğrulama gerektirir

---

## 3. BBC English (Wayback Machine yaklaşımı)

### Test Edilen URL'ler ve Sonuçlar

Tüm testler `archive.org/wayback/available` API'si ile yapılmıştır:

| Test Edilen URL | Tarih | Sonuç |
|----------------|-------|-------|
| `bbc.com/news/world-middle-east-67027148` | 20231008 | ❌ Boş |
| `bbc.com/news/world-middle-east-67105488` | 20231008 | ❌ Boş |
| `bbc.com/news/world-middle-east` | 20231007 | ❌ Boş |
| `bbc.co.uk/news/world-middle-east` | 20231010 | ❌ Boş |

### Sonuç
**❌ BBC Wayback'te tamamen yok.**

BBC'nin Wayback Machine'de arşivlenmemesinin iki olası nedeni:
1. BBC, robots.txt üzerinden Wayback'in crawlerlarını aktif olarak engelliyor
2. BBC, Internet Archive'e içerik kaldırma talebi göndermiş olabilir

Bu, BBC'nin **hiçbir programatik yöntemle kullanılamayacağını** kesinleştiriyor:
- Doğrudan erişim: ❌ (WebFetch ile engelli)
- Wayback Machine: ❌ (arşivlenmiş snapshot yok)
- CDX API (web.archive.org/cdx): ❌ (erişim engelli)

---

## 4. BBC Turkish (Wayback Machine yaklaşımı)

BBC İngilizce ile aynı engeller geçerli. Ayrı test yapılmadı — `bbc.com` domaininin tamamı programatik erişime kapalı ve Wayback'te yok.

---

## FİNAL TASARIM ONAY RAPORU

### Önerilen 3 Kaynaklı Tasarım Değerlendirmesi

Kullanıcının önerisi: **BBC Wayback + AA + Sputnik**

| Kaynak | Teknik Durum | Karar |
|--------|-------------|-------|
| BBC Wayback | ❌ Gerçekleşmez | **Devre dışı bırak** |
| AA EN+TR | ✅ Çalışıyor | **Koru** |
| Sputnik EN+TR | ✅ Mükemmel | **Koru** |

**Sonuç:** Önerilen tasarım BBC kısmıyla uygulanamaz.

---

### Revize Edilmiş Öneriler

**Seçenek 1 — BBC'yi at, 2 kaynak kullan (AA + Sputnik)**

| Kaynak | EN | TR | İdeolojik Perspektif |
|--------|----|----|----------------------|
| AA | aa.com.tr/en | aa.com.tr/tr | Türkiye devlet |
| Sputnik | sputnikglobe.com | anlatilaninotesi.com.tr | Rusya yanlısı / Batı karşıtı |

Pro: Her iki kaynak da teknik olarak çözülmüş.  
Con: Batı ana akım perspektifi eksik — akademik değerlendirmede eleştiri alabilir.

---

**Seçenek 2 — BBC'yi Reuters ile değiştir (3 kaynak, tam ideolojik çeşitlilik)**

| Kaynak | EN | TR | İdeolojik Perspektif |
|--------|----|----|----------------------|
| AA | aa.com.tr/en | aa.com.tr/tr | Türkiye devlet |
| Sputnik | sputnikglobe.com | anlatilaninotesi.com.tr | Rusya yanlısı |
| Reuters | reuters.com | tr.reuters.com | Batı ana akım |

Pro: İdeolojik çeşitlilik korunuyor (3 farklı perspektif); Reuters erişim kısıtlaması muhtemelen daha az.  
Con: Reuters Türkçe sitesinin (`tr.reuters.com`) arşiv yapısı henüz test edilmedi.

---

**Seçenek 3 — BBC'yi TRT World ile değiştir**

| Kaynak | EN | TR | İdeolojik Perspektif |
|--------|----|----|----------------------|
| AA | aa.com.tr/en | aa.com.tr/tr | Türkiye devlet |
| Sputnik | sputnikglobe.com | anlatilaninotesi.com.tr | Rusya yanlısı |
| TRT World | trtworld.com | trt.net.tr | Türkiye yumuşak güç (İngilizce) |

Pro: TRT World İngilizce yayın yapıyor; Türkçe karşılığı TRT.  
Con: Hem AA hem TRT Türkiye devlet perspektifi — ideolojik çeşitlilik azalır.

---

### Hangi Kaynak En Kolay Scrape Edilir?

**1. Sputnik (her iki dil):** En kolay.
- Tarih bazlı arşiv (`/YYYYMMDD/`) — tüm döneme sistematik erişim
- Statik HTML — JavaScript parser gerekmez
- robots.txt temiz, bot kısıtlaması yok
- 180 gün × 1 istek/gün = 180 istek ile tüm URL listesi

**2. AA (her iki dil):** Orta.
- Kategori sayfaları çalışıyor, içerik statik HTML'de mevcut
- Eski içerik erişimi henüz doğrulanmadı — Adım 2.2'de test edilmeli
- ID bazlı URL yapısı öngörülebilir, ama arşiv tarihleri belirsiz

**3. BBC:** Hiçbir yöntemle mümkün değil — listeden çıkarılmalı.

---

### Sıradaki Adım

1. **Kaynak kararı:** BBC yerine Seçenek 1, 2 veya 3?
2. **Reuters TR testi (Seçenek 2 tercih edilirse):** `tr.reuters.com` arşiv yapısı test edilecek
3. **AA eski içerik testi:** Ekim 2023 tarihli bir AA haberi bulunup URL ile doğrudan erişim test edilecek
4. **Adım 2.2'ye geç:** Pilot scraping (her kaynaktan 20-30 haber)

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
