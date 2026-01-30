# 🚀 Ro-Start

**Linux Dağıtımları için Modern Karşılama Uygulaması** - Rust + GTK4 + libadwaita ile geliştirilmiştir.

[English](README.md) | **Türkçe**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Rust CI](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml/badge.svg)](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml)

---

## 📖 Genel Bakış

Ro-Start, modern Linux dağıtımları için özel olarak tasarlanmış, native bir karşılama uygulamasıdır. Tamamen Rust ile yazılmış olup GTK4 ve libadwaita kullanarak mükemmel performans ve native GNOME deneyimi sunar.

## ✨ Özellikler

- ✅ **Sistem Bilgisi Gösterimi** - CPU, RAM ve depolama istatistikleri
- ✅ **GTK4 + libadwaita Arayüz** - Native GNOME entegrasyonu
- ✅ **Yıldırım Hızı** - Alternatiflerden 5x daha hızlı başlangıç
- ✅ **Hafif** - Sadece ~45MB RAM kullanımı
- ✅ **Hızlı Aksiyonlar** - Sistem güncellemeleri, yazılım önerileri
- ⏳ **Sürücü Yönetimi** - Otomatik algılama ve kurulum (yakında)
- ⏳ **Çoklu Dil Desteği** - i18n desteği (yakında)

## 📋 Gereksinimler

### Kullanıcılar İçin

- **GTK4** 4.12+ 
- **libadwaita** 1.5+
- **Linux** (herhangi bir modern dağıtım)

### Geliştiriciler İçin

- **Rust** 1.70+ ([rustup ile yükle](https://rustup.rs/))
- **GTK4 geliştirme dosyaları**
- **libadwaita geliştirme dosyaları**  
- **pkg-config**

## 📦 Kurulum

### Hazır Paket (Önerilen)

[GitHub Releases](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases) sayfasından en son sürümü indirin:

```bash
# İndir ve çıkart
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-v2.0.0-linux-amd64.tar.gz
tar xzf ro-start-v2.0.0-linux-amd64.tar.gz
cd ro-start-v2.0.0

# Sistem genelinde kur
sudo install -Dm755 ro-start /usr/local/bin/ro-start
sudo install -Dm644 ro-start.desktop /usr/share/applications/ro-start.desktop
sudo install -Dm644 ro-start.png /usr/share/icons/hicolor/512x512/apps/ro-start.png
```

### Kaynak Koddan Derleme

**Ubuntu/Debian:**
```bash
sudo apt install build-essential pkg-config libgtk-4-dev libadwaita-1-dev
```

**Fedora:**
```bash
sudo dnf install gcc pkg-config gtk4-devel libadwaita-devel
```

**Derleme:**
```bash
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start
./build.sh
./target/release/ro-start
```

## 📊 Performans

| Metrik | Python + Qt | Electron | **Rust + GTK4** |
|--------|-------------|----------|-----------------|
| Başlangıç | 2.5s | 3.0s | **0.5s** ✅ |
| RAM | 200MB | 300MB | **45MB** ✅ |
| Binary Boyutu | - | ~100MB | **8MB** ✅ |
| Native Görünüm | ⚠️ | ❌ | **✅** |

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

## 📄 Lisans

Bu proje **GNU General Public License v3.0** ile lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

<div align="center">

**Türkiye'de ❤️ ile geliştirildi - [Açık Kaynak Geliştirme Topluluğu](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu)**

⭐ GitHub'da yıldızlamayı unutmayın!

</div>
