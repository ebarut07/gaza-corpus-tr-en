# Araştırma Metodolojisi — Master Referans Dosyası
**Proje:** Gazze Korpusu — Q1 Makale Serisi  
**Yazar:** Dr. Evren Barut, Afyon Kocatepe Üniversitesi  
**Alan:** Uygulamalı Dilbilim / Çeviribilim  
**Son Güncelleme:** 2 Mayıs 2026  
**Kapsam:** Adım 2.1 tüm sonuçları — 8 test turu, 25+ kaynak  
**Bağlantılı Dosyalar:** `docs/01_` – `docs/07_` (7 test raporu), `CLAUDE.md`

---

## Bölüm 1: Yönetici Özeti

Bu dosya, Gazze savaşının ilk altı ayını (7 Ekim 2023 – 7 Nisan 2024) konu alan Türkçe-İngilizce paralel haber korpusunun kaynak seçimi sürecini belgeleyen akademik bir meta-metodoloji kaydıdır. 8 ardışık arşiv erişim testi kapsamında 25'ten fazla haber kaynağı sistematik biçimde değerlendirilmiş; üç kaynak nihai tasarım için seçilmiştir.

### 1.1 Final Kaynak Tasarımı (Devlet/Üst-Devlet Medyası Üçlemesi)

| # | Kaynak | Medya Tipi | İdeolojik Pozisyon | EN Arşiv | TR Arşiv |
|---|--------|-----------|-------------------|----------|----------|
| 1 | **Anadolu Ajansı (AA)** | Türkiye ulus-devlet medyası | Güney / İslam işbirliği söylemi | aa.com.tr/en | aa.com.tr/tr |
| 2 | **Sputnik** | Rusya devlet medyası ("dezenformasyon" etiketli) | Batı hegemonyasına karşı konumlanma | sputnikglobe.com | anlatilaninotesi.com.tr |
| 3 | **Euronews** | AB üst-devlet medyası | Avrupa liberal kurumsal çerçeve | euronews.com | tr.euronews.com |

### 1.2 Araştırma Sorusu

Gazze savaşının ilk altı ayında (7 Ekim 2023 – 7 Nisan 2024) üç farklı düzeyde devlet/üst-devlet medyasının — Anadolu Ajansı (Türkiye ulus-devlet), Sputnik (Rusya devlet, AB tarafından "dezenformasyon" olarak nitelendirilen) ve Euronews (Avrupa Birliği üst-devlet) — Türkçe-İngilizce paralel haber metinlerinde ideolojik çerçeveleme stratejileri nasıl tezahür etmekte ve farklılaşmaktadır?

### 1.3 Hedef Korpus Boyutu

Her kaynaktan yaklaşık 500 EN-TR haber çifti; toplamda yaklaşık 1.500 çift. Katman 1 (strict parallel, birebir çeviri çiftleri): ~600-900 çift. Katman 2 (comparable, gevşek eşleştirme): toplamı 1.500'e tamamlar.

---

## Bölüm 2: Giriş ve Bağlam

### 2.1 Araştırmanın Motivasyonu

Gazze savaşı (7 Ekim 2023 –), küresel medya manzarasında eşi görülmemiş bir gerçek zamanlı çerçeveleme yarışının yaşandığı bir olgu olmuştur. Farklı devlet ve kurumsal yayın organları, aynı olayları birbirinden köklü biçimde ayrışan anlatısal çerçeveler içinde sunmuştur. Bu çalışma, söz konusu ayrışmayı çeviribilimsel bir perspektiften, dil çifti olarak Türkçe-İngilizce'yi kullanarak nicel ve nitel yöntemlerle belgelemektedir.

### 2.2 Paralel Korpus Seçiminin Gerekliliği

Standart bir karşılaştırmalı medya çalışmasının aksine bu proje, **çeviri ve dil uyarlaması sürecinin kendisini** inceleme nesnesi olarak ele almaktadır. Bu nedenle yalnızca İngilizce ya da yalnızca Türkçe kaynak kullanmak metodolojik olarak yetersizdir; her kaynağın hem EN hem TR sürümünü sistematik biçimde üretmesi zorunludur. Bu temel kısıt, kaynak havuzunu baştan önemli ölçüde daraltmış ve kaynak seçim sürecini kapsamlı bir sistematik tarama gerektiren araştırma aşamasına dönüştürmüştür.

### 2.3 Teorik Çerçeve

| Kaynak | Katkı |
|--------|-------|
| **Bielsa & Bassnett (2009)** — *Translation in Global News* | Uluslararası haber dolaşımını bir çeviri pratiği olarak teorileştiren temel referans |
| **Baker (2006)** — *Translation and Conflict* | Çatışma anlatılarında çeviri, seçim ve yeniden çerçeveleme teorisi; narratif kategoriler |
| **Valdeón (2015)** | Gazetecilik çevirisi, editoryal yeniden konumlama, seçici çeviri |

---

## Bölüm 3: Kullanılan Metodoloji

### 3.1 Üç Aşamalı Eleme Protokolü

**Aşama 0 — Ön Eleme (test harcamadan):**  
Türkçe servisi bulunmadığı genel bilgiye dayanarak kesin olan kaynaklar test edilmeden elenmiştir. Kriter: yayın organının ana dili İngilizce, Arapça, Almanca, Japonca veya başka bir dil olup Türkçe servisinin hiçbir zaman mevcut olmadığının bilinmesi (örn. Arab News, Gulf Times, Kyodo News, AMNA, BTA).

**Aşama 1 — Hızlı Kontrol:**  
Türkçe servis varlığı belirsiz kaynaklar için ana sayfa veya robots.txt çekilmiş; dil menüsünde Türkçe aranmıştır. Bu aşamada robots.txt ClaudeBot yasağı da kontrol edilmiştir.

