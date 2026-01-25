import React from "react";
import { motion } from "motion/react";
import { Cpu, ExternalLink, HardDrive, Monitor } from "lucide-react";
import { themeConfig } from "../../config/welcome-config";

interface SystemSpecs {
  cpu: string;
  gpu: string;
  ram: string;
  storage: string;
}

export function DriverUpdatesStep({
  t,
  specs,
}: {
  step: any;
  t: any;
  specs: SystemSpecs | null;
}) {
  const openDriverManager = () => {
    window.location.href = "app://launch-driver-manager";
  };

  const displayCpu = specs?.cpu || t.driverUpdates.specs.cpuVal;
  const displayGpu = specs?.gpu || t.driverUpdates.specs.gpuVal;
  const displayRam = specs?.ram || t.driverUpdates.specs.ramVal;
  const displayStorage = specs?.storage || t.driverUpdates.specs.storageVal;

  return (
    <div className="space-y-4 flex flex-col items-center h-full w-full justify-center">
      <div className="text-center space-y-2 flex-shrink-0">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{
            scale: { delay: 0.2, type: "spring" },
          }}
          className={`inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-1 shadow-lg`}
        >
          <Cpu className={`w-7 h-7 ${themeConfig.iconPrimary}`} />
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-3xl md:text-4xl font-bold tracking-tight`}>
          {t.driverUpdates.title}
        </h1>
        <p className={`${themeConfig.textSubheading} text-base max-w-xl mx-auto opacity-90`}>
          {t.driverUpdates.subtitle}
        </p>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className={`w-full max-w-2xl backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-xl border ${themeConfig.borderColor} p-6 shadow-sm flex-shrink-0`}
      >
        <div className="flex flex-col items-center text-center space-y-4">
          <p className={`${themeConfig.textBody} text-sm opacity-80 max-w-lg`}>
            {t.driverUpdates.description}
          </p>

          <div className="grid grid-cols-2 gap-3 w-full mt-2">
            {[
              { icon: Cpu, label: t.driverUpdates.specs.cpu, val: displayCpu },
              { icon: Monitor, label: t.driverUpdates.specs.gpu, val: displayGpu },
              { icon: HardDrive, label: t.driverUpdates.specs.ram, val: displayRam, isRam: true },
              { icon: HardDrive, label: t.driverUpdates.specs.storage, val: displayStorage },
            ].map((item, idx) => (
              <div
                key={idx}
                className={`p-3 rounded-xl bg-white/20 dark:bg-slate-700/30 border ${themeConfig.borderColor} flex items-center gap-3 min-w-0`}
              >
                {item.isRam ? (
                  <div className={`w-5 h-5 shrink-0 rounded bg-slate-300 dark:bg-slate-700 flex items-center justify-center text-[10px] font-black ${themeConfig.textHeading} opacity-70`}>
                    RAM
                  </div>
                ) : (
                  <item.icon className={`w-5 h-5 ${themeConfig.iconSecondary} shrink-0`} />
                )}
                <div className="text-left overflow-hidden">
                  <div className={`${themeConfig.textSubheading} text-[10px] font-bold uppercase tracking-wider opacity-60 mb-0.5`}>
                    {item.label}
                  </div>
                  <div
                    className={`${themeConfig.textHeading} text-sm font-bold truncate`}
                    title={item.val}
                  >
                    {item.val}
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="pt-2 w-full flex flex-col items-center gap-3">
            <button
              onClick={openDriverManager}
              className={`group relative flex items-center gap-2 px-6 py-2.5 rounded-xl backdrop-blur-xl bg-blue-600 text-white shadow-lg shadow-blue-500/20 hover:bg-blue-700 hover:scale-[1.02] transition-all duration-300 font-bold text-sm overflow-hidden`}
            >
              <span className="relative z-10">{t.driverUpdates.openManager}</span>
              <ExternalLink className="relative z-10 w-4 h-4" />
            </button>
            <p className={`${themeConfig.textMuted} text-[11px] font-medium opacity-70 italic`}>
              {t.driverUpdates.footer}
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
