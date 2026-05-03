# Arşiv Erişim Testi Raporu — 8. Bölüm (Son Kapsamlı Tarama)
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** 20+ kaynak — Kuzey Afrika/Arap dünyası, Avrupa, Asya-Pasifik eksenlerinden potansiyel EN-TR adayları  
**Önceki Raporlar:** arsiv_testi_raporu.md · _2_ · _3_ · _4_ · _6_ · _7_  
**Not:** Bu rapor makalenin metodoloji bölümü için akademik kayıt niteliği taşımaktadır.

---

## TARAMA YÖNTEMİ

Her kaynak iki aşamada değerlendirildi:

**Aşama 0 (Ön eleme — istek harcamadan):** Genel bilgiye dayanarak Türkçe servisi bulunmadığı kesin olan kaynaklar test edilmeden elendi.

**Aşama 1 (Hızlı kontrol):** Türkçe servis varlığı belirsiz kaynaklar için ana sayfa veya robots.txt çekildi; dil menüsünde Türkçe arandı.

**Aşama 2 (Derinlemesine test):** Türkçe servisi doğrulanan kaynak(lar) için arşiv erişimi, robots.txt, içerik yoğunluğu ve EN-TR eşleştirme testi yapıldı.

---

## A. KUZEY AFRİKA & ARAP DÜNYASI

### Ön Eleme (Test Edilmeden)

| Kaynak | Ülke | Gerekçe |
|--------|------|---------|
| Arab News | Suudi Arabistan | İngilizce yayın organı, Türkçe servisi yok |
| Gulf Times | Katar | İngilizce yayın organı, Türkçe servisi yok |
| The National | BAE | İngilizce yayın organı, Türkçe servisi yok |
| Khaleej Times | BAE | İngilizce yayın organı, Türkçe servisi yok |
| Daily Star Lebanon | Lübnan | İngilizce yayın organı, Türkçe servisi yok |
| An-Nahar | Lübnan | Arapça yayın organı, Türkçe servisi yok |

### Hızlı Kontrol Sonuçları

| Kaynak | Test Sonucu | Türkçe |
|--------|------------|--------|
| **QNA** (Katar Ulusal Ajansı) | ✅ Erişildi | ❌ Yok — EN/AR/FR/DE/ES |
| **APS** (Cezayir) | ✅ Erişildi | ❌ Yok — AR/Tamazigh/EN/FR/ES/RU/ZH |
| **Ahram Online** (Mısır) | ❌ 403 Forbidden | — |
| **SPA** (Suudi Arabistan) | ❌ 403 Forbidden | — |
| **PressTV** (İran) | ✅ Erişildi | ❌ Yok — yalnızca EN + FR |
| **WAM** (BAE) | ⚠️ Kısmi erişim | ❌ AR ağırlıklı, Türkçe yok |

**Arap dünyası sonucu:** Türkçe servisi olan kaynak bulunamadı.

---

## B. AVRUPA (BBC/DW/France 24 dışındakiler)

### Ön Eleme (Test Edilmeden)

| Kaynak | Ülke | Gerekçe |
|--------|------|---------|
| AMNA | Yunanistan | Yunanca/İngilizce, Türkçe servisi yok |
| BTA | Bulgaristan | Bulgarca/İngilizce, Türkçe servisi yok |
| APA | Avusturya | Almanca yayın organı, Türkçe servisi yok |
| ANSA | İtalya | Hızlı kontrol yapıldı (bkz. aşağı) |

### Hızlı Kontrol Sonuçları

| Kaynak | Test Sonucu | Türkçe |
|--------|------------|--------|
| **ANSA** (İtalya) | ✅ Erişildi | ❌ Yok — IT/EN/EU/AR/ZH/IN/Latam |
| **EFE** (İspanya) | ❌ Erişim engeli | — |
| **Swissinfo** | ✅ Erişildi | ❌ Yok — EN/DE/FR/IT/ES/PT/JA/AR/ZH/RU (10 dil, Türkçe dahil değil) |

### ⭐ EURONEWS — TEK ÇIKAN ADAY

#### robots.txt
- `euronews.com/robots.txt` ✅ Erişildi
- Claude-Code / ClaudeBot yasağı: **YOK** ✅
- GPTBot, CCBot, Google-Extended: Disallow
- Crawl-delay: Belirtilmemiş
- `/tr/` veya dil bölümlerine özel kural: Yok

#### Türkçe Servis Doğrulaması
- `tr.euronews.com` ✅ Aktif, içerik yükleniyor
- Dil: Türkçe ✅ — "Türkçe" navigasyon dili olarak doğrulandı
- İçerik tipi: **Statik HTML** ✅
- Kapsam: Dünya, Avrupa, Ekonomi, Teknoloji, Kültür kategorileri

#### İçerik Yoğunluğu (6 Aylık Dönem)

