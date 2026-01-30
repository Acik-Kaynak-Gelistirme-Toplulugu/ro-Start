# Development Guide

This guide covers how to set up your development environment and contribute to Ro-Start.

## Prerequisites

### System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt install build-essential pkg-config \
    libgtk-4-dev libadwaita-1-dev \
    git curl
```

**Fedora:**
```bash
sudo dnf install gcc pkg-config \
    gtk4-devel libadwaita-devel \
    git curl
```

**Arch Linux:**
```bash
sudo pacman -S base-devel pkg-config \
    gtk4 libadwaita \
    git curl
```

### Rust Toolchain

```bash
# Install Rust via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Add components
rustup component add rustfmt clippy
```

## Getting Started

### Clone and Build

```bash
# Clone repository
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start

# Build debug version
cargo build

# Run
cargo run

# Or with logging
RUST_LOG=ro_start=debug cargo run
```

### Development Workflow

```bash
# Watch for changes and rebuild
cargo install cargo-watch
cargo watch -x run

# Run tests
cargo test

# Format code
cargo fmt

# Lint code
cargo clippy

# Check without building
cargo check
```

## Project Structure

```
src/
├── main.rs           # Application entry point
├── ui/               # User interface
│   ├── mod.rs
│   └── main_window.rs
├── system.rs         # System information
└── config.rs         # Configuration

resources/
└── style.css         # GTK CSS styling

data/
├── ro-start.desktop  # Desktop entry
├── ro-start.png      # Icon
└── *.appdata.xml     # AppStream metadata
```

## Code Style

We follow standard Rust conventions:

- Use `cargo fmt` before committing
- Fix all `cargo clippy` warnings
- Write tests for new features
- Document public APIs
- Keep commits atomic

## GTK4 Development

### Useful Resources

- [GTK4 Documentation](https://docs.gtk.org/gtk4/)
- [libadwaita Documentation](https://gnome.pages.gitlab.gnome.org/libadwaita/)
- [gtk-rs Book](https://gtk-rs.org/gtk4-rs/stable/latest/book/)
- [GNOME HIG](https://developer.gnome.org/hig/)

### Adding New UI Components

1. Create widget in `src/ui/`
2. Use libadwaita components when possible
3. Follow GNOME Human Interface Guidelines
4. Add CSS styling to `resources/style.css`

Example:
```rust
use gtk::prelude::*;
use libadwaita as adw;

pub fn create_settings_view() -> adw::PreferencesPage {
    let page = adw::PreferencesPage::new();
    page.set_title("Settings");
    
    let group = adw::PreferencesGroup::new();
    group.set_title("General");
    
    page.add(&group);
    page
}
```

## Testing

```bash
# Run all tests
cargo test

# Run specific test
cargo test test_name

# Run with output
cargo test -- --nocapture

# Run ignored tests
cargo test -- --ignored
```

## Building Packages

### Debian Package

```bash
cargo install cargo-deb
cargo deb
# Output: target/debian/ro-start_*.deb
```

### RPM Package

```bash
cargo install cargo-generate-rpm
cargo build --release
cargo generate-rpm
# Output: target/generate-rpm/ro-start-*.rpm
```

## Debugging

### Enable Debug Logs

```bash
RUST_LOG=debug cargo run
```

### GTK Inspector

```bash
GTK_DEBUG=interactive cargo run
```

## Continuous Integration

Our CI runs on every push and PR:

- Format checking (`cargo fmt --check`)
- Linting (`cargo clippy`)
- Tests (`cargo test`)
- Build (`cargo build --release`)

Make sure all checks pass before submitting a PR.

## Release Process

1. Update version in `Cargo.toml`
2. Update `CHANGELOG.md`
3. Commit changes: `git commit -m "chore: bump version to X.Y.Z"`
4. Create tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
5. Push: `git push && git push --tags`
6. GitHub Actions will create the release automatically

## Getting Help

- **Issues:** [GitHub Issues](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/discussions)
- **Email:** info@osdev.shop
