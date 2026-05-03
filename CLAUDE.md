# GAZZE KORPUSU - Q1 MAKALE PROJESİ

## Proje Sahibi
Dr. Evren Barut, Akademisyen
Alan: Filoloji, Uygulamalı Dilbilim, Çeviribilim, İdeoloji, Makine Çevirisi, AI Çeviri, CAT Araçları
Kurum: Afyon Kocatepe Üniversitesi (AKÜ)
Çalışma dili: Türkçe (kullanıcıyla iletişim), İngilizce/Türkçe (korpus dilleri)
İşletim sistemi: Windows 11
Kodlama deneyimi: Yok — açıklamalar adım adım, jargon-az olmalı

## Genel Araştırma Programı
Aynı korpus ailesinden 3 sıralı Q1 makale planlanıyor:
- **Makale 1 (mevcut)**: Korpus inşası ve metodoloji - Hedef: Language Resources and Evaluation, Corpora
- **Makale 2 (gelecek)**: İdeolojik leksikon analizi + CDA - Hedef: Target, Perspectives, Translation Studies
- **Makale 3 (gelecek)**: İstatistiksel/teknik bias tespit metrikleri - Hedef: Machine Translation, Natural Language Engineering, Meta

## MAKALE 1 ÇERÇEVESİ

### Olay ve Tarih Aralığı
- Olay: Gazze savaşı, ilk altı ay
- Tarih: 7 Ekim 2023 - 7 Nisan 2024
- Yaklaşım: Statik söylem analizi (Senaryo A)
- Hedef korpus boyutu: ~500 haber çifti

### Araştırma Sorusu
"Gazze savaşının ilk altı ayında (7 Ekim 2023 - 7 Nisan 2024) üç farklı düzeyde devlet/üst-devlet medyasının — Anadolu Ajansı (Türkiye ulus-devlet medyası), Sputnik (Rusya devlet medyası, AB tarafından 'dezenformasyon' olarak nitelendirilen) ve Euronews (Avrupa Birliği üst-devlet medyası) — Türkçe-İngilizce paralel haber metinlerinde ideolojik çerçeveleme stratejileri nasıl tezahür etmekte ve karşılaşmaktadır?"

### Üç Kaynak (Devlet/Üst-Devlet Medyası Üçlemesi)
1. **Anadolu Ajansı (AA) EN-TR** - Türkiye ulus-devlet medyası (resmi haber ajansı)
2. **Sputnik EN-TR** - Rusya devlet medyası, AB tarafından "dezenformasyon" olarak nitelendirilmiş (alternatif domain anlatilaninotesi.com.tr ile yayınını sürdürüyor) - bu durum tasarımın bilinçli teorik bir parçasıdır: 'haber' ile 'dezenformasyon' arasındaki sınır kendisi bir ideolojik çerçeveleme eylemidir (Baker 2006, Valdeón 2015 çerçevesinde)
3. **Euronews EN-TR** - AB üst-devlet medyası, pan-Avrupa liberal merkez yayıncısı

### Elenmiş Kaynaklar (Akademik Kayıt)
Bu çalışmanın kaynak seçimi sırasında 25+ haber kaynağı sistematik olarak test edildi ve aşağıdakiler erişim engelleri nedeniyle elendi:
- **Al Jazeera EN-TR**: Türkçe servisi 2017'de kapatıldı
- **BBC EN-TR**: CloudFlare/IP düzeyinde otomatik erişim engeli
- **DW EN-TR**: CloudFlare/IP engeli + alternatif domainlerde SSL hataları
- **France 24 EN-TR**: robots.txt'de Claude-Code'a spesifik yasak
- **Reuters EN-TR**: Erişim engelli
- **VOA EN-TR**: 2025 USAGM krizi sonrası site stabilitesi sorunlu, erişim engelli
- **CGTN EN-TR**: 2023-2024 arşivine erişim yok (sadece son 5 gün arşivlenmekte)
- **Xinhua, ANSA, EFE, Swissinfo, NHK ve diğer 15+ kaynak**: Türkçe servisi yok veya erişim engeli

