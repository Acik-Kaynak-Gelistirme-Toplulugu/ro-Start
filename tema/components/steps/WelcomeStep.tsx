import React from 'react';
import { motion } from 'motion/react';
import { features, themeConfig } from '../../config/welcome-config';

export function WelcomeStep({ step, t }: { step: any, t: any }) {
  return (
    <div className="space-y-8">
      <div className="text-center space-y-4">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-4 shadow-lg`}
        >
          {React.createElement(features[0].icon, { className: `w-10 h-10 ${themeConfig.iconPrimary}` })}
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-6xl font-bold`}>{t.welcome.title}</h1>
        <p className={`${themeConfig.textSubheading} text-2xl`}>{t.welcome.subtitle}</p>
        <p className={`${themeConfig.textBody} text-lg max-w-2xl mx-auto`}>
          {t.welcome.description}
        </p>
      </div>

      <div className="grid grid-cols-2 gap-4 mt-12">
        {features.map((feature, index) => {
          // Map feature keys to translation keys
          const featureKeys = ['modern', 'fast', 'secure', 'custom'];
          const key = featureKeys[index];
          const title = t.welcome.features[key].title;
          const desc = t.welcome.features[key].desc;

          return (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + index * 0.1 }}
              className={`backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-2xl border ${themeConfig.borderColor} p-6 transition-all duration-300 shadow-sm`}
            >
              {React.createElement(feature.icon, { className: `w-8 h-8 ${themeConfig.iconPrimary} mb-3` })}
              <h3 className={`${themeConfig.textHeading} mb-2 font-semibold`}>{title}</h3>
              <p className={`${themeConfig.textBody} text-sm`}>{desc}</p>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
