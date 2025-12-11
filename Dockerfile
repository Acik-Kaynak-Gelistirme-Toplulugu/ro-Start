FROM --platform=linux/arm64 ubuntu:22.04

# Etkileşimsiz kurulum için
ENV DEBIAN_FRONTEND=noninteractive

# Gerekli sistem paketlerini yükle
# PyQt6 ve WebEngine için gerekli Qt ve X11 kütüphaneleri + Python Bindings
# universe reposu eklenmeli çünkü pyqt6 paketleri orada olabilir
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-pyqt6 \
    python3-pyqt6.qtwebengine \
    libgl1-mesa-glx \
    libegl1 \
    libxkbcommon-x11-0 \
    libdbus-1-3 \
    libfontconfig1 \
    libxrender1 \
    libxi6 \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala (Gerek kalmayabilir ama diğer bağımlılıklar için dursun)
COPY requirements.txt .

# Sanal ortam oluşturma ve bağımlılıkları yükleme
# PyQt6 zaten sistemden geldiği için pip ile tekrar yüklemeye gerek yok, hatta çakışma olmaması için yüklemiyoruz.
# Sadece requirements.txt içinde PyQt6 harici bir şey varsa yüklenmeli.
# RUN pip3 install --no-cache-dir -r requirements.txt

# Kaynak kodları kopyala
COPY src/ ./src/
COPY assets/ ./assets/
COPY resources/ ./resources/
COPY README.md .

# Dil ayarlarını yap (Türkçe karakter sorunu için)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Uygulamayı başlat
# Not: Docker içinde GUI çalıştırmak için host'un X server'ına bağlanmak gerekir.
CMD ["python3", "src/main.py"]
