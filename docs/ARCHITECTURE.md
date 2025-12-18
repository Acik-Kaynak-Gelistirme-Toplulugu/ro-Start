# Architecture Overview

## System Design

Ro-Start uses a **hybrid architecture** combining the strengths of both Python and React:

```
┌─────────────────────────────────────────┐
│          User Interface (React)         │
│  ┌────────────────────────────────────┐ │
│  │  Components (TypeScript + Tailwind)│ │
│  │  - WelcomeScreen                   │ │
│  │  - SystemUpdatesStep               │ │
│  │  - DriverUpdatesStep               │ │
│  │  - AppSuggestionsStep              │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
                    ↕ (WebEngine Bridge)
┌─────────────────────────────────────────┐
│      Backend Logic (Python/PyQt6)       │
│  ┌────────────────────────────────────┐ │
│  │  Core Modules                      │ │
│  │  - sys_info: Hardware detection    │ │
│  │  - i18n: Internationalization      │ │
│  │  - autostart: Startup management   │ │
│  │  - logger: Logging system          │ │
│  └────────────────────────────────────┘ │
│  ┌────────────────────────────────────┐ │
│  │  UI Pages                          │ │
│  │  - home: Main dashboard            │ │
│  │  - update: System updates          │ │
│  │  - drivers: Driver management      │ │
│  │  - software: App recommendations   │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────┐
│         System Layer (Linux)            │
│  - Package managers (apt, dnf, pacman)  │
│  - Hardware detection (lspci, lscpu)    │
│  - Desktop integration (XDG)            │
└─────────────────────────────────────────┘
```

## Key Design Decisions

### 1. Hybrid Architecture

- **Frontend (React)**: Provides modern, responsive UI with smooth animations
- **Backend (Python)**: Handles system-level operations and hardware access
- **Bridge (QtWebEngine)**: Connects both layers seamlessly

### 2. Modular Structure

- **Core modules**: Reusable system utilities
- **UI pages**: Separate concerns for each feature
- **Config files**: Easy customization for different distros

### 3. Internationalization

- Auto-detection of system language
- JSON-based translation files
- Fallback to English if translation missing

### 4. Performance Optimizations

- LRU caching for hardware detection
- Async loading of system specs
- Lazy loading of UI components

## Communication Flow

### Frontend → Backend

```typescript
// Frontend triggers backend action
window.location.href = "app://start-system-update";
```

### Backend → Frontend

```python
# Backend sends data to frontend
js_code = f"window.dispatchEvent(new CustomEvent('system-specs-update', {{ detail: {json.dumps(specs)} }}))"
self.web_view.page().runJavaScript(js_code)
```

## Security Considerations

1. **Privilege Escalation**: Uses `pkexec` for system operations
2. **Input Validation**: All user inputs are sanitized
3. **Sandboxing**: Frontend runs in isolated WebEngine context
4. **No Remote Code**: All code is local, no external scripts

## Extensibility

### Adding a New Feature

1. **Backend**: Create module in `backend/core/` or page in `backend/ui/pages/`
2. **Frontend**: Add component in `frontend/components/`
3. **Config**: Update `configs/app.json` if needed
4. **i18n**: Add translations to `assets/locales/`
5. **Tests**: Write tests in `tests/backend/` or `tests/frontend/`

### Supporting a New Distribution

1. Add entry to `configs/distros.yaml`
2. Update `backend/core/sys_info.py` if needed
3. Test on target distribution
4. Update documentation
