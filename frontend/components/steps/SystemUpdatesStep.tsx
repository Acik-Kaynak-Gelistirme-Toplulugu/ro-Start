import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "motion/react";
import { Download, Terminal, CheckCircle2, ChevronDown, ChevronUp } from "lucide-react";
import { themeConfig } from "../../config/welcome-config";

export function SystemUpdatesStep({ step, t }: { step: any; t: any }) {
  const [status, setStatus] = useState<"idle" | "updating" | "completed">("idle");
  const [logs, setLogs] = useState<string[]>([]);
  const [progress, setProgress] = useState(0);
  const [showLogs, setShowLogs] = useState(true);
  const logContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (logContainerRef.current) {
      logContainerRef.current.scrollTop = logContainerRef.current.scrollHeight;
    }
  }, [logs, showLogs]);

  const addLog = (message: string) => {
    setLogs((prev) => [...prev, `> ${message}`]);
  };

  useEffect(() => {
    const handleLog = (event: CustomEvent) => {
      addLog(event.detail.message);
    };

    const handleStatus = (event: CustomEvent) => {
      if (event.detail.status === "completed") {
        setStatus("completed");
        setProgress(100);
      } else if (event.detail.status === "error") {
        setStatus("idle");
        addLog(`Error: ${event.detail.message}`);
      } else if (event.detail.status === "progress") {
        setProgress(event.detail.percentage);
      }
    };

    window.addEventListener("system-update-log", handleLog as EventListener);
    window.addEventListener("system-update-status", handleStatus as EventListener);

    return () => {
      window.removeEventListener("system-update-log", handleLog as EventListener);
      window.removeEventListener("system-update-status", handleStatus as EventListener);
    };
  }, []);

  const startUpdate = () => {
    setStatus("updating");
    setShowLogs(true);
    setProgress(0);
    setLogs([]);
    window.location.href = "app://start-system-update";
  };

  return (
    <div className="space-y-4 flex flex-col h-full w-full max-h-full">
      <div className="text-center space-y-2 flex-shrink-0">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className={`inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-white/40 to-white/10 backdrop-blur-xl border ${themeConfig.borderColor} mb-2 shadow-xl`}
        >
          {status === "completed" ? (
            <CheckCircle2 className="w-8 h-8 text-green-600" />
          ) : (
            <Download className={`w-8 h-8 ${themeConfig.iconPrimary}`} />
          )}
        </motion.div>
        <h1 className={`${themeConfig.textHeading} text-3xl md:text-4xl font-bold tracking-tight`}>
          {t.systemUpdates.title}
        </h1>
        <p className={`${themeConfig.textSubheading} text-base max-w-xl mx-auto opacity-90`}>
          {status === "completed" ? t.systemUpdates.completedTitle : t.systemUpdates.subtitle}
        </p>
      </div>

      <div className="flex-1 flex flex-col items-center justify-center min-h-0 max-w-3xl mx-auto w-full">
        {status === "idle" && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center space-y-6 py-4"
          >
            <p className={`${themeConfig.textBody} text-sm max-w-lg`}>{t.systemUpdates.description}</p>
            <button
              onClick={startUpdate}
              className="px-8 py-3 rounded-xl backdrop-blur-xl bg-blue-600 text-white shadow-lg shadow-blue-500/20 hover:bg-blue-700 hover:scale-105 transition-all duration-300 font-bold text-base"
            >
              {t.systemUpdates.updateButton}
            </button>
          </motion.div>
        )}

        {status !== "idle" && (
          <motion.div
            initial={{ opacity: 0, scale: 0.98 }}
            animate={{ opacity: 1, scale: 1 }}
            className="w-full h-full flex flex-col space-y-4 min-h-0"
          >
            {/* Progress Bar Container - Compact */}
            <div className="space-y-2 flex-shrink-0">
              <div className="flex justify-between items-center px-1">
                <span className={`${themeConfig.textSubheading} text-xs font-semibold uppercase tracking-wider`}>
                  {status === "completed" ? t.systemUpdates.completed : t.systemUpdates.updating}
                </span>
                <span className={`${themeConfig.textHeading} text-sm font-bold`}>{progress}%</span>
              </div>
              <div className="h-3 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden shadow-inner">
                <motion.div
                  className={`h-full ${status === "completed" ? "bg-green-500" : "bg-blue-600"}`}
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  transition={{ duration: 0.5 }}
                />
              </div>
            </div>

            {/* Terminal Window - Flexible Height */}
            <AnimatePresence>
              {showLogs && (
                <motion.div
                  initial={{ opacity: 0, flexGrow: 0 }}
                  animate={{ opacity: 1, flexGrow: 1 }}
                  exit={{ opacity: 0, flexGrow: 0 }}
                  className="flex flex-col min-h-0"
                >
                  <div
                    className="flex-1 bg-slate-900/95 dark:bg-black/80 rounded-xl border border-slate-700 p-4 shadow-2xl font-mono text-[10px] md:text-xs text-green-400 overflow-y-auto custom-scrollbar"
                    ref={logContainerRef}
                  >
                    <div className="flex items-center gap-2 border-b border-slate-800 pb-2 mb-2 text-slate-500 text-[10px] uppercase font-bold tracking-widest">
                      <Terminal className="w-3 h-3" />
                      <span>system-update-log</span>
                    </div>
                    <div className="space-y-1">
                      {logs.map((log, i) => (
                        <div key={i} className="break-all opacity-90 transition-opacity hover:opacity-100">
                          {log}
                        </div>
                      ))}
                      {status === "updating" && <div className="animate-pulse inline-block w-2 h-4 bg-green-400"></div>}
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
            
            {/* Log Terminal Toggle - Minimal */}
            <div className="flex justify-center flex-shrink-0">
              <button
                onClick={() => setShowLogs(!showLogs)}
                className={`flex items-center gap-1.5 text-[10px] uppercase font-bold tracking-widest ${themeConfig.textMuted} hover:${themeConfig.textHeading} transition-colors`}
              >
                {showLogs ? t.systemUpdates.hideLogs : t.systemUpdates.showLogs}
                {showLogs ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
              </button>
            </div>
          </motion.div>
        )}
      </div>
    </div>
  );
}
