import React from "react";
import { motion } from "motion/react";
import { Sparkles, Globe, BookOpen, MessageCircle } from "lucide-react";
import { generalConfig, themeConfig } from "../../config/welcome-config";

import { Checkbox } from "../ui/checkbox";

export function ReadyStep({
  step,
  t,
  specs,
  autostartEnabled,
  onAutostartChange,
}: {
  step: any;
  t: any;
  specs?: any;
  autostartEnabled?: boolean;
  onAutostartChange?: (checked: boolean) => void;
}) {
  return (
    <div className="space-y-6 text-center flex flex-col items-center h-full pt-4">
      <motion.div
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ delay: 0.2, type: "spring" }}
        className={`inline-flex items-center justify-center w-24 h-24 rounded-3xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-4 shadow-lg`}
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
        >
          <Sparkles className={`w-12 h-12 ${themeConfig.iconPrimary}`} />
        </motion.div>
      </motion.div>
      <h1 className={`${themeConfig.textHeading} text-6xl font-bold`}>{t.ready.title}</h1>
      <p className={`${themeConfig.textSubheading} text-2xl`}>{t.ready.subtitle}</p>
      <p className={`${themeConfig.textBody} text-lg max-w-2xl mx-auto`}>{t.ready.description}</p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className={`mt-12 backdrop-blur-xl ${themeConfig.glassOpacity} rounded-2xl border ${themeConfig.borderColor} p-8 w-full max-w-2xl mx-auto shadow-sm`}
      >
        <div className="grid grid-cols-3 gap-8">
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>
              {t.ready.system}
            </div>
            <div className={`${themeConfig.textHeading} text-xl font-bold`}>
              {specs?.distro || generalConfig.appName}
            </div>
          </div>
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>
              {t.ready.version}
            </div>
            <div className={`${themeConfig.textHeading} text-xl font-bold`}>
              {specs?.version || generalConfig.version}
            </div>
          </div>
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>
              {t.ready.status}
            </div>
            <div className="text-green-600 text-xl font-bold">{t.ready.readyStatus}</div>
          </div>
        </div>
      </motion.div>

      {/* Ro-Start-Mini Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className={`mt-4 mb-16 backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-2xl border ${themeConfig.borderColor} p-6 w-full max-w-2xl mx-auto shadow-sm text-left flex items-start gap-4`}
      >
        <div
          className={`flex-shrink-0 w-12 h-12 rounded-xl bg-blue-500/10 flex items-center justify-center`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="w-6 h-6 text-blue-600 dark:text-blue-400"
          >
            <rect x="2" y="4" width="20" height="16" rx="2" />
            <path d="M10 4v4" />
            <path d="M2 8h20" />
            <path d="M6 4v4" />
          </svg>
        </div>

        <div className="flex-1">
          <h3 className={`${themeConfig.textHeading} text-lg font-bold mb-1`}>
            {t.ready.miniApp?.title || "Ro-Start-Mini"}
          </h3>
          <p className={`${themeConfig.textBody} text-sm`}>{t.ready.miniApp?.description}</p>
        </div>
      </motion.div>
    </div>
  );
}
