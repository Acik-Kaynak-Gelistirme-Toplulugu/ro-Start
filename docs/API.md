# API Reference

## Rust Module API

### Core Modules

#### system.rs

System information retrieval module.

##### Types

**`SystemInfo` struct**

```rust
pub struct SystemInfo {
    pub cpu_name: String,              // CPU model name
    pub cpu_usage: f32,                // Current CPU usage percentage
    pub cpu_info: String,              // Formatted: "12.5% (Intel Core i7)"
    pub total_memory: u64,             // Total memory in KB
    pub used_memory: u64,              // Used memory in KB
    pub memory_info: String,           // Formatted: "2048 MB / 16384 MB"
    pub os_name: String,               // Operating system name
    pub os_version: String,            // OS version
    pub desktop_environment: String,   // Detected DE (KDE Plasma, GNOME, etc.)
    pub kernel_version: String,        // Kernel version
    pub hostname: String,              // System hostname
}
```

**`SystemState` struct**

```rust
pub struct SystemState {
    sys: System,  // Internal sysinfo::System
}
```

##### Functions

**`SystemState::new() -> Self`**

- Creates new system state with all info refreshed
- Returns: `SystemState` instance

**`SystemState::get_system_info(&self) -> SystemInfo`**

- Retrieves current system information
- Returns: `SystemInfo` with all system details
- Example:
  - CPU: "12.5% (Intel Core i7-9750H)"
  - Memory: "2048 MB / 16384 MB"
  - Desktop: "KDE Plasma"

**`SystemState::refresh(&mut self)`**

- Refreshes all system information
- Useful for real-time updates

**`detect_desktop_environment() -> String`**

- Detects running desktop environment
- Checks: `XDG_CURRENT_DESKTOP` and `DESKTOP_SESSION` env vars
- Returns: Desktop environment name
- Supported:
  - KDE Plasma
  - GNOME
  - Xfce
  - LXDE
  - Cinnamon
  - MATE
  - Budgie
  - Deepin

#### i18n.rs

Internationalization (i18n) module for multi-language support.

##### Types

**`Translations` struct**

```rust
pub struct Translations {
    pub app: AppTranslations,
    pub sidebar: SidebarTranslations,
    pub home: HomeTranslations,
    pub update: UpdateTranslations,
    pub drivers: DriversTranslations,
    pub software: SoftwareTranslations,
}
```

##### Functions

**`init() -> anyhow::Result<()>`**

- Initializes i18n system
- Loads all available translations from JSON files
- Detects system locale
- Returns: Result (Ok or error)

**`set_locale(locale: &str)`**

- Sets current locale
- Validates locale is available
- Example: `set_locale("tr_TR")`

**`get_locale() -> String`**

- Gets current locale code
- Returns: Locale string (e.g., "en_US")

**`t() -> Translations`**

- Gets translations for current locale
- Returns: `Translations` struct with all strings
- Falls back to English if locale unavailable

**`available_locales() -> Vec<String>`**

- Gets list of available locales
- Returns: Vector of locale codes
- Example: `["en_US", "tr_TR", "de", ...]`

**`locale_name(locale: &str) -> &str`**

- Gets display name for locale
- Example: `locale_name("tr_TR")` → `"Türkçe"`

##### Supported Languages

- 🇺🇸 English (en_US)
- 🇹🇷 Turkish (tr_TR)
- 🇩🇪 German (de)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇮🇹 Italian (it)
- 🇯🇵 Japanese (ja)
- 🇷🇺 Russian (ru)
- 🇨🇳 Chinese (zh)

#### package_manager.rs

Package manager detection and update checking.

##### Types

**`PackageManager` enum**

```rust
pub enum PackageManager {
    Apt,     // Debian/Ubuntu
    Dnf,     // Fedora/RHEL
    Pacman,  // Arch Linux
    Zypper,  // openSUSE
}
```

**`UpdateInfo` struct**

```rust
pub struct UpdateInfo {
    pub available: bool,
    pub count: usize,
    pub package_manager: PackageManager,
}
```

##### Functions

**`PackageManager::detect() -> Result<Self>`**

- Detects system package manager
- Checks: apt, dnf, pacman, zypper (in order)
- Returns: Detected `PackageManager` or error

**`PackageManager::check_updates(&self) -> Result<UpdateInfo>`**

- Checks for available updates
- Returns: `UpdateInfo` with update count
- Supported managers: apt, dnf, pacman, zypper

