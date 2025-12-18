import sys
import os
from PyQt6.QtWidgets import QApplication

# Adjust path for running directly vs as generic package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from src.ui.main_window import MainWindow
    from src.core.logger import setup_logging
except ImportError:
    from ui.main_window import MainWindow
    from core.logger import setup_logging

def main():
    # Setup Logging
    log_file = setup_logging()
    
    # Uyarıları Sustur (Log Kirliliğini Önle)
    os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"
    
    app = QApplication(sys.argv)
    
    # Uygulama genel ayarları
    app.setApplicationName("Ro-Start")
    app.setApplicationVersion("1.1.0")
    
    # Ana pencereyi oluştur ve göster
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
