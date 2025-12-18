# API Reference

## Backend API

### Core Modules

#### sys_info.py

System information retrieval module.

##### Functions

**`get_cpu_info() -> str`**

- Returns: CPU model name
- Cached: Yes (LRU cache)
- Example: `"Intel Core i7-9750H @ 2.60GHz"`

**`get_gpu_info() -> str`**

- Returns: GPU model name
- Cached: Yes (LRU cache)
- Example: `"NVIDIA GeForce GTX 1650"`

**`get_distro_info() -> tuple[str, str, str]`**

- Returns: (distro_name, version, distro_id)
- Example: `("Ubuntu", "22.04", "ubuntu")`

**`get_system_specs() -> dict`**

- Returns: Complete system specifications
- Example:

```python
{
    "cpu": "Intel Core i7-9750H",
    "gpu": "NVIDIA GeForce GTX 1650",
    "ram": "16.0 GB",
    "storage": "512.0 GB",
    "distro": "Ubuntu",
    "version": "22.04",
    "distro_id": "ubuntu"
}
```

**`get_size_str(size_bytes: int) -> str`**

- Parameters: Size in bytes
- Returns: Human-readable size string
- Example: `get_size_str(1073741824)` → `"1.0 GB"`

#### i18n.py

Internationalization module.

##### Class: Translator

**`__init__()`**

- Auto-detects system language
- Loads appropriate translation file
- Falls back to English if translation not found

**`t(key: str, default: str = None) -> str`**

- Parameters:
  - `key`: Translation key (supports nested: "home.title")
  - `default`: Default value if key not found
- Returns: Translated string
- Example: `tr.t("home.title")` → `"Welcome to Your System"`

#### autostart.py

Autostart management module.

##### Functions

**`get_autostart_file_path() -> str`**

- Returns: Path to autostart desktop file
- Example: `"~/.config/autostart/ro-start.desktop"`

**`is_autostart_enabled() -> bool`**

- Returns: True if autostart is enabled

**`set_autostart(enable: bool = True) -> bool`**

- Parameters: Enable or disable autostart
- Returns: True if successful
- Side effects: Creates/removes desktop file

#### logger.py

Logging configuration module.

##### Functions

**`setup_logging(app_name: str = "ro-start") -> str`**

- Parameters: Application name
- Returns: Path to log file
- Side effects: Configures root logger with console and file handlers

### UI Pages

#### home.py

##### Class: HomePage(QWidget)

Main dashboard page.

**Methods:**

- `get_system_info() -> dict`: Retrieves system information
- `check_autostart() -> bool`: Checks autostart status
- `toggle_autostart(checked: bool)`: Toggles autostart

#### update.py

##### Class: UpdatePage(QWidget)

System update page.

**Methods:**

- `run_update()`: Starts system update process
- `get_distro_update_command() -> str`: Gets distro-specific update command

#### drivers.py

##### Class: DriversPage(QWidget)

Driver management page.

**Methods:**

- `detect_nvidia_gpu()`: Detects NVIDIA GPU
- `check_driver_version()`: Checks installed driver version
- `launch_nvidia_settings()`: Opens NVIDIA settings

#### software.py

##### Class: SoftwarePage(QWidget)

Software recommendations page.

## Frontend API

### Custom Events

#### system-specs-update

Fired when system specifications are loaded.

```typescript
window.addEventListener("system-specs-update", (event: CustomEvent) => {
  const specs = event.detail;
  console.log(specs.cpu, specs.gpu, specs.ram);
});
```

#### autostart-status-update

Fired when autostart status changes.

```typescript
window.addEventListener("autostart-status-update", (event: CustomEvent) => {
  const { enabled } = event.detail;
  console.log("Autostart:", enabled);
});
```

#### theme-status-update

Fired when theme is detected.

```typescript
window.addEventListener("theme-status-update", (event: CustomEvent) => {
  const { isDark } = event.detail;
  console.log("Dark mode:", isDark);
});
```

#### system-update-log

Fired during system update with log messages.

```typescript
window.addEventListener("system-update-log", (event: CustomEvent) => {
  const { message } = event.detail;
  console.log(message);
});
```

#### system-update-status

Fired when update status changes.

```typescript
window.addEventListener("system-update-status", (event: CustomEvent) => {
  const { status, percentage } = event.detail;
  // status: 'idle' | 'updating' | 'completed' | 'error'
  console.log(`${status}: ${percentage}%`);
});
```

### App Protocol

Frontend can trigger backend actions using `app://` protocol:

```typescript
// Start system update
window.location.href = "app://start-system-update";

// Launch driver manager
window.location.href = "app://launch-driver-manager";

// Close application
window.location.href = "app://close-welcome";

// Set autostart
window.location.href = "app://set-autostart?enabled=true";

// Install apps
window.location.href = "app://install-apps?apps=chrome,vscode";
```

## Configuration Files

### configs/app.json

Main application configuration.

```json
{
  "app": {
    "name": "Ro-Start",
    "version": "1.1.0"
  },
  "ui": {
    "theme": "liquid-glass",
    "default_language": "auto"
  },
  "features": {
    "system_update": true,
    "driver_management": true
  }
}
```

### configs/distros.yaml

Distribution-specific configurations.

```yaml
distributions:
  ubuntu:
    update_command: "apt update && apt upgrade -y"
    package_manager: "apt"
```

## Translation Files

### assets/locales/{locale}.json

Translation files for different languages.

```json
{
  "app": {
    "title": "Welcome to Linux"
  },
  "home": {
    "title": "Welcome to Your System",
    "description": "Essential tools..."
  }
}
```

Supported locales:

- `en_US.json` - English
- `tr_TR.json` - Turkish
