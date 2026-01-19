import {
  LucideIcon,
  Sparkles,
  Zap,
  Shield,
  Palette,
  Cpu,
  Chrome,
  Code,
  Music,
  Film,
  Image,
  Terminal,
} from "lucide-react";

// ============================================
// GENEL AYARLAR - Buradan kolayca düzenleyebilirsiniz
// ============================================

export const generalConfig = {
  appName: "Ro-Start",
  year: "2026",
  version: "2026.01",
  copyrightText: "© 2026 Ro-Start. Tüm hakları saklıdır.",
};

// ============================================
// ÖZELLİKLER - Hoş geldiniz sayfasındaki özellikler
// ============================================

export interface Feature {
  icon: LucideIcon;
  title: string;
  description: string;
}

export const features: Feature[] = [
  {
    icon: Sparkles,
    title: "Modern Arayüz",
    description: "Zarif ve kullanıcı dostu tasarım ile seamless deneyim",
  },
  {
    icon: Zap,
    title: "Hızlı ve Güçlü",
    description: "Optimize edilmiş performans için yüksek hız",
  },
  {
    icon: Shield,
    title: "Güvenli",
    description: "Verileriniz için en üst düzey güvenlik",
  },
  {
    icon: Palette,
    title: "Özelleştirilebilir",
    description: "Kişiselleştirme seçenekleri ile istediğiniz gibi ayarlayın",
  },
];

// ============================================
// SİSTEM GÜNCELLEMELERİ
// ============================================

export interface SystemUpdate {
  name: string;
  currentVersion: string;
  newVersion: string;
  size: string;
  priority: "critical" | "recommended" | "optional";
  description: string;
}

export const systemUpdates: SystemUpdate[] = [
  {
    name: "Sistem Çekirdeği",
    currentVersion: "6.5.0",
    newVersion: "6.8.0",
    size: "245 MB",
    priority: "critical",
    description: "Güvenlik yamaları ve performans iyileştirmeleri",
  },
  {
    name: "Güvenlik Güncellemeleri",
    currentVersion: "1.2.3",
    newVersion: "1.2.8",
    size: "85 MB",
    priority: "critical",
    description: "Kritik güvenlik açıklarının giderilmesi",
  },
  {
    name: "Sistem Araçları",
    currentVersion: "4.1.0",
    newVersion: "4.3.0",
    size: "120 MB",
    priority: "recommended",
    description: "Yeni özellikler ve hata düzeltmeleri",
  },
  {
    name: "Dil Paketleri",
    currentVersion: "2.0",
    newVersion: "2.1",
    size: "45 MB",
    priority: "optional",
    description: "Güncellenmiş çeviriler",
  },
];

// ============================================
// SÜRÜCÜ GÜNCELLEMELERİ
// ============================================

export interface DriverUpdate {
  name: string;
  manufacturer: "nvidia" | "amd" | "intel" | "other";
  currentVersion: string;
  newVersion: string;
  size: string;
  status: "available" | "installed" | "optional";
  description: string;
  icon: LucideIcon;
}

export const driverUpdates: DriverUpdate[] = [
  {
    name: "NVIDIA GeForce Sürücüsü",
    manufacturer: "nvidia",
    currentVersion: "535.86",
    newVersion: "545.29",
    size: "320 MB",
    status: "available",
    description: "Gelişmiş oyun performansı ve yeni oyun desteği",
    icon: Cpu,
  },
];

// ============================================
// UYGULAMA ÖNERİLERİ
// ============================================

export interface AppSuggestion {
  name: string;
  category: string;
  description: string;
  icon: LucideIcon;
  size: string;
  popular: boolean;
  preselected?: boolean;
}