**`UpdateInfo::message(&self) -> String`**

- Gets user-friendly update message
- Returns: String like "5 update(s) available"

#### config.rs

Application configuration management.

##### Types

**`AppConfig` struct**

```rust
pub struct AppConfig {
    pub app_name: String,      // Application name
    pub version: String,       // Version
    pub autostart: bool,       // Autostart on login
    pub language: String,      // Language preference
}
```

##### Functions

**`AppConfig::load() -> Result<Self>`**

- Loads configuration from file
- Creates default if file not exists
- Returns: `AppConfig` or error

**`AppConfig::save(&self) -> Result<()>`**

- Saves configuration to file
- Creates directories if needed
- Returns: Result

**`AppConfig::default() -> Self`**

- Creates default configuration
- app_name: "Ro-Start"
- version: "2.0.0"
- autostart: false
- language: "auto"

#### notifications.rs

Desktop notification system.

##### Functions

**`show_notification(title: &str, body: &str)`**

- Shows desktop notification
- Uses system notification daemon
- Timeout: 5 seconds

**`notify_updates_available(count: usize)`**

- Shows update notification
- Example message: "5 update(s) are ready to install"

**`notify_success(message: &str)`**

- Shows success notification
- Title: "Success"

**`notify_error(message: &str)`**

- Shows error notification
- Title: "Error"

### UI Modules

#### main_window.rs

Main application window with dashboard.

**`MainWindow::new(app: &Application) -> ApplicationWindow`**

- Creates main window with all UI elements
- System info dashboard
- Quick action buttons
- Menu bar with actions

##### Quick Actions

1. **Update System** - Opens package manager (dist-specific)
   - KDE Plasma: `discover`
   - GNOME: `gnome-software`
   - Xfce: `xfce4-appfinder`
2. **Software Center** - Opens app store
   - Same as Update System
3. **System Settings** - Opens settings
   - KDE Plasma: `systemsettings5`
   - GNOME: `gnome-control-center`
   - Xfce: `xfce4-settings-manager`

#### settings.rs

Settings and preferences window.

**`show_settings(parent: Option<&gtk::Window>)`**

- Shows preferences window
- Language selection dropdown
- Autostart toggle
- Transient window modal

#### about.rs

About dialog display.

**`show_about(parent: Option<&gtk::Window>)`**

- Shows about dialog
- Application name, version
- Developer info
- License information
- Links to project

#### dialogs.rs

Common dialog utilities.

**`show_error(parent: Option<&gtk::Window>, title: &str, message: &str)`**

- Shows error dialog

**`show_info(parent: Option<&gtk::Window>, title: &str, message: &str)`**

- Shows info dialog

**`show_confirm(parent: Option<&gtk::Window>, title: &str, message: &str, confirm_label: &str, callback: Box<dyn Fn() + 'static>)`**

- Shows confirmation dialog with callback

## Error Handling

### RoStartError enum

```rust
pub enum RoStartError {
    SystemInfo(String),
    Config(anyhow::Error),
    Io(std::io::Error),
    CommandFailed(String),
    PackageManagerNotFound,
    UpdateCheckFailed(String),
}
```

- All errors implement Display and Debug
- Used throughout application for robust error handling
- Graceful fallbacks with proper logging

## File Locations

- **Config**: `~/.config/ro-start/config.toml`
- **Translations**: `assets/locales/{lang}.json`
- **Icon**: `/usr/share/icons/hicolor/512x512/apps/ro-start.png`
- **Desktop**: `/usr/share/applications/ro-start.desktop`
- **AppStream**: `/usr/share/metainfo/org.osdev.ro_start.appdata.xml`

## Environment Variables

- `LANG` or `LC_ALL`: System language (auto-detected)
- `XDG_CURRENT_DESKTOP`: Current desktop environment
- `DESKTOP_SESSION`: Fallback DE detection
- `RUST_LOG`: Logging level (e.g., `ro_start=debug`)

## Threading & Concurrency

- **RwLock**: Thread-safe access to translations and locale
- **Graceful Error Handling**: All lock acquisitions properly handled
- **No Panics**: Production code never panics on lock poisoning

## Performance Notes

- **Startup**: < 0.5 seconds
- **Memory**: ~45 MB resident
- **CPU**: < 0.2% idle
- **Binary**: ~8 MB (stripped)

## Future Extensions

- Package manager integration APIs
- Driver detection and installation
- Custom theme support
- Plugin system for additional actions
