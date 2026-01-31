# Contributing to Ro-Start

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Development Setup](#development-setup)
- [Styleguides](#styleguides)

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## I Have a Question

> Before asking a question, please read the [Documentation](README.md) and search existing [Issues](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/issues).

If you still need clarification, feel free to open a new issue with the "question" label.

## I Want To Contribute

### Legal Notice

When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license (GPL-3.0).

### Development Setup

1. **Fork and Clone:**

   ```bash
   git clone https://github.com/your-username/ro-start.git
   cd ro-start
   ```

2. **Install System Dependencies:**

   **Ubuntu/Debian:**
   ```bash
   sudo apt install build-essential pkg-config \
       libgtk-4-dev libadwaita-1-dev git curl
   ```

   **Fedora:**
   ```bash
   sudo dnf install gcc pkg-config \
       gtk4-devel libadwaita-devel git curl
   ```

   **Arch Linux:**
   ```bash
   sudo pacman -S base-devel pkg-config \
       gtk4 libadwaita git curl
   ```

3. **Install Rust:**

   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   rustup component add rustfmt clippy
   ```

4. **Build and Run:**

   ```bash
   # Debug build (faster compilation)
   cargo run

   # Release build (optimized)
   cargo build --release
   ./target/release/ro-start

   # With logging
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

### Testing on Different Desktop Environments

The application is designed to work on multiple Linux desktop environments. When testing:

**KDE Plasma:**
```bash
# The app will auto-detect as "KDE Plasma" and show in system info
DESKTOP_SESSION=plasmadesktop ./target/debug/ro-start
# or
export XDG_CURRENT_DESKTOP="KDE"
./target/debug/ro-start
```

**GNOME:**
```bash
export XDG_CURRENT_DESKTOP="GNOME"
./target/debug/ro-start
```

**Xfce:**
```bash
export XDG_CURRENT_DESKTOP="XFCE"
./target/debug/ro-start
```

The desktop environment detection is in `src/system.rs` - `detect_desktop_environment()` function.

### Project Structure

```
src/
├── main.rs           # Application entry point
├── ui/               # GTK4 UI components
│   ├── mod.rs
│   └── main_window.rs
├── system.rs         # System information (includes DE detection)
└── config.rs         # Configuration

resources/
└── style.css         # GTK CSS styling

data/
├── ro-start.desktop
├── ro-start.png
└── org.osdev.ro_start.appdata.xml
```

## Styleguides

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: add system update checking
fix: resolve memory leak in system info
docs: update installation instructions
```

### Rust Coding Style

- **Follow Rust conventions:** Use `rustfmt` for formatting
- **Use `clippy`:** Fix all clippy warnings before submitting
- **Write tests:** Add tests for new functionality
- **Document public APIs:** Use doc comments (`///`)
- **Error handling:** Use `Result` and `?` operator
- **Avoid `unwrap()`:** Use proper error handling
- **Keep functions small:** Single responsibility principle

**Example:**
```rust
/// Retrieves system information
///
/// # Errors
///
/// Returns an error if system information cannot be retrieved
pub fn get_system_info() -> Result<SystemInfo, SystemError> {
    // Implementation
}
```

### GTK4/UI Guidelines

- **Follow GNOME HIG:** [Human Interface Guidelines](https://developer.gnome.org/hig/)
- **Use libadwaita widgets:** PreferencesGroup, ActionRow, etc.
- **Responsive design:** Support different window sizes
- **Accessibility:** Add proper labels and ARIA attributes
- **Icons:** Use symbolic icons from the icon theme

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Run `cargo fmt`** and **`cargo clippy`**
4. **Ensure all tests pass:** `cargo test`
5. **Update CHANGELOG.md** with notable changes
6. **Request review** from maintainers

### Testing

```bash
# Run all tests
cargo test

# Run specific test
cargo test test_name

# Run tests with output
cargo test -- --nocapture

# Run ignored tests
cargo test -- --ignored
```

---

## Questions?

Feel free to reach out:
- **GitHub Issues:** [Report issues](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/issues)
- **GitHub Discussions:** [Ask questions](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/discussions)
- **Email:** info@osdev.shop

Happy Coding! 🚀
