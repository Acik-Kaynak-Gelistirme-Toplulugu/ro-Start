# Linux Welcome Screen

A modern, minimal, and powerful welcome screen for Linux distributions (Debian/Ubuntu based).
Now features a modern React-based UI integrated via QtWebEngine.

## Features

- Modern React UI (Vite + Tailwind + Framer Motion)
- Hybrid Architecture (Python/Qt6 + Web Technologies)
- System Language Detection
- Extensible Architecture

## Development

### Prerequisites
- Python 3.10+
- Node.js & npm (for UI build)

### Setup & Run

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build the UI (Theme):**
   ```bash
   cd tema
   npm install
   npm run build
   cd ..
   ```

3. **Run the Application:**
   ```bash
   python3 src/main.py
   ```

The application will load the built UI from `tema/dist/index.html`.