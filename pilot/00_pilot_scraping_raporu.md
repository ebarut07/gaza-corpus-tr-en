# Pilot Scraping Raporu — Adım 2.2
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu — Q1 Makale  
**Kapsam:** AA, Sputnik, Euronews — 7 Ekim 2023 – 7 Nisan 2024 aralığından pilot çekim  
**Toplam çekilen dosya:** 29 JSON (Sputnik: 9, Euronews: 4, AA: 15 + 1 format-test)

---

## 1. Çekilen Haber Sayıları

| Kaynak | EN | TR | Toplam | Tarih Aralığı |
|--------|----|----|--------|---------------|
| **Sputnik** | 5 | 4 | 9 | 7 Eki 2023 + 17 Eki 2023 |
| **Euronews** | 1 | 3 | 4 | 7 Eki 2023 + 17 Eki 2023 |
| **AA** | 10 | 5 | 15 | 7 Eki – 11 Kas 2023 (EN); 7–15 Eki 2023 (TR) |
| **AA test** | 1 | 0 | 1 | 2 May 2026 (format doğrulama — hedef dışı) |
| **TOPLAM** | 17 | 12 | **29** | — |

---

## 2. Kaynak Bazında Erişim Durumu

### 2.1 Sputnik — ✅ SORUNSUZ

| Test | Sonuç |
|------|-------|
| EN Oct 7 2023 arşivi | ✅ `sputnikglobe.com/20231007/` açılıyor, 7+ Gazze haberi listeleniyor |
| TR Oct 7 2023 arşivi | ✅ `anlatilaninotesi.com.tr/20231007/` açılıyor, 11+ Gazze haberi |
| EN Oct 17 2023 arşivi | ✅ Al-Ahli hastane haberi doğrulandı (ID: 1114268312) |
| TR Oct 17 2023 arşivi | ✅ Listelendi (fetch edilmedi ama arşiv yapısı identik) |
| İçerik statik HTML mi? | ✅ Evet |
| Türkçe karakter kalitesi | ✅ Mükemmel (ş, ğ, ı, ü vb. sorunsuz) |
| Konu filtresi uyumu | ✅ Tüm çekilen haberler askeri/insani/diplomatik kapsama giriyor |

**Sputnik için hiçbir teknik sorun saptanmadı.** Tam scraping doğrudan uygulanabilir.

---

### 2.2 Euronews — ✅ KAPSAMLI TEST TAMAMLANDI

#### 7-16 Ekim 2023 Boşluğu — KRİTİK SONUÇ: ✅ KAPANDI