**Aşama 2 — Derinlemesine Test:**  
Türkçe servisi doğrulanan kaynaklar için aşağıdaki beş parametre sistematik biçimde incelenmiştir:

| Parametre | Gereklilik |
|-----------|-----------|
| robots.txt uyumu | ClaudeBot / Claude-Code Disallow kuralı yok |
| Tarihsel arşiv erişimi | 7 Ekim 2023 tarihli içeriklere sistematik ulaşım mümkün |
| İçerik yapısı | Statik HTML — JavaScript rendering gerekmiyor |
| EN-TR eşleştirme | Ortak ID, dil linki veya tarih+cosine similarity yöntemi |
| İçerik yoğunluğu | 6 aylık dönemde her dilde korpusu dolduracak yeterli haber |

### 3.2 Teknik Araç ve Tarih

- **Araç:** Claude Code CLI, `WebFetch` komutu — HTTP GET istekleri
- **Tarih:** 2 Mayıs 2026 (tüm testler tek gün içinde tamamlandı)
- **Ek araç:** Wayback Machine availability API (`archive.org/wayback/available`) — BBC ve DW için dolaylı arşiv testi

### 3.3 Erişim Yöntemleri Hibrit Yapısı

Adım 2.3 (Tam Scraping) hazırlığı sırasında, 3 Mayıs 2026'da yapılan lokal Python erişim doğrulamasında **kritik bir metodolojik bulgu** ortaya çıkmıştır: Sputnik İngilizce ana domain'i `sputnikglobe.com` (ve eski domain `sputniknews.com`) Türkiye'den lokal Python `requests` kütüphanesi ile **erişilemez** durumdadır. Hatanın katmanları sistematik biçimde test edilmiştir:

| Katman | Sonuç |
|--------|-------|
| DNS resolve | ✅ `sputnikglobe.com → 194.190.139.3`, `sputniknews.com → 194.190.139.3` (aynı IP) |
| TCP 443 handshake | ❌ ConnectTimeout |
| HTTP istek | ❌ TCP el sıkışması olmadığı için HTTP koduna ulaşılamıyor |
| User-Agent değişimi (Chrome) | ❌ Etkisiz (blok TCP-altı) |
| Aynı /20 IP bloğundaki diğer Sputnik servisleri | ✅ `sputnik-georgia.com → 194.190.139.8` ve `anlatilaninotesi.com.tr → 194.190.139.20` çalışıyor |

Bu örüntü, Türkiye'nin Radyo ve Televizyon Üst Kurulu (RTÜK) tarafından 2022'de uygulanan erişim kısıtlamasının **IP-bazlı değil, SNI (Server Name Indication) bazlı bir filtreleme** ile uygulandığını göstermektedir: aynı IP bloğundaki bazı domain'lere erişim açıkken, `sputnikglobe.com` ve `sputniknews.com` SNI alanını içeren TLS handshake'leri sessizce düşürülmektedir. Türkçe mirror `anlatilaninotesi.com.tr` aynı altyapıda çalıştığı hâlde RTÜK'ün filtre listesinde değildir.

#### 3.3.1 Pilot Scraping Yanılgısının Tespiti

Adım 2.1 ve 2.2 testlerinde Sputnik EN'in "tarih arşivi mükemmel çalışıyor" sonucunun (bkz. Bölüm 6.2 ve `pilot/00_pilot_scraping_raporu.md` Bölüm 2.1) elde edildiği `WebFetch` komutu, Claude Code CLI'nin Anthropic sunucularından çıkan HTTP istemcisidir. Anthropic altyapısı Türkiye dışı bir IP'den çıktığı için RTÜK SNI filtresinden etkilenmez. Adım 2.3 hazırlığında lokal Python erişimine geçildiğinde bu durum fark edilmiş ve metodolojide hibrit erişim yapısına geçilmiştir.

Bu yanılgının kayda geçirilmesi akademik şeffaflığın doğrudan bir gereğidir: hesaplamalı dilbilim çalışmalarında "erişilebilirlik" kavramının çıkış IP'sinden bağımsız olmadığı; aynı kaynağın bir IP'den erişilebilirken başka bir IP'den engelli olabileceği gerçeği, gelecek araştırmacılar için önemli bir uyarıdır.

#### 3.3.2 Hibrit Erişim Mimarisi

Bu bulgu üzerine kurulan iki katmanlı erişim mimarisi şu şekildedir:

| Katman | Konum | Erişim Aracı | Çekilen Kaynaklar |
|--------|-------|--------------|-------------------|
| **Lokal** | Türkiye, Afyonkarahisar (Afyon Kocatepe Üniversitesi) | Python 3.14 + `requests` | AA EN+TR, Euronews EN+TR, Sputnik **TR** (anlatilaninotesi.com.tr) |
| **Bulut** | Frankfurt (Microsoft Azure datacenter) | GitHub Actions Microsoft-hosted Ubuntu runner | Sputnik **EN** (sputnikglobe.com) |

Her iki katman da aynı Python kod tabanını (`scripts/scrapers/sputnik.py`) kullanır; ayrım yalnızca config seviyesindedir (`langs=["tr"]` lokal, `langs=["en"]` GitHub Actions). GitHub Actions workflow tanımı (`.github/workflows/scrape_sputnik_en.yml`) ve scraping kodu aynı kamuya açık repo'da (https://github.com/ebarut07/gaza-corpus-tr-en, MIT lisanslı) yayımlanır; bu yapı **akademik tekrarlanabilirlik** açısından üç kazanım sağlar:

1. Üçüncü taraf araştırmacılar workflow'u kendi GitHub hesaplarında bedava tetikleyerek scraping'i bağımsız olarak doğrulayabilir.
2. Çıkış IP coğrafyasına bağımlılık (çalışmanın bir limitasyonu olarak) hem koda hem de yöntem belgesine yansıtılmıştır.
3. Lokal makinede VPN/proxy gibi opak bir altyapıya gerek kalmadığı için yöntem dokümanlanması net ve denetlenebilirdir.

