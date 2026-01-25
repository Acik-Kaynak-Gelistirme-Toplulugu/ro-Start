import React from "react";
import { motion } from "motion/react";
import { Sparkles } from "lucide-react";
import { generalConfig, themeConfig } from "../../config/welcome-config";

export function ReadyStep({
  t,
  specs,
}: {
  step: any;
  t: any;
  specs?: any;
  autostartEnabled?: boolean;
  onAutostartChange?: (checked: boolean) => void;
}) {
  return (
    <div className="space-y-4 text-center flex flex-col items-center h-full w-full justify-center">
      <motion.div
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ delay: 0.2, type: "spring" }}
        className={`inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-1 shadow-lg`}
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
        >
          <Sparkles className={`w-8 h-8 ${themeConfig.iconPrimary}`} />
        </motion.div>
      </motion.div>
      
      <div className="space-y-1">
        <h1 className={`${themeConfig.textHeading} text-3xl md:text-4xl font-bold tracking-tight`}>
          {t.ready.title}
        </h1>
        <p className={`${themeConfig.textSubheading} text-lg font-medium`}>{t.ready.subtitle}</p>
        <p className={`${themeConfig.textBody} text-sm max-w-lg mx-auto opacity-80`}>{t.ready.description}</p>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className={`mt-4 backdrop-blur-xl ${themeConfig.glassOpacity} rounded-xl border ${themeConfig.borderColor} p-6 w-full max-w-xl mx-auto shadow-sm`}
      >
        <div className="grid grid-cols-3 gap-4">
          <div className="text-center">
            <div className={`${themeConfig.textSubheading} text-[10px] uppercase font-bold tracking-wider mb-0.5 opacity-60`}>
              {t.ready.system}
            </div>
            <div className={`${themeConfig.textHeading} text-base font-bold truncate`}>
              {specs?.distro || generalConfig.appName}
            </div>
          </div>
          <div className="text-center border-x border-slate-400/10">
            <div className={`${themeConfig.textSubheading} text-[10px] uppercase font-bold tracking-wider mb-0.5 opacity-60`}>
              {t.ready.version}
            </div>
            <div className={`${themeConfig.textHeading} text-base font-bold truncate`}>
              {specs?.version || generalConfig.version}
            </div>
          </div>
          <div className="text-center">
            <div className={`${themeConfig.textSubheading} text-[10px] uppercase font-bold tracking-wider mb-0.5 opacity-60`}>
              {t.ready.status}
            </div>
            <div className="text-green-600 text-base font-bold">{t.ready.readyStatus}</div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className={`mt-2 backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-xl border ${themeConfig.borderColor} p-4 w-full max-w-xl mx-auto shadow-sm text-left flex items-center gap-4`}
      >
        <div
          className={`flex-shrink-0 w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="w-5 h-5 text-blue-600 dark:text-blue-400"
          >
            <rect x="2" y="4" width="20" height="16" rx="2" />
            <path d="M10 4v4" />
            <path d="M2 8h20" />
            <path d="M6 4v4" />
          </svg>
        </div>

        <div className="flex-1 min-w-0">
          <h3 className={`${themeConfig.textHeading} text-sm font-bold truncate`}>
            {t.ready.miniApp?.title || "Ro-Start-Mini"}
          </h3>
          <p className={`${themeConfig.textBody} text-[11px] leading-tight opacity-90 truncate`}>{t.ready.miniApp?.description}</p>
        </div>
      </motion.div>
    </div>
  );
}
