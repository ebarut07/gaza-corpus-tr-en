# Arşiv Erişim Testi Raporu — 6. Bölüm (VOA + Reuters + Çin Medyası)
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** VOA EN/TR · Reuters EN/TR · Xinhua EN/TR · CGTN EN/TR · CRI Türkçe  
**Önceki Raporlar:** arsiv_testi_raporu.md · _2_ · _3_ · _4_

---

## ÖZET KARAR TABLOSU (Öne Çekilen)

| Kaynak | EN | TR | ClaudeBot Yasağı | Karar |
|--------|----|----|-----------------|-------|
| **Reuters** | ❌ Tam engel | ❌ Tam engel | Bilinmiyor (erişilemedi) | **Kullanılamaz** |
| **VOA English** | ❌ 403 | — | Bilinmiyor (403) | **Kullanılamaz** |
| **VOA Türkçe** | — | Test edilmedi | — | Belirsiz |
| **Xinhua** | ❌ SSL hatası | ❌ ECONNREFUSED | — | **Kullanılamaz** |
| **CGTN English** | ✅ Çalışıyor | — | Yok | **Kullanılabilir** |
| **CGTN Türkçe** | — | ⚠️ JS-rendered | — | **Sınırlı** |
| **CRI Türkçe** | — | ✅ Çalışıyor | Yok | **Kullanılabilir** |

---

## 1. REUTERS

### Test Sonuçları
| URL | Sonuç |
|-----|-------|
| `www.reuters.com/robots.txt` | ❌ Claude Code unable to fetch |
| `tr.reuters.com/robots.txt` | ❌ Claude Code unable to fetch |

### Değerlendirme
Reuters, `reuters.com` ve `tr.reuters.com` domainlerinin tamamında BBC ve DW ile özdeş ağ düzeyinde engel uyguluyor. robots.txt'e bile ulaşılamadı. Wayback Machine'de de bulunma ihtimali düşük (BBC ile aynı örüntü).

**Karar: ❌ KULLAНИLAMAZ** — Batı ticari ajans koruması. 6 testten 6'ıncı başarısız Batı kaynağı.

---

## 2. VOA (Voice of America)

