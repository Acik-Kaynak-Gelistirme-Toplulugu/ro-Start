from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt, QUrl, QStandardPaths
from PyQt6.QtGui import QDesktopServices
from core.i18n import tr
import platform
import os


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)

        # --- Hero Section ---
        hero_layout = QVBoxLayout()
        hero_layout.setSpacing(10)

        title = QLabel(tr.t("home.title"))
        title.setObjectName("pageTitle")

        description = QLabel(tr.t("home.description"))
        description.setObjectName("pageDesc")
        description.setWordWrap(True)

        hero_layout.addWidget(title)
        hero_layout.addWidget(description)
        layout.addLayout(hero_layout)

        # --- System Info Card ---
        # Sistem bilgilerini çek
        sys_info = self.get_system_info()

        info_card = QFrame()
        info_card.setObjectName("cardFrame")
        info_layout = QGridLayout(info_card)
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setHorizontalSpacing(30)
        info_layout.setVerticalSpacing(10)

        # Bilgileri ekle (Sol: Etiket, Sağ: Değer)
        self.add_info_row(info_layout, 0, "OS:", sys_info["distro"])
        self.add_info_row(info_layout, 1, "Kernel:", sys_info["kernel"])
        self.add_info_row(info_layout, 2, "Processor:", sys_info["cpu"])
        self.add_info_row(info_layout, 3, "Memory:", sys_info["ram"])

        layout.addWidget(info_card)

        layout.addStretch()

        # --- Quick Links ---
        links_lbl = QLabel(
            tr.t("home.links_title") if tr.t("home.links_title") != "home.links_title" else "Quick Links"
        )
        links_lbl.setStyleSheet("font-weight: bold; color: #ffffff; margin-bottom: 5px;")
        layout.addWidget(links_lbl)

        links_layout = QHBoxLayout()
        links_layout.setSpacing(15)

        self.add_link_button(links_layout, tr.t("home.website"), "https://example.com")
        self.add_link_button(links_layout, tr.t("home.docs"), "https://example.com/docs")
        self.add_link_button(links_layout, tr.t("home.forum"), "https://example.com/forum")
        self.add_link_button(links_layout, tr.t("home.github"), "https://github.com/Acik-Kaynak-Gelistirme-Toplulugu")

        layout.addLayout(links_layout)

        layout.addSpacing(20)

        # --- Autostart Checkbox ---
        self.autostart_cb = QCheckBox(tr.t("home.autostart_label"))
        # Stil zaten main_window.py css'inden gelecek (QCheckBox selector)
        self.autostart_cb.setCursor(Qt.CursorShape.PointingHandCursor)

        # Mevcut durumu kontrol et
        if self.check_autostart():
            self.autostart_cb.setChecked(True)

        self.autostart_cb.toggled.connect(self.toggle_autostart)

        # Sağ alta hizala
        cb_layout = QHBoxLayout()
        cb_layout.addStretch()
        cb_layout.addWidget(self.autostart_cb)
        layout.addLayout(cb_layout)

    def add_info_row(self, layout, row, label, value):
        lbl = QLabel(label)
        lbl.setStyleSheet("color: #9a9a9a; font-weight: 600;")
        val = QLabel(value)
        val.setStyleSheet("color: #ffffff; font-weight: normal;")
        layout.addWidget(lbl, row, 0)
        layout.addWidget(val, row, 1)

    def add_link_button(self, layout, text, url):
        btn = QPushButton(text)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(url)))
        btn.setObjectName("linkButton")
        layout.addWidget(btn)

    def get_system_info(self):
        info = {"distro": "Unknown Linux", "kernel": platform.release(), "cpu": platform.processor(), "ram": "Unknown"}

        # Distro Name
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        info["distro"] = line.split("=")[1].strip('"').strip()
                        break
        except Exception:
            pass

        # CPU Info (Cleaned)
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        info["cpu"] = line.split(":")[1].strip()
                        break
        except Exception:
            pass

        # RAM Info
        try:
            with open("/proc/meminfo") as f:
                mem_total = 0
                for line in f:
                    if "MemTotal" in line:
                        mem_total = int(line.split()[1])  # KB
                        break
                gb = mem_total / 1024 / 1024
                info["ram"] = f"{gb:.1f} GB"
        except Exception:
            pass

        return info

    def get_autostart_path(self):
        # ~/.config/autostart/welcome-screen-user.desktop
        config_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.ConfigLocation)
        autostart_dir = os.path.join(config_dir, "autostart")
        if not os.path.exists(autostart_dir):
            os.makedirs(autostart_dir)
        return os.path.join(autostart_dir, "welcome-screen-user.desktop")

    def check_autostart(self):
        return os.path.exists(self.get_autostart_path())

    def toggle_autostart(self, checked):
        path = self.get_autostart_path()
        if checked:
            # Create .desktop file
            content = """[Desktop Entry]
Type=Application
Exec=/usr/bin/welcome-screen
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Welcome Screen
Comment=Welcome Screen for Linux
"""
            try:
                with open(path, "w") as f:
                    f.write(content)
            except Exception as e:
                print(f"Error enabling autostart: {e}")
        else:
            # Delete file
            if os.path.exists(path):
                try:
                    os.remove(path)
                except Exception as e:
                    print(f"Error disabling autostart: {e}")
