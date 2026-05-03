# Arşiv Erişim Testi Raporu — 3. Bölüm (DW)
**Tarih:** 2 Mayıs 2026  
**Proje:** Gazze Korpusu - Q1 Makale  
**Test Kapsamı:** Deutsche Welle EN ve TR  
**Önceki Raporlar:** `arsiv_testi_raporu.md` (AJ, BBC, AA), `arsiv_testi_2_raporu.md` (Sputnik, BBC Wayback)

---

## SONUÇ (Öne Çekilen)

**DW: KULLAНИLAMAZ** — BBC ile aynı engel kategorisi.

`dw.com` ve tüm alt domainleri Claude Code WebFetch aracılığıyla erişilemez durumdadır. Wayback Machine'de de DW arşivi bulunmamaktadır. Alternatif domainlerin SSL sertifikaları geçersiz.

---

## Test Sonuçları

### Erişilen URL'ler ve Sonuçlar

| Test Edilen URL | Yöntem | Sonuç |
|----------------|--------|-------|
| `www.dw.com/robots.txt` | WebFetch | ❌ Erişim engelli |
| `www.dw.com/tr/` | WebFetch | ❌ Erişim engelli |
| `www.dw.com/en/search?q=Gaza&...` | WebFetch | ❌ Erişim engelli |
| `dw.com/robots.txt` | WebFetch (www'suz) | ❌ Erişim engelli |
| `dw.com/en/` | WebFetch (HTTP) | ❌ Erişim engelli |
| `dwturkce.com/` | WebFetch | ❌ SSL sertifika hatası (TLS_CERT_ALTNAME_INVALID) — geçersiz/terk edilmiş domain |
| `dw-world.de/robots.txt` | WebFetch | ❌ SSL sertifika hatası — geçersiz domain |
| `p.dw.com` | WebFetch | ❌ Erişim engelli |
| `dw.com/en/...` | Wayback availability API | ❌ Boş — arşiv yok |
| `dw.com/en/israel-hamas-war/a-...` | Wayback availability API | ❌ Boş — arşiv yok |

**Toplam: 10 test, 10 başarısızlık.**

### Teknik Engel Türü
- `dw.com` / `www.dw.com` / `p.dw.com`: CloudFlare veya IP bazlı tam engel (BBC ile özdeş hata mesajı)
- `dwturkce.com` / `dw-world.de`: SSL sertifikası geçersiz — bunlar gerçek DW ayna siteleri değil, terk edilmiş/sahte domainler
- Wayback Machine: DW büyük olasılıkla Wayback crawlerlarını da engelliyor (BBC gibi)

---

## Projeye Etki

### Genel Tablo — Tüm Test Edilen Kaynaklar

| Kaynak | EN | TR | Durum |
|--------|----|----|-------|
| Al Jazeera | ✅ Mükemmel | ❌ Mevcut değil | EN only |
| AA | ✅ İyi | ✅ İyi | **Kullanılabilir** |
| Sputnik | ✅ Mükemmel | ✅ Mükemmel | **Kullanılabilir** |
| BBC | ❌ Engelli | ❌ Engelli | Kullanılamaz |
| DW | ❌ Engelli | ❌ Engelli | Kullanılamaz |

### Sonuç Durumu
Üç raporun ardından **programatik olarak erişilebilen EN+TR kaynak sayısı ikide kaldı:** AA ve Sputnik.

---

## Net Öneri

### DW Kullanılabilir mi?
**Hayır. DW kullanılamaz.**

DW, BBC ve www.dw.com domaininin tamamı CloudFlare veya benzeri bir koruma katmanının arkasında. Wayback'te de arşivi yok. Hiçbir programatik erişim yolu bulunamadı.

---

### Projenin Kaynak Tasarımı İçin Sonuç

Şimdiye kadar test edilen 5 kaynaktan 2'si çalışıyor. 3. kaynak için test edilmesi gereken tek gerçekçi aday kaldı:

**Reuters** — `reuters.com` (EN) + `tr.reuters.com` (TR)

Reuters'ın seçilme gerekçesi:
- Batı ana akım perspektifini temsil eder (ideolojik denge için kritik)
- Büyük haber ajansları genellikle CloudFlare kullanmaz (BBC/DW'den farklı)
- `tr.reuters.com` Türkçe versiyonu mevcut ve Türkiye'de erişilebilir
- EN-TR URL yapısı muhtemelen paylaşılan ID sistemi kullanıyor (AA ve Sputnik gibi)

**Öneri:** Adım 2.1d olarak Reuters'ı test et. Eğer Reuters da erişilemezse, proje 2 kaynaklı tasarıma (AA + Sputnik) geçmeli.

---

## Durum Özeti — 3 Rapor Sonrası

### Kesinleşmiş Kaynaklar
| # | Kaynak | EN Domain | TR Domain | Arşiv Yöntemi |
|---|--------|-----------|-----------|---------------|
| 1 | **Sputnik** | `sputnikglobe.com` | `anlatilaninotesi.com.tr` | `/YYYYMMDD/` tarih arşivi |
| 2 | **AA** | `aa.com.tr/en` | `aa.com.tr/tr` | Kategori sayfaları (eski içerik TBD) |

### Test Bekleniyor
| # | Kaynak | Beklenti |
|---|--------|---------|
| 3 | **Reuters** | Yüksek ihtimalle erişilebilir — test gerekiyor |

### Elenen Kaynaklar
BBC, DW, Al Jazeera TR — hiçbir programatik erişim yolu yok.

---
*Rapor otomatik olarak Claude Code ile oluşturulmuştur.*