| Test | Sonuç |
|------|-------|
| TR `/tag/gazze` p=42 (son sayfa) | Oldest: **16-17 Ekim 2023** — Boşluk var |
| TR `/tag/hamas` p=23 | **7 Ekim 2023 haberleri mevcut** ✅ |
| TR Oct 7 haberleri listesi | 3 makale doğrulandı (URL'ler alındı) |
| TR Oct 8 haberleri listesi | 3 makale doğrulandı (URL'ler alındı) |
| TR Oct 9-12 haberleri | `/tag/hamas` p=22'de mevcut |

**Sonuç:** TR'de 7-16 Ekim 2023 haberleri `/tag/gazze` altında DEĞİL, `/tag/hamas` altında erişilebilir. Boşluk kapandı. Tam scraping stratejisi:
- TR Oct 7-15: `/tag/hamas?p=22-23` üzerinden
- TR Oct 16+: `/tag/gazze?p=1-42` üzerinden
- Deduplication gerekecek (bazı haberler her iki tag'de de olabilir)

#### Doğrulanan Oct 7-8 TR Makale URL'leri:

```
Oct 7:
- https://tr.euronews.com/2023/10/07/hamas-saldirisinda-en-az-70-israilli-hayatini-kaybetti
- https://tr.euronews.com/2023/10/07/bitmeyen-savas-hamas-ve-israil-arasindaki-savasin-yakin-tarihcesi
- https://tr.euronews.com/2023/10/07/israile-en-buyuk-saldiriyi-baslatan-kassam-tugaylari-kimdir

Oct 8:
- https://tr.euronews.com/2023/10/08/israilli-genclerin-colde-duzenledigi-muzik-festivali-kabusa-donustu
- https://tr.euronews.com/video/2023/10/08/israilin-gazze-saldirisinda-yuzlerce-filistinli-oldu
- https://tr.euronews.com/2023/10/08/israili-kuzeyden-vurmaya-baslayan-lubnan-hizbullahi-kimlerdir-hedefleri-ne
```

#### EN-TR Dil Linki Test Sonucu:

| Test | Sonuç |
|------|-------|
| EN Oct 7 makalesinde TR link | ⚠️ Yalnızca `tr.euronews.com` ana sayfa — spesifik URL yok |
| TR Oct 7 makalesinde EN link | ⚠️ Yalnızca `euronews.com` ana sayfa — spesifik URL yok |
| TR Oct 17 makalesinde EN link | ⚠️ Yalnızca `euronews.com` ana sayfa — spesifik URL yok |
| HTML'de hreflang meta tag | ❌ WebFetch ile alınamadı — büyük ihtimalle JS ile yükleniyor |

**Sonuç:** Dil linki üzerinden doğrudan EN→TR URL eşleştirme WebFetch ile mümkün değil. Python Requests/BeautifulSoup ile hreflang tag'leri alınabilir veya tarih + cosine similarity kullanılabilir.

#### Ek Bulgu:
Bazı Euronews TR makaleler "euronews & AA (Anadolu Agency)" olarak atıflandırılıyor (örn. `kassam-tugaylari` makalesi). Bu, Euronews TR'nin bazı içeriklerinde AA'yı kaynak olarak kullandığını gösteriyor — çeviribilimsel analiz için metodolojik not.

---

### 2.3 AA — ✅ ARŞİV SORUNU ÇÖZÜLDÜ

| Test | Sonuç |
|------|-------|
| Oct 7, 2023 EN makaleleri | ✅ Erişilebilir — 6 makale doğrulandı (ID 3010318–3010959) |
| Oct 8, 2023 EN makaleleri | ✅ Erişilebilir — 6 makale doğrulandı (ID 3011258–3011860) |
| Oct 15 – Nov 11 EN makaleleri | ✅ 7 makale erişilebilir |
| Oct 7-8, 2023 TR makaleleri | ✅ En az 4 makale erişilebilir |
| Oct 15, 2023 TR makalesi | ✅ Erişilebilir (ID 3020523) |
| AA TR URL path çeşitliliği | ⚠️ `/tr/dunya/`, `/tr/politika/`, `/tr/ortadogu/` — bölüme göre değişiyor |
| Bazı kısa TR makaleler | ⚠️ Sadece navigasyon HTML dönüyor (içerik yüklenmez) |

**Çözüm Yöntemi — GDELT + CommonCrawl:**
1. **GDELT API**: `api.gdeltproject.org/api/v2/doc/doc?query=domain:aa.com.tr+[keyword]&mode=artlist&startdatetime=YYYYMMDD&enddatetime=YYYYMMDD&format=json`
   - Oct 7 için verilen EN URL sayısı: 6+ (ID 3010318–3010959)
   - Oct 7-8 için TR URL sayısı: 7+ (ID 3010626–3011860)
   - Rate limit: 429 hatası mümkün; kısa bekleme sonrası tekrar çalışıyor
2. **CommonCrawl CC-MAIN-2023-50**: `index.commoncrawl.org/CC-MAIN-2023-50-index?url=aa.com.tr/en/middle-east/*&output=text&limit=100`
   - Oct 10–Nov 12 arası 10+ EN makale URL'si doğrulandı
   - TR için `aa.com.tr/tr/dunya/*` kısıtlı sonuç verdi (sadece 3060xxx range)

**AA ID Sistemi — Triangüle Edilen Değerler:**
| Tarih | ID | Kaynak |
|-------|----|----|
| 07 Ekim 2023 (erken) | ~3,010,318 | Doğrudan doğrulama |
| 10 Ekim 2023 | 3,014,450 | Doğrudan doğrulama |
| 18 Ekim 2023 | 3,024,720 | Doğrudan doğrulama |
| 26 Ekim 2023 | ~3,033,662 | Doğrudan doğrulama |
| 28 Ekim 2023 | 3,036,204 | Doğrudan doğrulama |
| 02 Kasım 2023 | 3,040,900 | Doğrudan doğrulama |
| 07 Kasım 2023 | 3,046,146 | Doğrudan doğrulama |
| 11 Kasım 2023 | 3,050,418 | Doğrudan doğrulama |

**Ortalama ID artış hızı: ~1,100–1,300 ID/gün** (tüm diller ve bölümler dahil global sayaç)

**Adım 2.3 İçin Yöntem:**
1. GDELT API ile her 7 günlük blok için URL listesi çek
2. Çekilen URL'leri doğrudan AA sayfasından fetch et
3. TR makaleler için 400-1000 kelimeli makaleleri tercih et (kısa breaking news haber blokları zaman zaman sadece navigasyon döndürüyor)
4. `/tr/dunya/` + `/tr/politika/` + `/tr/ortadogu/` tüm path'leri dahil et

---

## 3. Euronews 7-16 Ekim Boşluğu — Final Karar

**DURUM: ÇÖZÜLDÜ** ✅

- `/tag/gazze` Oct 7-15 içermiyor → DOĞRU
- `/tag/hamas` p=22-23 Oct 7-8-9-12 içeriyor → DOĞRULANMIŞ  
- Tam scraping stratejisi:
  1. TR: `/tag/hamas` p=1 ila son (Oct 7 başlangıcı için)
  2. TR: `/tag/gazze` p=1 ila 42 (Oct 16+ için)
  3. URL listelerini birleştir + tarih bazlı deduplication
  4. Oct 7-15 aralığı için `/tag/hamas` öncelikli kaynak

---

## 4. EN-TR Eşleştirme — Pilot Bulguları

### Sputnik
| Özellik | Bulgu |
|---------|-------|
| EN-TR aynı ID? | ❌ Hayır (EN ~1113-1114M, TR ~1076M) |
| Aynı gün aynı olay haberleri var mı? | ✅ Evet — her iki dilde Oct 7 Gazze haberleri mevcut |
| Birebir çeviri (Katman 1) var mı? | ❓ Test edilmedi — aynı günde başlıklar farklı köşeler kapsıyor |
| Comparable (Katman 2) eşleştirme | ✅ Tarih + cosine similarity uygulanabilir |
| Örnek eşleştirme adayı | EN "Russia Urges Ceasefire" (Bogdanov) ↔ TR "Rusya DİŞB çatışmadan endişe" (Lavrov) — aynı konu, farklı kaynak |

**Sputnik değerlendirmesi:** EN ve TR bağımsız redaksiyon yapısı var; aynı haberi farklı Russian diplomats/officials üzerinden kapsıyorlar. Çoğunlukla Katman 2 (comparable). Aynı konferanstan alınan alıntılar Katman 1 eşleşmesi yaratabilir — cosine similarity >0.85 eşiğiyle test edilmeli.

### Euronews
| Özellik | Bulgu |
|---------|-------|
| EN-TR dil linki | ⚠️ WebFetch ile alınamıyor (JS render) |
| hreflang meta tag | ❌ WebFetch'de görünmüyor |
| Aynı URL slug? | ❌ Hayır — slug dile çevriliyor |
| Oct 7 EN makalesi TR karşılığı var mı? | ❌ Spesifik TR URL yok ("en büyük saldırı" makalesi için) |
| Bağımsız üretim mi çeviri mi? | Karışık: bazı makaleler bağımsız (hamas, israil tag'i), bazıları co-production (euronews & AA) |
| Eşleştirme yöntemi | Tarih + cosine similarity + Python hreflang extraction |

**Euronews değerlendirmesi:** EN ve TR İÇERİK üretimi kısmen asenkron — bazı EN haberlerin TR versiyonu yok, bazıları euronews & AA co-production. Katman 1 eşleştirmesi daha az ama mevcut; Katman 2 bolca mevcut. Python ile hreflang taglerini çekerek gerçek Katman 1 çiftleri tespit edilebilir.

### AA
| Özellik | Bulgu |
|---------|-------|
| EN-TR aynı ID? | ❌ Hayır — global ID sistemi, diller farklı ID alıyor |
| TR dil linki EN makalede | ⚠️ Dil seçici mevcut ama spesifik URL WebFetch ile alınamıyor |
| Oct 2023 arşiv erişimi | ❌ Çözülmedi |

---

## 5. Veri Kalitesi Notları

### Türkçe Karakter Testi
| Kaynak | Karakter Durumu |
|--------|----------------|
| Sputnik TR | ✅ Mükemmel — ş, ğ, ı, ü, ö, ç tümü doğru |
| Euronews TR | ✅ Mükemmel — aynı durum |
| AA TR | Test edilemedi (arşiv sorunu) |

### HTML Temizleme Zorluğu (Tahmini)
| Kaynak | Zorluk | Gerekçe |
|--------|--------|---------|
| Sputnik | Düşük | Statik HTML, yapı basit |
| Euronews | Orta | Bazı "No Comment" video haberleri var (metin az) |
| AA | Orta | "Load more" JS sorunu çözüldükten sonra orta zorluk |

### Önemli İçerik Notu:
Sputnik EN, Al-Ahli hastane haberinin başlığında saldırıyı açıkça İsrail'e atfediyor: "Israeli Strike on Hospital". Bu, AA'nın ("İsrail ve Hamas Gazze'yi bombaladı" gibi daha nötr bir çerçeveleme kullanması olasılığına karşılık ideolojik çerçeveleme analizinin somut bir örneğini oluşturuyor. Corpus'ta bu tür etiket farklılıkları Katman 1 için çok değerli mikro analiz materyali.

---

## 6. AA Arşiv Sorunu — ÇÖZÜLDÜ ✅

AA pilot scrapinginin temel bulgusu ilk oturumda "Oct 2023 makalelerine statik WebFetch ile erişmek mümkün değil" olarak tespit edilmişti. Bu sorun ikinci oturumda **tamamen çözüldü**.

**Çözüm Yöntemi:**

1. **GDELT Project API** — URL Keşfi:
   - `api.gdeltproject.org/api/v2/doc/doc?query=domain:aa.com.tr+hamas+attack&mode=artlist&startdatetime=20231007000000&enddatetime=20231009000000&format=json`
   - GDELT, Oct 7-8 için 20+ aa.com.tr URL'si (EN ve TR karışık) döndürdü
   - Rate limit (429): kısa bekleme sonrası çalışıyor
   - Robots.txt'deki `/api/` yasağı GDELT'i etkilemiyor (harici servis)

2. **CommonCrawl CC-MAIN-2023-50** — Ek URL Havuzu:
   - `index.commoncrawl.org/CC-MAIN-2023-50-index?url=aa.com.tr/en/middle-east/*&output=text&limit=100`
   - Oct 10 – Nov 12 aralığından 10+ EN makale URL'si doğrulandı
   - Wayback Machine bloklu (web.archive.org), CommonCrawl alternatif ve işlevsel

3. **ID Triangülasyonu** — Doğrulama:
   - GDELT'ten URL alındıktan sonra AA sayfası doğrudan fetch edildi
   - Oct 7, 2023 erişimi %100 onaylandı (ID 3010318, 3010683)
   - TR makaleler `/tr/dunya/`, `/tr/politika/` gibi farklı path'larda — ikisi de çalışıyor

**Kalan Küçük Sorun:**
Kısa breaking news haberleri (özellikle TR) zaman zaman sadece navigasyon HTML döndürüyor. Uzun/analizci makalelerin (500+ kelime) erişim oranı çok daha yüksek. Adım 2.3 için çözüm: GDELT ile URL al → AA'dan fetch et → metin uzunluğu < 200 kelimeyse atla (farklı haberi seç).

---

## 7. Adım 2.3 İçin Tahmini Haber Sayısı

### Sputnik (6 ay = ~180 gün)
| Gün | Tahmini Gazze haberi/gün | 6 ay toplam | EN | TR |
|-----|--------------------------|-------------|----|----|
| Oct 7-31, 2023 | 8-15/gün | ~250 | ~125 | ~125 |
| Nov 2023 – Apr 2024 | 5-10/gün | ~900 | ~450 | ~450 |
| **TOPLAM** | — | **~1.150** | **~575** | **~575** |

**500 çift için yeterlilik:** ✅ Evet (hem EN hem TR'de yeterli stok var)

### Euronews
| Kaynak | Sayfa Sayısı | Tahmini Makale |
|--------|-------------|----------------|
| EN `/tag/israel-hamas-war` | 86 sayfa × ~20 | **~1.720** |
| TR `/tag/gazze` | 42 sayfa × ~20 | **~840** |
| TR `/tag/hamas` (Oct 7-15 ek) | p=22-23 × ~20 | **~40** |
| **TR toplam** | — | **~880** |

**500 çift için yeterlilik:** ✅ Evet  
**Not:** EN 1.720 >> TR 880 → Her EN için TR karşılığı olmayabilir. 500 eşleştirilebilir çift için EN tarafından seçim yapılacak.

### AA
| Durum | Tahmini |
|-------|---------|
| Oct 2023 – Apr 2024 dönemindeki Gazze haberleri | ~800-1.200 EN + ~800-1.200 TR (tahmin — arşiv erişimi çözülmedikçe doğrulanamaz) |
| Erişilebilirlik | ❌ Henüz bilinmiyor |

---

## 8. Görülen Sorunlar ve Önerilen Çözümler

| # | Sorun | Kaynak | Durum | Çözüm |
|---|-------|--------|-------|-------|
| 1 | AA Oct 2023 arşiv erişimi yok | AA | ✅ ÇÖZÜLDÜ | GDELT API + CommonCrawl CC-MAIN-2023-50 URL keşfi; doğrudan AA fetch çalışıyor |
| 2 | EN-TR dil linki WebFetch ile alınamıyor | Euronews + AA | ⚠️ DEVAM | Python requests + BeautifulSoup ile hreflang meta tag çek; alternatif: tarih + cosine similarity |
| 3 | EN-TR farklı ID'ler | Sputnik, AA | ⚠️ DEVAM | Tarih + cosine similarity — threshold >0.7 strict, >0.5 comparable |
| 4 | Kısa AA TR makaleler navigasyon HTML döndürüyor | AA TR | ⚠️ KISMEN | Metin uzunluğu < 200 kelimeyse atla; GDELT'te birden fazla URL al ve alternatif seç |
| 5 | Euronews TR bazı makaleler video (metin az) | Euronews | ⚠️ DEVAM | `/video/` URL'lerini filtrele; sadece `/YYYY/MM/DD/` formatındaki text haberleri al |
| 6 | Bazı Euronews TR makaleler "euronews & AA" co-production | Euronews | ℹ️ BİLGİ | Metodoloji bölümünde belirt; "co-produced" sınıfı eklenebilir |
| 7 | Sputnik EN-TR bağımsız üretim (çeviri değil) | Sputnik | ℹ️ BİLGİ | Cosine similarity ile Katman 1 (>0.85) ve Katman 2 (>0.5) eşiklerini ayrı uygula |

---

## 9. Özet ve Sonraki Adım Önerisi

### Özet (Güncellenmiş — 2 Mayıs 2026)
- **Sputnik:** ✅ Tam scrapinge hazır. Oct 2023 arşivi doğrulandı, içerik kalitesi yüksek, Türkçe karakterler sorunsuz.
- **Euronews:** ✅ Oct 7-16 boşluğu `/tag/hamas` ile kapatıldı. EN-TR dil linki WebFetch ile alınamıyor; Python ile çözülecek. Tam scrapinge hazır (Python adımından sonra).
- **AA:** ✅ Oct 2023 arşiv erişimi ÇÖZÜLDÜ. GDELT + CommonCrawl URL keşif yöntemi doğrulandı. 10 EN + 5 TR pilot makalesi elde edildi. Tam scrapinge hazır.

### AA Pilot Sonuçları
| Kategori | Sayı | ID Aralığı | Tarih Aralığı |
|----------|------|------------|---------------|
| AA EN | 10 | 3010318–3050418 | 7 Eki – 11 Kas 2023 |
| AA TR | 5 | 3010626–3020523 | 7–15 Eki 2023 |

**Önemli Not:** Oct 7 (Kritik Olay #1) makaleleri ONAYLANDI:
- EN: "Premier Netanyahu says Israel at war" (ID 3010318, 11:00 UTC)
- EN: "Gaza Health Ministry: 232 Palestinians killed" (ID 3010683, 21:30 UTC)
- TR: "İsrail-Filistin'deki gelişmelere dünyadan tepkiler" (ID 3010626, 15:00 UTC)
- TR: "Bakan Fidan-Blinken görüştü" (ID 3011013, 20:30 UTC)

### Sıradaki Adım: Adım 2.3 — Tam Scraping

Üç kaynak için tam scraping artık uygulanabilir. Önerilen sıra:
1. **Sputnik** (en hazır): Günlük `sputnikglobe.com/YYYYMMDD/` ve `anlatilaninotesi.com.tr/YYYYMMDD/` fetch döngüsü
2. **AA** (GDELT yöntemi): 7 günlük bloklar halinde GDELT sorgusu → AA doğrudan fetch → metin < 200 kelimeyse atla
3. **Euronews** (Python gerekiyor): `/tag/gazze` + `/tag/hamas` + `/tag/israel-hamas-war` tüm sayfa listesi → Python ile hreflang eşleştirme

**Adım 2.3 Ön Koşul (Euronews için):** Python requests + BeautifulSoup ile hreflang meta tag çekimi doğrulanmalı.

---

*Pilot scraping raporu — Claude Code ile oluşturulmuştur. 2 Mayıs 2026.*

---

## 10. Sonradan Düzeltme — 3 Mayıs 2026 (Sputnik EN Erişim Yanılgısı)

Adım 2.3 (Tam Scraping) hazırlığında bu pilot raporun **kritik bir metodolojik yanılgı içerdiği** tespit edilmiş ve burada şeffaflık adına kayıt altına alınmıştır.

### 10.1 Yanılgının Tespiti

Adım 2.3 için yazılan lokal Python scraping kodu (`scripts/scrapers/sputnik.py`) test edildiğinde, `sputnikglobe.com` (Sputnik EN ana domain) host'una **TCP düzeyinde ConnectTimeout** alındı. Aşağıdaki sistematik teşhis (`scripts/diag_sputnik.py`) yapıldı:

| Domain | DNS | TCP 443 | HTTP | Sonuç |
|--------|-----|---------|------|-------|
| `sputnikglobe.com` | ✅ → 194.190.139.3 | ❌ TIMEOUT | ❌ ulaşılamıyor | **Engelli** |
| `sputniknews.com` (eski domain) | ✅ → 194.190.139.3 (aynı IP) | ❌ TIMEOUT | ❌ | **Engelli** |
| `sputnikinternational.com` | ✅ → 13.223.25.84 (CloudFront) | ❌ TIMEOUT | ❌ | **Engelli** |
| `sputnik-georgia.com` | ✅ → 194.190.139.8 | ✅ OK | ✅ HTTP 200 | **Açık** |
| `anlatilaninotesi.com.tr` (TR mirror) | ✅ → 194.190.139.20 | ✅ OK | ✅ HTTP 200 | **Açık** |

DNS resolve oluyor ama TCP el sıkışması gerçekleşmiyor → **RTÜK SNI-bazlı domain filtresi** (IP-bazlı değil — aynı /20 IPv4 bloğundaki diğer Sputnik servisleri açık). User-Agent değişimi etkisiz (TCP-altı blok).

### 10.2 Pilot Raporundaki Hatalı Sonuçlar

Bu raporun **Bölüm 2.1** ("Sputnik — SORUNSUZ") ve **Bölüm 6.2** referansları (master metodoloji) **lokal Python erişim perspektifinden geçerli değildir.** Pilot scraping testleri Claude Code CLI'nin `WebFetch` komutu ile yapılmış; bu komut Anthropic'in sunucularından (Türkiye dışı IP) çıkar ve RTÜK SNI filtresinden etkilenmez. Yani:

- "EN Oct 7 2023 arşivi: ✅ `sputnikglobe.com/20231007/` açılıyor" — **WebFetch için doğru, lokal Python için yanlış.**
- "TR Oct 7 2023 arşivi: ✅ `anlatilaninotesi.com.tr/20231007/` açılıyor" — **Hem WebFetch hem lokal Python için doğru.**

### 10.3 Düzeltilen Yöntem — Hibrit Erişim

Sputnik EN scraping artık **GitHub Actions** üzerinden yapılır:
- Workflow: `.github/workflows/scrape_sputnik_en.yml`
- Runner: Microsoft-hosted Ubuntu (Frankfurt datacenter)
- Tetik: manuel `workflow_dispatch` (kullanıcı GitHub Actions sekmesinden Run workflow basar)
- Sonuç: ZIP artifact, `scripts/merge_github_artifacts.py` ile lokal corpus'a eklenir

Sputnik TR (anlatilaninotesi.com.tr), AA (EN+TR) ve Euronews (EN+TR) lokal Python ile çalışmaya devam eder.

### 10.4 Akademik Katkı Olarak

Bu yanılgı ve düzeltme, makalenin metodoloji bölümünde **bir bulgu olarak** sunulacaktır (bkz. master metodoloji dosyası, Bölüm 3.3 ve Bölüm 9.4 — "Hybrid Access Strategy"). Hesaplamalı dilbilim çalışmalarında "erişilebilirlik" kavramının kaynak–istemci–ağ üçlüsünden bağımsız bir özellik olmadığı; aynı kaynağın bir IP'den erişilebilirken başka bir IP'den engelli olabileceği gerçeği, gelecek araştırmacılar için akademik olarak değerli bir uyarıdır.

*Düzeltme notu — 3 Mayıs 2026.*