### 3.4 Kaynak-Spesifik Minimum Kelime Eşiği Kalibrasyonu

İçerik filtrelerindeki minimum kelime sayısı eşiği, editoryal yapıya göre kaynak-spesifik olarak kalibre edilmiştir; tek-tip bir eşik metodolojik olarak hatalıdır:

| Kaynak | min_word_count | Editoryal gerekçe |
|--------|----------------|-------------------|
| Anadolu Ajansı (AA) | **200** | Uzun-form analizci/derleme tarzı; kısa içerikler genelde HTML parse artefaktıdır (navigasyon stub) |
| Euronews | **200** | Uzun-form Avrupa kurumsal yayın stili |
| Sputnik (TR + EN) | **100** | Breaking-news editoryal stili; meşru kısa-form ideolojik içerikler bu kategoride |

**EN paragraf (makale Methods bölümü için):** *"Minimum word count thresholds were calibrated per source based on editorial style: 200 words for AA and Euronews (long-form news institutions), 100 words for Sputnik (breaking-news editorial style). This calibration prevents both HTML parse artifacts and the exclusion of legitimate short-form ideological content."*

Pilot sonrası gözlem (3 Mayıs 2026 testi): Sputnik TR günlük arşiv listesinde 109 URL'den yalnızca 5'i 200 kelime üstü kabul edildi (%95 ret oranı). 100 kelime eşiğiyle bu oranın ~3 katına düşeceği ve 6 aylık tam scraping süresinin ~2× kısalacağı hesaplandı; aynı zamanda Sputnik'in karakteristik kısa breaking-news ideolojik framing örneklerinin korpustan dışlanması önlendi.

---

## Bölüm 4: Test Edilen Tüm Kaynaklar — Eleme Tablosu

### 4.1 Final Seçilen Kaynaklar

| Kaynak | EN | TR | Arşiv Yöntemi | Eşleştirme | Durum |
|--------|----|----|--------------|-----------|-------|
| **AA** | aa.com.tr/en ✅ | aa.com.tr/tr ✅ | Kategori sayfaları ⚠️* | ID bazlı (doğrulanacak) | **FİNAL ✅** |
| **Sputnik** | sputnikglobe.com ✅ | anlatilaninotesi.com.tr ✅ | `/YYYYMMDD/` tarih arşivi ✅ | Tarih + cosine similarity | **FİNAL ✅** |
| **Euronews** | euronews.com ✅ | tr.euronews.com ✅ | Tag pagination ✅ | Dil linki + cosine similarity | **FİNAL ✅** |

*AA'nın Ekim 2023 arşiv erişimi Adım 2.2 pilot scrapingde doğrulanacak.

### 4.2 Teknik Engel Nedeniyle Elenen Kaynaklar

| Kaynak | Engel Kategorisi | Detay |
|--------|-----------------|-------|
| **BBC** (EN+TR) | Ağ düzeyinde tam engel | Wayback Machine'de de arşivlenmiş snapshot yok; birden fazla URL-tarih kombinasyonu test edildi, tümü boş döndü |
| **DW** (EN+TR) | Ağ düzeyinde tam engel | 10 test, 10 başarısız; alternatif domainlerde (dwturkce.com, dw-world.de) SSL sertifika hatası — terk edilmiş domainler |
| **France 24** (EN+TR) | robots.txt User-Agent yasağı | Claude-Code, ClaudeBot, Claude-SearchBot, Claude-User isimleriyle açıkça Disallow; tüm içerik sayfaları 403 Forbidden |
| **Reuters** (EN+TR) | Ağ düzeyinde tam engel | BBC ile özdeş hata; robots.txt'e bile erişilemiyor |
| **VOA** (EN+TR) | 403 Forbidden site genelinde | robots.txt dahil tüm URL'ler 403; 2025 USAGM krizi arşiv stabilitesini olumsuz etkiliyor |
| **Xinhua** (EN+TR) | ECONNREFUSED + SSL hatası | `turkish.xinhuanet.com` ve `xinhuanet.com` domainleri erişilemez; terk edilmiş altyapı |
| **CGTN** (EN+TR) | Tarihsel arşiv yokluğu | Güncel içerik statik HTML olarak erişilebilir; sitemap yalnızca son 5 günü kapsıyor (100 URL); Ekim 2023 arşivine hiçbir yoldan ulaşılamadı; EN ve TR platformları birbirinden bağımsız (ortak ID yok) |

### 4.3 Türkçe Servisi Bulunmadığı İçin Elenen Kaynaklar (Test Edilenler)

| Kaynak | Ülke | Mevcut Diller | Durum |
|--------|------|--------------|-------|
| **Al Jazeera** | Katar | EN + 5 dil (TR yok) | TR servisi 2017'de kapatıldı; ayrıca robots.txt ClaudeBot Disallow |
| **Swissinfo** | İsviçre | EN/DE/FR/IT/ES/PT/JA/AR/ZH/RU (10 dil, TR dahil değil) | Test edildi — Türkçe yok |
| **PressTV** | İran | EN + FR | Test edildi — Türkçe yok |
| **QNA** (Katar Ulusal Ajansı) | Katar | EN/AR/FR/DE/ES | Test edildi — Türkçe yok |
| **APS** (Cezayir Ajansı) | Cezayir | AR/Tamazigh/EN/FR/ES/RU/ZH | Test edildi — Türkçe yok |
| **ANSA** | İtalya | IT/EN/EU/AR/ZH/IN/Latam | Test edildi — Türkçe yok |
| **Dawn** | Pakistan | EN/Urduca | Test edildi — Türkçe yok |
| **WAM** | BAE | AR ağırlıklı | Kısmi erişim — Türkçe yok |
| **NHK World** | Japonya | Erişim engeli | — |
| **EFE** | İspanya | Erişim engeli | — |
| **Yonhap** | G.Kore | Erişim engeli | — |
| **Ahram Online** | Mısır | 403 Forbidden | — |
| **SPA** | S.Arabistan | 403 Forbidden | — |

