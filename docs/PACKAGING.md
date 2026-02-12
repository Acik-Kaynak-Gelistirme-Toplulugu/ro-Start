# Packaging Guide for Ro-Start

This guide explains how to build distribution packages for Ro-Start.

## Table of Contents

- [Debian/Ubuntu (.deb)](#building-deb-package)
- [Fedora/RHEL (RPM)](#building-rpm-package)
- [Arch Linux (PKGBUILD)](#building-arch-package)

---

## Building .deb Package

## Prerequisites

### Install Dependencies

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    pkg-config \
    libgtk-4-dev \
    libadwaita-1-dev \
    cargo \
    rustc
```

### Install cargo-deb

```bash
cargo install cargo-deb
```

## Build Package

### Option 1: Using scripts/build_deb.sh

The simplest method:

```bash
./scripts/build_deb.sh
```

This script will:

1. Install cargo-deb if not present
2. Clean previous builds
3. Build the release binary
4. Strip the binary
5. Create the .deb package
6. Display package information

### Option 2: Manual Build

```bash
# Build release binary
cargo build --release

# Strip binary (optional, reduces size)
strip -s target/release/ro-start

# Create .deb package
cargo deb --no-build
```

## Package Location

The generated package will be located at:

```
target/debian/ro-start_2.0.0-1_amd64.deb
```

## Install Package

```bash
sudo dpkg -i target/debian/ro-start_2.0.0-1_amd64.deb
```

If you encounter dependency errors:

```bash
sudo apt-get install -f
```

## Package Contents

The .deb package includes:

- **Binary**: `/usr/bin/ro-start`
- **Desktop file**: `/usr/share/applications/ro-start.desktop`
- **Autostart file**: `/etc/xdg/autostart/ro-start-autostart.desktop`
- **Icon**: `/usr/share/icons/hicolor/512x512/apps/ro-start.png`
- **AppData**: `/usr/share/metainfo/org.osdev.ro_start.appdata.xml`
- **Man page**: `/usr/share/man/man1/ro-start.1`
- **Shell completions**:
  - Bash: `/usr/share/bash-completion/completions/ro-start`
  - Zsh: `/usr/share/zsh/site-functions/_ro-start`
  - Fish: `/usr/share/fish/vendor_completions.d/ro-start.fish`
- **Documentation**: `/usr/share/doc/ro-start/README.md`

## Inspect Package

### View package information

```bash
dpkg-deb --info target/debian/ro-start_2.0.0-1_amd64.deb
```

### List package contents

```bash
dpkg-deb --contents target/debian/ro-start_2.0.0-1_amd64.deb
```

### Extract package

```bash
dpkg-deb --extract target/debian/ro-start_2.0.0-1_amd64.deb /tmp/ro-start-extracted
```

## Verify Package

### Check package quality with Lintian

```bash
sudo apt-get install lintian
lintian target/debian/ro-start_2.0.0-1_amd64.deb
```

### Test installation in clean environment

Using Docker:

```bash
# Ubuntu 24.04
docker run -it --rm -v $(pwd):/work ubuntu:24.04 bash
cd /work
apt-get update
apt-get install -y ./target/debian/ro-start_2.0.0-1_amd64.deb
ro-start --version
```

## Configuration

The package metadata is configured in `Cargo.toml` under `[package.metadata.deb]`:

```toml
[package.metadata.deb]
maintainer = "Acik Kaynak Gelistirme Toplulugu <info@osdev.shop>"
copyright = "2026, Acik Kaynak Gelistirme Toplulugu"
license-file = ["LICENSE", "0"]
extended-description = """\
Ro-Start is a fast, safe, and beautiful Linux welcome application.
Built with Rust, GTK4, and libadwaita, it provides native GNOME
integration with excellent performance."""
depends = "$auto, libgtk-4-1, libadwaita-1-0"
section = "x11"
priority = "optional"
assets = [
    # Files to include in the package
]
```

## Troubleshooting

### cargo-deb not found

Install it:

```bash
cargo install cargo-deb
```

### Missing GTK4 dependencies

```bash
sudo apt-get install -y libgtk-4-dev libadwaita-1-dev pkg-config
```

### Binary too large

The binary is already stripped in the build script. If you need it even smaller:

```bash
# Use UPX compression (optional)
sudo apt-get install upx-ucl
upx --best --lzma target/release/ro-start
```

### Package doesn't install

Check dependencies:

```bash
dpkg-deb --info target/debian/ro-start_2.0.0-1_amd64.deb | grep Depends
apt-cache policy libgtk-4-1 libadwaita-1-0
```

## Distribution

### Upload to GitHub Releases

The `.github/workflows/build-deb.yml` workflow automatically builds and uploads .deb packages to GitHub Releases when you push a tag.

```bash
git tag v2.0.0
git push origin v2.0.0
```

### Host on PPA (Personal Package Archive)

For Ubuntu users, consider creating a PPA:

1. Create a Launchpad account
2. Set up your PPA
3. Build source package with `debuild`
4. Upload with `dput`

See: https://help.launchpad.net/Packaging/PPA

### Host on Custom Repository

Create an APT repository:

```bash
# Create repository structure
mkdir -p repo/pool/main
cp target/debian/ro-start_2.0.0-1_amd64.deb repo/pool/main/

# Generate Packages file
cd repo
dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz

# Create Release file
apt-ftparchive release . > Release

# Sign the release
gpg --clearsign -o InRelease Release
```

## See Also

- [INSTALL.md](INSTALL.md) - Installation guide
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guide
- [../debian/](../debian/) - Debian packaging files
- [../packaging/ro-start.spec](../packaging/ro-start.spec) - RPM spec file
- [../packaging/PKGBUILD](../packaging/PKGBUILD) - Arch Linux PKGBUILD
- [cargo-deb documentation](https://github.com/kornelski/cargo-deb)
- [cargo-generate-rpm documentation](https://github.com/cat-in-136/cargo-generate-rpm)

---

## Building RPM Package

### For Fedora / RHEL

#### Prerequisites

```bash
sudo dnf install gcc pkg-config gtk4-devel libadwaita-devel rpm-build
```

#### Using cargo-generate-rpm

```bash
# Install cargo-generate-rpm
cargo install cargo-generate-rpm

# Build release binary
cargo build --release
strip -s target/release/ro-start

# Generate RPM
cargo generate-rpm

# Install
sudo rpm -i target/generate-rpm/ro-start-*.rpm
```

The RPM metadata is configured in `Cargo.toml` under `[package.metadata.generate-rpm]`.

#### Using rpmbuild with spec file

```bash
# The spec file is located at packaging/ro-start.spec
rpmbuild -ba packaging/ro-start.spec
```

---

## Building Arch Package

### Using PKGBUILD

```bash
cd packaging/
makepkg -si
```

The `PKGBUILD` file handles:

1. Downloading the source from GitHub
2. Building with `cargo build --release`
3. Installing binary, desktop files, icons, man page, and shell completions
