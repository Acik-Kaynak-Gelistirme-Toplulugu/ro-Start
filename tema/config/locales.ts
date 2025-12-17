export const translations = {
  tr: {
    welcome: {
      title: 'Hoş Geldiniz',
      subtitle: 'Yeni deneyiminize başlayalım',
      description: 'Modern Linux deneyiminize hoş geldiniz. Bu kurulum birkaç dakika sürecek.',
      features: {
        modern: { title: 'Modern Arayüz', desc: 'Zarif ve kullanıcı dostu tasarım ile seamless deneyim' },
        fast: { title: 'Hızlı ve Güçlü', desc: 'Optimize edilmiş performans için yüksek hız' },
        secure: { title: 'Güvenli', desc: 'Verileriniz için en üst düzey güvenlik' },
        custom: { title: 'Özelleştirilebilir', desc: 'Kişiselleştirme seçenekleri ile istediğiniz gibi ayarlayın' },
      }
    },
    systemUpdates: {
      title: 'Sistem Güncellemeleri',
      subtitle: 'Sisteminizi güncel tutun',
      description: 'Kararlı ve güvenli bir deneyim için sisteminizi güncellemeniz önerilir. Bu işlem internet hızınıza bağlı olarak birkaç dakika sürebilir.',
      updateButton: 'Sistemi Güncelle',
      updating: 'Güncelleniyor...', 
      completed: 'Tamamlandı',
      completedTitle: 'Sisteminiz başarıyla güncellendi.',
      showLogs: 'İşlem Kaydını Göster',
      hideLogs: 'İşlem Kaydını Gizle',
      progressTitle: 'İlerleme',
      logs: {
        list: 'Paket listeleri güncelleniyor...', 
        tree: 'Bağımlılık ağacı oluşturuluyor...', 
        status: 'Durum bilgisi okunuyor...', 
        count: '42 paket güncellenecek.',
        download: 'İndiriliyor:',
        unpack: 'Paketler açılıyor...', 
        config: 'Sistem yapılandırılıyor...', 
        initramfs: 'initramfs oluşturuluyor...', 
        clean: 'Önbellek temizleniyor...', 
        done: 'İşlem başarıyla tamamlandı.'
      }
    },
    driverUpdates: {
      title: 'Sürücü Güncellemeleri',
      subtitle: 'Donanım sürücülerinizi güncelleyin',
      description: 'Bu araç, sisteminizdeki NVIDIA grafik kartları için en uygun sürücüleri otomatik olarak tespit edip yüklemenize yardımcı olur. Diğer donanımlarınız için gerekli sürücüler sistem çekirdeği ile birlikte gelmektedir.',
      specs: {
        cpu: 'İşlemci',
        gpu: 'Ekran Kartı',
        ram: 'Bellek (RAM)',
        storage: 'Depolama',
        cpuVal: 'Sistem İşlemcisi',
        gpuVal: 'Grafik Birimi',
        ramVal: '16 GB DDR4', // Placeholder
        storageVal: '512 GB NVMe SSD', // Placeholder
      },
      openManager: 'Sürücü Yöneticisini Aç',
      footer: 'Sistem ayarlarından donanım sürücülerini yapılandırın.'
    },
    appSuggestions: {
      title: 'Uygulama Önerileri',
      subtitle: 'Popüler uygulamalar',
      description: 'Size önerilen popüler uygulamaları seçin ve yükleyin.',
      selected: 'Seçildi',
      select: 'Seçmek için tıkla',
      categories: {
        internet: "İnternet",
        development: "Geliştirme",
        music: "Müzik",
        media: "Medya",
        graphics: "Grafik",
        system: "Sistem"
      },
      footer: 'Daha sonra Uygulama Mağazası\'sından istediğiniz zaman yeni uygulamalar yükleyebilirsiniz.'
    },
    ready: {
      title: 'Hazırsınız!',
      subtitle: 'Başlamaya hazır mısınız?',
      description: 'Tüm ayarlar tamamlandı. Artık yeni sisteminizi kullanmaya başlayabilirsiniz.',
      system: 'Sistem',
      version: 'Sürüm',
      status: 'Durum',
      readyStatus: 'Hazır ✓',
      startButton: 'Sistemi Başlat'
    },
    nav: {
      back: 'Geri',
      next: 'İleri',
      start: 'Başla'
    },
    footer: {
      copyright: '© 2024 Linux. Tüm hakları saklıdır.'
    }
  },
  en: {
    welcome: {
      title: 'Welcome',
      subtitle: 'Let\'s start your new experience',
      description: 'Welcome to your modern Linux experience. This setup will take a few minutes.',
      features: {
        modern: { title: 'Modern Interface', desc: 'Seamless experience with elegant and user-friendly design' },
        fast: { title: 'Fast & Powerful', desc: 'High speed for optimized performance' },
        secure: { title: 'Secure', desc: 'Top-level security for your data' },
        custom: { title: 'Customizable', desc: 'Set it up as you like with personalization options' },
      }
    },
    systemUpdates: {
      title: 'System Updates',
      subtitle: 'Keep your system up to date',
      description: 'It is recommended to update your system for a stable and secure experience. This process may take a few minutes depending on your internet speed.',
      updateButton: 'Update System',
      updating: 'Updating...', 
      completed: 'Completed',
      completedTitle: 'System successfully updated.',
      showLogs: 'Show Process Log',
      hideLogs: 'Hide Process Log',
      progressTitle: 'Progress',
      logs: {
        list: 'Updating package lists...', 
        tree: 'Building dependency tree...', 
        status: 'Reading state information...', 
        count: '42 packages will be updated.',
        download: 'Downloading:',
        unpack: 'Unpacking packages...', 
        config: 'Configuring system...', 
        initramfs: 'Generating initramfs...', 
        clean: 'Cleaning cache...', 
        done: 'Operation completed successfully.'
      }
    },
    driverUpdates: {
      title: 'Driver Updates',
      subtitle: 'Update your hardware drivers',
      description: 'This tool helps you automatically detect and install the most appropriate drivers for NVIDIA graphics cards on your system. Drivers for your other hardware come with the system kernel.',
      specs: {
        cpu: 'Processor',
        gpu: 'Graphics Card',
        ram: 'Memory (RAM)',
        storage: 'Storage',
        cpuVal: 'System Processor',
        gpuVal: 'Graphics Unit',
        ramVal: '16 GB DDR4', // Placeholder
        storageVal: '512 GB NVMe SSD', // Placeholder
      },
      openManager: 'Open Driver Manager',
      footer: 'Configure hardware drivers from system settings.'
    },
    appSuggestions: {
      title: 'App Suggestions',
      subtitle: 'Popular applications',
      description: 'Select and install popular applications recommended for you.',
      selected: 'Selected',
      select: 'Click to select',
      categories: {
        internet: "Internet",
        development: "Development",
        music: "Music",
        media: "Media",
        graphics: "Graphics",
        system: "System"
      },
      footer: 'You can install new applications from the App Store at any time later.'
    },
    ready: {
      title: 'You\'re Ready!',
      subtitle: 'Ready to start?',
      description: 'All settings are complete. You can now start using your new system.',
      system: 'System',
      version: 'Version',
      status: 'Status',
      readyStatus: 'Ready ✓',
      startButton: 'Start System'
    },
    nav: {
      back: 'Back',
      next: 'Next',
      start: 'Start'
    },
    footer: {
      copyright: '© 2024 Linux. All rights reserved.'
    }
  }
};
