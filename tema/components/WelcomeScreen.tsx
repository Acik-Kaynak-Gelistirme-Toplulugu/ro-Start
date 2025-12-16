import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { ChevronRight, Globe, Moon, Sun } from "lucide-react";
import { ImageWithFallback } from "./figma/ImageWithFallback";
import { Checkbox } from "./ui/checkbox";
import { steps, themeConfig } from "../config/welcome-config";
// import { translations } from '../config/locales'; // Temporarily commented out
import { WelcomeStep } from "./steps/WelcomeStep";
import { SystemUpdatesStep } from "./steps/SystemUpdatesStep";
import { DriverUpdatesStep } from "./steps/DriverUpdatesStep";
import { AppSuggestionsStep } from "./steps/AppSuggestionsStep";
import { ReadyStep } from "./steps/ReadyStep";

const translations = {
  tr: {
    welcome: {
      title: "Hoş Geldiniz",
      subtitle: "Yeni deneyiminize başlayalım",
      description:
        "Modern Linux deneyiminize hoş geldiniz. Bu kurulum birkaç dakika sürecek.",
      features: {
        modern: {
          title: "Modern Arayüz",
          desc: "Zarif ve kullanıcı dostu tasarım ile seamless deneyim",
        },
        fast: {
          title: "Hızlı ve Güçlü",
          desc: "Optimize edilmiş performans için yüksek hız",
        },
        secure: {
          title: "Güvenli",
          desc: "Verileriniz için en üst düzey güvenlik",
        },
        custom: {
          title: "Özelleştirilebilir",
          desc: "Kişiselleştirme seçenekleri ile istediğiniz gibi ayarlayın",
        },
      },
    },
    systemUpdates: {
      title: "Sistem Güncellemeleri",
      subtitle: "Sisteminizi güncel tutun",
      description:
        "Kararlı ve güvenli bir deneyim için sisteminizi güncellemeniz önerilir. Bu işlem internet hızınıza bağlı olarak birkaç dakika sürebilir.",
      updateButton: "Sistemi Güncelle",
      updating: "Güncelleniyor...",
      completed: "Tamamlandı",
      completedTitle: "Sisteminiz başarıyla güncellendi.",
      showLogs: "İşlem Kaydını Göster",
      hideLogs: "İşlem Kaydını Gizle",
      progressTitle: "İlerleme",
      logs: {
        list: "Paket listeleri güncelleniyor...",
        tree: "Bağımlılık ağacı oluşturuluyor...",
        status: "Durum bilgisi okunuyor...",
        count: "42 paket güncellenecek.",
        download: "İndiriliyor:",
        unpack: "Paketler açılıyor...",
        config: "Sistem yapılandırılıyor...",
        initramfs: "initramfs oluşturuluyor...",
        clean: "Önbellek temizleniyor...",
        done: "İşlem başarıyla tamamlandı.",
      },
    },
    driverUpdates: {
      title: "Sürücü Güncellemeleri",
      subtitle: "Donanım sürücülerinizi güncelleyin",
      description:
        "Bu araç, sisteminizdeki NVIDIA grafik kartları için en uygun sürücüleri otomatik olarak tespit edip yüklemenize yardımcı olur. Diğer donanımlarınız için gerekli sürücüler sistem çekirdeği ile birlikte gelmektedir.",
      specs: {
        cpu: "İşlemci",
        gpu: "Ekran Kartı",
        ram: "Bellek (RAM)",
        storage: "Depolama",
        cpuVal: "Sistem İşlemcisi",
        gpuVal: "Grafik Birimi",
        ramVal: "16 GB DDR4", // Placeholder
        storageVal: "512 GB NVMe SSD", // Placeholder
      },
      openManager: "Sürücü Yöneticisini Aç",
      footer: "Sistem ayarlarından donanım sürücülerini yapılandırın.",
    },
    appSuggestions: {
      title: "Uygulama Önerileri",
      subtitle: "Popüler uygulamalar",
      description: "Size önerilen popüler uygulamaları seçin ve yükleyin.",
      selected: "Seçildi",
      select: "Seçmek için tıkla",
      footer:
        "Daha sonra Uygulama Mağazası'sından istediğiniz zaman yeni uygulamalar yükleyebilirsiniz.",
    },
    ready: {
      title: "Hazırsınız!",
      subtitle: "Başlamaya hazır mısınız?",
      description:
        "Tüm ayarlar tamamlandı. Artık yeni sisteminizi kullanmaya başlayabilirsiniz.",
      system: "Sistem",
      version: "Sürüm",
      status: "Durum",
      readyStatus: "Hazır ✓",
      startButton: "Sistemi Başlat",
    },
    nav: {
      back: "Geri",
      next: "İleri",
      start: "Başla",
    },
    footer: {
      copyright: "© 2026 Ro-Start. Tüm hakları saklıdır.",
      autostart: "Başlangıçta Göster",
    },
  },
  en: {
    welcome: {
      title: "Welcome",
      subtitle: "Let's start your new experience",
      description:
        "Welcome to your modern Linux experience. This setup will take a few minutes.",
      features: {
        modern: {
          title: "Modern Interface",
          desc: "Seamless experience with elegant and user-friendly design",
        },
        fast: {
          title: "Fast & Powerful",
          desc: "High speed for optimized performance",
        },
        secure: { title: "Secure", desc: "Top-level security for your data" },
        custom: {
          title: "Customizable",
          desc: "Set it up as you like with personalization options",
        },
      },
    },
    systemUpdates: {
      title: "System Updates",
      subtitle: "Keep your system up to date",
      description:
        "It is recommended to update your system for a stable and secure experience. This process may take a few minutes depending on your internet speed.",
      updateButton: "Update System",
      updating: "Updating...",
      completed: "Completed",
      completedTitle: "System successfully updated.",
      showLogs: "Show Process Log",
      hideLogs: "Hide Process Log",
      progressTitle: "Progress",
      logs: {
        list: "Updating package lists...",
        tree: "Building dependency tree...",
        status: "Reading state information...",
        count: "42 packages will be updated.",
        download: "Downloading:",
        unpack: "Unpacking packages...",
        config: "Configuring system...",
        initramfs: "Generating initramfs...",
        clean: "Cleaning cache...",
        done: "Operation completed successfully.",
      },
    },
    driverUpdates: {
      title: "Driver Updates",
      subtitle: "Update your hardware drivers",
      description:
        "This tool helps you automatically detect and install the most appropriate drivers for NVIDIA graphics cards on your system. Drivers for your other hardware come with the system kernel.",
      specs: {
        cpu: "Processor",
        gpu: "Graphics Card",
        ram: "Memory (RAM)",
        storage: "Storage",
        cpuVal: "System Processor",
        gpuVal: "Graphics Unit",
        ramVal: "16 GB DDR4", // Placeholder
        storageVal: "512 GB NVMe SSD", // Placeholder
      },
      openManager: "Open Driver Manager",
      footer: "Configure hardware drivers from system settings.",
    },
    appSuggestions: {
      title: "App Suggestions",
      subtitle: "Popular applications",
      description:
        "Select and install popular applications recommended for you.",
      selected: "Selected",
      select: "Click to select",
      footer:
        "You can install new applications from the App Store at any time later.",
    },
    ready: {
      title: "You're Ready!",
      subtitle: "Ready to start?",
      description:
        "All settings are complete. You can now start using your new system.",
      system: "System",
      version: "Version",
      status: "Status",
      readyStatus: "Ready ✓",
      startButton: "Start System",
    },
    nav: {
      back: "Back",
      next: "Next",
      start: "Start",
    },
    footer: {
      copyright: "© 2026 Ro-Start. All rights reserved.",
      autostart: "Show on Startup",
    },
  },
};

