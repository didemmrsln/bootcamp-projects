## 🎯 Arka Plan ve Amaçlar

Bu challenge, bir öncekinin devamı niteliğindedir: çiftlik ilk hayvanlarını karşılıyor!

Sınıflarınızı tamamen sıfırdan, yalnızca kodun onları nasıl kullandığını yorumlayarak yazmaya başlayacaksınız. Ayrıca test yazma konusunda da biraz daha bilgi edineceğiz.

## 📝 Specs

![Animals](https://drive.google.com/file/d/1T12LkxrN8-eqFtGX-BNemMaNwydpRpBC/view?usp=drive_link)

`make` kullanma! Challenge’ın sonuna kadar bekleyin; yönergeleri takip edin ve sınıfları kodlarken farming diary’nin sizi yönlendirmesine izin verin.

---

### 🐄 Parent ve Children

Artık inheritance’ın faydalarına aşinayız, o hâlde:

* Üç boş sınıf oluşturun.
* Parent ve children sınıfları arasındaki doğru inheritance ilişkisini kurun.

Bu kez önce parent sınıfa ortak davranışları yazıyoruz:

* Bir hayvan sıfır **energy** ile başlatılır.
* Bir hayvanı **feed** edebilirsiniz: energy değeri 1 artar.

---

### 🐔 Animals Talk

Sınıfları anlamak için çalıştırmak istediğimiz **programdan** başlayalım:

* `farm/farming_diary.py` dosyasını açın, *Day Three* bölümünü okuyun ve sınıfları kodlamak için ihtiyaç duyduğunuz bilgileri toplayın.
* Kodu çalıştırın: `python -m farm.farming_diary`. Hataları birer birer çözerek `Cow` ve `Chicken` sınıflarındaki eksik `talk` metotlarını yazın.

Beklenen çıktı:

```bash
📝 Day Three: Animals Talk
The cow says moo
The female chicken says cluck cluck
The male chicken says cock-a-doodle-doo
```

Program çalıştıktan sonra `make` çalıştırın. Bu aşamada 12 testin geçtiğini, 1 testin ise başarısız olduğunu görmelisiniz. Onu daha sonra çözeceğiz.

Şimdi yazdığınız kodu commit edip push etme zamanı. `git status` ile değişen dosyaları kontrol edin, ardından commit ve push yapın.

---

### 🍽️ Feed The Animals

Day Four’a geçelim ve tüm hayvanları bir iterasyonla besleyelim. Hayvanların ortak bir `feed` metodu olduğunu unutmayın! Farklı türde iki obje üzerinde aynı metodu çağırabilirsiniz. Bu kavrama [polymorphism](https://realpython.com/ref/glossary/polymorphism/) denir 🤓

`feed` hakkında bilmeniz gerekenler:

* `Cow`: enerji kazanmanın yanında 2 litre **milk** üretir.
* `Chicken`: enerji kazanmanın yanında yalnızca dişiler 2 **eggs** üretir (erkekler 0 üretir 🤷‍♂️).

**İpucu:** children metodu parent metodunu **genişletir**. Parent kısmını çağırmak için `super` kullanmayı unutma!

Beklenen çıktı:

```bash
📝 Day Four: Feed The Animals
The cow produced 2 liters of milk
The female chicken produced 2 eggs
The male chicken produced 0 eggs
```

---

### ✅ Test Zamanı

Programınız çalıştığında tekrar `make` çalıştırarak doğru kodlayıp kodlamadığınızı test edin.

Her şey yolundaysa hâlâ 12 test geçecek ve 1 test başarısız kalacaktır.

Bu son test neden başarısız? Sorunu bulun.

<details>
  <summary markdown='span'>💡 İpucu</summary>

`Cow` sınıfı için testleriniz olup olmadığını kontrol eden bir test yazdık. Ve hayır… henüz yok 🙂

Görev: Bu testleri sen yaz.

</details>

Devam edin ve:

* Yeni bir `tests/test_cow.py` dosyası oluşturun.
* Gerekli testleri yazın. İlham almak için `Chicken` sınıfının testlerine bakabilirsiniz.
* Toplamda 6 test olmalıdır.

<details>
  <summary markdown='span'>💡 6 teste ulaşamazsan ipuçları</summary>

* `test_initialize_sets_milk_to_zero`
* `test_initialize_sets_energy_to_zero`
* `test_feed_extends_method`
* `test_feed_adds_milk`
* `test_feed_adds_energy`
* `test_talk_returns_moo`

</details>

Hazır olduğunuzda `make` çalıştırın ve ek testlerin yürütüldüğünü görün. Artık 19 testin de geçtiğini görmelisiniz.

Test yazmak zaman alır. Neyse ki daha önce yazılmış testlerden bolca ilham alabilirsiniz. Baştan yazmanıza gerek yok; boilerplate kod kopyalamakta yanlış bir şey yok. Testlerin nasıl yazıldığını ve yorumlandığını anladıktan sonra GitHub Copilot gibi araçlar bu tür tekrar eden görevlerde oldukça yardımcı olabilir.

---

## 🏁 Çıkarımlar

Tebrikler! Artık `make` çalıştırarak kodunuzun düzgün organize edildiğini kontrol edebilirsiniz.

Children sınıflarda dört tür metod vardır:

* **inherit** edilen metotlar: yalnızca parent sınıfta tanımlıdır.
* Parent metodunu **extend** edenler: children sınıfta hafifçe değiştirilmiş hâlidir.
* Parent metodunu **override** edenler: tanımı tamamen farklıdır.
* Çocuk sınıfa özel metotlar: parent sınıfta hiç bulunmaz.

Bir metodu genişletmek `super` kullanmayı gerektirir; bu, parent metodunun gövdesini children metodunun içine kopyalayıp yapıştırmışsınız gibi davranır.

Ayrıca kendi testlerinizi yazmayı öğrendiniz. Sık yapmasanız bile testlerin nasıl yazıldığını bilmek çok değerlidir!
