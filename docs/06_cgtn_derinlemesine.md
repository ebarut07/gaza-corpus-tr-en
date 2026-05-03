# Arşiv Erişim Testi Raporu — 7. Bölüm (CGTN Derinlemesine Doğrulama)
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** CGTN EN ve TR — pratik kullanılabilirlik doğrulaması  
**Önceki Rapor:** arsiv_testi_6_toplu_raporu.md

---

## SONUÇ (Öne Çekilen)

**CGTN: Ekim 2023 – Nisan 2024 dönemli tarihsel korpus için KULLAНИLAMAZ.**

Güncel içeriğe erişim teknik olarak mümkün (hem EN hem TR statik HTML), ancak tarihsel arşive sistematik erişim yolu bulunmuyor. EN ve TR platformları birbirinden tamamen bağımsız — otomatik eşleştirme imkânsız.

---

## Test Sonuçları

### 1. CGTN TR İçerik Sayfası — HTML Yapısı

**Test URL:** `turkish.cri.cn/2026/05/02/ARTI1777721302929717`

| Özellik | Sonuç |
|---------|-------|
| Sayfa açılıyor mu? | ✅ Evet |
| İçerik statik HTML'de mi? | ✅ **Evet — JavaScript rendering GEREKMİYOR** |
| Nuxt.js sorunu çözüldü mü? | ✅ SSR (Server-Side Rendering) aktif — içerik pre-rendered |
| Türkçe kalitesi | ✅ Profesyonel, doğal Türkçe |

**Türkçe kalite örnekleri:**
> *"Çin'de 1 Mayıs İşçi Bayramı tatilinin ilk gününde ülke genelinde 337 milyon 470 bin seyahat gerçekleştirildi."*  
> *"Sierra Leone Cumhurbaşkanı Julius Maada Bio, Çin'in ülkesinin en güvenilir ortaklarından biri olduğunu söyledi."*

Coğrafi adlar, sayılar, dilbilgisi tutarlı. Makine çevirisi izi minimal; editöryal süzgeçten geçmiş içerik.

> **Akademik not:** Bu durum aslında bir bulgudur — Çin devlet medyasının Türkçe servisi profesyonel kalitede, sembolik değil. Bu, makale için "non-Western devlet medyası Türkçe üretim kalitesi" tartışmasına malzeme olabilir.

---

### 2. CGTN EN İçerik Sayfası — HTML Yapısı

**Test URL:** `news.cgtn.com/news/2026-05-02/UAE-MoUs-with-Chinese-banks--1MOK7m4n3zO/p.html`

| Özellik | Sonuç |
|---------|-------|
| Sayfa açılıyor mu? | ✅ Evet |
| İçerik statik HTML'de mi? | ✅ **Evet — statik HTML** |
| Dil değiştirme menüsü var mı? | ✅ Var |
| Türkçe dil seçeneği var mı? | ❌ **Yok — Türkçe listede yok** |

CGTN EN sayfasındaki dil menüsü Arapça, Rusça, İspanyolca, Fransızca gibi dilleri içeriyor. **Türkçe bu listede yer almıyor.** Yani CGTN EN platformu CGTN TR platformunu kendi kardeş servisi olarak tanımıyor.

---

### 3. Sitemap ve Arşiv Yapısı

| Test | Sonuç |
|------|-------|
| `cgtn.com/sitemap_index.xml` | ❌ 404 |
| `turkish.cri.cn/sitemap_index.xml` | ✅ Var — ama yalnızca `latest_sitemap.xml` |
| `latest_sitemap.xml` içeriği | 100 URL, yalnızca son 5 gün (28 Nis – 2 May 2026) |
| Ekim 2023 sitemap'ta var mı? | ❌ **Hayır** |
| `cgtn.com/world/middle-east/Gaza.html` | ❌ 404 |
| `turkish.cgtn.com/2023/10/07/` | ❌ Tarih arşivi değil — güncel ana sayfayı gösteriyor |
| `news.cgtn.com/news/2023-10-07/` | ❌ 404 |
| CGTN TR Wayback Machine'de var mı? | ❌ Hayır |

**Tüm arşiv erişim yolları başarısız.**

---

### 4. RSS Feed

| Test | Sonuç |
|------|-------|
| `turkish.cgtn.com/rss` | ❌ RSS değil — HTML ana sayfa dönüyor |

RSS feed bulunmuyor. Alternatif altyapı yok.

---

### 5. EN-TR Eşleştirme Analizi

