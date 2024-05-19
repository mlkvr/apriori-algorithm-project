## Proje Özeti
Bu proje, kullanıcıların kendi veri setlerini yükleyerek apriori algoritmasını kullanarak birliktelik analizi yapmalarını sağlayan bir web uygulamasıdır. Kullanıcılar, minimum destek eşiğini belirleyerek sık itemsetleri ve birliktelik kurallarını çıkarabilirler. Sonuçlar grafiksel olarak ve tablo şeklinde gösterilir.

## Kullanılan Teknolojiler
Python
Flask
Pandas
mlxtend
Bootstrap 5
DataTables (jQuery)
Kurulum ve Çalıştırma
Gereksinimler
Python 3.6+
pip (Python paket yöneticisi)


## Gerekli Python Kütüphaneleri
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```python
pip install flask pandas mlxtend matplotlib seaborn
```

## Proje Dosyaları
app.py: Flask uygulaması için ana Python dosyası.
templates/index.html: Uygulamanın HTML şablonu.
static/apriori_results.png: Grafiklerin kaydedildiği dizin.

##Çalıştırma
Proje dosyalarını indirdikten ve gerekli kütüphaneleri kurduktan sonra, terminal veya komut istemcisinde aşağıdaki komutu çalıştırarak uygulamayı başlatabilirsiniz:

```python
python app.py
```

Uygulama, http://127.0.0.1:5000/ adresinde çalışacaktır.

## Kullanım Kılavuzu
Veri Seti Yükleme: .csv formatında bir veri seti seçin.
Minimum Destek Eşiği Belirleme: Minimum destek eşiğini (örneğin, 0.01) girin.
Yükleme ve Analiz: "Upload and Analyze" düğmesine tıklayın.

## Çıktılar
Grafik: Apriori analizi sonuçlarının destek ve güven değerleri arasındaki ilişkiyi gösteren bir grafik.
Tablo: Sık itemsetlerin ve birliktelik kurallarının yer aldığı, sıralanabilir bir tablo.