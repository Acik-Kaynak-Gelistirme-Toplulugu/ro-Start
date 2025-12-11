import os
import shutil
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt, QProcess
from core.i18n import tr

class DriversPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)

        # Başlık
        title = QLabel(tr.t("drivers.title"))
        title.setObjectName("pageTitle")
        
        description = QLabel(tr.t("drivers.description"))
        description.setObjectName("pageDesc")
        description.setWordWrap(True)

        # Bilgi Kartı (GPU Model + Driver Version + Session)
        info_frame = QFrame()
        info_frame.setObjectName("cardFrame")
        info_layout = QVBoxLayout(info_frame)
        
        self.gpu_label = QLabel(tr.t("drivers.detecting"))
        self.version_label = QLabel("")
        self.session_label = QLabel("")
        
        info_layout.addWidget(self.gpu_label)
        info_layout.addWidget(self.version_label)
        info_layout.addWidget(self.session_label)

        # Butonlar
        btn_layout = QHBoxLayout()
        self.driver_btn = QPushButton(tr.t("drivers.btn_launch"))
        self.driver_btn.setObjectName("actionButton")
        self.driver_btn.setFixedSize(220, 45)
        self.driver_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.driver_btn.clicked.connect(self.launch_nvidia_settings)
        
        btn_layout.addWidget(self.driver_btn)
        btn_layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(info_frame)
        layout.addLayout(btn_layout)
        layout.addStretch()

        # GPU ve Sürücü Kontrolünü EN SONA ALIYORUZ
        self.check_system_status()

    def check_system_status(self):
        # 1. Oturum Tipi (Wayland / X11)
        session_type = os.environ.get('XDG_SESSION_TYPE', 'Unknown')
        self.session_label.setText(f"<small style='color: #a6adc8;'>{tr.t('drivers.session_type')}: {session_type.capitalize()}</small>")

        # 2. GPU ve Driver Kontrolü
        self.detect_nvidia_gpu()

    def detect_nvidia_gpu(self):
        # GPU Modeli
        gpu_found = False
        try:
            if shutil.which("lspci"):
                process = QProcess()
                process.start("lspci", [])
                process.waitForFinished()
                output = str(process.readAllStandardOutput(), 'utf-8')
                
                for line in output.split('\n'):
                    if "NVIDIA" in line.upper():
                         gpu_name = line.split(":", 2)[-1].strip()
                         # Köşeli parantez içindeki kısmı al (genelde daha temiz model adıdır)
                         if "[" in gpu_name:
                             gpu_name = gpu_name.split("[")[1].split("]")[0]
                         
                         self.gpu_label.setText(f"{tr.t('drivers.detected')} {gpu_name}")
                         gpu_found = True
                         break
        except:
            pass
            
        if not gpu_found:
            # Geliştirme ortamı (Mac)
            import platform
            if platform.system() == "Darwin":
                 self.gpu_label.setText(f"System: Apple Silicon ({platform.machine()})")
            else:
                 self.gpu_label.setText(tr.t("drivers.unknown_gpu"))
                 self.driver_btn.setEnabled(False)

        # Sürücü Versiyonu (nvidia-smi)
        self.check_driver_version()

    def check_driver_version(self):
        try:
            if shutil.which("nvidia-smi"):
                process = QProcess()
                # Sadece versiyon numarasını al
                process.start("nvidia-smi", ["--query-gpu=driver_version", "--format=csv,noheader"])
                process.waitForFinished()
                version = str(process.readAllStandardOutput(), 'utf-8').strip()
                
                if version:
                    self.version_label.setText(f"{tr.t('drivers.driver_installed')} {version} <span style='color:#a6e3a1;'>({tr.t('drivers.driver_current')})</span>")
                else:
                    self.version_label.setText(tr.t("drivers.driver_not_found"))
            else:
                self.version_label.setText(f"<span style='color:#f38ba8;'>{tr.t('drivers.driver_not_found')}</span>")
        except:
            self.version_label.setText("")

    def launch_nvidia_settings(self):
        nvidia_cmd = "nvidia-settings" 
        QProcess.startDetached(nvidia_cmd, [])
