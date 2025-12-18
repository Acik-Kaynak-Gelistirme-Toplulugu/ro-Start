import sys
import os
from PyQt6.QtWidgets import QApplication


def setup_environment():
    """
    Sets up the environment for imports.
    If running from source (not installed), adds the project root to sys.path.
    """
    # Check if we are running as a script or installed package
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # ../

    # If the package 'backend' is not importable, we might be running from source
    # Add project root to path so 'import backend' works
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


def main():
    # Setup environment FIRST
    setup_environment()

    # Now imports should work via 'backend.xxx'
    try:
        from backend.ui.main_window import MainWindow
        from backend.core.logger import setup_logging
    except ImportError as e:
        print(f"Critical Import Error: {e}")
        print("Ensure you are running from the project root or have the package installed.")
        print("Try: python3 backend/main.py")
        sys.exit(1)

    # Implement proper cleanup handler
    import signal

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Setup Logging
    setup_logging()

    # Silence Qt spam
    os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"

    app = QApplication(sys.argv)

    # Application Metadata
    app.setApplicationName("Ro-Start")
    app.setOrganizationName("AcikKaynakGelistirmeToplulugu")
    app.setApplicationVersion("1.1.0")

    # Create and Show Window
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
