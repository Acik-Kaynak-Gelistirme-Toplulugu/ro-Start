import sys
import os
import subprocess
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
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
            # We can't use self (QWebEnginePage) as parent for QMessageBox easily without casting to widget, 
            # so we use None -- this will show a modal dialog
            QMessageBox.information(None, "Simulation", "Launching Driver Manager\n(Simulated on non-Linux OS)")

    def close_application(self):
        print("Closing application requested.")
        # Find the main window and close it
        # self.view() returns the QWebEngineView given in constructor or setPage
        if self.view() and self.view().window():
            self.view().window().close()

    def install_apps(self, query):
        print(f"Install Apps Requested: {query}")
        # Here you would parse the query string to get app names
        # e.g., ?apps=vlc,discord
        if sys.platform == "linux":
            # Real installation logic would go here (likely needing polkit)
            print("Native installation not yet implemented.")
        else:
            QMessageBox.information(None, "Simulation", f"Installing Apps: {query}\n(Simulated)")

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
        
        # Set Custom Page for handling navigation requests
        self.custom_page = CustomWebEnginePage(self.web_view)
        self.web_view.setPage(self.custom_page)
        
        # Enable Developer Extras (Optional, helpful for debugging)
        # self.web_view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.DeveloperExtrasEnabled, True)
        
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
