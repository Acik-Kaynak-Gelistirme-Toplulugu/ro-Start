import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { ChevronRight, Globe, Moon, Sun } from "lucide-react";
import { ImageWithFallback } from "./common/ImageWithFallback";
import { Checkbox } from "./ui/checkbox";
import { steps, themeConfig } from "../config/welcome-config";
import { translations } from "../config/locales";
import { WelcomeStep } from "./steps/WelcomeStep";
import { SystemUpdatesStep } from "./steps/SystemUpdatesStep";
import { DriverUpdatesStep } from "./steps/DriverUpdatesStep";
import { AppSuggestionsStep } from "./steps/AppSuggestionsStep";
import { ReadyStep } from "./steps/ReadyStep";

export function WelcomeScreen() {
  const [currentStep, setCurrentStep] = useState(0);
  const [language, setLanguage] = useState<string>("en");
  const [showLangMenu, setShowLangMenu] = useState(false);
  // Theme state: false = light, true = dark
  const [isDark, setIsDark] = useState(false);
  const [autostartEnabled, setAutostartEnabled] = useState(true);

  const [systemSpecs, setSystemSpecs] = useState<any>(null);

  const langNames: Record<string, string> = {
    tr: "Türkçe",
    en: "English",
    de: "Deutsch",
    fr: "Français",
    es: "Español",
    it: "Italiano",
    ru: "Русский",
    zh: "中文",
    ja: "日本語",
  };

  // Apply theme class to document
  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [isDark]);

  useEffect(() => {
    const handleAutostartUpdate = (event: CustomEvent<{ enabled: boolean }>) => {
      setAutostartEnabled(event.detail.enabled);
    };

    const handleSpecsUpdate = (event: CustomEvent<any>) => {
      setSystemSpecs(event.detail);
    };

    const handleThemeUpdate = (event: CustomEvent<{ isDark: boolean }>) => {
      setIsDark(event.detail.isDark);
    };

    const handleLanguageUpdate = (event: CustomEvent<{ language: string }>) => {
      setLanguage(event.detail.language);
    };

    window.addEventListener("autostart-status-update" as any, handleAutostartUpdate as any);
    window.addEventListener("system-specs-update" as any, handleSpecsUpdate as any);
    window.addEventListener("theme-status-update" as any, handleThemeUpdate as any);
    window.addEventListener("language-status-update" as any, handleLanguageUpdate as any);

    return () => {
      window.removeEventListener("autostart-status-update" as any, handleAutostartUpdate as any);
      window.removeEventListener("system-specs-update" as any, handleSpecsUpdate as any);
      window.removeEventListener("theme-status-update" as any, handleThemeUpdate as any);
      window.removeEventListener("language-status-update" as any, handleLanguageUpdate as any);
    };
  }, []);

  const toggleTheme = () => {
    setIsDark(!isDark);
  };

  const handleAutostartChange = (checked: boolean) => {
    setAutostartEnabled(checked);
    window.location.href = `app://set-autostart?enabled=${checked}`;
  };

  const t = (translations as any)[language];

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
        return <DriverUpdatesStep step={step} t={t} specs={systemSpecs} />;
      case "app-suggestions":
        return <AppSuggestionsStep step={step} t={t} />;
      case "ready":
        return (
          <ReadyStep
            step={step}
            t={t}
            specs={systemSpecs}
            autostartEnabled={autostartEnabled}
            onAutostartChange={handleAutostartChange}
          />
        );
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

      {/* Floating orbs for depth - Adjusted to be more relative to window center */}
      <motion.div
        className={`absolute top-[10%] left-[10%] w-[30vw] h-[30vw] min-w-[300px] min-h-[300px] ${themeConfig.orb1Color} rounded-full mix-blend-multiply filter blur-3xl opacity-40`}
        animate={{
          x: [-20, 20, -20],
          y: [-20, 20, -20],
        }}
        transition={{
          duration: 20,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className={`absolute bottom-[10%] right-[10%] w-[30vw] h-[30vw] min-w-[300px] min-h-[300px] ${themeConfig.orb2Color} rounded-full mix-blend-multiply filter blur-3xl opacity-40`}
        animate={{
          x: [20, -20, 20],
          y: [20, -20, 20],
        }}
        transition={{
          duration: 15,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className={`absolute top-[40%] left-[40%] w-[25vw] h-[25vw] min-w-[250px] min-h-[250px] ${themeConfig.orb3Color} rounded-full mix-blend-multiply filter blur-3xl opacity-30`}
        animate={{
          x: [30, -30, 30],
          y: [-30, 30, -30],
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
            <span>{langNames[language] || language.toUpperCase()}</span>
          </button>

          <AnimatePresence>
            {showLangMenu && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="absolute right-0 mt-2 w-40 bg-white dark:bg-slate-800 rounded-xl shadow-2xl border border-slate-100 dark:border-slate-700 overflow-hidden z-[100]"
              >
                <div className="max-h-64 overflow-y-auto custom-scrollbar">
                  {Object.entries(langNames).map(([code, name]) => (
                    <button
                      key={code}
                      onClick={() => {
                        setLanguage(code);
                        setShowLangMenu(false);
                      }}
                      className={`w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors flex items-center justify-between ${
                        language === code
                          ? "text-blue-600 font-bold bg-blue-50/50 dark:bg-blue-900/20"
                          : "text-slate-600 dark:text-slate-300"
                      }`}
                    >
                      <span>{name}</span>
                      {language === code && <div className="w-1.5 h-1.5 rounded-full bg-blue-600" />}
                    </button>
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>

      {/* Main content */}
      <div className="relative z-10 h-screen flex flex-col">
        {/* Glassmorphism container */}
        <div
          className={`backdrop-blur-3xl ${themeConfig.glassOpacity} flex-1 flex flex-col shadow-none overflow-hidden transition-colors duration-500 m-4 md:m-10 rounded-3xl border ${themeConfig.borderColor} shadow-2xl`}
        >
          {/* Content area - Flex-1 ensures it takes available space */}
          <div className="flex-1 relative flex flex-col min-h-0 overflow-hidden">
            {/* Centered inner container - No main scrollbar for cleaner look */}
            <div className="flex-1 flex items-center justify-center p-6 md:p-12 overflow-hidden">
              <AnimatePresence mode="wait">
                <motion.div
                  key={currentStep}
                  initial={{ opacity: 0, scale: 0.98 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 1.02 }}
                  transition={{ duration: 0.4, ease: "easeOut" }}
                  className="w-full max-w-5xl mx-auto h-full flex flex-col items-center justify-center overflow-hidden"
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
