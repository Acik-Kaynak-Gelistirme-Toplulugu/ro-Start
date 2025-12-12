import React from 'react';
import { motion } from 'motion/react';
import { Sparkles } from 'lucide-react';
import { generalConfig, themeConfig } from '../../config/welcome-config';

export function ReadyStep({ step, t }: { step: any, t: any }) {
  return (
    <div className="space-y-8 text-center flex flex-col items-center justify-center h-full">
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
      <p className={`${themeConfig.textBody} text-lg max-w-2xl mx-auto`}>
        {t.ready.description}
      </p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className={`mt-12 backdrop-blur-xl ${themeConfig.glassOpacity} rounded-2xl border ${themeConfig.borderColor} p-8 w-full max-w-2xl mx-auto shadow-sm`}
      >
        <div className="grid grid-cols-3 gap-8">
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>{t.ready.system}</div>
            <div className={`${themeConfig.textHeading} text-xl font-bold`}>{generalConfig.appName}</div>
          </div>
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>{t.ready.version}</div>
            <div className={`${themeConfig.textHeading} text-xl font-bold`}>{generalConfig.version}</div>
          </div>
          <div>
            <div className={`${themeConfig.textSubheading} text-sm mb-1 font-medium`}>{t.ready.status}</div>
            <div className="text-green-600 text-xl font-bold">{t.ready.readyStatus}</div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
