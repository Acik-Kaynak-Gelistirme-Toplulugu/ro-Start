# Architecture Overview

## System Design

Ro-Start is a **native Rust application** using GTK4 and libadwaita for a modern, efficient Linux welcome application.

```
┌─────────────────────────────────────────────────┐
│    Ro-Start Application (Single Binary)         │
│                                                  │
│  ┌─────────────────────────────────────────┐   │
│  │   GTK4 + libadwaita UI Layer            │   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  MainWindow                         ││   │
│  │  │  - System Info Dashboard            ││   │
│  │  │  - Quick Actions (Update/Software)  ││   │
│  │  │  - Settings Panel                   ││   │
│  │  │  - About Dialog                     ││   │
│  │  └─────────────────────────────────────┘│   │
│  └─────────────────────────────────────────┘   │
│                      ↕                          │
│  ┌─────────────────────────────────────────┐   │
│  │   Core Modules (Rust)                  │   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  system.rs                          ││   │
│  │  │  - System info retrieval            ││   │
│  │  │  - Desktop env detection            ││   │
│  │  │  - CPU, memory, storage stats       ││   │
│  │  │  - Hostname and kernel version      ││   │
│  │  └─────────────────────────────────────┘│   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  i18n.rs                            ││   │
│  │  │  - 8 language support               ││   │
│  │  │  - System locale detection          ││   │
│  │  │  - Translation management           ││   │
│  │  └─────────────────────────────────────┘│   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  package_manager.rs                 ││   │
│  │  │  - Package manager detection        ││   │
│  │  │  - Update checking                  ││   │
│  │  │  - apt, dnf, pacman, zypper support ││   │
│  │  └─────────────────────────────────────┘│   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  notifications.rs                   ││   │
│  │  │  - Desktop notifications            ││   │
│  │  │  - User feedback                    ││   │
│  │  └─────────────────────────────────────┘│   │
│  │  ┌─────────────────────────────────────┐│   │
│  │  │  config.rs                          ││   │
│  │  │  - App configuration                ││   │
│  │  │  - Settings persistence             ││   │
│  │  └─────────────────────────────────────┘│   │
│  └─────────────────────────────────────────┘   │
│                      ↕                          │
│  ┌─────────────────────────────────────────┐   │
│  │   System Interface                      │   │
│  │  - sysinfo library (CPU, memory, etc)   │   │
│  │  - Environment variables (locale, DE)   │   │
│  │  - Command execution (package mgmt)     │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
                        ↕
        ┌───────────────────────────────┐
        │    Linux System / Kernel       │
        │  - File system                 │
        │  - Process management          │
        │  - Device drivers              │
        └───────────────────────────────┘
```

## Key Design Decisions

### 1. Single Binary, Zero Dependencies

- **Rust**: Fast, safe, and memory-efficient compiled language
- **GTK4**: Native, modern Linux toolkit
- **libadwaita**: GNOME design system for beautiful UI
- **Static Build**: Portable across distributions

### 2. Multi-Desktop Environment Support

- **Auto-detection**: Intelligently detects running desktop environment
- **Supported**: KDE Plasma, GNOME, Xfce, LXDE, Cinnamon, MATE, Budgie, Deepin
- **DE-aware Actions**: Opens appropriate tools (discover, gnome-software, etc.)
- **Graceful Fallback**: Works on any desktop, even unknown ones

### 3. Modular Architecture

```
src/
├── main.rs              # Application entry point
├── system.rs            # System info & DE detection
├── i18n.rs              # Internationalization (8 languages)
├── package_manager.rs   # Package manager abstraction
├── notifications.rs     # Desktop notifications
├── config.rs            # Configuration management
├── error.rs             # Error types
└── ui/
    ├── mod.rs
    ├── main_window.rs   # Main window implementation
    ├── about.rs         # About dialog
    ├── settings.rs      # Settings panel
    └── dialogs.rs       # Dialog utilities
```

### 4. Internationalization

- **8 Languages**: en_US, tr_TR, de, es, fr, it, ja, ru, zh
- **Automatic Detection**: System locale detection from LANG/LC_ALL
- **JSON-based**: Easy to add new translations
- **Fallback**: Default to English if translation unavailable

### 5. Error Handling

- **No Panics**: Graceful error handling throughout
- **RwLock Safety**: Protected concurrent access to translation data
- **Command Execution**: Safe subprocess handling with error logging
- **User Feedback**: Notifications for success/failure states

## Component Interaction

### System Info Retrieval

```
MainWindow::new()
    ↓
get_system_info()
    ↓
SystemState::new() [sysinfo]
    ↓
Returns: CPU, Memory, Desktop Env, etc.
    ↓
Display in UI
```

### Desktop Environment Detection

```
Quick Action Button Clicked
    ↓
detect_desktop_environment()
    ↓
Check XDG_CURRENT_DESKTOP
    ↓
Map to DE-specific tool (discover, gnome-software, etc.)
    ↓
Execute command
    ↓
Show notification
```

### Language Detection

```
App Startup
    ↓
detect_system_locale()
    ↓
Check LANG/LC_ALL env var
    ↓
Match against available translations
    ↓
Load translations
    ↓
Render UI in selected language
```

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Startup Time** | ~0.5 seconds |
| **Memory Usage** | ~45 MB |
| **Binary Size** | ~8 MB (stripped) |
| **CPU (idle)** | <0.2% |
| **Compilation Time** | ~30-60 seconds (release) |

## Extensibility

### Adding a New Language

1. Add JSON file: `assets/locales/{lang_code}.json`
2. Update `i18n.rs` locales list
3. Add to language dropdown in settings

### Adding Desktop Environment Support

Desktop environments are auto-detected in `system.rs::detect_desktop_environment()`:

```rust
if xdg.contains("kde") || xdg.contains("plasmadesktop") {
    return "KDE Plasma".to_string();
}
// Add new check here
```

### Adding Quick Actions

Edit `main_window.rs::create_actions_card()`:

```rust
let cmd = match de.as_str() {
    "KDE Plasma" => "discover",
    "GNOME" => "gnome-software",
    // Add new actions here
    _ => "default-command",
};
```

## Security Considerations

1. **No Elevated Privileges**: Application runs as regular user
2. **Safe Command Execution**: Uses standard process spawning
3. **Input Validation**: Configuration file parsing with serde
4. **Error Handling**: Comprehensive error logging, no unwraps in production code

## Testing Strategy

### Unit Tests
```bash
cargo test --all
```

### Format Check
```bash
cargo fmt --all -- --check
```

### Linting
```bash
cargo clippy --all-features -- -D warnings
```

### Build
```bash
cargo build --release
```

## Build Pipeline (GitHub Actions)

1. **Check**: `cargo check --all-features`
2. **Test**: `cargo test --all-features`
3. **Format**: `cargo fmt --all -- --check`
4. **Clippy**: `cargo clippy --all-features -- -D warnings`
5. **Build**: `cargo build --release` with artifact upload
