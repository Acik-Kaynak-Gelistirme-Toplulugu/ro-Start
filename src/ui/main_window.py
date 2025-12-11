from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QStackedWidget, QFrame)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont

# Import Pages
from ui.pages.home import HomePage
from ui.pages.update import UpdatePage
from ui.pages.drivers import DriversPage
from ui.pages.software import SoftwarePage

# Import i18n
from core.i18n import tr

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(tr.t("app.title"))
        self.setMinimumSize(960, 640)
        
        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- Sidebar (Left Menu) ---
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(260)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 25, 0, 25)
        sidebar_layout.setSpacing(8)

        # Logo / Title
        title_label = QLabel(tr.t("sidebar.welcome"))
        title_label.setObjectName("sidebarTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(title_label)
        
        sidebar_layout.addSpacing(30)

        # Navigation Buttons
        self.nav_buttons = []
        self.btn_home = self.create_nav_button(tr.t("sidebar.home"), 0)
        self.btn_update = self.create_nav_button(tr.t("sidebar.update"), 1)
        self.btn_drivers = self.create_nav_button(tr.t("sidebar.drivers"), 2)
        self.btn_software = self.create_nav_button(tr.t("sidebar.software"), 3)
        
        # Add buttons to layout
        sidebar_layout.addWidget(self.btn_home)
        sidebar_layout.addWidget(self.btn_update)
        sidebar_layout.addWidget(self.btn_drivers)
        sidebar_layout.addWidget(self.btn_software)
        
        sidebar_layout.addStretch()
        
        # Version
        version_label = QLabel(tr.t("app.version"))
        version_label.setObjectName("versionLabel")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(version_label)

        # --- Content Area (Right Side) ---
        content_area = QFrame()
        content_area.setObjectName("contentArea")
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(0,0,0,0)
        
        # Stacked Widget for Pages
        self.pages = QStackedWidget()
        
        # Initialize Pages
        self.home_page = HomePage()
        self.update_page = UpdatePage()
        self.drivers_page = DriversPage()
        self.software_page = SoftwarePage()

        # Add to Stack
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.update_page)
        self.pages.addWidget(self.drivers_page)
        self.pages.addWidget(self.software_page)

        content_layout.addWidget(self.pages)

        # Join Layouts
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(content_area)

        # Default Page
        self.btn_home.setChecked(True)
        self.pages.setCurrentIndex(0)

        # Apply Styles
        self.apply_styles()

    def create_nav_button(self, text, index):
        btn = QPushButton(text)
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        btn.setFixedHeight(50)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.clicked.connect(lambda: self.switch_page(index))
        self.nav_buttons.append(btn)
        return btn

    def switch_page(self, index):
        self.pages.setCurrentIndex(index)

    def apply_styles(self):
        # Modern Native-Like Dark Theme (Adwaita Inspired)
        # Nötr Griler ve Sistem Mavisi (#3584e4)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #242424;
            }
            QWidget {
                color: #ffffff;
                font-family: 'Inter', 'Noto Sans', 'Liberation Sans', sans-serif;
                font-size: 14px;
            }
            
            /* --- Sidebar --- */
            #sidebar {
                background-color: #1e1e1e;
                border-right: 1px solid #383838;
            }
            #sidebarTitle {
                color: #ffffff;
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            #versionLabel {
                color: #9a9a9a;
                font-size: 11px;
            }
            
            /* Navigation Buttons (Modern Rounded Style) */
            QPushButton {
                background-color: transparent;
                color: #d0d0d0;
                border: none;
                text-align: left;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 8px; /* Yuvarlatılmış köşeler */
                margin: 2px 10px; /* Kenarlardan boşluk */
            }
            QPushButton:hover {
                background-color: #333333;
                color: #ffffff;
            }
            QPushButton:checked {
                background-color: #3584e4; /* Sistem Vurgu Rengi */
                color: #ffffff;
                font-weight: 600;
            }

            /* --- Content Area --- */
            #contentArea {
                background-color: #242424;
            }

            /* Page Headers */
            #pageTitle {
                font-size: 28px;
                font-weight: 800; /* Extra Bold */
                color: #ffffff;
                margin-bottom: 5px;
            }
            #pageDesc {
                font-size: 15px;
                color: #b0b0b0;
                margin-bottom: 25px;
            }

            /* --- Cards / Frames --- */
            #cardFrame {
                background-color: #303030;
                border-radius: 12px;
                border: 1px solid #3e3e3e;
            }
            
            #appCard {
                background-color: #303030;
                border-radius: 12px;
                border: 1px solid #3e3e3e;
            }
            #appCard:hover {
                border: 1px solid #505050;
                background-color: #363636;
            }

            /* --- Buttons (Action & Links) --- */
            #linkButton {
                background-color: #383838;
                color: #ffffff;
                border-radius: 8px;
                padding: 8px 16px;
                border: 1px solid #454545;
                font-weight: 500;
            }
            #linkButton:hover {
                background-color: #454545;
                border-color: #555555;
            }

            #actionButton {
                background-color: #3584e4; /* Primary Blue */
                color: #ffffff;
                border-radius: 8px;
                font-weight: bold;
                font-size: 15px;
                border: none;
            }
            #actionButton:hover {
                background-color: #1c71d8; /* Darker Blue */
            }
            
            #actionButton:disabled {
                background-color: #2f343f;
                color: #7c818c;
            }

            #installButton {
                background-color: #383838;
                color: #3584e4;
                border-radius: 6px;
                padding: 5px;
                font-weight: bold;
                border: 1px solid transparent;
            }
            #installButton:hover {
                background-color: #3584e4;
                color: #ffffff;
            }
            
            /* --- Status & Logs --- */
            #statusLabel {
                font-weight: bold;
                color: #f6f5f4;
            }
            
            QTextEdit {
                background-color: #1e1e1e;
                color: #d0d0d0;
                border: 1px solid #383838;
                border-radius: 8px;
                font-family: 'Monospace', monospace;
                font-size: 12px;
                padding: 10px;
                selection-background-color: #3584e4;
            }
            
            /* --- Small Texts --- */
            #appCategory {
                font-size: 12px;
                color: #9a9a9a;
                text-transform: uppercase;
                font-weight: 600;
            }
            #appName {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 5px;
            }

            /* --- Toggle Switch (QCheckBox) --- */
            QCheckBox {
                spacing: 10px;
                color: #d0d0d0;
                font-size: 13px;
                font-weight: 500;
            }
            QCheckBox::indicator {
                width: 44px;
                height: 24px;
                border-radius: 12px;
                background-color: #383838;
                border: 2px solid #383838;
            }
            QCheckBox::indicator:checked {
                background-color: #3584e4; /* Blue when checked */
                border: 2px solid #3584e4;
            }
            /* The sliding circle */
            QCheckBox::indicator:checked:before {
                /* Qt stylesheet doesn't support pseudo elements for indicators fully like web, 
                   but we can simulate with images or just simple styling. 
                   Standard QCheckboxes in Qt don't support 'before' CSS pseudo.
                   Instead we use standard image replacement or detailed coloring.
                   For simplicity in pure QSS without image assets, we stick to color change or use 'image' property.
                   
                   Alternative: Use distinct image urls for states if we had assets.
                   Since we don't have assets, we rely on background color change which is clear enough for 'native' feel.
                */
            }
            /* To make it look like a real toggle with pure CSS in Qt is tricky without images. 
               Let's try a circular image trick or just trust the color. 
               Better approach: User requested "looks like native". 
               Gnome uses simple color toggles.
            */
        """)
    
    def set_page(self, index):
        # Helper for external calls if needed
        self.pages.setCurrentIndex(index)
        self.nav_buttons[index].setChecked(True)