Bu eleme süreci makalenin metodoloji bölümünde "çağdaş dijital medya manzarasında akademik scraping erişiminin giderek kısıtlandığı" tespitiyle birlikte sunulacaktır - yani bu tarama süreci kendisi bir akademik bulgudur.

NOT: Al Jazeera EN tek başına sitemap arşivi mükemmel olduğu için Claude Code tarafından ısrarla 3. kaynak olarak önerilmektedir, ancak TR servisi yokluğu nedeniyle bu makalede KULLANILMAYACAK (TR-EN paralel çeviri analizi yapılamaz). Asimetrik tasarım önerilerini reddet.

### Teorik Çerçeve
- Bielsa & Bassnett (2009) - Translation in Global News
- Mona Baker - Narrative theory (Translation and Conflict, 2006)
- Roberto Valdeón - Journalistic translation research

## KORPUS TASARIMI

### İki Katmanlı Yapı
- **Katman 1 (Strict parallel)**: Birebir çeviri çiftleri (~200-300 çift) - mikro analiz için
- **Katman 2 (Comparable)**: Aynı olay/gün loose eşleşme (toplamı 500'e tamamlar) - makro analiz için

### Sampling Stratejisi
- %70 stratified random sampling (algoritmik, reproducible seed=42)
- %30 event-based sampling (10 kritik olay üzerinden)

### Konu Filtresi
**Dahil**: Askeri operasyonlar + insani durum + diplomasi
**Hariç**: İç siyaset, kampüs protestoları, ekonomi-piyasa haberleri

## 10 KRİTİK OLAY (Event-based Sampling İçin)
1. 7 Ekim 2023 - Hamas saldırısı
2. 17 Ekim 2023 - Al-Ahli hastane patlaması
3. 25 Ekim 2023 - Erdoğan'ın "Hamas terör örgütü değildir" açıklaması
4. 27 Ekim 2023 - İsrail kara harekâtı başlangıcı
5. 15 Kasım 2023 - Şifa Hastanesi baskını
6. 24 Kasım 2023 - İlk ateşkes ve esir takası
7. 29 Aralık 2023 - Güney Afrika'nın ICJ başvurusu
8. 26 Ocak 2024 - ICJ ara kararı
9. 29 Şubat 2024 - Un kamyonu katliamı (Flour Massacre)
10. Mart 2024 sonu - Refah operasyonu öncesi gerilim

## İŞ AKIŞI - ADIMLAR

### Adım 1: Araştırma Tasarımı ✅ TAMAMLANDI
### Adım 2: URL Çıkarma ve Scraping (MEVCUT)
- 2.1 Arşiv erişim testi ✅ TAMAMLANDI (8 rapor, 25+ kaynak, final tasarım: AA + Sputnik + Euronews)
- 2.2 Pilot scraping (her kaynaktan 20-30 haber)
- 2.3 Tam scraping (tüm tarih aralığı)
- 2.4 EN-TR eşleştirme (cosine similarity >0.7 strict için, NER-based comparable için)
- 2.5 Sampling uygulaması
- 2.6 Manuel doğrulama (50 haberlik alt-örneklem, hedef hata oranı <%5)

### Adım 3: Annotation şeması ve uygulama (gelecek)
### Adım 4: Korpus paketi ve yayını (Zenodo + GitHub)
### Adım 5: Makale yazımı ve submission

## TEKNİK NOTLAR
- Çalışma klasörü: C:\GazzeKorpus
- Tüm dosyalar bu klasörde tutulacak (OneDrive senkronize değil, performans için)
- Yedekleme: GitHub (kod ve metodoloji), Zenodo (final korpus için), harici USB (kritik veriler)
- Ham veri (HTML, JSON) yedeklenmez, gerekirse yeniden scrape edilir
- **GitHub repo:** https://github.com/ebarut07/gaza-corpus-tr-en (Public, MIT lisanslı)
- Python sürümü: 3.14.4 (Windows Python Launcher `py` ile çağrılır)

## ERİŞİM ALTYAPISI — HİBRİT YAKLAŞIM
- **Lokal Python (Türkiye, Afyonkarahisar)**: AA EN+TR, Euronews EN+TR, Sputnik TR (anlatilaninotesi.com.tr)
- **GitHub Actions (Microsoft-hosted Ubuntu, Frankfurt)**: Sputnik EN (sputnikglobe.com)
- **Sebep**: Türkiye'den lokal Python ile sputnikglobe.com'a TCP-level ConnectTimeout (DNS resolve oluyor 194.190.139.3, ama TCP 443 handshake yok). Bu RTÜK'ün SNI-bazlı erişim filtrelemesi. Aynı IP bloğundaki sputnik-georgia.com ve anlatilaninotesi.com.tr çalışıyor; yani IP-bazlı değil, domain/SNI-bazlı blok. User-Agent değişimi etkisiz (TCP düzeyi).
- **WebFetch yanılgısı (3 Mayıs 2026'da fark edildi)**: Pilot scraping'de yapılan tüm Sputnik EN testleri Claude Code CLI'nin `WebFetch` komutuyla yapılmıştı; bu komut Anthropic sunucularından (TR dışı IP) çıkar, dolayısıyla "Sputnik EN tarih arşivi mükemmel çalışıyor" sonucu lokal Python perspektifinden geçerli değildi. Hibrit yapı (lokal + GitHub Actions) bu yanılgıyı düzeltmek için tasarlandı.

## İLETİŞİM TERCİHLERİ
- Türkçe yanıt
- Adım adım, jargon-az açıklamalar
- Kararları gerekçelendir
- Karmaşık seçimleri matris/karşılaştırma ile sun
- Akademik standartlar her zaman öncelikli (Q1 dergi gerekleri)

### Bilinen Sorunlar ve Notlar
- Euronews TR 7-16 Ekim 2023 boşluğu: ÇÖZÜLDÜ — `/tag/hamas?p=22-23` üzerinden Oct 7-15 haberleri erişilebilir
- AA Oct 2023 arşiv sorunu: ÇÖZÜLDÜ — GDELT API + CommonCrawl CC-MAIN-2023-50 URL keşif yöntemi doğrulandı; Oct 7, 2023 makaleleri (ID ~3010318) erişilebilir
- AA ID sistemi global (~1,100–1,300 ID/gün); Oct 7 ≈ ID 3010318, Nisan 2024 ≈ ~3180000 tahmini
- AA TR makaleleri `/tr/dunya/`, `/tr/politika/`, `/tr/ortadogu/` path'lerinde dağılmış; GDELT URL keşfinde hepsi yakalanıyor
- Kısa AA TR breaking news haberleri bazen navigasyon HTML döndürüyor; 500+ kelime filtresi önerilir
- Euronews EN-TR hreflang eşleştirme JS-rendered, Python requests gerekiyor (Adım 2.3 için)
- **Sputnik EN için Türkiye'den lokal Python ile erişim**: TR ✓ (anlatilaninotesi.com.tr), EN ✗ (sputnikglobe.com — RTÜK SNI bloğu). Çözüm: GitHub Actions Microsoft-hosted Ubuntu runner (Frankfurt) — `.github/workflows/scrape_sputnik_en.yml` workflow'u manuel `workflow_dispatch` ile tetiklenir.

## SON DURUM
Adım 2.2 Pilot Scraping TAMAMLANDI: 29 JSON dosyası oluşturuldu (Sputnik: 5 EN + 4 TR, Euronews: 1 EN + 3 TR, AA: 10 EN + 5 TR + 1 format-test). Üç kritik sorun çözüldü: (1) AA arşiv erişimi, (2) Euronews TR Ekim boşluğu, (3) AA Oct 7, 2023 URL keşfi. Pilot raporu: C:\GazzeKorpus\pilot\00_pilot_scraping_raporu.md. Sıradaki adım: Adım 2.3 Tam Scraping — GDELT+AA döngüsü, Sputnik günlük arşiv döngüsü, Euronews tag pagination + Python hreflang.
