import React, { useState } from "react";
import { motion } from "motion/react";
import { Package, CheckCircle2 } from "lucide-react";
import { appSuggestions, themeConfig } from "../../config/welcome-config";

export function AppSuggestionsStep({ step, t }: { step: any; t: any }) {
  const [selectedApps, setSelectedApps] = useState<string[]>([]);

  const toggleApp = (name: string) => {
    setSelectedApps((prev) =>
      prev.includes(name) ? prev.filter((n) => n !== name) : [...prev, name]
    );
  };

  const popularApps = appSuggestions.filter((app) => app.popular);

  return (
    <div className="space-y-4 h-full flex flex-col w-full">
      <div className="text-center space-y-1 flex-shrink-0">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-1 shadow-lg`}
        >
          <Package className={`w-7 h-7 ${themeConfig.iconPrimary}`} />
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-3xl font-bold tracking-tight`}>
          {t.appSuggestions.title}
        </h1>
        <p className={`${themeConfig.textSubheading} text-base opacity-90`}>
          {t.appSuggestions.subtitle}
        </p>
      </div>

      {/* Apps Grid - Centered and compact */}
      <div className="flex-1 min-h-0 py-2 max-w-4xl mx-auto w-full">
        <div className="grid grid-cols-2 lg:grid-cols-3 gap-3 h-full overflow-y-auto px-1 custom-scrollbar content-start">
          {popularApps.map((app, index) => (
            <motion.div
              key={app.name}
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.2 + index * 0.05 }}
              onClick={() => toggleApp(app.name)}
              className={`backdrop-blur-xl rounded-xl border p-3 transition-all duration-300 cursor-pointer relative flex items-center gap-3 ${
                selectedApps.includes(app.name)
                  ? "bg-blue-500/10 border-blue-400/30 ring-1 ring-blue-500/20"
                  : `${themeConfig.glassCardOpacity} ${themeConfig.borderColor} hover:bg-white/40`
              }`}
            >
              <div
                className={`flex-shrink-0 w-10 h-10 rounded-lg bg-white/20 border ${themeConfig.borderColor} flex items-center justify-center shadow-sm`}
              >
                {React.createElement(app.icon, {
                  className: `w-5 h-5 ${themeConfig.iconPrimary}`,
                })}
              </div>

              <div className="flex-1 min-w-0">
                <h3 className={`${themeConfig.textHeading} text-sm font-bold truncate`}>
                  {app.name}
                </h3>
                <p className={`${themeConfig.textMuted} text-[10px] font-bold uppercase tracking-tighter`}>
                  {t.appSuggestions.categories?.[app.category] || app.category}
                </p>
              </div>

              {selectedApps.includes(app.name) && (
                <div className="flex-shrink-0">
                  <CheckCircle2 className="w-4 h-4 text-blue-600" />
                </div>
              )}
            </motion.div>
          ))}
        </div>
      </div>

      {/* Tooltip/Footer - Compact */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="backdrop-blur-xl bg-blue-500/5 rounded-xl border border-blue-500/10 p-3 flex justify-between items-center flex-shrink-0"
      >
        <p className="text-blue-700/80 dark:text-blue-300/80 text-[11px] font-medium italic">
          💡 {t.appSuggestions.footer}
        </p>

        {selectedApps.length > 0 && (
          <button
            onClick={() => {
              const params = new URLSearchParams();
              params.append("apps", selectedApps.join(","));
              window.location.href = `app://install-apps?${params.toString()}`;
            }}
            className="px-4 py-1.5 bg-blue-600 text-white rounded-lg text-xs font-bold shadow-md hover:bg-blue-700 transition-all hover:scale-105"
          >
            {t.appSuggestions.install} ({selectedApps.length})
          </button>
        )}
      </motion.div>
    </div>
  );
}
