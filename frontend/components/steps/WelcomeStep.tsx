import React from "react";
import { motion } from "motion/react";
import { features, themeConfig } from "../../config/welcome-config";

export function WelcomeStep({ step, t }: { step: any; t: any }) {
  return (
    <div className="space-y-6 w-full">
      <div className="text-center space-y-2">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-2 shadow-lg`}
        >
          {React.createElement(features[0].icon, {
            className: `w-8 h-8 ${themeConfig.iconPrimary}`,
          })}
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-4xl md:text-5xl font-bold tracking-tight`}>
          {t.welcome.title}
        </h1>
        <p className={`${themeConfig.textSubheading} text-lg md:text-xl font-medium`}>
          {t.welcome.subtitle}
        </p>
        <p className={`${themeConfig.textBody} text-base max-w-xl mx-auto opacity-80`}>
          {t.welcome.description}
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-8 max-w-2xl mx-auto">
        {features.map((feature, index) => {
          const featureKeys = ["modern", "fast", "secure", "custom"];
          const key = featureKeys[index];
          const title = t.welcome.features[key].title;
          const desc = t.welcome.features[key].desc;

          return (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + index * 0.1 }}
              className={`backdrop-blur-xl ${themeConfig.glassCardOpacity} rounded-xl border ${themeConfig.borderColor} p-4 transition-all duration-300 shadow-sm flex items-start gap-4`}
            >
              <div className={`flex-shrink-0 p-2 rounded-lg bg-white/10`}>
                {React.createElement(feature.icon, {
                  className: `w-5 h-5 ${themeConfig.iconPrimary}`,
                })}
              </div>
              <div>
                <h3 className={`${themeConfig.textHeading} text-sm font-bold mb-0.5`}>{title}</h3>
                <p className={`${themeConfig.textBody} text-xs leading-relaxed opacity-90`}>{desc}</p>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