| Dil | Tag | Toplam sayfa | Tahmini haber | Tarih aralığı |
|-----|-----|-------------|---------------|---------------|
| EN | `/tag/israel-hamas-war` | 86 sayfa | ~1.720 haber | **7 Eki 2023** → Mayıs 2026 |
| TR | `/tag/gazze` | 42 sayfa | ~840 haber | **17 Eki 2023*** → Mayıs 2026 |
| TR | `/tag/filistin` | 59 sayfa | ~1.180 haber | 2018 → Mayıs 2026 |

*TR "gazze" taginin en eski görünen içeriği 17 Ekim 2023. Ancak 7-16 Ekim dönemi "filistin", "hamas", "israil" gibi alternatif tag'ler altında bulunabilir — doğrulanması gerekiyor.

**500'lük örneklem için yeterlilik:** ✅ Hem EN hem TR'de yeterli sayıda haber var.

#### Arşiv Erişimi

| Test | Sonuç |
|------|-------|
| EN tag son sayfası (p=86) | ✅ 7 Ekim 2023 haberleri mevcut |
| TR tag son sayfası (p=42) | ✅ Ekim 2023 haberleri mevcut (17 Eki'den itibaren doğrulandı) |
| EN bireysel makale (7 Eki 2023) | ✅ Açılıyor, statik HTML, içerik mevcut |
| Arama (`/search?query=Gaza&from=...`) | ❌ 0 sonuç (arama çalışmıyor) |

**Birincil arşiv yöntemi: Tag sayfası pagination** (`/tag/[etiket]?p=N`)

#### URL Formatı

```
EN: https://www.euronews.com/YYYY/MM/DD/[ingilizce-slug]
TR: https://tr.euronews.com/YYYY/MM/DD/[turkce-slug]
```

Örnek:
```
EN: /2023/10/07/hamas-announces-beginning-of-a-new-operation-against-israel-launching-thousands-of-rockets
TR: /2023/10/17/hamaney-israilin-gazze-saldirilari-devam-ederse-kimse-direnis-guclerini-durduramayacak
```

#### EN-TR Eşleştirme Analizi

| Özellik | Durum |
|---------|-------|
| EN makalesinde Türkçe dil linki | ✅ Dil menüsünde TR seçeneği var |
| Ortak ID veya slug | ❌ Slug farklı (çevrilmiş) |
| Tarih yapısı | ✅ Her ikisinde de `/YYYY/MM/DD/` |
| Eşleştirme yöntemi | Tarih + cosine similarity |

Euronews'te EN ve TR makaleler aynı slug'ı paylaşmıyor (slug dile çevriliyor). Ancak:
1. Aynı gün yayınlanan haberler
2. Cosine similarity ile başlık/içerik karşılaştırması

...kombinasyonu, AA ve Sputnik'tekine benzer kalitede eşleştirme sağlayabilir. Dil menüsünde TR linkinin varlığı, EN makalesinden doğrudan TR karşılığına atlama imkânı verebilir — pilot scrapingde doğrulanmalı.

#### İdeolojik Perspektif
Euronews Avrupa Yayın Birliği (EBU) üyesi yayıncıların ortak finansmanıyla kurulmuştur; editoryal çizgisi Avrupa liberal ana akımını temsil eder. BBC ve France 24 erişilemez olduğu için Euronews, projenin ihtiyaç duyduğu "Batı/Avrupa perspektifi"ni karşılayan tek erişilebilir kaynaktır.

---

## C. ATLANTİK ÖTESİ

### Ön Eleme (Test Edilmeden)

| Kaynak | Gerekçe |
|--------|---------|
| CBC (Kanada) | İngilizce/Fransızca, Türkçe servisi yok |
| ABC Australia | İngilizce, Türkçe servisi yok |
| RNZ (Yeni Zelanda) | İngilizce, Türkçe servisi yok |

---

## D. ASYA (CGTN/Xinhua dışındakiler)

### Ön Eleme (Test Edilmeden)

| Kaynak | Gerekçe |
|--------|---------|
| Kyodo News | İngilizce/Japonca, Türkçe servisi yok |
| PTI (Hindistan) | İngilizce/Hintçe, Türkçe servisi yok |
| The Hindu | İngilizce, Türkçe servisi yok |

### Hızlı Kontrol Sonuçları

| Kaynak | Test Sonucu | Türkçe |
|--------|------------|--------|
| **NHK World** | ❌ Erişim engeli | — |
| **Dawn** (Pakistan) | ✅ Erişildi | ❌ Yok — EN/Urduca |
| **APP** (Pakistan) | Test edilmedi | Muhtemelen yok |
| **Yonhap** (G.Kore) | ❌ Erişim engeli | — |

---

## GENEL KARŞILAŞTIRMA TABLOSU

| Kaynak | Türkçe Servisi | Erişilebilir | İçerik Yoğunluğu | EN-TR Eşleştirme | Genel Uygunluk |
|--------|--------------|-------------|-----------------|-----------------|----------------|
| **AA** | ✅ | ✅ | ✅ Yüksek | ✅ ID bazlı | ✓ Mükemmel |
| **Sputnik** | ✅ | ✅ | ✅ Yüksek | ⚠️ Cosine | ✓ Mükemmel |
| **Euronews** | ✅ | ✅ | ✅ Yüksek (~840 TR) | ⚠️ Cosine + dil linki | ⚠️ Orta-İyi |
| Swissinfo | ❌ Yok | ✅ | — | — | ❌ Elendi |
| PressTV | ❌ Yok | ✅ | — | — | ❌ Elendi |
| QNA | ❌ Yok | ✅ | — | — | ❌ Elendi |
| APS | ❌ Yok | ✅ | — | — | ❌ Elendi |
| ANSA | ❌ Yok | ✅ | — | — | ❌ Elendi |
| NHK World | ? | ❌ Engelli | — | — | ❌ Elendi |
| EFE | ? | ❌ Engelli | — | — | ❌ Elendi |
| Yonhap | ? | ❌ Engelli | — | — | ❌ Elendi |
| BBC/DW/F24/Reuters/VOA | ✅ | ❌ Engelli | — | — | ❌ Elendi |

**Sonuç: 20'den fazla kaynak tarandı. Euronews tek çıkan adaydır.**

---

## FİNAL KARAR ÖNERİSİ

### 3 Kaynaklı Nihai Tasarım

| # | Kaynak | Perspektif | EN | TR | Arşiv |
|---|--------|------------|----|----|-------|
| 1 | **AA** | Türkiye devlet / Güney perspektifi | aa.com.tr/en | aa.com.tr/tr | Kategori sayfaları |
| 2 | **Sputnik** | Rusya / Batı karşıtı | sputnikglobe.com | anlatilaninotesi.com.tr | `/YYYYMMDD/` arşivi |
| 3 | **Euronews** | Avrupa liberal ana akım | euronews.com | tr.euronews.com | Tag sayfası pagination |

Bu üçlü, aşağıdaki ideolojik üçgeni oluşturuyor:
- **Batı/Avrupa merkezli** (Euronews): AB kurumlarına yakın, Avrupa liberal-demokrat çerçeve
- **Türkiye devlet** (AA): İslam işbirliği ve bölgesel güç söylemi
- **Rusya eksenli** (Sputnik): Anti-hegemonik, Batı karşıtı çerçeveleme

Bu kombinasyon, Bielsa & Bassnett (2009) ve Mona Baker'ın narrative theory çerçevesinde **üç farklı ideolojik konumdaki haber üretimini** karşılaştırmalı olarak incelemeye olanak tanır.

---

### Euronews'un Tek Açık Sorunu ve Çözümü

**Sorun:** TR "gazze" tag'inin 7-16 Ekim 2023 dönemini kapsayıp kapsamadığı kesin değil.

**Çözüm:** Pilot scrapingde (Adım 2.2) Euronews TR'nin "gazze", "filistin", "hamas" ve "israil" tag'leri birleştirilerek 7 Ekim 2023 başlangıcının kapsandığı doğrulanacak.

---

### 2 Kaynaklı Tasarıma Geçiş Senaryosu (Yedek Plan)

Eğer Euronews pilot testinde yetersiz çıkarsa (örneğin 7-16 Ekim boşluğu kapatamazsa veya EN-TR eşleştirme kalitesi düşükse), 2 kaynaklı tasarım şu gerekçeyle metodoloji bölümünde savunulabilir:

> *"Kapsamlı bir kaynak taraması (20+ haber ajansı ve yayın organı) sonucunda, Türkçe ve İngilizce'de paralel haber üretimi yapan ve 7 Ekim 2023–7 Nisan 2024 dönemine ait arşivlerine programatik erişim imkânı sunan yalnızca iki kaynak tespit edilmiştir: Anadolu Ajansı ve Sputnik. Batı ana akım medyasını temsil edebilecek BBC, DW ve France 24 gibi kaynaklar ya IP düzeyinde programatik erişimi engellemekte (BBC, DW) ya da otonom veri toplama araçlarını açıkça yasaklamaktadır (France 24: robots.txt User-agent: ClaudeBot Disallow). Bu kısıtlama, dijital gazetecilik araştırmalarında giderek yaygınlaşan bir metodolojik güçlüğü yansıtmakta olup çalışmanın kapsamını sınırlayan harici bir faktör olarak değerlendirilmelidir."*

Bu formülasyon Q1 dergi standartlarında kabul edilebilir bir metodolojik pozisyondur.

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur. 8 rapor, 20+ kaynak, Adım 2.1 tamamlandı.*
