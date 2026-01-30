# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-30

### Added
- Production-ready packaging with `pyproject.toml`
- Desktop entry file (`ro-start.desktop`) for Linux integration
- Application icon (512x512 gradient rocket design)
- AppStream metadata (`org.osdev.ro_start.appdata.xml`) for software centers
- Uninstall script (`scripts/uninstall.sh`)
- Clean script (`scripts/clean.sh`) for development artifacts
- Pydantic dependency for input validation
- Config-based URL loading for home page links

### Changed
- Improved `install.sh` with full system integration
  - Desktop file installation to `/usr/share/applications/`
  - Icon installation to `/usr/share/icons/`
  - AppStream metadata installation
  - System-wide symlink creation
- Fixed Flatpak manifest security (removed `filesystem=host`)
- Updated Flatpak manifest with proper build commands
- Enhanced `requirements.txt` with version pinning
- Fixed autostart feature to use `ro-start` executable
- Updated autostart desktop file name to `ro-start.desktop`
- Updated README with production installation instructions

### Security
- Removed broad filesystem access from Flatpak manifest  
- Added minimal D-Bus permissions for PackageKit and login manager
- Restricted filesystem access to only `xdg-config/autostart`

## [1.0.0] - 2024-XX-XX

### Added
- Initial release
- Hybrid architecture (Python + PyQt6 + React)
- Liquid Glass UI theme
- System information dashboard (CPU, GPU, RAM, Storage)
- System update management
- Driver installation support
- Software recommendations
- Autostart configuration
- Multi-language support (i18n)
- Security hardening with input sanitization

[1.1.0]: https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/releases/tag/v1.0.0
