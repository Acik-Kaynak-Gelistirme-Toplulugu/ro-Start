# 🚀 Ro-Start

> **Modern Linux karşılama uygulaması — Hızlı, güvenli ve güzel**  
> Rust + GTK4 + libadwaita ile geliştirildi

[English](README.md) | [Türkçe](README.tr.md)

[![Lisans: GPL v3](https://img.shields.io/badge/Lisans-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Rust CI](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml/badge.svg)](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml)
[![GitHub sürümü](https://img.shields.io/github/v/release/Acik-Kaynak-Gelistirme-Toplulugu/ro-start)](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest)
[![Rust](https://img.shields.io/badge/Rust-1.70%2B-orange)](https://www.rust-lang.org/)
[![GTK4](https://img.shields.io/badge/GTK-4.12%2B-blue)](https://gtk.org/)

[Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Derleme](#%EF%B8%8F-kaynaktan-derleme) • [Katkıda Bulunma](#-katkıda-bulunma) • [Lisans](#-lisans)

---

## 🎯 Özellikler

- ✅ **Sistem Bilgisi Gösterimi** — CPU, RAM, çekirdek ve sistem istatistiklerini tek bakışta görün
- ✅ **GTK4 + libadwaita** — GNOME entegrasyonlu modern, yerel Linux arayüzü
- ✅ **Çoklu Masaüstü Desteği** — GNOME, KDE Plasma, Xfce ve diğer masaüstü ortamlarında çalışır
- ✅ **Hafif** — Düşük kaynak kullanımı (~45 MB RAM)
- ✅ **Hızlı Başlatma** — Rust ile optimize edilmiş performans (~0.5s)
- ✅ **Çoklu Dil Desteği** — 9 dil: English, Türkçe, Deutsch, Español, Français, Italiano, 日本語, Русский, 中文
- ✅ **Paket Yöneticisi Entegrasyonu** — apt, dnf, pacman, zypper otomatik algılama

---

## 📋 Gereksinimler

### Kullanıcılar İçin

- **Linux** (modern herhangi bir dağıtım — Fedora, Ubuntu, Arch, vb.)
- **GTK4** 4.12+
- **libadwaita** 1.5+

### Geliştiriciler İçin

Kaynaktan derleme için ek gereksinimler:

- **Rust** 1.70+ ([rustup ile kurun](https://rustup.rs/))
- **GTK4 geliştirme dosyaları**
- **libadwaita geliştirme dosyaları**
- **pkg-config**

---

## 📦 Kurulum

### Fedora / RHEL (RPM)

```bash
# En son RPM paketini indirin
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-2.0.0-1.x86_64.rpm

# Kurun
sudo dnf install ./ro-start-2.0.0-1.x86_64.rpm
```

### Debian / Ubuntu (.deb)

```bash
# En son .deb paketini indirin ve kurun
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start_2.0.0-1_amd64.deb
sudo dpkg -i ro-start_2.0.0-1_amd64.deb
sudo apt-get install -f
```

### Binary Sürümden

En son sürümü [GitHub Releases](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases) sayfasından indirin:

```bash
# İndirin ve çıkartın
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-v2.0.0-linux-amd64.tar.gz
tar xzf ro-start-v2.0.0-linux-amd64.tar.gz
cd ro-start-v2.0.0

# Sistem genelinde kurun
sudo ./install.sh
```

Daha fazla kurulum seçeneği için [docs/INSTALL.md](docs/INSTALL.md) dosyasına bakın.

---

## 🏗️ Kaynaktan Derleme

### Bağımlılıkları Kurun

**Fedora 39+:**

```bash
sudo dnf install gcc pkg-config gtk4-devel libadwaita-devel
```

**Ubuntu 24.04+ / Debian:**

```bash
sudo apt install build-essential pkg-config libgtk-4-dev libadwaita-1-dev
```

**Arch Linux:**

```bash
sudo pacman -S base-devel pkg-config gtk4 libadwaita
```

### Derleme

```bash
# Depoyu klonlayın
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start

# Release derlemesi
./build.sh

# Veya manuel olarak
cargo build --release
strip -s target/release/ro-start

# Çalıştırın
./target/release/ro-start
```

---

## 🚀 Neden Rust + GTK4?

| Metrik               | Değer            |
| -------------------- | ---------------- |
| **Başlatma Süresi**  | ~0.5 saniye      |
| **Bellek Kullanımı** | ~45 MB           |
| **Binary Boyutu**    | ~8 MB (stripped) |
| **CPU (boşta)**      | <%0.2            |

- **Performans** — Hızlı başlatma ile derlenmiş yerel binary
- **Bellek Verimli** — Electron tabanlı uygulamalara kıyasla düşük bellek ayak izi
- **Küçük Binary** — Kompakt çalıştırılabilir boyut
- **Yerel Entegrasyon** — Gerçek GTK4/libadwaita görünümü ve hissi

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Detaylar için [Katkıda Bulunma Rehberi](CONTRIBUTING.md) dosyasına bakın.

---

## 📄 Lisans

Bu proje **GNU Genel Kamu Lisansı v3.0** altında lisanslanmıştır — detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 📚 Dokümantasyon

- [Kurulum Rehberi](docs/INSTALL.md)
- [Geliştirme Rehberi](docs/DEVELOPMENT.md)
- [Mimari Genel Bakış](docs/ARCHITECTURE.md)
- [Paketleme Rehberi](docs/PACKAGING.md)
- [API Referansı](docs/API.md)
- [Değişiklik Günlüğü](CHANGELOG.md)
- [Güvenlik Politikası](SECURITY.md)
