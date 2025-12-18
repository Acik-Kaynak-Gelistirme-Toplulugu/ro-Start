import sys
import os
import subprocess
import json
import logging
import shutil
from urllib.parse import parse_qs

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtCore import QUrl, QThread, pyqtSignal

# Try import based on execution context
try:
    from core.sys_info import get_system_specs, get_distro_info
    from core.autostart import is_autostart_enabled, set_autostart
    import darkdetect
except ImportError:
    # Fallback if running relative
    from backend.core.sys_info import get_system_specs, get_distro_info
    from backend.core.autostart import is_autostart_enabled, set_autostart
    import darkdetect

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SystemUpdateThread(QThread):
    log_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str, int)  # status (idle, updating, completed, error), progress %

    def run(self):
        self.status_signal.emit("updating", 0)
        self.log_signal.emit("Starting system update...")

        if sys.platform == "darwin":
            # Simulation for macOS - Mimic Real APT Output
            import time
            import random

            self.log_signal.emit("Requesting privileges...")
            time.sleep(1)  # Simulate auth delay

            simulated_logs = [
                "Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease",
                "Reading package lists... Done",
                "Building dependency tree... Done",
                "Reading state information... Done",
                "Calculated upgrade... Done",
                "The following packages will be upgraded:",
                "  firefox firefox-locale-en libglib2.0-0 libglib2.0-bin",
                "4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.",
                "Need to get 42.5 MB of archives.",
                "After this operation, 1024 KB of additional disk space will be used.",
                "Fetched 42.5 MB in 2s (18.5 MB/s)",
                "(Reading database ... 185432 files and directories currently installed.)",
                "Preparing to unpack .../libglib2.0-0_2.80.0_amd64.deb ...",
                "Unpacking libglib2.0-0:amd64 (2.80.0) over (2.79.0) ...",
                "Setting up libglib2.0-0:amd64 (2.80.0) ...",
                "done."
            ]

            total_lines = len(simulated_logs)
            for idx, line in enumerate(simulated_logs):
                self.log_signal.emit(line)
                delay = random.uniform(0.1, 0.5) if "Get:" not in line else 0.8
                time.sleep(delay)
                progress = int((idx / total_lines) * 100)
                self.status_signal.emit("updating", progress)

            self.log_signal.emit("System update completed successfully!")
            self.status_signal.emit("completed", 100)
            return

        # Linux Implementation
        _, _, distro_id = get_distro_info()
        distro_id = distro_id.lower()

        update_cmd = ""

        # Debuan/Ubuntu
        if distro_id in ["ubuntu", "debian", "linuxmint", "pop", "kali", "neon"]:
            update_cmd = "apt-get update && env DEBIAN_FRONTEND=noninteractive apt-get upgrade -y"

        # Fedora/RHEL
        elif distro_id in ["fedora", "rhel", "centos", "almalinux"]:
            update_cmd = "dnf update -y"

        # Arch Linux
        elif distro_id in ["arch", "manjaro", "endeavouros"]:
            update_cmd = "pacman -Syu --noconfirm"

        # OpenSUSE
        elif "suse" in distro_id:
            update_cmd = "zypper up -y"

        else:
            # Fallback or generic
            self.log_signal.emit(f"Unsupported distribution: {distro_id}")
            self.status_signal.emit("error", 0)
            return

        # Wrap in pkexec
        full_command = f"pkexec /bin/sh -c '{update_cmd}'"

        self.log_signal.emit(f"Detected Distro: {distro_id}")
        self.log_signal.emit(f"Executing: {update_cmd}")
        self.status_signal.emit("updating", 10)

        try:
            process = subprocess.Popen(
                full_command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            for line in process.stdout:
                self.log_signal.emit(line.strip())
                # Update progress artificially or parse output (parsing is hard across distros)
                self.status_signal.emit("updating", 50)  # Indeterminate state mainly

            process.wait()

            if process.returncode != 0:
                self.log_signal.emit(f"Command failed with return code {process.returncode}")
                self.status_signal.emit("error", 0)
                return

        except Exception as e:
            self.log_signal.emit(f"Execution failed: {str(e)}")
            self.status_signal.emit("error", 0)
            return

        self.log_signal.emit("System update completed successfully!")
        self.status_signal.emit("completed", 100)


class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.update_thread = None

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        # Intercept app:// scheme
        if url.scheme() == "app":
            host = url.host()
            query = url.query()
            logging.info(f"Intercepted command: {host}, Query: {query}")

            if host == "launch-driver-manager":
                self.launch_driver_manager()
            elif host == "close-welcome":
                self.close_application()
            elif host == "install-apps":
                self.install_apps(query)
            elif host == "set-autostart":
                self.handle_set_autostart(query)
            elif host == "start-system-update":
                self.start_system_update()

            return False  # Stop navigation
        return super().acceptNavigationRequest(url, _type, isMainFrame)

    def start_system_update(self):
        logging.info("Starting System Update Thread...")
        if self.update_thread and self.update_thread.isRunning():
            logging.warning("Update already running.")
            return

        self.update_thread = SystemUpdateThread()
        self.update_thread.log_signal.connect(self.on_update_log)
        self.update_thread.status_signal.connect(self.on_update_status)
        self.update_thread.start()

    def on_update_log(self, message):
        # Escape quotes for JS
        safe_msg = message.replace('"', '\\"').replace("'", "\\'")
        js = f"window.dispatchEvent(new CustomEvent('system-update-log', {{ detail: {{ message: '{safe_msg}' }} }}));"
        self.runJavaScript(js)

    def on_update_status(self, status, percentage):
        js = f"window.dispatchEvent(new CustomEvent('system-update-status', {{ detail: {{ status: '{status}', percentage: {percentage} }} }}));"
        self.runJavaScript(js)

    def launch_driver_manager(self):
        if sys.platform == "linux":
            logging.info("Checking for Ro-Control...")
            if shutil.which("ro-control"):
                try:
                    subprocess.Popen(["ro-control"])
                    logging.info("Ro-Control launched.")
                except Exception as e:
                    logging.error(f"Error launching ro-control: {e}")
                    # Fallback to URL if launch fails? Maybe better to show error.
                    # For now, let's just log it.
            else:
                logging.info("Ro-Control not found. Redirecting to GitHub.")
                QDesktopServices.openUrl(QUrl("https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-control"))
        else:
            # Simulation for macOS/Windows
            logging.info("Simulation: Checking Ro-Control")
            # In sim mode, we'll act as if it's missing to test the URL redirect logic,
            # or pop up a dialog. User said "if not installed, redirect".
            # Let's verify URL opening on macOS too.
            QDesktopServices.openUrl(QUrl("https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-control"))
            logging.info("Opened GitHub URL due to simulation/missing app.")

    def close_application(self):
        logging.info("Closing application requested.")
        if self.view() and self.view().window():
            self.view().window().close()

    def install_apps(self, query):
        logging.info(f"Install Apps Requested: {query}")
        if sys.platform == "linux":
            logging.info("Native installation not yet implemented.")
        else:
            QMessageBox.information(None, "Simulation", f"Installing Apps: {query}\n(Simulated)")

    def handle_set_autostart(self, query):
        params = parse_qs(query)
        enabled = params.get('enabled', ['false'])[0].lower() == 'true'
        logging.info(f"Setting autostart to: {enabled}")
        set_autostart(enabled)


class SystemSpecsLoader(QThread):
    specs_signal = pyqtSignal(dict)

    def run(self):
        try:
            specs = get_system_specs()
            self.specs_signal.emit(specs)
        except Exception as e:
            logging.error(f"Error calling get_system_specs: {e}")
            self.specs_signal.emit({})


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ro-Start")
        self.setMinimumSize(960, 640)

        # State
        self.is_page_loaded = False
        self.cached_specs = None

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Web View
        self.web_view = QWebEngineView()
        self.web_view.loadFinished.connect(self.on_load_finished)

        # Set Custom Page for handling navigation requests
        self.custom_page = CustomWebEnginePage(self.web_view)
        self.web_view.setPage(self.custom_page)

        self.layout.addWidget(self.web_view)

        # Start async loading of specs
        self.start_specs_loader()

        # Load Content
        self.load_ui()

    def start_specs_loader(self):
        self.specs_loader = SystemSpecsLoader()
        self.specs_loader.specs_signal.connect(self.on_specs_loaded)
        self.specs_loader.start()

    def on_specs_loaded(self, specs):
        self.cached_specs = specs
        logging.info("System specs loaded in background.")
        if self.is_page_loaded:
            self.inject_system_data()

    def load_ui(self):
        # Resolve path to frontend/dist/index.html
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up from backend/ui to backend, then to root
        project_root = os.path.abspath(os.path.join(script_dir, "../../"))
        html_path = os.path.join(project_root, "frontend", "dist", "index.html")

        if os.path.exists(html_path):
            url = QUrl.fromLocalFile(html_path)
            self.web_view.setUrl(url)
            logging.info(f"Loading UI from: {url.toString()}")
        else:
            error_msg = f"""
            <html>
            <body style="font-family: sans-serif; text-align: center; padding: 50px;">
                <h1>UI Not Found</h1>
                <p>Could not find <code>index.html</code> at:</p>
                <code style="background: #eee; padding: 5px;">{html_path}</code>
                <p>Please build the React application in the <code>frontend</code> directory first.</p>
                <p>Run: <code>cd frontend && npm install && npm run build</code></p>
            </body>
            </html>
            """
            self.web_view.setHtml(error_msg)
            logging.error(f"UI not found at {html_path}")

    def on_load_finished(self, ok):
        if ok:
            logging.info("Page loaded.")
            self.is_page_loaded = True

            # If specs are already here, inject them immediately.
            # If not, wait for on_specs_loaded to trigger injection.
            if self.cached_specs:
                self.inject_system_data()
            else:
                logging.info("Waiting for system specs to finish loading...")

    def inject_system_data(self):
        if not self.cached_specs:
            return

        try:
            specs = self.cached_specs
            autostart = is_autostart_enabled()
            is_dark = darkdetect.isDark()

            # JS Injection
            js_code = f"""
            window.dispatchEvent(new CustomEvent('system-specs-update', {{ detail: {json.dumps(specs)} }}));
            window.dispatchEvent(new CustomEvent('autostart-status-update', {{ detail: {{ enabled: {str(autostart).lower()} }} }}));
            window.dispatchEvent(new CustomEvent('theme-status-update', {{ detail: {{ isDark: {str(is_dark).lower()} }} }}));
            """
            self.web_view.page().runJavaScript(js_code)
            logging.info(f"Injected specs: {specs}, Autostart: {autostart}, DarkMode: {is_dark}")
        except Exception as e:
            logging.error(f"Failed to inject data: {e}")
