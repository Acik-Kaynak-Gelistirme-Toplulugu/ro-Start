from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt6.QtCore import Qt, QProcess
from core.i18n import tr


class UpdatePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        title = QLabel(tr.t("update.title"))
        title.setObjectName("pageTitle")

        description = QLabel(tr.t("update.description"))
        description.setObjectName("pageDesc")
        description.setWordWrap(True)

        # Durum Göstergesi
        # İlk açılışta kontrol yapmadığımız için "Kontrol ediliyor" demek yanıltıcı.
        # "Sistem durumu: Güncelleme için hazır" gibi nötr bir ifade daha doğru.
        self.status_label = QLabel(tr.t("update.status_unknown"))
        self.status_label.setObjectName("statusLabel")
        self.status_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 10px;")

        # Update Button
        self.update_btn = QPushButton(tr.t("update.btn_update"))
        self.update_btn.setMinimumWidth(260)  # Sabit değil, minimum genişlik veriyoruz ki taşmasın
        self.update_btn.setFixedHeight(50)
        self.update_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.update_btn.setObjectName("actionButton")
        self.update_btn.clicked.connect(self.run_update)

        # Log Başlığı
        log_title = QLabel(tr.t("update.log_title"))
        log_title.setStyleSheet("margin-top: 10px; font-weight: bold;")

        # Log Görüntüleyici
        self.log_viewer = QTextEdit()
        self.log_viewer.setReadOnly(True)
        self.log_viewer.setStyleSheet(
            """
            QTextEdit {
                background-color: #11111b;
                color: #a6adc8;
                border: 1px solid #313244;
                border-radius: 8px;
                font-family: 'Consolas', 'Monospace';
                font-size: 12px;
                padding: 10px;
            }
        """
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(10)
        layout.addWidget(self.status_label)
        layout.addWidget(self.update_btn)
        layout.addWidget(log_title)
        layout.addWidget(self.log_viewer)

        # Process nesnesi
        self.process = None

    def run_update(self):
        # Butonu pasif yap
        self.update_btn.setEnabled(False)
        self.log_viewer.clear()
        self.log_viewer.append(">>> " + tr.t("update.status_started"))

        # Komut belirle
        cmd = self.get_distro_update_command()

        # Mac OS Fallback
        import platform

        if platform.system() == "Darwin":
            cmd = "echo 'Simulating update on Mac OS...'; sleep 1; echo 'Downloading packages...'; sleep 1; echo 'Installing...'; sleep 1; echo 'Done.'"

        # Process başlat
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

        # Sudo gerektiren komutlar için pkexec kullanılabilir veya kullanıcı terminalden çalıştırırmış gibi simüle edilir.
        # En temiz yöntem: pkexec ile yetki alıp komutu çalıştırmak.
        # "pkexec bash -c 'komut'"

        if platform.system() != "Darwin":
            full_cmd = "pkexec"
            args = ["bash", "-c", cmd]
            self.process.start(full_cmd, args)
        else:
            self.process.start("bash", ["-c", cmd])

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.log_viewer.append(stdout.strip())
        # Scroll to bottom
        sb = self.log_viewer.verticalScrollBar()
        sb.setValue(sb.maximum())

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.log_viewer.append(f"<span style='color: #f38ba8;'>{stderr.strip()}</span>")

    def process_finished(self):
        self.update_btn.setEnabled(True)
        if self.process.exitCode() == 0:
            self.status_label.setText(f"<span style='color: #a6e3a1;'>✔ {tr.t('update.status_uptodate')}</span>")
            self.log_viewer.append(f"\n✅ {tr.t('update.success')}")
        else:
            self.status_label.setText(f"<span style='color: #f38ba8;'>✘ {tr.t('update.error')}</span>")
            self.log_viewer.append(f"\n❌ {tr.t('update.error')}")

    def get_distro_update_command(self):
        distro_id = "debian"
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("ID="):
                        distro_id = line.strip().split("=")[1].strip('"').lower()
                        break
        except Exception:
            pass

        if distro_id in ["fedora", "rhel", "centos"]:
            return "dnf update -y"
        elif distro_id in ["arch", "manjaro"]:
            return "pacman -Syu --noconfirm"
        elif distro_id in ["opensuse"]:
            return "zypper update -y"
        else:
            return "apt update && apt upgrade -y"
