use sysinfo::System;

#[derive(Debug, Clone)]
pub struct SystemInfo {
    pub cpu_name: String,
    pub cpu_usage: f32,
    pub cpu_info: String,
    pub total_memory: u64,
    pub used_memory: u64,
    pub memory_info: String,
    pub os_name: String,
    pub os_version: String,
    pub desktop_environment: String,
    pub kernel_version: String,
    pub hostname: String,
}

pub struct SystemState {
    sys: System,
}

impl SystemState {
    pub fn new() -> Self {
        let mut sys = System::new_all();
        sys.refresh_all();

        Self { sys }
    }

    pub fn get_system_info(&self) -> SystemInfo {
        let cpu_name = self
            .sys
            .cpus()
            .first()
            .map(|cpu| cpu.brand().to_string())
            .unwrap_or_else(|| "Unknown CPU".to_string());

        let cpu_usage = self.sys.global_cpu_usage();
        let total_memory = self.sys.total_memory();
        let used_memory = self.sys.used_memory();

        // Format CPU info as percentage and model name
        let cpu_info = format!("{:.1}% ({})", cpu_usage, cpu_name);

        // Format memory info as "used / total"
        let memory_mb_used = used_memory / 1024;
        let memory_mb_total = total_memory / 1024;
        let memory_info = format!("{} MB / {} MB", memory_mb_used, memory_mb_total);

        let os_name = System::name().unwrap_or_else(|| "Linux".to_string());
        let os_version = System::os_version().unwrap_or_else(|| "Unknown".to_string());
        let kernel_version = System::kernel_version().unwrap_or_else(|| "Unknown".to_string());
        let hostname = System::host_name().unwrap_or_else(|| "localhost".to_string());

        // Detect desktop environment
        let desktop_environment = std::env::var("XDG_CURRENT_DESKTOP")
            .or_else(|_| std::env::var("DESKTOP_SESSION"))
            .unwrap_or_else(|_| "Unknown".to_string());

        SystemInfo {
            cpu_name,
            cpu_usage,
            cpu_info,
            total_memory,
            used_memory,
            memory_info,
            os_name,
            os_version,
            desktop_environment,
            kernel_version,
            hostname,
        }
    }

    pub fn refresh(&mut self) {
        self.sys.refresh_all();
    }
}

impl Default for SystemState {
    fn default() -> Self {
        Self::new()
    }
}
