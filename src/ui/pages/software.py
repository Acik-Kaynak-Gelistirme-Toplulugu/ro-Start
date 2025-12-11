from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from core.i18n import tr

class SoftwarePage(QWidget):
    def __init__(self):
        super().__init__()
        
        # Scroll Area Setup
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        content_widget = QWidget()
        self.layout = QVBoxLayout(content_widget)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(20)

        title = QLabel(tr.t("software.title"))
        title.setObjectName("pageTitle")
        
        description = QLabel(tr.t("software.description"))
        description.setObjectName("pageDesc")
        
        self.layout.addWidget(title)
        self.layout.addWidget(description)
        self.layout.addSpacing(10)

        # Grid for Apps
        grid = QGridLayout()
        grid.setSpacing(20)
        
        # (Category Key, App Name, Pkg Name)
        apps = [
            ("web", "Firefox", "firefox"),
            ("editor", "VS Code", "code"),
            ("music", "Spotify", "spotify"),
            ("chat", "Discord", "discord"),
            ("graphics", "GIMP", "gimp"),
            ("media", "VLC", "vlc")
        ]

        row = 0
        col = 0
        for cat_key, name, pkg_name in apps:
            # tr.t("software.categories.web") gibi çağrılacak
            category = tr.t(f"software.categories.{cat_key}")
            card = self.create_app_card(category, name, pkg_name)
            grid.addWidget(card, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1

        self.layout.addLayout(grid)
        self.layout.addStretch()
        
        scroll.setWidget(content_widget)

        # Main Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(scroll)

    def create_app_card(self, category, name, pkg_name):
        frame = QFrame()
        frame.setObjectName("appCard")
        frame.setFixedSize(250, 120)
        
        layout = QVBoxLayout(frame)
        
        cat_lbl = QLabel(category)
        cat_lbl.setObjectName("appCategory")
        
        name_lbl = QLabel(name)
        name_lbl.setObjectName("appName")
        
        btn = QPushButton(tr.t("software.btn_install"))
        btn.setObjectName("installButton")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Mağaza entegrasyonu: appstream:// protokolü genellikle varsayılan yazılım ofisini açar (Gnome Software, Plasma Discover vb.)
        # Eğer özel bir mağaza komutu varsa burası `process.start('my-store', ['view', pkg_name])` şeklinde değiştirilebilir.
        btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(f"appstream://{pkg_name}")))
        
        layout.addWidget(cat_lbl)
        layout.addWidget(name_lbl)
        layout.addWidget(btn)
        
        return frame
