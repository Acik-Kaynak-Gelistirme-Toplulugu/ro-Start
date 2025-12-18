import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    # Çalışma dizinini scriptin olduğu yerin bir üstüne (proje köküne) ayarla
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    project_root = os.path.dirname(script_dir) 
    os.chdir(project_root)
    
    # Uyarıları Sustur (Log Kirliliğini Önle)
    os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"
    
    # Font uyarısı için (Opsiyonel: Sistem 'Segoe UI' bulamazsa sessizce sans-serif'e düşer ama log basar)
    # Biz bunu CSS tarafında çözeceğiz.

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