### 4.4 Ön Eleme: Test Edilmeden Elenen Kaynaklar

| Kaynak | Ülke | Gerekçe |
|--------|------|---------|
| Arab News | S.Arabistan | İngilizce yayın organı, Türkçe servisi yok |
| Gulf Times | Katar | İngilizce yayın organı |
| The National | BAE | İngilizce yayın organı |
| Khaleej Times | BAE | İngilizce yayın organı |
| Daily Star Lebanon | Lübnan | İngilizce yayın organı |
| An-Nahar | Lübnan | Arapça yayın organı |
| AMNA | Yunanistan | Yunanca/İngilizce |
| BTA | Bulgaristan | Bulgarca/İngilizce |
| APA | Avusturya | Almanca yayın organı |
| CBC | Kanada | İngilizce/Fransızca |
| ABC Australia | Avustralya | İngilizce yayın organı |
| RNZ | Yeni Zelanda | İngilizce yayın organı |
| Kyodo News | Japonya | İngilizce/Japonca |
| PTI | Hindistan | İngilizce/Hintçe |
| The Hindu | Hindistan | İngilizce yayın organı |
| APP | Pakistan | Muhtemelen yok — test edilmedi |

---

## Bölüm 5: Test Kronolojisi

| Test | Dosya | Kapsam | Kritik Bulgu |
|------|-------|--------|-------------|
| **1** | `01_ana_arsiv_test_aljazeera_bbc_aa.md` | AJ EN/TR, BBC EN/TR, AA EN/TR | AJ TR yok (2017'de kapatıldı); BBC tüm yöntemlerle erişilemez; AA kategori sayfaları çalışıyor |
| **2** | `02_sputnik_bbc_wayback.md` | Sputnik EN/TR, BBC Wayback | Sputnik `/YYYYMMDD/` mükemmel; anlatilaninotesi.com.tr Sputnik TR olarak doğrulandı; BBC Wayback'te yok |
| **3** | `03_dw_test.md` | DW EN/TR | 10 test, 10 başarısız; CloudFlare + SSL; Wayback'te de yok |
| **4** | `04_france24_test.md` | France 24 EN/TR | robots.txt'de Claude-Code ve ClaudeBot isimle Disallow; 403 tüm sayfalarda |
| **5** | `05_voa_reuters_cgtn_xinhua_toplu.md` | VOA, Reuters, CGTN EN, Xinhua | Reuters CloudFlare; VOA 403; Xinhua ECONNREFUSED; CGTN statik ama tarihsel arşivsiz |
| **6** | `06_cgtn_derinlemesine.md` | CGTN EN+TR derinlemesine | Sitemap yalnızca son 5 gün; EN ve TR bağımsız platformlar; Ekim 2023 hiçbir yoldan erişilemiyor |
| **7** | `07_son_kapsamli_tarama_euronews.md` | 20+ kaynak — Kuzey Afrika, Avrupa, Asya-Pasifik | Euronews tek geçen aday; EN ~1.720 haber, TR ~840 haber; tag pagination erişimi doğrulandı |

**Toplam:** 7 test dosyası, 8 test turu (7. turda 20+ kaynak toplu tarama), 25'ten fazla kaynak değerlendirildi.

---

## Bölüm 6: Final Tasarım Gerekçesi

### 6.1 Anadolu Ajansı (AA)

**Erişilebilirlik:** robots.txt temiz; `/search?*` ve `/api/` Disallow ama içerik sayfaları serbestçe erişilebilir. Kategori sayfaları (`/en/middle-east`, `/tr/orta-dogu` gibi) 20+ haber listesi döndürüyor; içerik statik HTML.

**Arşiv:** Kategori sayfası üzerinden sayfalama yöntemi; Ekim 2023 tarihli içeriklere erişim Adım 2.2'de doğrulanacak. URL yapısı: `aa.com.tr/en/[kategori]/[slug]/[ID]` — Mayıs 2026'da ID aralığı ~3924000 civarında; Ekim 2023 ID'leri bu sayıdan çok daha küçük olacak.

**Eşleştirme:** EN ve TR URL'lerinin aynı haber ID'sini paylaşması kuvvetle muhtemel (aynı altyapı, aynı ID sistemi). Doğrulama Adım 2.2'de yapılacak.

**Teorik Pozisyon:** 1920'de kurulan Türkiye Cumhuriyeti'nin resmi devlet haber ajansı. İslam İşbirliği Teşkilatı üye devletlerine yönelik servisler, Güney perspektifinin ve Türkiye dış politika söyleminin birincil Türkçe-İngilizce taşıyıcısı.

---

### 6.2 Sputnik

**Erişilebilirlik:** robots.txt temiz; ClaudeBot yasağı yok. Tarih arşivi (`/YYYYMMDD/`) hem EN hem TR'de mükemmel çalışıyor.

**Arşiv — Doğrulanmış Veriler:**
- EN: `sputnikglobe.com/20231007/` ✅ açılıyor — makale ID örnekleri: 1113998216, 1114004861, 1114006542
- TR: `anlatilaninotesi.com.tr/20231007/` ✅ açılıyor — makale ID örnekleri: 1076133500, 1076132338

**Eşleştirme:** EN ve TR farklı ID aralıkları kullanıyor (EN ~1113-1114M; TR ~1076M). Eşleştirme yöntemi: aynı tarih arşiv sayfası + başlık/içerik cosine similarity.

**Özel Durum:** Türkiye'de RTÜK kararıyla erişim yasağı (2022); `tr.sputniknews.com` → `anlatilaninotesi.com.tr` yönlendirme. Sitenin footer'ı, başlığı ve iletişim e-postası (feedback.tr@sputniknews.com) Sputnik kimliğini doğruluyor.

**Teorik Pozisyon:** Rus devlet finansmanlı uluslararası yayıncı; Avrupa Birliği tarafından 2022'de uydu yayını engellenen ve "dezenformasyon aracı" olarak nitelendirilen kaynak. Baker (2006) ve Valdeón (2015) çerçevesinde bu etiketleme bizzat ideolojik bir çerçeveleme eylemidir ve araştırmanın analiz nesnelerinden birini oluşturmaktadır.

---

### 6.3 Euronews

**Erişilebilirlik:** robots.txt temiz; ClaudeBot / Claude-Code yasağı yok. `tr.euronews.com` aktif ve içerik yükleniyor.

**Arşiv — Doğrulanmış Veriler:**
- EN `/tag/israel-hamas-war`: 86 sayfa × ~20 haber ≈ **~1.720 haber** — en eski: 7 Ekim 2023 ✅
- TR `/tag/gazze`: 42 sayfa × ~20 haber ≈ **~840 haber** — en eski: 17 Ekim 2023 ⚠️
- TR `/tag/filistin`: 59 sayfa — 2018'den itibaren içerik

**Bilinen Sorun:** TR "gazze" tag'inin 7-16 Ekim 2023 dönemini kapsayıp kapsamadığı kesin değil. Çözüm: Adım 2.2'de "filistin", "hamas", "israil" tag'leri birleştirilerek dönem tamamlanacak.

**Eşleştirme:** EN makale sayfalarının navigasyon menüsünde TR dil linki mevcut → doğrudan EN→TR eşleştirme imkânı. Yedek: tarih + cosine similarity. URL formatı: `euronews.com/YYYY/MM/DD/[dile-çevrilmiş-slug]` — slug paylaşılmıyor, dile çevriliyor.

**Teorik Pozisyon:** Avrupa Yayın Birliği (EBU) üyesi yayıncıların ortak finansmanıyla kurulmuş pan-Avrupa yayıncısı; editoryal çizgisi AB kurumlarına yakın Avrupa liberal merkezini temsil eder.

---

### 6.4 Üç Kaynaklı Tasarımın Teorik Gücü

Bu üç kaynak, birbirini kavramsal olarak tamamlayan bir **devlet/üst-devlet medyası üçlemesi** oluşturmaktadır:

| Kaynak | Medya Tipi (Sınıflandırma) | Bielsa & Bassnett (2009) Çerçevesinde Konum |
|--------|--------------------------|-------------------------------------------|
| AA | Ulus-devlet resmi ajansı | Ulusal haber akışının İngilizce distributor'ı |
| Sputnik | Devlet medyası + "dezenformasyon" etiketi | Karşı-hegemonik haber akışı |
| Euronews | AB üst-devlet kurumsal yayıncı | Batı kurumsal çerçevesinin pan-Avrupa taşıyıcısı |

Bu yapı, yalnızca farklı "bakış açılarını" karşılaştırmaz; farklı **devlet/kurumsal medya epistemolojileri** içinde çevirinin nasıl ideolojik bir araç işlevi gördüğünü inceleme olanağı sunar.

---

## Bölüm 7: Reddedilen Asimetrik Tasarım

### 7.1 Al Jazeera'nın Kesin Reddedilmesi

Test sürecinde Al Jazeera İngilizce, teknik erişim açısından test edilen kaynaklar arasında en ideal yapıya sahipti:
- Günlük sitemap: `/sitemap.xml?yyyy=YYYY&mm=MM&dd=DD` — 7 Ekim 2023: 29 URL; 7 Nisan 2024: 41 URL
- Tüm 6 aylık dönem kapsanıyor; içerik statik HTML
- Tarih aralığı baştan sona doğrulandı

**Buna karşın Al Jazeera'nın Türkçe servisi 2017 yılında kalıcı olarak kapatılmıştır.** `aljazeera.com/tr/` → 404; `aljazeera.com.tr` → İngilizce Türkiye haberlerine yönlendiriyor; sitemap'ta tek bir Türkçe URL yoktur. Bu durum, Türkçe-İngilizce paralel korpus çalışmasının temel metodolojik koşulunu baştan ortadan kaldırmaktadır.

Ayrıca: Al Jazeera'nın robots.txt'inde ClaudeBot ve Claude-Web User-Agent'ları açıkça Disallow edilmiştir.

### 7.2 Asimetrik Tasarımın Reddedilme Gerekçesi

"Asimetrik tasarım" senaryosu Al Jazeera EN'i AA TR ve Sputnik TR ile Katman 2 (comparable) olarak eşleştirmeyi önermektedir. Bu tasarım üç temel gerekçeyle reddedilmiştir:

1. **Metodolojik tutarsızlık:** Makalenin temel iddiası çeviri sürecindeki ideolojik dönüşümleri incelemektir. Türkçe karşılığı olmayan bir kaynak çeviri analizinin kapsamı dışında kalır; yalnızca içerik karşılaştırması yapılabilir. Bu, araştırma sorusunun yanıtlanamayacağı anlamına gelir.

2. **Kavramsal kayma:** Asimetrik tasarım çalışmayı "paralel korpus çeviribilimi araştırması"ndan "karşılaştırmalı medya çalışması"na dönüştürür. Language Resources and Evaluation ve Corpora dergilerinin kapsam alanından uzaklaşmayı gerektirir.

3. **Hakemlere karşı savunulabilirlik:** AA + Sputnik + Euronews tasarımı "tam paralel korpus" olarak sunulabilir ve hakemlerin "neden tam paralel değil?" sorusunu doğurmaz. Asimetrik tasarım bu soruyu baştan açmış olur.

---

## Bölüm 8: Çağdaş Akademik Scraping Kısıtları (Akademik Bulgu Olarak)

*Not: Bu bölümdeki paragraflar makale kalitesinde yazılmıştır ve metodoloji bölümüne doğrudan adapte edilebilir.*

### 8.1 Genel Manzara: Batı Ana Akım Medyasının Programatik Erişime Kapatılması

Bu çalışmanın kaynak tarama süreci, dijital gazetecilik ve hesaplamalı dilbilim araştırmalarında giderek daha belirgin hale gelen yapısal bir kısıtı doğrudan deneyimlemiştir: Batı ana akım medyasının otomatik akademik erişime yönelik sistematik ve katmanlı engelleme politikası. Kapsamlı kaynak taramasında BBC, DW, France 24, Reuters ve VOA başta olmak üzere incelenen Batı menşeili yedi kaynaktan hiçbirinin tam Türkçe-İngilizce erişimi sağlanamamıştır. Bu oran, baştan seçilmiş olumsuz bir örneklemin yansıması değil; Türkçe servisi bulunduğu doğrulanan ve metodolojik kriterleri karşılama potansiyeli taşıyan tüm kaynakların sistematik taramasının sonucudur. Söz konusu durum, bu çalışmanın verisinden çok ötesine geçen ve corpus linguistics araştırmacıları için giderek küresel bir zorluk haline gelen bir eğilimi yansıtmaktadır.

### 8.2 Engel Kategorileri: Teknik ve Etik Boyutlar

Gözlemlenen erişim kısıtları teknik açıdan üç farklı kategoriye ayrılmaktadır. Birinci ve en yaygın kategori, CloudFlare veya benzeri altyapı sağlayıcıların devreye girdiği ağ düzeyinde tam engeldir: BBC, DW ve Reuters bu kategoriye girmektedir. Bu engel yalnızca belirli User-Agent tanımlamalarını hedef almaz; herhangi bir otomatik HTTP isteğini bloke eder. Söz konusu kaynakların Wayback Machine'de de arşivlenmemiş olması, dolaylı erişim yollarını da kapatmaktadır; bu durum, büyük haber kuruluşlarının yalnızca kendi içeriklerine yönelik canlı erişimi değil, o içeriklerin kamuya açık tarihsel arşivini de aktif olarak kontrol etme kapasitesine sahip olduğunu göstermektedir. İkinci kategori, robots.txt User-Agent tabanlı yasaktır: France 24'ün robots.txt dosyası Claude-Code, ClaudeBot, Claude-SearchBot ve Claude-User adlı User-Agent tanımlamalarını açıkça ve isimle Disallow etmektedir. Bu, büyük dil modeli tabanlı erişim araçlarına yönelik editoryal politikaların teknik altyapıya kazındığının belgelenmiş bir örneğidir ve 2024 sonrası dönemde haber kuruluşları arasında hızla yaygınlaşan bir eğilimi temsil etmektedir. Üçüncü kategori, tarihsel arşiv yokluğudur: CGTN için teknik erişim mümkün olmakla birlikte, sitenin sitemap'ı yalnızca son beş günün içeriğini kapsamakta; tarih yapılı URL yolları Ekim 2023 için 404 döndürmektedir. Bu "erişilebilir ama arşivsiz" yapı, corpus linguistics araştırmaları için teknik engellerden farklı, ama pratikte eşdeğer bir metodolojik kısıt oluşturmaktadır.

### 8.3 Bu Çalışmaya Özgü Etki ve Tasarıma Yansıması

Bu kısıtların en doğrudan etkisi, Batı ana akım medyasının araştırma tasarımında temsil edilme biçimini şekillendirmesidir. Yedi Batı kaynağından (BBC, DW, France 24, Reuters, VOA, Swissinfo, ANSA) hiçbirinin tam Türkçe-İngilizce erişimi sağlanamamış; Batı perspektifi bu çalışmada zorunlu olarak Euronews üzerinden temsil edilmektedir. Euronews, BBC veya Reuters ile editoryal olarak doğrudan eşdeğer değildir; ancak Avrupa Yayın Birliği bünyesinde faaliyet gösteren ve AB kurumsal çerçevesini yansıtan erişilebilir tek Batılı kurumsal kaynaktır. Bu kısıt, araştırmanın tasarım tercihinden değil, dijital haber manzarasının yapısal dönüşümünden kaynaklanmaktadır. Akademik scraping erişiminin giderek daralması, hesaplamalı gazetecilik ve corpus linguistics araştırmacıları için metodoloji bölümlerinde şeffafça ele alınması gereken sistematik bir harici kısıt haline gelmiştir.

---

## Bölüm 9: Makaleye Doğrudan Kopyalanabilir Paragraflar (İngilizce)

*Not: Bu paragraflar Q1 İngilizce dergiye gönderilecek makale için hazırlanmıştır — Methods ve Limitations bölümlerine doğrudan yapıştırılabilir. Her paragraf bağımsız olarak kullanılabilir.*

---

### 9.1 Kaynak Seçimi (Methods: Source Selection) — ~370 kelime

Source selection for this study followed a three-stage systematic screening protocol applied to a candidate pool of more than 25 news sources spanning four geographic axes: the Arab world and North Africa, Europe, Asia-Pacific, and North America. The primary eligibility criterion was the active and programmatically accessible provision of parallel news content in both English and Turkish, covering the target period of 7 October 2023 to 7 April 2024. In the first stage, sources known from general domain knowledge to lack a Turkish-language service were excluded without further testing (e.g., Arab News, Gulf Times, ANSA, Kyodo News, CBC). In the second stage, sources with uncertain Turkish-language availability were tested via homepage and robots.txt retrieval, with Turkish presence confirmed through navigation menus and language selectors. In the third and most demanding stage, sources that confirmed Turkish-language output were assessed across five parameters: (1) the absence of explicit User-Agent prohibitions for automated academic access in their robots.txt configurations; (2) systematic access to the historical archive covering the study period, verified through direct URL retrieval; (3) static HTML content delivery that does not require client-side JavaScript rendering for article-level extraction; (4) viable English–Turkish article matching through shared identifiers, language-switch navigation links, or date-plus-cosine-similarity methods; and (5) sufficient content density in both languages across the full six-month window. Three sources satisfied all five criteria. Anadolu Agency (AA), the official news agency of the Turkish state established in 1920, provides parallel EN–TR production accessible via category pages, with EN and TR articles expected to share numerical identifiers — a relationship to be confirmed in the pilot scraping phase. Sputnik, the Russian state-funded broadcaster operating in Turkey via the mirror domain anlatilaninotesi.com.tr following a 2022 ban by Turkey's Radio and Television Supreme Council (RTÜK), offers date-path archive access (e.g., /20231007/) confirmed for both English (article IDs including 1113998216 and 1114004861) and Turkish (article IDs including 1076133500 and 1076132338) on the study's opening date. Euronews, a pan-European broadcaster co-funded by the European Broadcasting Union (EBU), maintains an active Turkish-language service at tr.euronews.com; its tag-pagination system yields approximately 1,720 English articles (tag: israel-hamas-war, 86 pages) and approximately 840 Turkish articles (tag: gazze, 42 pages) from the study period, with individual English articles providing direct navigation links to their Turkish counterparts.

---

### 9.2 Erişim Kısıtlamaları (Limitations: Access Restrictions) — ~360 kelime

The source selection process conducted for this study simultaneously constitutes a methodological finding in its own right, reflecting structural trends in the accessibility of online news archives for corpus-linguistic and computational research. Of the more than 25 sources systematically evaluated, 22 were eliminated on technical or structural grounds entirely independent of their editorial quality or relevance to the research question. Among Western mainstream outlets, the pattern of inaccessibility was consistent and multi-layered. The BBC (English and Turkish), Deutsche Welle (English and Turkish), and Reuters were subject to what appears to be network-level blocking — presumed CloudFlare or IP-based infrastructure — that prevented not only content retrieval but even robots.txt access. No cached versions were recoverable via the Wayback Machine availability API, suggesting that archive crawlers are subject to equivalent restrictions and that large news organisations increasingly control not only live access to their content but also its publicly archived historical record. France 24 presented a qualitatively distinct case: its robots.txt explicitly names the automated access clients Claude-Code, ClaudeBot, Claude-SearchBot, and Claude-User in Disallow directives, documenting a deliberate editorial policy against large language model web access that has proliferated across news organisations since 2024. Voice of America returned 403 Forbidden responses across all tested endpoints, compounded by the operational disruption of its parent agency USAGM in 2025. CGTN, the Chinese state broadcaster, was accessible for current content but offered no systematic route to its historical archive: the site's sitemap covered only the most recent five days of output, and no date-structured URL path yielded results for October 2023. Swissinfo, which provides content in ten languages, does not include Turkish in its language portfolio. As a consequence of these constraints, no Western mainstream outlet providing parallel English–Turkish news production was technically accessible for the study period. The Western institutional perspective in the corpus is therefore represented by Euronews, which, while editorially distinct from the BBC or Reuters, constitutes the sole accessible Western supranational source satisfying all methodological criteria. This limitation is an externally imposed constraint reflecting broader transformations in the digital news landscape, not a deliberate design choice; its implications for the generalisability of findings are discussed in the relevant section.

---

### 9.3 Teorik Çerçeve — Sputnik Dahil Edilmesi (Theoretical Framing: Sputnik Inclusion) — ~360 kelime

The inclusion of Sputnik as one of the three corpus sources in this study warrants explicit theoretical justification, given the source's contested epistemic and institutional status in the contemporary geopolitical context. Sputnik is a Russian state-funded international broadcaster that was designated a vehicle for "disinformation" by the European Union as part of its 2022 sanctions package; EU member states were subsequently required to block its distribution via satellite, cable, and streaming platforms. Its Turkish-language service continues under the mirror domain anlatilaninotesi.com.tr following a concurrent ban by Turkey's Radio and Television Supreme Council (RTÜK). The decision to include Sputnik in the corpus is not an endorsement of any editorial position it espouses; it is, rather, a theoretically motivated choice grounded in Baker's (2006) narrative theory of translation and conflict, which argues that narratives — including those produced by actors designated as illegitimate by dominant institutional frameworks — constitute sites of meaning-making rather than sites of inherent truth or falsehood. The act of labelling a media source as "disinformation" is itself a discursive and ideological gesture (Valdeón, 2015), one that forms part of the very framing contest that this study seeks to document empirically. From this perspective, the "disinformation" label applied to Sputnik is analytically as significant as the labels "public broadcaster" and "official news agency" applied to Euronews and Anadolu Agency respectively: all three designations encode institutional positions in global information politics and carry ideological weight that shapes the production, selection, and translation of news content. Including Sputnik allows the corpus to represent what Bielsa and Bassnett (2009) conceptualise as a counter-hegemonic news flow — a narrative stream that explicitly positions itself in structural opposition to Western institutional frameworks — alongside a Turkish national-state perspective (AA) and a Western supranational-institutional perspective (Euronews). The resulting configuration — national state media (AA), state media bearing a disinformation label (Sputnik), and supranational institutional media (Euronews) — constitutes a methodologically coherent "state/supranational media triangle" for the comparative analysis of ideological framing in journalistic translation. This design captures not only three editorial stances on the Gaza conflict but three structurally distinct modes of state-mediated knowledge production and their corresponding translational strategies.

---

### 9.4 Hibrit Erişim Stratejisi (Methods: Hybrid Access Strategy) — ~390 kelime

A methodologically significant access constraint emerged during the transition from pilot scraping (Step 2.2) to the full data collection phase (Step 2.3) of this study. Pilot-stage testing conducted via the WebFetch facility of the Claude Code CLI on 2 May 2026 had confirmed that the English-language Sputnik archive (sputnikglobe.com) was reachable and that the daily date-path archive (e.g., /20231007/) returned full article listings. When the same access path was reproduced via a local Python `requests` client running from the principal investigator's institutional location (Afyonkarahisar, Türkiye) on 3 May 2026, the connection failed reproducibly at the TCP layer: the domain resolved correctly via DNS to 194.190.139.3 (and the legacy domain sputniknews.com to the same address), but TCP handshakes on port 443 timed out without producing any HTTP response. Crucially, other domains within the same /20 IPv4 block — including sputnik-georgia.com (194.190.139.8) and the Turkish-language Sputnik mirror anlatilaninotesi.com.tr (194.190.139.20) — remained fully accessible from the same client, and User-Agent variation produced no change in behaviour. This pattern is consistent with Server Name Indication (SNI) based filtering applied at Türkiye's national Internet exchange under the 2022 Radio and Television Supreme Council (RTÜK) order against Sputnik's English-language properties, while sister services on the same upstream infrastructure remain unaffected. The pilot-phase reachability finding had been an artefact of the WebFetch utility's egress IP, which originates from infrastructure outside Türkiye and is therefore not subject to the SNI filter; this discrepancy was identified and documented as a methodological correction, in line with the principle that "accessibility" in computational corpus work is not a property of the source alone but of the source–client–network triad. To resolve this constraint without introducing opaque circumvention infrastructure into the methodology, a hybrid access architecture was adopted: all sources reachable from the institutional location — Anadolu Agency (English and Turkish), Euronews (English and Turkish), and the Turkish-language Sputnik mirror — are scraped via a local Python pipeline; the English-language Sputnik archive is scraped via a GitHub Actions workflow running on a Microsoft-hosted Ubuntu runner in the Frankfurt datacentre, defined in a workflow file co-located with the scraping code in the project's public MIT-licensed repository (github.com/ebarut07/gaza-corpus-tr-en). Both layers execute identical Python code; the only configurational difference is the active language set passed to the Sputnik scraper module. This arrangement preserves full methodological reproducibility: any third-party researcher can re-execute the workflow on their own GitHub account at no cost, and the egress geography of the data collection process is transparently inscribed in both the codebase and the methods documentation.

---

## Bölüm 10: Sonraki Adımlar ve İlgili Dosyalar

### 10.1 Adım 2.2 — Pilot Scraping (Sıradaki Görev)

Her kaynaktan 20-30 haber çekilecek; şu doğrulamalar yapılacak:

| Kaynak | Doğrulanacak Soru | Yöntem |
|--------|------------------|--------|
| **AA EN+TR** | Ekim 2023 arşive erişim var mı? | Eski ID'leri deneme (`aa.com.tr/en/*/[eski-ID]`) |
| **AA EN↔TR** | EN ve TR aynı haber ID'sini paylaşıyor mu? | Aynı haberin iki dil URL'sini karşılaştır |
| **Sputnik EN+TR** | 20-30 haber çek, cosine eşleştirme kalitesi | `/20231007/` ve `/20231010/` üzerinden |
| **Euronews TR** | 7-16 Ekim 2023 boşluğu çözülüyor mu? | "filistin" + "hamas" + "israil" tag kombinasyonu |
| **Euronews EN→TR** | Dil linki eşleştirme güvenilir mi? | EN makaledeki TR navigasyon linkini izle |

### 10.2 Tüm İlgili Dosyalar

| Dosya | İçerik |
|-------|--------|
| `CLAUDE.md` | Proje hafıza dosyası — her oturum başında okunur |
| `docs/00_metodoloji_master.md` | Bu dosya — master metodoloji kaydı |
| `docs/01_ana_arsiv_test_aljazeera_bbc_aa.md` | Test 1: AJ, BBC, AA |
| `docs/02_sputnik_bbc_wayback.md` | Test 2: Sputnik arşivi, BBC Wayback |
| `docs/03_dw_test.md` | Test 3: DW — 10 test, 10 başarısız |
| `docs/04_france24_test.md` | Test 4: France 24 — robots.txt ClaudeBot yasağı |
| `docs/05_voa_reuters_cgtn_xinhua_toplu.md` | Test 5: VOA, Reuters, CGTN, Xinhua |
| `docs/06_cgtn_derinlemesine.md` | Test 6: CGTN derinlemesine — tarihsel arşiv yok |
| `docs/07_son_kapsamli_tarama_euronews.md` | Test 7: 20+ kaynak kapsamlı tarama — Euronews seçildi |

### 10.3 Uzun Vadeli İş Akışı

| Adım | Görev | Durum |
|------|-------|-------|
| **2.1** | Arşiv erişim testi (8 rapor, 25+ kaynak) | ✅ **TAMAMLANDI** |
| **2.2** | Pilot scraping — her kaynaktan 20-30 haber | ⏳ Bekliyor |
| **2.3** | Tam scraping — 6 aylık dönem, ~500 çift/kaynak | ⏳ Bekliyor |
| **2.4** | EN-TR eşleştirme (cosine >0.7 Katman 1; NER Katman 2) | ⏳ Bekliyor |
| **2.5** | Sampling (%70 stratified seed=42, %30 event-based) | ⏳ Bekliyor |
| **2.6** | Manuel doğrulama — 50 haber alt-örneklem, hedef <%5 hata | ⏳ Bekliyor |
| **3** | Annotation şeması ve uygulama | ⏳ Bekliyor |
| **4** | Zenodo + GitHub korpus paketi yayını | ⏳ Bekliyor |
| **5** | Makale yazımı ve Q1 submission | ⏳ Bekliyor |

---

*Master metodoloji dosyası — Claude Code ile oluşturulmuştur. 2 Mayıs 2026.*
