import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Download, Terminal, CheckCircle2, ChevronDown, ChevronUp } from 'lucide-react';
import { themeConfig } from '../../config/welcome-config';

export function SystemUpdatesStep({ step, t }: { step: any, t: any }) {
  const [status, setStatus] = useState<'idle' | 'updating' | 'completed'>('idle');
  const [logs, setLogs] = useState<string[]>([]);
  const [progress, setProgress] = useState(0);
  const [showLogs, setShowLogs] = useState(false);
  const logContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (logContainerRef.current) {
      logContainerRef.current.scrollTop = logContainerRef.current.scrollHeight;
    }
  }, [logs, showLogs]);

  const addLog = (message: string) => {
    setLogs(prev => [...prev, `> ${message}`]);
  };

  const startUpdate = () => {
    setStatus('updating');
    setShowLogs(true);
    setProgress(0);
    setLogs([]);

    const logMessages = t.systemUpdates.logs;
    const steps = [
      { msg: logMessages.list, progress: 10 },
      { msg: logMessages.tree, progress: 20 },
      { msg: logMessages.status, progress: 25 },
      { msg: logMessages.count, progress: 30 },
      { msg: `${logMessages.download} linux-headers-generic (45 MB)`, progress: 40 },
      { msg: `${logMessages.download} systemd-sysv (12 MB)`, progress: 50 },
      { msg: logMessages.unpack, progress: 60 },
      { msg: logMessages.config, progress: 75 },
      { msg: logMessages.initramfs, progress: 85 },
      { msg: logMessages.clean, progress: 95 },
      { msg: logMessages.done, progress: 100 }
    ];

    let currentStep = 0;

    const interval = setInterval(() => {
      if (currentStep >= steps.length) {
        clearInterval(interval);
        setStatus('completed');
        return;
      }

      const stepData = steps[currentStep];
      addLog(stepData.msg);
      setProgress(stepData.progress);
      currentStep++;

    }, 800);
  };

  return (
    <div className="space-y-6 flex flex-col h-full">
      <div className="text-center space-y-4">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-24 h-24 rounded-3xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-4 shadow-xl`}
        >
          {status === 'completed' ? (
            <CheckCircle2 className="w-12 h-12 text-green-600" />
          ) : (
            <Download className={`w-12 h-12 ${themeConfig.iconPrimary}`} />
          )}
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-5xl font-bold`}>{t.systemUpdates.title}</h1>
        <p className={`${themeConfig.textSubheading} text-xl max-w-2xl mx-auto`}>
            {status === 'completed' ? t.systemUpdates.completedTitle : t.systemUpdates.subtitle}
        </p>
      </div>

      <div className="flex-1 flex flex-col items-center justify-start mt-8 max-w-3xl mx-auto w-full">
        
        {status === 'idle' && (
             <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center space-y-8"
             >
                <p className={`${themeConfig.textBody} text-lg`}>
                    {t.systemUpdates.description}
                </p>
                <button
                    onClick={startUpdate}
                    className="px-10 py-4 rounded-2xl backdrop-blur-xl bg-blue-600 text-white shadow-lg shadow-blue-500/30 hover:bg-blue-700 hover:scale-105 transition-all duration-300 font-bold text-lg"
                >
                    {t.systemUpdates.updateButton}
                </button>
             </motion.div>
        )}

        {status !== 'idle' && (
            <motion.div
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                className="w-full space-y-6"
            >
                {/* Progress Bar */}
                <div className="space-y-2">
                    <div className="flex justify-between items-center px-1">
                        <span className={`${themeConfig.textSubheading} text-sm font-medium`}>
                            {status === 'completed' ? t.systemUpdates.completed : t.systemUpdates.updating}
                        </span>
                        <span className={`${themeConfig.textHeading} font-bold`}>{progress}%</span>
                    </div>
                    <div className="h-4 bg-slate-200 rounded-full overflow-hidden shadow-inner">
                        <motion.div
                            className={`h-full ${status === 'completed' ? 'bg-green-500' : 'bg-blue-600'}`}
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 0.5 }}
                        />
                    </div>
                </div>

                {/* Log Terminal Toggle */}
                <div className="flex justify-center">
                    <button 
                        onClick={() => setShowLogs(!showLogs)}
                        className={`flex items-center gap-2 text-sm ${themeConfig.textMuted} hover:${themeConfig.textHeading} transition-colors`}
                    >
                        {showLogs ? t.systemUpdates.hideLogs : t.systemUpdates.showLogs}
                        {showLogs ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                    </button>
                </div>

                {/* Terminal Window */}
                <AnimatePresence>
                    {showLogs && (
                        <motion.div
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: 'auto' }}
                            exit={{ opacity: 0, height: 0 }}
                            className="overflow-hidden"
                        >
                            <div className="bg-slate-900 rounded-xl border border-slate-700 p-4 shadow-2xl font-mono text-xs md:text-sm text-green-400 h-64 overflow-y-auto custom-scrollbar" ref={logContainerRef}>
                                <div className="flex items-center gap-2 border-b border-slate-800 pb-2 mb-2 text-slate-500">
                                    <Terminal className="w-4 h-4" />
                                    <span>system-update-log</span>
                                </div>
                                <div className="space-y-1">
                                    {logs.map((log, i) => (
                                        <div key={i} className="break-all">{log}</div>
                                    ))}
                                    {status === 'updating' && (
                                        <div className="animate-pulse">_</div>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </motion.div>
        )}
      </div>
    </div>
  );
}
