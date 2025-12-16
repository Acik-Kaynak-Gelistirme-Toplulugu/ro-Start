# 🚀 Ro-Start

[![Türkçe Oku](https://img.shields.io/badge/Dili_Değiştir-Türkçe-red?style=for-the-badge)](README.tr.md)

> **A next-generation, transparent welcome application for Linux distributions.**

**Ro-Start** replaces traditional welcome screens with a modern, "Liquid Glass" aesthetic. Built with a hybrid architecture combining the system-level power of **Python (PyQt6)** and the reactive UI capabilities of **React (Vite + TailwindCSS)**, it creates a premium first impression for your Linux distro.

![Ro-Start Banner](assets/welcome_screen.png)

## ✨ key Features

- **🎨 Liquid Glass UI:** A stunning, transparent, and matte design language inspired by modern OS aesthetics.
- **🚀 Hybrid Architecture:**
  - **Backend:** Python + PyQt6 + QtWebEngine for limitless system access.
  - **Frontend:** React + TypeScript + Framer Motion for 60fps animations.
- **📊 System Canvas:** Beautiful visualization of CPU, GPU, RAM, and Storage statistics.
- **🎮 Driver Manager:** Simplified NVIDIA driver installation and management.
- **🌍 Adaptive:** Auto-detects system language and scales to different resolutions.
- **⚡ Autostart Ready:** Optional system startup integration.

![Driver Manager UI](assets/driver_manager.png)

## 🏗️ Project Structure

The project is divided into two distinct parts:

```
ro-start/
├── src/               # 🐍 Python Backend (App Logic)
│   ├── core/          # System utilities, driver logic, specs
│   ├── ui/            # PyQt6 window and WebEngine setup
│   └── main.py        # Entry point
│
├── tema/              # ⚛️ React Frontend (The Look)
│   ├── src/           # Components, hooks, styles
│   ├── dist/          # Built static files (loaded by Python)
│   └── public/        # Assets
│
└── requirements.txt   # Python Dependencies
```

## 🛠️ Installation & Development

Follow these steps to set up the environment on your local machine.

### Prerequisites

- **Python 3.10+**
- **Node.js 18+ & npm** (for building the UI)
- **Linux Environment** (Recommended for full driver functionality, but runs on macOS/Windows in simulation mode)

### 1. Build the User Interface (Theme)

The Python application loads the compiled HTML/CSS/JS. You must build the frontend first.

```bash
cd tema
npm install
npm run build
cd ..
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment.

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Ro-Start

Launch the application.

```bash
python3 src/main.py
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
