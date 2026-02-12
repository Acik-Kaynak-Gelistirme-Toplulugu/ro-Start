# 🚀 Ro-Start

> **Modern Linux welcome application — Fast, safe, and beautiful**  
> Built with Rust + GTK4 + libadwaita

[English](README.md) | [Türkçe](README.tr.md)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Rust CI](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml/badge.svg)](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/actions/workflows/rust.yml)
[![GitHub release](https://img.shields.io/github/v/release/Acik-Kaynak-Gelistirme-Toplulugu/ro-start)](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest)
[![Rust](https://img.shields.io/badge/Rust-1.70%2B-orange)](https://www.rust-lang.org/)
[![GTK4](https://img.shields.io/badge/GTK-4.12%2B-blue)](https://gtk.org/)

[Features](#-features) • [Installation](#-installation) • [Building](#%EF%B8%8F-building-from-source) • [Contributing](#-contributing) • [License](#-license)

---

## 🎯 Features

- ✅ **System Information Display** — View CPU, RAM, kernel, and system stats at a glance
- ✅ **GTK4 + libadwaita** — Modern, native Linux UI with GNOME integration
- ✅ **Multi-Desktop Support** — Works on GNOME, KDE Plasma, Xfce, and other DEs
- ✅ **Lightweight** — Minimal resource usage (~45 MB RAM)
- ✅ **Fast Startup** — Built with Rust for optimal performance (~0.5s)
- ✅ **Multi-language Support** — 9 languages: English, Türkçe, Deutsch, Español, Français, Italiano, 日本語, Русский, 中文
- ✅ **Package Manager Integration** — Auto-detects apt, dnf, pacman, zypper

---

## 📋 Requirements

### For Users

- **Linux** (any modern distribution — Fedora, Ubuntu, Arch, etc.)
- **GTK4** 4.12+
- **libadwaita** 1.5+

### For Developers

Additional requirements for building from source:

- **Rust** 1.70+ ([install via rustup](https://rustup.rs/))
- **GTK4 development files**
- **libadwaita development files**
- **pkg-config**

### Desktop Environment Support

| Desktop Environment  | Status             |
| -------------------- | ------------------ |
| **GNOME** 40+        | ✅ Fully supported |
| **KDE Plasma** 5.27+ | ✅ Fully supported |
| **Xfce** 4.16+       | ✅ Fully supported |
| **Cinnamon** 5.0+    | ✅ Supported       |
| **MATE** 1.24+       | ✅ Supported       |
| **Budgie** 10+       | ✅ Supported       |
| **LXDE** 0.9.3+      | ✅ Supported       |
| **Deepin** 20+       | ✅ Supported       |

---

## 📦 Installation

### Fedora / RHEL (RPM)

```bash
# Download the latest RPM package
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-2.0.0-1.x86_64.rpm

# Install
sudo dnf install ./ro-start-2.0.0-1.x86_64.rpm
```

### Debian / Ubuntu (.deb)

```bash
# Download and install the latest .deb package
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start_2.0.0-1_amd64.deb
sudo dpkg -i ro-start_2.0.0-1_amd64.deb
sudo apt-get install -f
```

### From Binary Release

Download the latest release from [GitHub Releases](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases):

```bash
# Download and extract
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-v2.0.0-linux-amd64.tar.gz
tar xzf ro-start-v2.0.0-linux-amd64.tar.gz
cd ro-start-v2.0.0

# Install system-wide
sudo ./install.sh
```

For more installation options, see [docs/INSTALL.md](docs/INSTALL.md).

---

## 🏗️ Building from Source

### Install Dependencies

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

### Build

```bash
# Clone repository
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start

# Build release binary
./build.sh

# Or manually
cargo build --release
strip -s target/release/ro-start

# Run
./target/release/ro-start
```

### Distribution Packages

#### Fedora / RHEL (RPM)

```bash
cargo install cargo-generate-rpm
cargo build --release
strip -s target/release/ro-start
cargo generate-rpm
sudo rpm -i target/generate-rpm/ro-start-*.rpm
```

#### Debian / Ubuntu (.deb)

```bash
cargo install cargo-deb
cargo deb
sudo dpkg -i target/debian/ro-start_*.deb
```

---

## 🚀 Why Rust + GTK4?

| Metric           | Value            |
| ---------------- | ---------------- |
| **Startup Time** | ~0.5 seconds     |
| **Memory Usage** | ~45 MB           |
| **Binary Size**  | ~8 MB (stripped) |
| **CPU (idle)**   | <0.2%            |

- **Performance** — Compiled native binary with fast startup
- **Memory Efficient** — Low memory footprint compared to Electron-based apps
- **Small Binary** — Compact executable size
- **Native Integration** — True GTK4/libadwaita look and feel

---

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Check format: `cargo fmt --check`
5. Run lint: `cargo clippy --all-features`
6. Build: `cargo build --release`
7. Commit (`git commit -m 'feat: add amazing feature'`)
8. Push (`git push origin feature/amazing-feature`)
9. Open a Pull Request

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

## 📚 Documentation

- [Installation Guide](docs/INSTALL.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Packaging Guide](docs/PACKAGING.md)
- [API Reference](docs/API.md)
- [Changelog](CHANGELOG.md)
- [Security Policy](SECURITY.md)
