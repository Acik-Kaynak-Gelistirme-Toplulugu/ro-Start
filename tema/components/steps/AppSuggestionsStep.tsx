import React, { useState } from 'react';
import { motion } from 'motion/react';
import { Package, CheckCircle2 } from 'lucide-react';
import { appSuggestions, themeConfig } from '../../config/welcome-config';

export function AppSuggestionsStep({ step, t }: { step: any, t: any }) {
  const [selectedApps, setSelectedApps] = useState<string[]>([]);

  const toggleApp = (name: string) => {
    setSelectedApps(prev =>
      prev.includes(name)
        ? prev.filter(n => n !== name)
        : [...prev, name]
    );
  };

  const popularApps = appSuggestions.filter(app => app.popular);

  return (
    <div className="space-y-4 h-full flex flex-col">
      <div className="text-center space-y-2 flex-shrink-0">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-2 shadow-lg`}
        >
          <Package className={`w-8 h-8 ${themeConfig.iconPrimary}`} />
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-4xl font-bold`}>{t.appSuggestions.title}</h1>
        <p className={`${themeConfig.textSubheading} text-lg max-w-2xl mx-auto`}>
          {t.appSuggestions.subtitle}
        </p>
        <p className={`${themeConfig.textBody} text-base max-w-2xl mx-auto hidden md:block`}>
          {t.appSuggestions.description}
        </p>
      </div>

      {/* Apps Grid */}
      <div className="flex-1 min-h-0">
        <div className="grid grid-cols-2 gap-4 h-full overflow-y-auto pr-2 custom-scrollbar content-start">
            {popularApps.map((app, index) => (
            <motion.div
                key={app.name}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.3 + index * 0.05 }}
                onClick={() => toggleApp(app.name)}
                className={`backdrop-blur-xl rounded-2xl border p-4 transition-all duration-300 cursor-pointer relative h-[120px] ${
                selectedApps.includes(app.name)
                    ? 'bg-white/60 border-white/50 ring-2 ring-blue-400/30 shadow-sm'
                    : `${themeConfig.glassCardOpacity} ${themeConfig.borderColor} hover:bg-white/40`
                }`}
            >
                {/* Popular badge removed since all are popular now, or we can keep it for style if desired. keeping it minimal as requested */}
                
                <div className="flex items-start gap-4 h-full">
                <div className={`flex-shrink-0 w-14 h-14 rounded-xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} flex items-center justify-center shadow-sm`}>
                    {React.createElement(app.icon, { className: `w-7 h-7 ${themeConfig.iconPrimary}` })}
                </div>
                
                <div className="flex-1 min-w-0 flex flex-col justify-between h-full py-1">
                    <div>
                        <h3 className={`${themeConfig.textHeading} mb-1 truncate font-semibold text-lg`}>{app.name}</h3>
                        <p className={`${themeConfig.textMuted} text-sm font-medium`}>
                          {t.appSuggestions.categories?.[app.category] || app.category}
                        </p>
                    </div>
                    
                    <div className="flex items-center justify-end">
                    {selectedApps.includes(app.name) ? (
                        <div className="flex items-center gap-1 text-green-600 bg-green-500/10 px-2 py-1 rounded-lg">
                            <CheckCircle2 className="w-4 h-4" />
                            <span className="text-xs font-bold">{t.appSuggestions.selected}</span>
                        </div>
                    ) : (
                        <div className={`text-xs ${themeConfig.textMuted}`}>{t.appSuggestions.select}</div>
                    )}
                    </div>
                </div>
                </div>
            </motion.div>
            ))}
        </div>
      </div>
      
      {/* Quick Actions Footer - Added based on translation file, though previously it was specific text. Using translation now. */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.7 }}
        className="backdrop-blur-xl bg-blue-500/10 rounded-2xl border border-blue-500/20 p-4 flex justify-between items-center"
      >
        <p className="text-blue-700 dark:text-blue-200 text-sm">
          💡 <strong>Tip:</strong> {t.appSuggestions.footer}
        </p>

        {selectedApps.length > 0 && (
            <button
                onClick={() => {
                    const params = new URLSearchParams();
                    params.append('apps', selectedApps.join(','));
                    window.location.href = `app://install-apps?${params.toString()}`;
                }}
                className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-bold shadow-md hover:bg-blue-700 transition-colors"
            >
                Install {selectedApps.length} Apps
            </button>
        )}
      </motion.div>
    </div>
  );
}
