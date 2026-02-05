# Bershka Stok Takip Botu
Bu proje, Bershka mağazasındaki belirli ürünlerin stok durumunu otomatik olarak takip eden ve stok geldiğinde anlık bildirim gönderen bir otomasyon sistemidir.

## Özellikler
* **Gerçek Zamanlı Takip:** Ürün sayfalarını Selenium kullanarak belirli aralıklarla tarar.
* **Telegram Bildirimleri:** Stok durumu değiştiğinde anlık olarak Telegram üzerinden mesaj gönderir.
* **Bulut Entegrasyonu:** Google Cloud Platform (GCP) üzerinde 7/24 kesintisiz çalışacak şekilde yapılandırılmıştır.
* **Performans Odaklı:** `finally: driver.quit()` bloğu ile sunucu kaynaklarını (RAM/CPU) verimli kullanır.

## Kullanılan Teknolojiler
* **Dil:** Python 3
* **Otomasyon:** Selenium / Webdriver
* **Sunucu:** Google Cloud Compute Engine
* **Yönetim:** Linux Screen (Arka plan süreç yönetimi için)

## Kurulum ve Çalıştırma
Sunucuda gerekli kütüphaneleri yükle:
`pip install selenium webdriver-manager python-telegram-bot`
Botu arka planda kesintisiz çalıştırmak için:
1. `screen -S bershka_bot` komutuyla yeni bir ekran aç.
2. `python3 bershka.py` yazarak botu başlat.
3. `Ctrl + A` ve sonra `D` tuşlarına basarak ekrandan çık.
