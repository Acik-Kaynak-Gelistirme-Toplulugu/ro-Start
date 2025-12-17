import sys
import os
import subprocess
import json
import logging
import shutil
from urllib.parse import parse_qs

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtCore import QUrl, QThread, pyqtSignal, QObject

# Try import based on execution context
try:
    from core.sys_info import get_system_specs
    from core.autostart import is_autostart_enabled, set_autostart
except ImportError:
    # Fallback if running relative
    from src.core.sys_info import get_system_specs
    from src.core.autostart import is_autostart_enabled, set_autostart

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemUpdateThread(QThread):
    log_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str, int) # status (idle, updating, completed, error), progress %

    def run(self):
        self.status_signal.emit("updating", 0)
        self.log_signal.emit("Starting system update...")
        
        if sys.platform == "darwin":
            # Simulation for macOS - Mimic Real APT Output
            import time
            import random
            
            self.log_signal.emit("Requesting privileges...")
            time.sleep(1) # Simulate auth delay
            
            simulated_logs = [
                "Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease",
                "Hit:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease",
                "Hit:3 http://archive.ubuntu.com/ubuntu noble-backports InRelease",
                "Hit:4 http://security.ubuntu.com/ubuntu noble-security InRelease",
                "Reading package lists... Done",
                "Building dependency tree... Done",
                "Reading state information... Done",
                "Calculated upgrade... Done",
                "The following packages will be upgraded:",
                "  firefox firefox-locale-en libglib2.0-0 libglib2.0-bin",
                "4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.",
                "Need to get 42.5 MB of archives.",
                "After this operation, 1024 KB of additional disk space will be used.",
                "Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libglib2.0-0 amd64 2.80.0 [1,400 kB]",
                "Get:2 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 firefox amd64 125.0.1 [40.0 MB]",
                "Fetched 42.5 MB in 2s (18.5 MB/s)",
                "(Reading database ... 185432 files and directories currently installed.)",
                "Preparing to unpack .../libglib2.0-0_2.80.0_amd64.deb ...",
                "Unpacking libglib2.0-0:amd64 (2.80.0) over (2.79.0) ...",
                "Setting up libglib2.0-0:amd64 (2.80.0) ...",
                "Processing triggers for libc-bin (2.39) ...",
                "Processing triggers for man-db (2.12.0) ...",
                "Setting up firefox (125.0.1) ...",
                "done."
            ]
            
            total_lines = len(simulated_logs)
            for idx, line in enumerate(simulated_logs):
                self.log_signal.emit(line)
                # Simulate variable processing speed
                delay = random.uniform(0.1, 0.5) if "Get:" not in line else 0.8
                time.sleep(delay)
                
                # Calculate progress roughly based on lines
                progress = int((idx / total_lines) * 100)
                self.status_signal.emit("updating", progress)
                
            self.log_signal.emit("System update completed successfully!")
            self.status_signal.emit("completed", 100)
            return

        # Combine commands into a single pkexec call to request password only once
        full_command = "apt-get update && env DEBIAN_FRONTEND=noninteractive apt-get upgrade -y"
        
        commands = [
            ("Updating system packages...", ["pkexec", "/bin/sh", "-c", full_command])
        ]
        
        total_steps = len(commands)
        
        for idx, (desc, cmd) in enumerate(commands):
            self.log_signal.emit(desc)
            self.status_signal.emit("updating", int((idx / total_steps) * 100))
            
            try:
                # Use stdbuf or pty for better realtime output if needed, but Popen is safer for now
                process = subprocess.Popen(
                    cmd, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, 
                    text=True,
                    bufsize=1  # Line buffered
                )
                
                for line in process.stdout:
                    self.log_signal.emit(line.strip())
                
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
            
            return False # Stop navigation
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
            logging.info("Launching Driver Manager...")
            # Check for standard Ubuntu update manager
            if shutil.which("software-properties-gtk"):
                try:
                    subprocess.Popen(["software-properties-gtk", "--open-tab=4"])
                except Exception as e:
                    logging.error(f"Error launching software-properties-gtk: {e}")
            else:
                logging.warning("software-properties-gtk not found.")
                # Fallback or alert? For now, log.
        else:
            # Simulation for macOS/Windows
            logging.info("Simulation: Launching Driver Manager")
            QMessageBox.information(None, "Simulation", "Launching Driver Manager\n(Simulated on non-Linux OS)")
            
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ro-Start")
        self.setMinimumSize(960, 640)
        
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
        
        # Load Content
        self.load_ui()

    def load_ui(self):
        # Resolve path to tema/dist/index.html
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up from src/ui to src, then to root
        project_root = os.path.abspath(os.path.join(script_dir, "../../"))
        html_path = os.path.join(project_root, "tema", "dist", "index.html")
        
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
                <p>Please build the React application in the <code>tema</code> directory first.</p>
                <p>Run: <code>cd tema && npm install && npm run build</code></p>
            </body>
            </html>
            """
            self.web_view.setHtml(error_msg)
            logging.error(f"UI not found at {html_path}")

    def on_load_finished(self, ok):
        if ok:
            logging.info("Page loaded. Injecting system data...")
            try:
                specs = get_system_specs()
                autostart = is_autostart_enabled()
                
                # JS Injection
                js_code = f"""
                window.dispatchEvent(new CustomEvent('system-specs-update', {{ detail: {json.dumps(specs)} }}));
                window.dispatchEvent(new CustomEvent('autostart-status-update', {{ detail: {{ enabled: {str(autostart).lower()} }} }}));
                """
                self.web_view.page().runJavaScript(js_code)
                logging.info(f"Injected specs: {specs}, Autostart: {autostart}")
            except Exception as e:
                logging.error(f"Failed to inject data: {e}")