| Özellik | CGTN EN | CGTN TR |
|---------|---------|---------|
| Ana domain | `news.cgtn.com` | `turkish.cgtn.com` / `turkish.cri.cn` |
| URL yapısı | `/news/YYYY-MM-DD/slug-ID/p.html` | `/YYYY/MM/DD/ARTI[timestamp]` |
| ID sistemi | Alfanümerik (ör. `1MOK7m4n3zO`) | Unix timestamp ms (ör. `1777721302929717`) |
| Ortak ID | ❌ **Yok** | ❌ **Yok** |
| Dil menüsünde Türkçe | ❌ Türkçe listede değil | — |
| Platform entegrasyonu | ❌ Bağımsız sistem | ❌ Bağımsız sistem |

CGTN EN ve CGTN TR, **farklı teknik altyapılar** üzerinde çalışıyor. AA'da aynı haber ID'si EN ve TR için ortaktı; Sputnik'te aynı tarih arşiv sayfasında her iki dil listeliydi. CGTN'de böyle bir köprü yok.

Eşleştirme yöntemi: yalnızca tarih + cosine similarity — ama bu, sistematik "strict parallel" (Katman 1) yerine yalnızca "comparable" (Katman 2) üretir.

---

## NET CEVAPLAR

**CGTN TR Claude Code ile pratik olarak scrape edilebilir mi?**  
⚠️ **Şartlı — güncel içerik için evet, arşiv için hayır.**  
Teknik engel (JavaScript) beklenen sorun değildi; asıl sorun arşiv erişimi.

**Hangi şartlar gerekli?**  
Playwright/Selenium GEREKMİYOR — SSR sayesinde içerik statik HTML'de geliyor. Ama bu fark etmiyor çünkü asıl sorun tarihsel içeriğe erişim yolu olmaması.

**EN-TR eşleştirme ne kadar tutarlı?**  
❌ Zayıf — iki platform bağımsız, ortak ID yok, Türkçe dil menüsünde bile yer almıyor.

**6 aylık dönemde içerik yeterli mi?**  
❌ Bilinmiyor ama erişilemiyor — Ekim 2023 – Nisan 2024 içeriğine hiçbir yoldan ulaşılamadı.

---

## SON ÖNERİ

### AA + Sputnik + CGTN tasarımı pratikte uygulanabilir mi?
**HAYIR — uygulanamaz.**

CGTN'nin temel sorunu içerik kalitesi veya erişim engeli değil: **tarihsel arşive sistematik erişim yolunun olmaması.** Ekim 2023 – Nisan 2024 dönemini kapsayan bir korpus için her kaynakta bu döneme ait haberlere ulaşmak şart. CGTN bu şartı karşılamıyor.

---

### Kesinleşmiş Karar: 2+1 Tasarım

**Rapor 1-7 sonrasında tek uygulanabilir yapı:**

| # | Kaynak | EN Domain | TR Domain | Arşiv Yöntemi | Perspektif |
|---|--------|-----------|-----------|---------------|------------|
| 1 | **Sputnik** | sputnikglobe.com | anlatilaninotesi.com.tr | `/YYYYMMDD/` tarih arşivi ✅ | Rusya / Batı karşıtı |
| 2 | **AA** | aa.com.tr/en | aa.com.tr/tr | Kategori + ID ⚠️* | Türkiye devlet |
| +1 | **Al Jazeera EN** | aljazeera.com | — | Günlük sitemap ✅ | Körfez / Arap |

*AA'nın Ekim 2023 arşiv erişimi henüz doğrulanmadı — Adım 2.2 pilot scrapingde test edilmeli.

**Al Jazeera Türkçe versiyonu olmadığı için metodolojik not:** Al Jazeera Katman 2 (comparable) olarak kullanılır; strict parallel (Katman 1) AA ve Sputnik kendi EN-TR çiftleri içinde kalır. Bu asimetrik tasarım makalede açıkça metodolojik bir tercih olarak sunulabilir ve Q1 dergi standardını karşılar.

---

### Sıradaki Adım: Adım 2.2 — Pilot Scraping

Artık kaynak seçimi kesinleşti. Pilot scraping hedefleri:
1. **AA EN+TR** — Ekim 2023 arşiv erişimi doğrulama
2. **Sputnik EN+TR** — `/20231007/` üzerinden 20-30 haber çekimi
3. **Al Jazeera EN** — Sitemap üzerinden 20-30 haber çekimi

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
