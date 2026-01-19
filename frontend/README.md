# Linux Karşılama Ekranı - Liquid Glass Tasarım

Modern macOS ve iOS tarzı Liquid Glass (glassmorphism) efektli Linux karşılama ekranı.

## 🎨 Özellikler

- ✨ Liquid Glass / Glassmorphism tasarım
- 🔄 Animasyonlu arka plan öğeleri
- 📦 6 adımlı kurulum süreci
- 🎯 Modüler ve kolayca düzenlenebilir yapı
- 🚀 Sistem güncelleme yönetimi
- 🖥️ Ekran kartı sürücü güncelleme sistemi
- 📱 Uygulama önerileri

## 📁 Proje Yapısı

```
/
├── config/
│   └── welcome-config.ts          # ANA YAPILANDIRMA DOSYASI - HER ŞEYİ BURADAN DÜZENLEYİN!
├── components/
│   ├── WelcomeScreen.tsx          # Ana ekran bileşeni
│   └── steps/                     # Her adım için ayrı component
│       ├── WelcomeStep.tsx        # 1. Hoş geldiniz
│       ├── FeaturesStep.tsx       # 2. Özellikler
│       ├── SystemUpdatesStep.tsx  # 3. Sistem güncellemeleri
│       ├── DriverUpdatesStep.tsx  # 4. Sürücü güncellemeleri
│       ├── AppSuggestionsStep.tsx # 5. Uygulama önerileri
│       └── ReadyStep.tsx          # 6. Hazır
└── App.tsx                        # Uygulama giriş noktası
```

## 🛠️ Nasıl Düzenlenir?

### 1. Genel Ayarlar (Uygulama Adı, Sürüm, vb.)

`/config/welcome-config.ts` dosyasını açın ve `generalConfig` bölümünü düzenleyin:

```typescript
export const generalConfig = {
  appName: "Linux", // Uygulama adı
  year: "2024", // Yıl
  version: "2024.12", // Sürüm
  copyrightText: "© 2024 ...", // Telif hakkı metni
};
```

### 2. Özellikler Listesi

`features` dizisini düzenleyerek ana özellikleri değiştirebilirsiniz:

```typescript
export const features: Feature[] = [
  {
    icon: Sparkles, // Lucide ikonu
    title: "Modern Arayüz", // Başlık
    description: "...", // Açıklama
  },
  // Daha fazla ekleyebilirsiniz...
];
```

### 3. Sistem Güncellemeleri

`systemUpdates` dizisini düzenleyin:

```typescript
export const systemUpdates: SystemUpdate[] = [
  {
    name: "Sistem Çekirdeği",
    currentVersion: "6.5.0",
    newVersion: "6.8.0",
    size: "245 MB",
    priority: "critical", // 'critical', 'recommended', 'optional'
    description: "...",
  },
  // Daha fazla güncelleme ekleyebilirsiniz...
];
```

### 4. Sürücü Güncellemeleri

`driverUpdates` dizisini düzenleyin:

```typescript
export const driverUpdates: DriverUpdate[] = [
  {
    name: "NVIDIA GeForce Sürücüsü",
    manufacturer: "nvidia", // 'nvidia', 'amd', 'intel', 'other'
    currentVersion: "535.86",
    newVersion: "545.29",
    size: "320 MB",
    status: "available", // 'available', 'installed', 'optional'
    description: "...",
    icon: Cpu,
  },
  // Daha fazla sürücü ekleyebilirsiniz...
];
```

### 5. Uygulama Önerileri

`appSuggestions` dizisini düzenleyin:

```typescript
export const appSuggestions: AppSuggestion[] = [
  {
    name: "Google Chrome",
    category: "İnternet",
    description: "...",
    icon: Chrome,
    size: "95 MB",
    popular: true, // Popüler rozeti gösterir
    preselected: true, // Varsayılan olarak seçili
  },
  // Daha fazla uygulama ekleyebilirsiniz...
];
```

### 6. Adımları Değiştirme

`steps` dizisini düzenleyerek adım başlıklarını ve açıklamalarını değiştirebilirsiniz:

```typescript
export const steps: StepConfig[] = [
  {
    id: "welcome",
    title: "Hoş Geldiniz",
    subtitle: "Yeni deneyiminize başlayalım",
    description: "...",
  },
  // Diğer adımlar...
];
```

### 7. Renk ve Tema

`themeConfig` bölümünü düzenleyin:

```typescript
export const themeConfig = {
  backgroundGradient: "from-purple-600 via-pink-500 to-orange-400",
  orb1Color: "bg-purple-400",
  orb2Color: "bg-pink-400",
  orb3Color: "bg-yellow-400",
  glassOpacity: "bg-white/10",
  // ...
};
```

## 🎯 Yeni Adım Ekleme

Yeni bir adım eklemek için:

1. `/config/welcome-config.ts` içindeki `steps` dizisine yeni adım ekleyin
2. `/components/steps/` klasöründe yeni component oluşturun
3. `/components/WelcomeScreen.tsx` içindeki `renderStep()` fonksiyonuna case ekleyin

## 💡 İpuçları

- Tüm metin ve veriler config dosyasında merkezi olarak yönetilir
- Her adım bağımsız bir component olduğu için kolay düzenlenebilir
- Icon'lar için `lucide-react` kütüphanesi kullanılıyor
- Animasyonlar için `motion/react` (Framer Motion) kullanılıyor
- Glassmorphism efekti için `backdrop-blur` ve `bg-white/opacity` kullanılıyor

## 🚀 Geliştirme Önerileri

- Dil seçenekleri ekleyebilirsiniz
- Kullanıcı profili oluşturma adımı eklenebilir
- Tema değiştirme özelliği eklenebilir
- Gerçek API entegrasyonları yapılabilir
- Kurulum ilerlemesi kaydedilebilir
