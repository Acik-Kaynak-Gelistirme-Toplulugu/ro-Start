# Ro-Start Kurulum Kılavuzu

## Ubuntu 25.10 ARM64 için Kurulum

### Yöntem 1: Terminal ile Kurulum (Önerilen)

Ubuntu App Center'da bilinen sorunlar nedeniyle, terminal üzerinden kurulum yapmanızı öneriyoruz:

```bash
# 1. .deb dosyasının bulunduğu dizine gidin
cd ~/Downloads  # veya dosyanın bulunduğu dizin

# 2. Paketi kurun
sudo apt install ./ro-start_1.0.0_arm64.deb

# 3. Eksik bağımlılıklar varsa otomatik olarak yüklenecektir
```

### Yöntem 2: App Center ile Kurulum

Eğer App Center kullanmak isterseniz:

1. `.deb` dosyasına çift tıklayın
2. App Center açılacak
3. "Yükle" butonuna basın
4. **Not:** Ubuntu 25.10'da App Center bazen takılabilir. Bu durumda Yöntem 1'i kullanın.

### Kurulum Sonrası

Uygulama başarıyla kurulduktan sonra:

1. Uygulama menüsünden "Ro-Start" uygulamasını bulabilirsiniz
2. Veya terminalden çalıştırabilirsiniz:
   ```bash
   ro-start
   ```

### Kaldırma

Uygulamayı kaldırmak için:

```bash
sudo apt remove ro-start
```

### Sorun Giderme

**Bağımlılık Hataları:**
Eğer kurulum sırasında eksik paket hatası alırsanız:

```bash
sudo apt update
sudo apt install -f
```

**App Center Takılıyor:**
Terminal yöntemini kullanın (Yöntem 1).

**Uygulama Açılmıyor:**
Terminalden çalıştırıp hata mesajlarını kontrol edin:

```bash
ro-start
```