export function WelcomeScreen() {
  const [currentStep, setCurrentStep] = useState(0);
  const [language, setLanguage] = useState<"tr" | "en">("tr");
  const [showLangMenu, setShowLangMenu] = useState(false);
  // Theme state: false = light, true = dark
  const [isDark, setIsDark] = useState(false);
  const [autostartEnabled, setAutostartEnabled] = useState(true);

  // Apply theme class to document
  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);

  useEffect(() => {
    const handleAutostartUpdate = (event: CustomEvent<{ enabled: boolean }>) => {
      setAutostartEnabled(event.detail.enabled);
    };
    window.addEventListener('autostart-status-update' as any, handleAutostartUpdate as any);
    return () => {
       window.removeEventListener('autostart-status-update' as any, handleAutostartUpdate as any);
    };
  }, []);

  const toggleTheme = () => {
    setIsDark(!isDark);
  };

  const handleAutostartChange = (checked: boolean) => {
    setAutostartEnabled(checked);
    window.location.href = `app://set-autostart?enabled=${checked}`;
  };

  const t = translations[language];

  if (!t) return null;

  const nextStep = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      // Last Step - Start System
      window.location.href = "app://close-welcome";
    }
  };

  const prevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const renderStep = () => {
    const step = steps[currentStep];

    switch (step.id) {
      case "welcome":
        return <WelcomeStep step={step} t={t} />;
      case "system-updates":
        return <SystemUpdatesStep step={step} t={t} />;
      case "driver-updates":
        return <DriverUpdatesStep step={step} t={t} />;
      case "app-suggestions":
        return <AppSuggestionsStep step={step} t={t} />;
      case "ready":
        return <ReadyStep step={step} t={t} />;
      default:
        return <WelcomeStep step={step} t={t} />;
    }
  };

  return (
    <div
      className={`h-screen w-full relative overflow-hidden bg-gradient-to-br ${themeConfig.backgroundGradient} transition-colors duration-500`}
    >
      {/* Animated background elements */}
      <div className="absolute inset-0">
        <ImageWithFallback
          src="https://images.unsplash.com/photo-1687618053208-28a67cf7bddb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxhYnN0cmFjdCUyMGdyYWRpZW50JTIwd2FsbHBhcGVyfGVufDF8fHx8MTc2NTU0NjE3M3ww&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral"
          alt="Background"
          className="w-full h-full object-cover opacity-10 mix-blend-overlay"
        />
      </div>

      {/* Floating orbs for depth */}
      <motion.div
        className={`absolute top-20 left-20 w-96 h-96 ${themeConfig.orb1Color} rounded-full mix-blend-multiply filter blur-3xl opacity-50`}
        animate={{
          x: [0, 100, 0],
          y: [0, 50, 0],
        }}
        transition={{
          duration: 20,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className={`absolute bottom-20 right-20 w-96 h-96 ${themeConfig.orb2Color} rounded-full mix-blend-multiply filter blur-3xl opacity-50`}
        animate={{
          x: [0, -100, 0],
          y: [0, -50, 0],
        }}
        transition={{
          duration: 15,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className={`absolute top-1/2 left-1/2 w-96 h-96 ${themeConfig.orb3Color} rounded-full mix-blend-multiply filter blur-3xl opacity-50`}
        animate={{
          x: [-50, 50, -50],
          y: [50, -50, 50],
        }}
        transition={{
          duration: 18,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      {/* Header Actions (Theme Toggle & Language) */}
      <div className="absolute top-6 right-8 z-50 flex items-center gap-3">
        {/* Theme Toggle Button */}
        <button
          onClick={toggleTheme}
          className={`group flex items-center justify-center w-10 h-10 rounded-xl backdrop-blur-xl ${themeConfig.glassCardOpacity} border ${themeConfig.borderColor} ${themeConfig.textHeading} hover:bg-white/60 transition-all duration-300`}
          aria-label="Toggle Theme"
        >
          {isDark ? (
            <Moon className="w-5 h-5 text-indigo-400" />
          ) : (
            <Sun className="w-5 h-5 text-amber-500" />
          )}
        </button>

        {/* Language Selector */}
        <div className="relative">
          <button
            onClick={() => setShowLangMenu(!showLangMenu)}
            className={`flex items-center gap-2 px-3 py-2 rounded-xl backdrop-blur-xl ${themeConfig.glassCardOpacity} border ${themeConfig.borderColor} ${themeConfig.textHeading} hover:bg-white/60 transition-all duration-300 font-medium text-sm`}
          >
            <Globe className="w-4 h-4" />
            <span>{language === "tr" ? "Türkçe" : "English"}</span>
          </button>

          <AnimatePresence>
            {showLangMenu && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="absolute right-0 mt-2 w-32 bg-white dark:bg-slate-800 rounded-xl shadow-xl border border-slate-100 dark:border-slate-700 overflow-hidden"
              >
                <button
                  onClick={() => {
                    setLanguage("tr");
                    setShowLangMenu(false);
                  }}
                  className={`w-full text-left px-4 py-2 text-sm hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors ${
                    language === "tr"
                      ? "text-blue-600 font-medium"
                      : "text-slate-600 dark:text-slate-300"
                  }`}
                >
                  Türkçe
                </button>
                <button
                  onClick={() => {
                    setLanguage("en");
                    setShowLangMenu(false);
                  }}
                  className={`w-full text-left px-4 py-2 text-sm hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors ${
                    language === "en"
                      ? "text-blue-600 font-medium"
                      : "text-slate-600 dark:text-slate-300"
                  }`}
                >
                  English
                </button>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>

      {/* Main content */}
      <div className="relative z-10 h-screen flex flex-col">
        {/* Glassmorphism container */}
        <div
          className={`backdrop-blur-3xl ${themeConfig.glassOpacity} flex-1 flex flex-col shadow-none overflow-hidden transition-colors duration-500`}
        >
          {/* Content area - Flex-1 ensures it takes available space */}
          <div className="flex-1 relative flex flex-col min-h-0">
            {/* Scrollable inner container */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-4 md:p-8">
              <AnimatePresence mode="wait">
                <motion.div
                  key={currentStep}
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  transition={{ duration: 0.3 }}
                  className="h-full flex flex-col justify-center min-h-min"
                >
                  {renderStep()}
                </motion.div>
              </AnimatePresence>
            </div>
          </div>

          {/* Navigation buttons - Fixed at bottom */}
          <div
            className={`flex-shrink-0 px-8 md:px-12 py-6 border-t ${themeConfig.borderColor} backdrop-blur-xl bg-white/10`}
          >
            <div className="flex justify-between items-center max-w-7xl mx-auto w-full">
              {/* Left Side: Autostart + Progress */}
              <div className="flex items-center gap-6">
                 {/* Autostart Toggle */}
                 <div className="flex items-center gap-2">
                    <Checkbox 
                        id="autostart" 
                        checked={autostartEnabled}
                        onCheckedChange={handleAutostartChange}
                        className={`border-slate-400 data-[state=checked]:bg-blue-600 data-[state=checked]:border-blue-600`}
                    />
                    <label 
                        htmlFor="autostart" 
                        className={`text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 ${themeConfig.textBody} cursor-pointer select-none`}
                    >
                        {t.footer.autostart}
                    </label>
                 </div>

                 {/* Separator */}
                 <div className={`h-6 w-px ${themeConfig.borderColor}`} />

                 {/* Progress Dots */}
                 <div className="flex gap-2">
                    {steps.map((_, index) => (
                    <div
                        key={index}
                        className={`h-1.5 rounded-full transition-all duration-300 ${
                        index === currentStep
                            ? "w-8 bg-slate-800 dark:bg-slate-200"
                            : index < currentStep
                            ? "w-1.5 bg-slate-400/60"
                            : "w-1.5 bg-slate-400/20"
                        }`}
                    />
                    ))}
                 </div>
              </div>

              <div className="flex gap-4">
                <button
                  onClick={prevStep}
                  disabled={currentStep === 0}
                  className={`px-6 py-3 rounded-xl backdrop-blur-xl bg-white/40 border ${themeConfig.borderColor} text-slate-700 dark:text-slate-200 disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/60 transition-all duration-300 font-medium`}
                >
                  {t.nav.back}
                </button>

                <button
                  onClick={nextStep}
                  className={`group px-8 py-3 rounded-xl backdrop-blur-xl bg-blue-600/90 border border-blue-400/30 text-white hover:bg-blue-600 transition-all duration-300 flex items-center gap-2 disabled:opacity-50 font-medium shadow-lg shadow-blue-500/20`}
                  disabled={currentStep === steps.length - 1}
                >
                  {currentStep === steps.length - 1 ? t.nav.start : t.nav.next}
                  <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
