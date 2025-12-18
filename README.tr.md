# 🚀 Ro-Start

[![Read in English](https://img.shields.io/badge/Switch_Language-English-blue?style=for-the-badge)](README.md)

> **Linux dağıtımları için yeni nesil, şeffaf karşılama uygulaması.**

**Ro-Start**, geleneksel karşılama ekranlarını modern "Akışkan Cam" (Liquid Glass) estetiği ile değiştirir. **Python (PyQt6)**'ın sistem erişim gücünü ve **React (Vite + TailwindCSS)**'in modern arayüz yeteneklerini birleştiren hibrit mimarisi ile Linux dağıtımınız için premium bir ilk izlenim yaratır.

![Ro-Start Banner](assets/welcome_screen.png)

## ✨ Temel Özellikler

- **🎨 Liquid Glass UI:** Modern işletim sistemi estetiğinden ilham alan çarpıcı, şeffaf ve mat tasarım dili.
- **🚀 Hibrit Mimari:**
  - **Backend:** Sınırsız sistem erişimi için Python + PyQt6 + QtWebEngine.
  - **Frontend:** 60fps animasyonlar için React + TypeScript + Framer Motion.
- **📊 Sistem Özeti:** CPU, GPU, RAM ve Depolama istatistiklerinin görsel sunumu.
- **🎮 Sürücü Yöneticisi:** Basitleştirilmiş NVIDIA sürücü kurulumu ve yönetimi.
- **🌍 Adaptif:** Sistem dilini otomatik algılar ve farklı çözünürlüklere uyum sağlar.
- **⚡ Hazır Başlangıç:** İsteğe bağlı sistem başlangıç entegrasyonu (Autostart).

![Driver Manager UI](assets/driver_manager.png)

## 🏗️ Proje Yapısı

Proje iki temel bölüme ayrılmıştır:

```
ro-start/
├── backend/           # 🐍 Python Backend (Uygulama Mantığı)
│   ├── core/          # Sistem araçları, sürücü mantığı, teknik özellikler
│   ├── ui/            # PyQt6 penceresi ve WebEngine kurulumu
│   └── main.py        # Giriş noktası
│
├── frontend/          # ⚛️ React Frontend (Görünüm)
│   ├── src/           # Bileşenler, hook'lar, stiller
│   ├── dist/          # Derlenmiş statik dosyalar (Python tarafından yüklenir)
│   └── public/        # Varlıklar (Assets)
│
└── requirements.txt   # Python Bağımlılıkları
```

## 🛠️ Kurulum ve Geliştirme

Yerel makinenizde geliştirme ortamını kurmak için aşağıdaki adımları izleyin.

### Gereksinimler

- **Python 3.10+**
- **Node.js 18+ & npm** (Arayüzü derlemek için)
- **Linux Ortamı** (Tam sürücü işlevselliği için önerilir, ancak macOS/Windows üzerinde simülasyon modunda çalışır)

### 1. Kullanıcı Arayüzünü Derleyin

Python uygulaması derlenmiş HTML/CSS/JS dosyalarını yükler. Önce frontend'i derlemelisiniz.

```bash
cd frontend
npm install
npm run build
cd ..
```

### 2. Python Ortamını Hazırlayın

Sanal ortam (venv) kullanmanız önerilir.

```bash
# Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# Bağımlılıkları yükle (Geliştirici modu)
pip install -e .
```

### 3. Ro-Start'ı Çalıştırın

Uygulamayı başlatın.

```bash
# Önerilen
ro-start

# veya doğrudan
python3 backend/main.py
```

> **Not:** macOS veya Windows üzerinde çalıştırıyorsanız, "Sürücü Kurulumu" gibi sisteme özgü özellikler **Simülasyon Modunda** (taklit yanıtlarla) çalışacaktır.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İster yeni bir dağıtım (Arch, Fedora) desteği eklemek, ister "Liquid Glass" tema bileşenlerini geliştirmek olsun.

1. Depoyu fork'layın (çatallayın)
2. Özellik dalınızı oluşturun (`git checkout -b feature/HarikaOzellik`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'HarikaOzellik eklendi'`)
4. Dalınıza push'layın (`git push origin feature/HarikaOzellik`)
5. Bir Pull Request (Çekme İsteği) açın

## 📄 Lisans

GNU General Public License v3.0 altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
