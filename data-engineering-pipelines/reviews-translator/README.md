## Reviews Translator 📚

Artık bazı değişkenlerin customer satisfaction üzerindeki etkisine dair ilk anlayışımıza sahibiz. Özellikle, review score'un, order delivery süresinin uzunluğundan olumsuz etkilendiği görülüyor.

Ancak kantitatif analiz tek bilgi kaynağımız değil. Yazılı review içeriğine de erişimimiz var!

Yeni bir dataset keşfederken iyi bir uygulama, her zaman rastgele bazı gözlemler seçmek ve onlar hakkında elimizde ne varsa keşfetmektir.

Nicel bulgularımızı, customers tarafından yazılan review'ların nitel (qualitative) analiziyle ilişkilendirelim.

### Exercise

- Python library [google-trans-new](https://pypi.org/project/google-trans-new/) kullanarak, 1-yıldızlı review'lardan rastgele seçilmiş 100 tanesini Portekizce'den İngilizce'ye çeviren bir Python script implement edin.
- ⚠️ **100.000 yorumun tamamını çevirmeyin, yoksa sınıfın tamamı ücretsiz API translator'lardan geçici olarak ban yiyebilir**
- Bu trendler, önceki bulgularınızla benzer mi?
- Hangi diğer trendleri ortaya çıkarıyorsunuz ve daha fazla keşfetmek istiyorsunuz?

Hints:
- Dokümantasyonu okuyup API'yi kendi başınıza çalıştırmayı deneyin – 10 satırdan fazla kod olmayacak
- Yeni bir notebook oluşturmakta ya da direkt olarak favori code editor'ınızda kod yazmakta özgürsünüz

## Nitel Analiz: AI Okuması vs. Anahtar Kelime Script'i

100 rastgele 1-yıldızlı yorum Portekizce'den İngilizce'ye çevrildi (92 başarılı, 8 çeviri hatası → data/translated_reviews.csv). Temalar iki farklı yöntemle çıkarıldı ve karşılaştırıldı:

### Yöntem 1 — AI ile manuel okuma (gözle tarama)
Tüm 92 çeviri tek tek okunarak temalar sezgisel olarak etiketlendi. Baskın olarak öne çıkanlar: teslimat gecikmesi/eksikliği, yanlış ürün, eksik sipariş, hasarlı/kusurlu ürün, iletişim sorunu, iade talebi, yanıltıcı açıklama.

### Yöntem 2 — Anahtar kelime tabanlı script (analyze_themes.py)
Aynı 92 yorum, önceden tanımlı İngilizce anahtar kelime setleriyle programatik olarak etiketlendi:

| Tema | Sayı | Yüzde |
|---|---|---|
| delivery_delay_or_missing | 20 | %22.2 |
| refund_or_cancellation | 13 | %14.4 |
| incomplete_order | 13 | %14.4 |
| damaged_or_defective | 7 | %7.8 |
| customer_service_issue | 7 | %7.8 |
| wrong_product | 5 | %5.6 |
| misleading_description | 5 | %5.6 |
| **Hiçbir temaya uymayan** | 33 | %36.7 |

### İki yöntem arasındaki farkın sebepleri
- **Örtüşme (overlap):** Bir yorum script'te birden fazla temaya aynı anda girebiliyor (örn. hem teslimat hem iade), bu yüzden yüzdeler toplamda %100'ü aşıyor — AI okumasında bu örtüşme daha az belirgindi çünkü tek "baskın tema" seçilmişti.
- **`refund_or_cancellation` bağımsız değil:** Script bunu ayrı bir tema olarak sayıyor, ama içerik olarak çoğunlukla teslimat/yanlış ürün sorununun **sonucu** (müşteri önce sorunu anlatıyor, sonra iade istiyor). AI okuması bunu otomatik olarak ana temanın altına gömmüştü; script bunu ayrıştıramadı çünkü sadece anahtar kelime eşleşmesine bakıyor, cümle içi neden-sonuç ilişkisini anlamıyor.
- **%36.7 "temasız" oranı:** Script'in anahtar kelime listesi sınırlı (7 tema, ~40 kelime/ifade). AI okuması bu yorumların çoğunu yine de bir temaya yerleştirebiliyordu çünkü bağlamı (context) anlayabiliyor — script ise tanımlı kelime dışına çıkan hiçbir ifadeyi yakalayamıyor.

### Analiz nasıl derinleştirilebilir
1. **Anahtar kelime listesini genişletmek** — "temasız" kalan 33 yorumu ayrıca okuyup ortak ifadeler bulmak, listeye eklemek.
2. **Basit kural tabanlı script yerine embedding/NLP tabanlı sınıflandırma** (örn. sentence embeddings + kümeleme) kullanmak — anahtar kelimeye değil, anlama dayalı gruplama sağlar.
3. **Örtüşen temaları hiyerarşik hale getirmek** — örn. `refund_or_cancellation`'ı bağımsız bir tema değil, diğer temaların bir "sonuç etiketi" olarak modellemek.
4. **Nicel doğrulama** — `delivery_delay_or_missing` etiketli siparişlerin gerçek `wait_time` / `delay_vs_expected` değerlerine bakıp, etiketin nicel veriyle ne kadar örtüştüğünü test etmek.

### Genel Sonuç
Her iki yöntem de en güçlü teması aynı buluyor: **teslimat gecikmesi/eksikliği**, önceki istatistiksel bulguyla (review score ile delivery süresi arasında r=-0.30, p<0.001) tutarlı. Ancak kesin sayılar için anahtar kelime script'i tek başına yeterli değil; AI'ın bağlamsal okuması ile birlikte kullanılması daha güvenilir bir resim veriyor — ikisi birbirini tamamlıyor, biri diğerinin yerini tutmuyor.

## Olist'in Sorması Gereken Soru: Lojistik mi, Satıcı mı?

Notebook'taki orijinal soru şuydu: kötü review'ların delivery mi yoksa seller/ürün kaynaklı mı olduğunu nasıl ayırt ederiz? Tema etiketleri bu ayrımı doğal olarak iki gruba böldü:

**🚚 Lojistik/teslimat kaynaklı (satıcının kontrolünde değil):**
- `delivery_delay_or_missing` (%22.2) — kargo gecikmesi, ürün hiç gelmemesi

**📦 Satıcı/ürün kaynaklı (seller'ın sorumluluğunda):**
- `wrong_product` (%5.6) — yanlış ürün gönderilmiş
- `damaged_or_defective` (%7.8) — kusurlu/hasarlı ürün
- `incomplete_order` (%14.4) — eksik gönderim
- `misleading_description` (%5.6) — yanıltıcı ürün açıklaması

**Karma/belirsiz (her iki kaynaktan da olabilir):**
- `customer_service_issue` (%7.8), `refund_or_cancellation` (%14.4)

### Kesin ayrım için önerilen yöntem
1. `delivery_delay_or_missing` + yüksek `wait_time`/`delay_vs_expected` → **lojistik/kargo sorunu**, satıcı suçlanmamalı
2. `wrong_product` / `damaged_or_defective` / `incomplete_order` + normal teslimat süresi → **satıcı hatası**
3. Her ikisi birden → karma sorun, ayrıca incelenmeli

### Olist için aksiyon önerileri
- **Katalogdan ürün çıkarma:** `wrong_product` + `damaged_or_defective` + `misleading_description` etiketlerinin belirli ürün kategorilerinde yoğunlaşıp yoğunlaşmadığına bakılmalı
- **Satıcı marketplace'ten kaldırma:** bu etiketlerin belirli `seller_id`'lerde tekrar edip etmediğine bakılmalı (tek seferlik hata vs. sistematik kötü satıcı ayrımı için)
- **Kargo/lojistik firması değişikliği:** `delivery_delay_or_missing` etiketli siparişlerin coğrafi bölge/kargo firması bazında kümelenip kümelenmediğine bakılmalı
