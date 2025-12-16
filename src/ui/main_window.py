import sys
import os
import subprocess
import json
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from urllib.parse import parse_qs
# Try import based on execution context
try:
    from core.sys_info import get_system_specs
    from core.autostart import is_autostart_enabled, set_autostart
except ImportError:
    # Fallback if running relative
    from src.core.sys_info import get_system_specs
    from src.core.autostart import is_autostart_enabled, set_autostart

from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PyQt6.QtCore import QUrl, QDir

class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        # Intercept app:// scheme
        if url.scheme() == "app":
            host = url.host()
            query = url.query()
            print(f"Intercepted command: {host}, Query: {query}")
            
            if host == "launch-driver-manager":
                self.launch_driver_manager()
            elif host == "close-welcome":
                self.close_application()
            elif host == "install-apps":
                self.install_apps(query)
            elif host == "set-autostart":
                self.handle_set_autostart(query)
            elif host == "open-url":
                # Example: app://open-url?url=https://google.com
                # Need to parse query to get 'url' param
                pass 
            
            return False # Stop navigation
        return super().acceptNavigationRequest(url, _type, isMainFrame)

    def launch_driver_manager(self):
        if sys.platform == "linux":
            print("Launching Driver Manager...")
            try:
                # Common driver manager for Ubuntu/Debian based systems
                # --open-tab=4 usually opens the 'Additional Drivers' tab
                subprocess.Popen(["software-properties-gtk", "--open-tab=4"])
            except FileNotFoundError:
                print("Error: software-properties-gtk not found.")
                # You might want to try other commands or show an error in the UI
        else:
            # Simulation for macOS/Windows
            print("Simulation: Launching Driver Manager")
            QMessageBox.information(None, "Simulation", "Launching Driver Manager\n(Simulated on non-Linux OS)")
            
    def close_application(self):
        print("Closing application requested.")
        if self.view() and self.view().window():
            self.view().window().close()

    def install_apps(self, query):
        print(f"Install Apps Requested: {query}")
        if sys.platform == "linux":
            print("Native installation not yet implemented.")
        else:
            QMessageBox.information(None, "Simulation", f"Installing Apps: {query}\n(Simulated)")

    def handle_set_autostart(self, query):
        params = parse_qs(query)
        # QUrl.query() might return string, parse_qs expects string
        enabled = params.get('enabled', ['false'])[0].lower() == 'true'
        print(f"Setting autostart to: {enabled}")
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
            print(f"Loading UI from: {url.toString()}")
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
            print(f"Error: UI not found at {html_path}")

    def on_load_finished(self, ok):
        if ok:
            print("Page loaded. Injecting system data...")
            try:
                specs = get_system_specs()
                autostart = is_autostart_enabled()
                
                # JS Injection
                js_code = f"""
                window.dispatchEvent(new CustomEvent('system-specs-update', {{ detail: {json.dumps(specs)} }}));
                window.dispatchEvent(new CustomEvent('autostart-status-update', {{ detail: {{ enabled: {str(autostart).lower()} }} }}));
                """
                self.web_view.page().runJavaScript(js_code)
                print(f"Injected specs: {specs}, Autostart: {autostart}")
            except Exception as e:
                print(f"Failed to inject data: {e}")
