# Hasta Kayıtları Keşifçi Veri Analizi (EDA) ve Veri Temizleme

## 📌 Proje Amacı
Bu proje, hasta kayıtlarını içeren bir veri seti üzerinde Python ve Pandas kütüphaneleri kullanılarak gerçekleştirilen detaylı bir veri temizleme, manipülasyon ve keşifçi veri analizi (EDA) çalışmasıdır.

## 🛠️ Kullanılan Teknolojiler
* Python
* Pandas

## 📊 Veri Seti Hakkında
Projede kullanılan `hasta_kayitlari.csv` veri seti; hastaların demografik bilgileri, yatış süreleri, tanıları ve tedavi maliyetleri gibi bilgileri içermektedir. [cite_start]Veri seti başlangıçta 12 sütun ve 1010 satırdan oluşmaktadır[cite: 13, 14]. 

## ⚙️ Proje Adımları

**1. Veriyi Tanıma ve Hazırlık**
* [cite_start]Veri seti Pandas kullanılarak projeye dahil edilmiş ve temel yapısı incelenmiştir[cite: 1, 2, 3].
* [cite_start]Veri setindeki eksik değerler ve tekrar eden kayıtlar tespit edilmiştir[cite: 17, 22].

**2. Veri Temizleme**
* [cite_start]Veri setinde tespit edilen 10 adet tekrar eden (dublicate) satır silinmiştir[cite: 24, 26].
* [cite_start]`bmi` ve `sistolik_kb` sütunlarında bulunan eksik veriler, ilgili sütunların medyan (ortanca) değerleri kullanılarak doldurulmuştur[cite: 56, 83].
* [cite_start]`maliyet` verisi eksik olan satırlar doğrudan veri setinden çıkarılmıştır[cite: 110].
* [cite_start]İşlemler sonucunda veri seti 978 satıra düşürülerek temiz hale getirilmiştir[cite: 139].

**3. Filtreleme ve Özellik Mühendisliği (Feature Engineering)**
* [cite_start]Hastaların toplam maliyeti yatış süresine bölünerek yeni bir `gunluk_maliyet` sütunu oluşturulmuştur[cite: 149].
* [cite_start]Hastalar yaşlarına göre "genç", "orta yaşlı" ve "yaşlı" olmak üzere `yas_grubu` adında yeni bir kategorik değişkene ayrılmıştır[cite: 149, 150, 151, 152].

**4. Özet İstatistikler ve Bulgular**
* [cite_start]Hasta yoğunluğu en yüksek olan şehir %28.8 oranıyla İstanbul olarak belirlenmiştir[cite: 188, 189, 206].
* [cite_start]Hastanede en yoğun başvuru alan bölüm Kardiyoloji'dir[cite: 209, 210, 239].
* [cite_start]Yaş ile Vücut Kitle İndeksi (BMI) arasında doğrusal bir ilişki gözlemlenmiş, yaş arttıkça ortalama BMI değerinin de arttığı tespit edilmiştir[cite: 249].
* [cite_start]Sigortası bulunmayan hastaların maliyetinin, sigortalı hastalara kıyasla daha yüksek olduğu görülmüştür[cite: 253].
* [cite_start]Kardiyoloji bölümünde sigortası olmayan hasta sayısı diğer bölümlere göre en yüksek seviyededir (34 hasta)[cite: 256, 257, 269].

## 🚀 Kurulum ve Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/repo-adi.git](https://github.com/KULLANICI_ADIN/repo-adi.git)