export const appSuggestions: AppSuggestion[] = [
  {
    name: "Google Chrome",
    category: "internet",
    description: "Hızlı ve güvenli web tarayıcısı",
    icon: Chrome,
    size: "95 MB",
    popular: true,
    preselected: true,
  },
  {
    name: "Visual Studio Code",
    category: "development",
    description: "Modern kod editörü",
    icon: Code,
    size: "120 MB",
    popular: true,
    preselected: true,
  },
  {
    name: "Spotify",
    category: "music",
    description: "Müzik streaming servisi",
    icon: Music,
    size: "180 MB",
    popular: true,
    preselected: false,
  },
  {
    name: "VLC Media Player",
    category: "media",
    description: "Güçlü medya oynatıcı",
    icon: Film,
    size: "45 MB",
    popular: true,
    preselected: true,
  },
  {
    name: "GIMP",
    category: "graphics",
    description: "Profesyonel görsel düzenleme",
    icon: Image,
    size: "210 MB",
    popular: false,
    preselected: false,
  },
  {
    name: "Terminal Emulator",
    category: "system",
    description: "Gelişmiş terminal özellikleri",
    icon: Terminal,
    size: "25 MB",
    popular: true,
    preselected: false,
  },
];

// ============================================
// ADIMLAR/SAYFALAR
// ============================================

export interface StepConfig {
  id: string;
  title: string;
  subtitle: string;
  description: string;
}

export const steps: StepConfig[] = [
  {
    id: "welcome",
    title: "Hoş Geldiniz",
    subtitle: "Yeni deneyiminize başlayalım",
    description: "Modern Linux deneyiminize hoş geldiniz. Bu kurulum birkaç dakika sürecek.",
  },
  {
    id: "system-updates",
    title: "Sistem Güncellemeleri",
    subtitle: "Sisteminizi güncel tutun",
    description: "Mevcut güncellemeleri yükleyerek en iyi performansı elde edin.",
  },
  {
    id: "driver-updates",
    title: "Sürücü Güncellemeleri",
    subtitle: "Donanım sürücülerinizi güncelleyin",
    description: "Ekran kartı ve diğer donanımlar için en son sürücüleri yükleyin.",
  },
  {
    id: "app-suggestions",
    title: "Uygulama Önerileri",
    subtitle: "Popüler uygulamalar",
    description: "Size önerilen uygulamaları seçin ve yükleyin.",
  },
  {
    id: "ready",
    title: "Hazırsınız!",
    subtitle: "Başlamaya hazır mısınız?",
    description: "Tüm ayarlar tamamlandı. Artık yeni sisteminizi kullanmaya başlayabilirsiniz.",
  },
];

// ============================================
// RENK VE TEMA AYARLARI
// ============================================

export const themeConfig = {
  // Gradient renkleri (Tailwind sınıfları)
  backgroundGradient:
    "from-slate-200 via-gray-100 to-slate-200 dark:from-slate-950 dark:via-purple-950 dark:to-slate-900",

  // Animasyonlu orb renkleri - Daha şeffaf/beyazımsı
  orb1Color: "bg-blue-300 dark:bg-purple-600/40",
  orb2Color: "bg-indigo-300 dark:bg-blue-600/40",
  orb3Color: "bg-slate-300 dark:bg-indigo-600/40",

  // Glass effect opacity - Daha mat
  glassOpacity: "bg-white/40 dark:bg-slate-800/40",
  glassOpacityHover: "bg-white/60 dark:bg-slate-800/60",
  glassCardOpacity: "bg-white/50 dark:bg-slate-800/20",

  // Border colors
  borderColor: "border-white/40 dark:border-slate-700/50",

  // Text colors for Light Mode
  textHeading: "text-slate-800 dark:text-slate-100",
  textSubheading: "text-slate-600 dark:text-slate-300",
  textBody: "text-slate-500 dark:text-slate-400",
  textMuted: "text-slate-400 dark:text-slate-500",

  // Icon colors
  iconPrimary: "text-slate-700 dark:text-slate-300",
  iconSecondary: "text-slate-500 dark:text-slate-500",
};
