# Installation Guide for Ro-Start

This guide provides detailed installation instructions for Ro-Start on various Linux distributions.

## Table of Contents

- [Binary Installation](#binary-installation)
- [Package Manager Installation](#package-manager-installation)
- [Building from Source](#building-from-source)
- [Post-Installation](#post-installation)
- [Uninstallation](#uninstallation)

---

## Binary Installation

### Download Pre-built .deb Package

For Debian/Ubuntu-based distributions:

```bash
# Download the latest .deb package
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start_2.0.0-1_amd64.deb

# Install the package
sudo dpkg -i ro-start_2.0.0-1_amd64.deb

# Install dependencies if needed
sudo apt-get install -f
```

### Download Pre-built Binary

For any Linux distribution:

```bash
# Download and extract
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-v2.0.0-linux-amd64.tar.gz
tar xzf ro-start-v2.0.0-linux-amd64.tar.gz
cd ro-start-v2.0.0

# Install using the install script
sudo ./install.sh
```

---

## Package Manager Installation

### Fedora / RHEL (RPM)

```bash
# Download the latest RPM package
wget https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/latest/download/ro-start-2.0.0-1.x86_64.rpm

# Install with dnf
sudo dnf install ./ro-start-2.0.0-1.x86_64.rpm
```

Or build RPM from source:

```bash
cargo install cargo-generate-rpm
cargo build --release
strip -s target/release/ro-start
cargo generate-rpm
sudo rpm -i target/generate-rpm/ro-start-*.rpm
```

### Debian / Ubuntu

```bash
# Using dpkg
sudo dpkg -i ro-start_2.0.0-1_amd64.deb
sudo apt-get install -f
```

### Arch Linux (AUR)

```bash
# Using PKGBUILD
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start/packaging
makepkg -si
```

### Flatpak (Universal)

Coming soon: `flatpak install org.osdev.ro_start`

---

## Building from Source

### Prerequisites

Install the required dependencies:

#### Debian/Ubuntu

```bash
sudo apt-get update
sudo apt-get install -y \
    curl \
    build-essential \
    pkg-config \
    libgtk-4-dev \
    libadwaita-1-dev \
    git
```

#### Fedora

```bash
sudo dnf install -y \
    curl \
    gcc \
    pkg-config \
    gtk4-devel \
    libadwaita-devel \
    git
```

#### Arch Linux

```bash
sudo pacman -S \
    curl \
    base-devel \
    pkg-config \
    gtk4 \
    libadwaita \
    git
```

### Install Rust

If you don't have Rust installed:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

### Clone and Build

```bash
# Clone the repository
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start

# Build the project
./build.sh

# Install system-wide (requires sudo)
sudo ./install.sh
```

### Build .deb Package

```bash
# Install cargo-deb
cargo install cargo-deb

# Build the .deb package
./scripts/build_deb.sh

# Install the generated package
sudo dpkg -i target/debian/ro-start_2.0.0-1_amd64.deb
```

---

## Post-Installation

### Verify Installation

```bash
# Check if installed correctly
ro-start --version

# View man page
man ro-start

# Run the application
ro-start
```

### Desktop Integration

Ro-Start should appear in your application menu automatically. If not, update the desktop database:

```bash
sudo update-desktop-database
sudo gtk-update-icon-cache -f -t /usr/share/icons/hicolor
```

### Autostart Configuration

To disable autostart:

```bash
# Remove autostart file
sudo rm /etc/xdg/autostart/ro-start-autostart.desktop

# Or launch with --no-startup flag
ro-start --no-startup
```

---

## Uninstallation

### Using install script

If you installed using the install script:

```bash
cd ro-start
sudo ./uninstall.sh
```

### Using dpkg (for .deb package)

```bash
sudo dpkg -r ro-start
```

### Manual uninstallation

```bash
# Remove binary
sudo rm /usr/bin/ro-start

# Remove desktop files
sudo rm /usr/share/applications/ro-start.desktop
sudo rm /etc/xdg/autostart/ro-start-autostart.desktop

# Remove icon
sudo rm /usr/share/icons/hicolor/512x512/apps/ro-start.png

# Remove AppData
sudo rm /usr/share/metainfo/org.osdev.ro_start.appdata.xml

# Remove man page
sudo rm /usr/share/man/man1/ro-start.1.gz

# Remove shell completions
sudo rm /usr/share/bash-completion/completions/ro-start
sudo rm /usr/share/zsh/site-functions/_ro-start
sudo rm /usr/share/fish/vendor_completions.d/ro-start.fish

# Update caches
sudo update-desktop-database
sudo gtk-update-icon-cache -f -t /usr/share/icons/hicolor
```

---

## Troubleshooting

### Missing Dependencies

If you get dependency errors:

**Debian/Ubuntu:**

```bash
sudo apt-get install -f
```

**Fedora:**

```bash
sudo dnf install gtk4 libadwaita
```

**Arch Linux:**

```bash
sudo pacman -S gtk4 libadwaita
```

### Application Not Starting

Check the logs:

```bash
ro-start --debug
```

Or check system logs:

```bash
journalctl -xe | grep ro-start
```

### Icon Not Showing

Update the icon cache:

```bash
sudo gtk-update-icon-cache -f -t /usr/share/icons/hicolor
```

---

## Support

- **Issues:** [GitHub Issues](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/discussions)
- **Email:** info@osdev.shop

---

## See Also

- [README.md](../README.md) - Project overview
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guide
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contributing guidelines
