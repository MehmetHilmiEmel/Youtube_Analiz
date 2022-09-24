# Youtube_Analiz

  Projede Doğal Dil İşleme alanında yaygın olarak kullanılan Hugging Face
  kütüphanesindeki
  <a href="https://huggingface.co/nanelimon/bert-base-turkish-bullying"
    >Nane Limon bert-base-turkish-bullying</a>
  modeli hazır olarak kullanılmıştır. Projedeki amaç, youtube üzerinden
  yapılan videoların siber zorbalık içerip içermediğini tespit etmek, ve
  tespit edilen yorumların hangi tür siber zorbalık içerdiğini bulmaktır.
  Bu proje, kullanıcıların herhangi bir siber zorbalığa maruz kalmadan
  önce içerisinde "Hakaret", "Irkçılık" ve "Cinsiyetçilik" içeren
  yorumları tespit edip, kullanıcıları bu tarz içerikli yorumlardan
  korumaktır.

# Projede Kullanılan Kütühaneler
Projede kullanılan kütüphaneleri ve versiyonlarını görmek için requirements.txt dosyasına tıklayabilirsiniz.

# Projeyi Nasıl Kullanabilirsiniz?
Öncelikle masaüstünde bir klasör oluşturup bu git reposunu o klasörün içine klonlayın <br>

```
$ git clone https://github.com/MehmetHilmiEmel/Youtube_Analiz.git
```
<br>
Sonrasında klasörün içine sanal ortam kurun ve sanal ortamı aktif hale getitirin

```
$ git virtualenv venv
$ source venv/bin/activate
```
Aktif hale getirdikten sonra requirements.txt dosyasındaki kütüphaneleri indirebiliriz. Bunun için:

```
$ pip install -r requirements.txt
```

komutunu yazmanız gerekiyor.<br>
Gerekli kütüphaneleri indirdikten sonra proje kullanıma hazır olacaktır. Projeyi çalıştırmak için

```
$ cd youtube/youtube
$ python manage.py runserver
```

komutlarını girin. 

Not(youtube_analiz/views.py) dosyasında key değişkenine string formatında kendi Google Developer anahtarınızı giriniz.
