import React, { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { Cpu, ExternalLink, HardDrive, Monitor } from 'lucide-react';
import { themeConfig } from '../../config/welcome-config';

interface SystemSpecs {
  cpu: string;
  gpu: string;
  ram: string;
  storage: string;
}

export function DriverUpdatesStep({ t }: { step: any, t: any }) {
  const [specs, setSpecs] = useState<SystemSpecs | null>(null);

  useEffect(() => {
    const handleSpecsUpdate = (event: CustomEvent<SystemSpecs>) => {
      setSpecs(event.detail);
    };

    window.addEventListener('system-specs-update' as any, handleSpecsUpdate as any);

    return () => {
      window.removeEventListener('system-specs-update' as any, handleSpecsUpdate as any);
    };
  }, []);

  const openDriverManager = () => {
    window.location.href = "app://launch-driver-manager";
  };

  const displayCpu = specs?.cpu || t.driverUpdates.specs.cpuVal;
  const displayGpu = specs?.gpu || t.driverUpdates.specs.gpuVal;
  const displayRam = specs?.ram || t.driverUpdates.specs.ramVal;
  const displayStorage = specs?.storage || t.driverUpdates.specs.storageVal;

  return (
    <div className="space-y-8 flex flex-col items-center justify-center h-full">
      <div className="text-center space-y-4">
        <motion.div
          initial={{ scale: 0, rotate: 0 }}
          animate={{ scale: 1 }}
          transition={{ 
            scale: { delay: 0.2, type: "spring" }
          }}
          className={`inline-flex items-center justify-center w-24 h-24 rounded-3xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-6 shadow-xl`}
        >
          <Cpu className={`w-12 h-12 ${themeConfig.iconPrimary}`} />
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-5xl font-bold`}>{t.driverUpdates.title}</h1>
        <p className={`${themeConfig.textSubheading} text-xl max-w-2xl mx-auto`}>
          {t.driverUpdates.subtitle}
        </p>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className={`w-full max-w-3xl backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-2xl border ${themeConfig.borderColor} p-8 shadow-sm`}
      >
        <div className="flex flex-col items-center text-center space-y-6">
          <p className={`${themeConfig.textBody} text-lg`}>
            {t.driverUpdates.description}
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full mt-4">
             {/* Dynamic Data System Specs */}
            <div className={`p-4 rounded-xl bg-white/40 dark:bg-slate-700/50 border ${themeConfig.borderColor} flex items-center gap-3`}>
                <Cpu className={`w-6 h-6 ${themeConfig.iconSecondary}`} />
                <div className="text-left overflow-hidden">
                    <div className={`${themeConfig.textSubheading} text-xs font-medium`}>{t.driverUpdates.specs.cpu}</div>
                    <div className={`${themeConfig.textHeading} font-semibold truncate`} title={displayCpu}>{displayCpu}</div>
                </div>
            </div>
            <div className={`p-4 rounded-xl bg-white/40 dark:bg-slate-700/50 border ${themeConfig.borderColor} flex items-center gap-3`}>
                <Monitor className={`w-6 h-6 ${themeConfig.iconSecondary}`} />
                <div className="text-left overflow-hidden">
                    <div className={`${themeConfig.textSubheading} text-xs font-medium`}>{t.driverUpdates.specs.gpu}</div>
                    <div className={`${themeConfig.textHeading} font-semibold truncate`} title={displayGpu}>{displayGpu}</div>
                </div>
            </div>
            <div className={`p-4 rounded-xl bg-white/40 dark:bg-slate-700/50 border ${themeConfig.borderColor} flex items-center gap-3`}>
                <div className={`w-6 h-6 shrink-0 rounded bg-slate-200 dark:bg-slate-600 flex items-center justify-center text-xs font-bold ${themeConfig.textHeading} dark:text-slate-200`}>R</div>
                <div className="text-left overflow-hidden">
                    <div className={`${themeConfig.textSubheading} text-xs font-medium`}>{t.driverUpdates.specs.ram}</div>
                    <div className={`${themeConfig.textHeading} font-semibold truncate`} title={displayRam}>{displayRam}</div>
                </div>
            </div>
            <div className={`p-4 rounded-xl bg-white/40 dark:bg-slate-700/50 border ${themeConfig.borderColor} flex items-center gap-3`}>
                <HardDrive className={`w-6 h-6 ${themeConfig.iconSecondary}`} />
                <div className="text-left overflow-hidden">
                    <div className={`${themeConfig.textSubheading} text-xs font-medium`}>{t.driverUpdates.specs.storage}</div>
                    <div className={`${themeConfig.textHeading} font-semibold truncate`} title={displayStorage}>{displayStorage}</div>
                </div>
            </div>
          </div>

          <div className="pt-4">
             <button
                onClick={openDriverManager}
                className={`group relative flex items-center gap-3 px-8 py-4 rounded-2xl backdrop-blur-xl bg-blue-600 text-white shadow-lg shadow-blue-500/30 hover:bg-blue-700 hover:scale-105 transition-all duration-300 font-semibold text-lg overflow-hidden`}
              >
                <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300" />
                <span className="relative">{t.driverUpdates.openManager}</span>
                <ExternalLink className="relative w-5 h-5" />
              </button>
              <p className={`mt-4 ${themeConfig.textMuted} text-sm`}>
                {t.driverUpdates.footer}
              </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}