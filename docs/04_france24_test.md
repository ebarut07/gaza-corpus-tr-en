# Arşiv Erişim Testi Raporu — 4. Bölüm (France 24)
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** France 24 EN ve TR  
**Önceki Raporlar:** arsiv_testi_raporu.md · arsiv_testi_2_raporu.md · arsiv_testi_3_raporu.md

---

## SONUÇ (Öne Çekilen)

**France 24: KULLAНИLAMAZ** — robots.txt'de `Claude-Code` ve `ClaudeBot` açıkça ve isimle Disallow edilmiş. Sayfalar 403 (Forbidden) döndürüyor.

---

## Test Sonuçları

| Test Edilen URL | Sonuç | Açıklama |
|----------------|-------|----------|
| `france24.com/robots.txt` | ✅ Okundu | ClaudeBot açıkça engellenmiş |
| `france24.com/en/search/?q=Gaza` | ❌ 403 Forbidden | Bot engeli aktif |
| `france24.com/tr/` | ❌ 403 Forbidden | Bot engeli aktif |

### robots.txt Önemli Bulgular
- **ClaudeBot, Claude-Code, Claude-SearchBot, Claude-User → Disallow** (isimle ve açıkça)
- Crawl-delay kuralları mevcut: archive.org_bot için 10 saniye, bazı ticari botlar için 5 saniye
- Genel içerik için Disallow yok — sadece AI botları hedef alınmış
- Googlebot için tek kural: `/en/_ws/urgent` dizini engelli

### Teknik Not
BBC ve DW'deki engel "sunucu tarafı IP/Cloudflare koruması" iken, France 24'ün engeli farklı: **robots.txt User-Agent tabanlı, aktif 403 yanıtı**. Bu daha kesin bir kasıtlı engel.

---

## 4 Test Sonrası Genel Tablo

| Kaynak | EN | TR | Engel Türü | Karar |
|--------|----|----|------------|-------|
| **Sputnik** | ✅ sputnikglobe.com | ✅ anlatilaninotesi.com.tr | Yok | **Kullanılabilir** |
| **AA** | ✅ aa.com.tr/en | ✅ aa.com.tr/tr | Yok | **Kullanılabilir** |
| BBC | ❌ | ❌ | IP/CloudFlare + Wayback'te yok | Kullanılamaz |
| DW | ❌ | ❌ | IP/CloudFlare + SSL hataları | Kullanılamaz |
| France 24 | ❌ | ❌ | robots.txt ClaudeBot Disallow + 403 | Kullanılamaz |

**Sonuç: 5 kaynaktan 2'si teknik olarak çalışıyor.**

---

## Üçüncü Kaynak İçin Durum ve Öneri

### Neden 3. Kaynak Önemli?
Projenin teorik çerçevesi **ideolojik çeşitlilik** üzerine kurulu:
- Sputnik → Rusya yanlısı / Batı karşıtı perspektif
- AA → Türkiye devlet perspektifi
- 3. kaynak → Batı/Uluslararası ana akım perspektifi (BBC/DW/France24/Reuters gibi)

3. kaynak olmadan iki Türk/Rus perspektifi karşılaştırılmış olur; bu akademik olarak zayıf bir tasarımdır.

### Test Edilmemiş Tek Gerçekçi Aday: Reuters

**Reuters'ın avantajları:**
- Büyük bir haber ajansı — CloudFlare kullanma ihtimali BBC/DW'ye göre daha düşük
- `reuters.com` (İngilizce) + `tr.reuters.com` (Türkçe) — iki dil servisi mevcut
- Türkiye'de erişim engeli yok
- Batı ana akım perspektifini temsil eder

**Reuters'ın olası sorunları:**
- Büyük ajanslar bazen sıkı bot koruması uygular
- tr.reuters.com'un Gazze haberlerindeki içerik yoğunluğu bilinmiyor
- EN-TR ID eşleşme yapısı henüz doğrulanmadı

---

## Alternatif Tasarım Seçeneği (Reuters da Başarısız Olursa)

Eğer Reuters da erişilemez çıkarsa, mevcut iki kaynakla devam etmek yerine **farklı eşleştirme stratejisi** düşünülebilir:

| Seçenek | Kaynak 1 | Kaynak 2 | Kaynak 3 | Notlar |
|---------|----------|----------|----------|--------|
| A (önerilen) | Sputnik EN+TR | AA EN+TR | Reuters EN+TR | 3 ideolojik perspektif |
| B (yedek) | Al Jazeera EN | AA EN+TR | Sputnik EN+TR | AJ EN karşılaştırmalı, TR eşi yok ama Katman 2 için yeterli |
| C (minimal) | AA EN+TR | Sputnik EN+TR | — | 2 kaynak, akademik olarak savunulabilir ama zayıf |

Seçenek B'de Al Jazeera İngilizce, AA ve Sputnik Türkçe ile "comparable" (Katman 2) olarak eşleştirilir. Strict parallel (Katman 1) yalnızca AA ve Sputnik kendi dil çiftleri içinde yapılır. Bu yaklaşım makalede açıkça metodolojik bir seçim olarak sunulabilir.

---

## Önerilen Sıradaki Adım

**Adım 2.1e: Reuters testi** (`reuters.com` + `tr.reuters.com`)

Test edilecekler:
- robots.txt ClaudeBot kuralı var mı?
- Arama URL formatı ve tarih filtresi
- EN-TR ortak ID/slug yapısı
- 6 aylık dönemde Gazze haber yoğunluğu

Reuters erişilebilirse → 3 kaynaklı tasarım tamamlanır.  
Reuters erişilemezse → Seçenek B veya C'den biri seçilir, pilot scrapinge geçilir.

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
