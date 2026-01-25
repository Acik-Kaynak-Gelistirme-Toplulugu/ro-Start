<div align="center">
  <h1>🚀 Ro-Start</h1>
  
  [![Türkçe Oku](https://img.shields.io/badge/Dili_Değiştir-Türkçe-red?style=for-the-badge)](README.tr.md)
  [![License](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](LICENSE)
  [![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg?style=for-the-badge)](https://www.linux.org/)
  [![Security](https://img.shields.io/badge/Security-Hardened-green.svg?style=for-the-badge)](SECURITY.md)

  <br />
  
  <p align="center">
    <b>A next-generation, transparent welcome application for Linux distributions.</b>
    <br />
    Replacing traditional welcome screens with a modern, <b>"Liquid Glass"</b> aesthetic.
  </p>

![Ro-Start Welcome](assets/welcome.png)

  <br />

  <!-- Tech Stack Badges -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="TailwindCSS" />
</div>

<br />

**Ro-Start** creates a premium first impression for your Linux distro by combining the system-level power of **Python (PyQt6)** with the reactive UI capabilities of **React (Vite + TailwindCSS)**.

## ✨ Key Features

- **🎨 Liquid Glass UI:** A stunning, transparent, and matte design language inspired by modern OS aesthetics.
- **🚀 Hybrid Architecture:**
  - **Backend:** Python + PyQt6 + QtWebEngine for limitless system access.
  - **Frontend:** React + TypeScript + Framer Motion for 60fps animations.
- **📊 System Canvas:** Beautiful visualization of CPU, GPU, RAM, and Storage statistics.
- **🔒 Security Hardened:** Input sanitization, no external connections, secure subprocess execution.
- **🌍 Adaptive:** Auto-detects system language and scales to different resolutions.
- **⚡ Autostart Ready:** Optional system startup integration.
- **🔐 Privacy Focused:** Zero telemetry, all operations local-only.

![System Updates UI](assets/updates.png)

## 🏗️ Project Structure

```
ro-start/
├── backend/           # 🐍 Python Backend (App Logic)
│   ├── core/          # System utilities, driver logic, specs
│   ├── ui/            # PyQt6 window and WebEngine setup
│   └── main.py        # Entry point
│
├── frontend/          # ⚛️ React Frontend (The Look)
│   ├── components/    # React components
│   ├── config/        # Frontend configuration
│   └── dist/          # Built static files (loaded by Python)
│
├── assets/            # 📦 Static Assets
│   └── locales/       # Translation files (i18n)
│
├── configs/           # ⚙️ Configuration Files
│   ├── app.json       # Application settings
│   └── distros.yaml   # Distribution-specific configs
│
├── scripts/           # 🔧 Build & Install Scripts
│   ├── install.sh     # Installation script
│   ├── build.sh       # Build script
│   └── pre-commit     # Git hook
│
├── tests/             # 🧪 Test Suite
│   ├── backend/       # Python tests (pytest)
│   └── frontend/      # React tests (vitest)
│
├── docs/              # 📚 Documentation
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   └── API.md
│
└── requirements.txt   # Python Dependencies
```

## 🛠️ Installation & Development

Follow these steps to set up the environment on your local machine.

### Prerequisites

- **Python 3.10+**
- **Node.js 18+ & npm** (for building the UI)
- **Linux Environment** (Recommended for full driver functionality, but runs on macOS/Windows in simulation mode)

### 1. Build the User Interface

The Python application loads the compiled HTML/CSS/JS. You must build the frontend first.

```bash
cd frontend
npm install
npm run build
cd ..
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment.

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Ro-Start

Launch the application using the entry point or directly via python.

```bash
# Recommended
ro-start

# Or directly
python3 backend/main.py
```

> **Note:** If running on macOS or Windows, system-specific features like "Driver Installation" will run in **Simulation Mode** (mocked responses).

## 🤝 Contributing

Contributions are welcome! Whether it's adding support for a new distro (Arch, Fedora) or improving the "Liquid Glass" theme components.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
