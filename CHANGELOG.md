# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-01

### Added

- Full Debian/Ubuntu package support (.deb)
- AppData/MetaInfo file for software center integration
- Automated .deb package building with cargo-deb
- GitHub Actions workflow for .deb package releases
- Installation and uninstallation scripts
- Shell completions (bash, zsh, fish)
- Man page documentation (ro-start.1)
- Desktop autostart support
- Package manager integration (apt, dnf, pacman, zypper)
- System notifications support
- Multi-language support (9 languages: en, tr, de, es, fr, it, ja, ru, zh)
- INSTALL.md documentation

### Changed

- Updated version to 2.0.0
- Improved Cargo.toml with optimized tokio features
- Enhanced AppData with developer info and release URLs
- Updated maintainer information to Acik Kaynak Gelistirme Toplulugu
- Improved desktop file with better metadata
- Optimized release profile for smaller binary size

### Fixed

- Desktop file version field corrected
- AppData validation warnings resolved
- Developer tag updated to modern format
- Proper icon reference in desktop files

## [1.0.0] - 2026-01-31

### Added

- Complete rewrite in Rust + GTK4 for native Linux experience
- GTK4 + libadwaita native interface
- System information dashboard (CPU, RAM, desktop environment, kernel info)
- Multi-language support (i18n ready)
- Multi-desktop environment support (GNOME, KDE Plasma, Xfce, etc.)
- Native application metadata and desktop integration

### Changed

- Migrated from Python + PyQt6 + React to native Rust + GTK4
- Replaced web-based UI with native GTK4 widgets
- Replaced custom theme with libadwaita components

### Removed

- Python backend implementation
- React frontend
- Node.js dependencies
- QtWebEngine dependency

## [Previous Versions]

### Python Implementation (Pre-1.0.0)

- Experimental implementations in Python and other languages
- These versions have been archived in separate branches
- Not recommended for production use

[2.0.0]: https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/tag/v2.0.0
[1.0.0]: https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/tag/v1.0.0