### Test Sonuçları
| URL | Sonuç |
|-----|-------|
| `www.voanews.com/robots.txt` | ❌ 403 Forbidden |
| `voanews.com/robots.txt` (www'suz) | ❌ 403 Forbidden |
| `voanews.com/z/5008` (Middle East arşivi) | ❌ 403 Forbidden |
| `voanews.com/p/5765.html` | ❌ 403 Forbidden |

### VOA Türkçe (`voaturkce.com`)
Test edilmedi. Türkiye'de RTÜK kararıyla erişim engeli mevcut (2022+). `voaturkce.com` bir ayna site olabilir. Ancak VOA İngilizce'nin 403 ile tamamen kapalı olması, TR ayna sitesine yönelmeyi anlamsız kılıyor: çift dil paralel corpus için EN tarafı çalışmak zorunda.

### Ek Not: USAGM Krizi
Trump yönetiminin 2025'te USAGM'yi büyük ölçüde kapatmasıyla VOA'nın 2023-2024 dönemi arşiv stabilitesi zaten belirsizdi. 403 yanıtı içerik yokluğundan da kaynaklanıyor olabilir.

**Karar: ❌ KULLAНИLAMAZ** — Site genelinde 403; EN kanalı çalışmadan TR paralel corpus mümkün değil.

---

## 3. ÇİN MEDYASI

### 3a. Xinhua

| URL | Sonuç |
|-----|-------|
| `turkish.xinhuanet.com/robots.txt` | ❌ ECONNREFUSED |
| `xinhuanet.com/robots.txt` | ❌ SSL sertifika hatası |
| `english.news.cn/robots.txt` | ❌ 404 |
| `turkish.xinhuanet.com/` (HTTP) | ❌ ECONNREFUSED |

**Karar: ❌ KULLAНИLAMAZ** — Domain tamamen erişilemez. SSL ve bağlantı hataları Xinhua'nın bu URL yapısını terk ettiğine işaret ediyor.

---

### 3b. CGTN English (`news.cgtn.com`)

#### robots.txt
- `cgtn.com/robots.txt` ✅ Erişildi
- ClaudeBot / Claude-Code: **Yasak yok** ✅
- Disallow: `/*.do*`, `/*shareUrl*`, `/*account.user.cgtn.com*` — minimal kısıtlama
- **23 sitemap dosyası** mevcut

#### İçerik Testi
- `cgtn.com/world/middle-east` ✅ Açıldı
- **50+ haber başlığı** görünüyor
- İçerik **statik HTML** (`/p.html` uzantılı URL'ler)
- Tarih bilgisi mevcut (DD-Mon-YYYY formatı)
- Gaza haberleri mevcut: "Gaza tent camps plagued with rats and parasites" (May 2026)

#### URL Formatı
```
https://news.cgtn.com/news/[YYYY-MM-DD]/[slug]/p.html
Örnek: https://news.cgtn.com/news/2026-05-02/UAE-MoUs-with-Chinese-banks/p.html
```

#### Arşiv/Arama Sorunları
| Test | Sonuç |
|------|-------|
| `cgtn.com/search?query=Gaza&from=...&to=...` | ❌ `/newspal` uygulamasına yönlendiriyor |
| `news.cgtn.com/news/2023-10-07/` (tarih arşivi) | ❌ 404 |

**Ekim 2023 arşivine doğrudan URL ile ulaşılamıyor.** Kategori sayfaları üzerinden "load more" ile geçmişe ulaşmak teorik olarak mümkün ama sistematik tarama için zor. Sitemap üzerinden tarih bazlı tarama araştırılmalı.

**Karar: ⚠️ SINIRLI KULLANILABİLİR** — İçerik erişilebilir, statik HTML, ama arşiv yapısı belirsiz.

---

### 3c. CGTN Türkçe (`turkish.cgtn.com`)

#### Erişim
- `turkish.cgtn.com/` ✅ Açıldı
- `turkish.cri.cn/` ✅ Açıldı (aynı platforma yönlendiriyor — CRI Türkçe CGTN'e entegre edilmiş)

#### robots.txt
- `turkish.cri.cn/robots.txt` ✅ Erişildi
- ClaudeBot yasağı: **Yok** ✅
- Facebook/Google botları için 120 saniye crawl-delay
- Sitemap: `turkish.cri.cn/sitemap_index.xml`

#### İçerik
- 12+ Türkçe haber başlığı görünüyor
- Orta Doğu haberleri mevcut ama Gaza spesifik içerik sınırlı
- **50+ dil desteği** (Türkçe dahil)

#### URL Formatı
```
https://turkish.cgtn.com/[YYYY]/[MM]/[DD]/ARTI[TIMESTAMP-ID]
Örnek: https://turkish.cgtn.com/2026/05/02/ARTI1777708865897496
```
ID: Unix timestamp tabanlı (~16 basamak milisaniye)

#### Teknik Sorun: JavaScript Rendering
`turkish.cgtn.com` **Nuxt.js** (Vue.js tabanlı SSR framework) kullanıyor. Bu, içeriğin kısmen JavaScript ile render edildiği anlamına gelir. Basit HTML fetch ile tüm içerik çıkarılamayabilir; **headless browser** (Selenium/Playwright) gerekebilir.

**Karar: ⚠️ SINIRLI KULLANILABİLİR** — Erişilebilir ama JS rendering ve zayıf Gaza içerik yoğunluğu sorun.

---

### EN-TR Eşleştirme Analizi (CGTN)

| Özellik | CGTN EN | CGTN TR |
|---------|---------|---------|
| Domain | `news.cgtn.com` | `turkish.cgtn.com` |
| URL yapısı | `/news/YYYY-MM-DD/slug/p.html` | `/YYYY/MM/DD/ARTI[timestamp]` |
| ID sistemi | Slug bazlı | Unix timestamp milisaniye |
| Ortak ID | ❌ Yok | ❌ Yok |
| Eşleştirme yöntemi | Tarih + cosine similarity | — |

CGTN'de AA ve Sputnik'teki gibi ortak ID ile otomatik EN-TR eşleştirme **mümkün değil**. Eşleştirme içerik benzerliği ile yapılmak zorunda.

---

## FİNAL DEĞERLENDİRME

### Tüm Testlerin Genel Tablosu (6 Rapor Sonrası)

| Kaynak | EN | TR | EN-TR ID Eşleşme | Arşiv | Karar |
|--------|----|----|-----------------|-------|-------|
| **Sputnik** | ✅ | ✅ | ❌ (farklı ID, cosine) | ✅ Tarih arşivi | **1. Öncelik** |
| **AA** | ✅ | ✅ | ⚠️ (eski içerik TBD) | ⚠️ Kategori | **1. Öncelik** |
| **CGTN** | ✅ statik | ⚠️ JS | ❌ (cosine gerekli) | ❌ Sorunlu | **3. Seçenek** |
| Al Jazeera EN | ✅ sitemap | ❌ Yok | — | ✅ Mükemmel | **Kısmi** |
| BBC | ❌ | ❌ | — | ❌ Wayback'te yok | Elendi |
| DW | ❌ | ❌ | — | — | Elendi |
| France 24 | ❌ (403) | ❌ (403) | — | — | Elendi |
| Reuters | ❌ | ❌ | — | — | Elendi |
| VOA | ❌ (403) | TBD | — | — | Elendi |
| Xinhua | ❌ | ❌ | — | — | Elendi |

---

### Üç Tasarım Seçeneği

**Seçenek A — "Non-Western Perspectives" (Önerilen)**
| # | Kaynak | Perspektif | EN | TR | Zorluk |
|---|--------|------------|----|----|--------|
| 1 | Sputnik | Rusya / Batı karşıtı | sputnikglobe.com | anlatilaninotesi.com.tr | Düşük |
| 2 | AA | Türkiye devlet | aa.com.tr/en | aa.com.tr/tr | Düşük |
| 3 | CGTN | Çin devlet | news.cgtn.com | turkish.cgtn.com | Orta-Yüksek |

Avantaj: Üç farklı non-Western perspektif — güçlü bir "alternatif medya ekosistemi" çerçevesi. Akademik olarak özgün ve savunulabilir.  
Dezavantaj: CGTN'nin JS rendering ve arşiv sorunları ek teknik yük getirir; Batı perspektifi eksik.

---

**Seçenek B — "2 Kesinleşmiş Kaynak + Al Jazeera Comparable"**
| # | Kaynak | Perspektif | EN | TR |
|---|--------|------------|----|----|
| 1 | Sputnik | Rusya / Batı karşıtı | sputnikglobe.com | anlatilaninotesi.com.tr |
| 2 | AA | Türkiye devlet | aa.com.tr/en | aa.com.tr/tr |
| 3 | Al Jazeera | Körfez / Arap | aljazeera.com/en | — (Katman 2) |

Al Jazeera İngilizce, Katman 2 (comparable) olarak AA ve Sputnik Türkçesi ile karşılaştırılır. Strict parallel (Katman 1) yalnızca AA ve Sputnik içi çiftler. Metodoloji bölümünde "asimetrik paralel tasarım" olarak savunulabilir.  
Avantaj: En teknik sorunsuz tasarım; 3 farklı ideolojik perspektif.  
Dezavantaj: Al Jazeera'nın TR karşılığı olmadığı için tam parallel yerine comparable kullanılmak zorunda.

---

**Seçenek C — "2 Kaynaklı Minimal Tasarım"**
AA EN+TR ve Sputnik EN+TR ile devam. CGTN atlansın.  
Avantaj: Teknik sorun sıfır; pilot scrapinge hemen geçilebilir.  
Dezavantaj: Sadece iki kaynak — Language Resources and Evaluation gibi Q1 dergilerde "neden yalnızca ikisi?" sorusu gelebilir.

---

### TAVSİYE

**Seçenek B (Al Jazeera EN + AA EN/TR + Sputnik EN/TR)** en iyi denge noktası:
- Teknik olarak 3 kaynaktan en sorunsuz kombinasyon
- Al Jazeera Körfez perspektifini, AA Türkiye perspektifini, Sputnik Rusya perspektifini temsil eder — güçlü ideolojik üçgen
- Metodolojik asimetri (Al Jazeera'nın TR'sinin olmaması) makalede şeffafça sunulursa Q1 dergi standardını karşılar
- CGTN'nin JS/arşiv sorunlarına zaman harcamaktan kurtulur

Eğer üç tam EN+TR çifti şart ise → **Seçenek A (CGTN ile)**, ama CGTN için Playwright/Selenium ile headless browser ek altyapı gerektirir.

---

### Sıradaki Adım

Tasarım kararı verilince doğrudan **Adım 2.2 (Pilot Scraping)**'e geçilebilir:
- Her kesinleşen kaynak için 20-30 haber pilot scraping
- AA eski içerik erişiminin doğrulanması (Ekim 2023 arşivi)
- Seçilen tasarıma göre scraping scriptlerinin yazılması

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
