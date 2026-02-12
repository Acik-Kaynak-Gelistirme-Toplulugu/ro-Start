use sysinfo::System;

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub struct SystemInfo {
    pub cpu_name: String,
    #[allow(dead_code)]
    pub cpu_usage: f32,
    pub cpu_info: String,
    pub total_memory: u64,
    #[allow(dead_code)]
    pub used_memory: u64,
    pub memory_info: String,
    pub os_name: String,
    #[allow(dead_code)]
    pub os_version: String,
    pub desktop_environment: String,
    pub kernel_version: String,
    #[allow(dead_code)]
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

        // Format memory info with smart units
        let memory_info = Self::format_memory(used_memory, total_memory);

        let os_name = System::name().unwrap_or_else(|| "Linux".to_string());
        let os_version = System::os_version().unwrap_or_else(|| "Unknown".to_string());
        let kernel_version = System::kernel_version().unwrap_or_else(|| "Unknown".to_string());
        let hostname = System::host_name().unwrap_or_else(|| "localhost".to_string());

        // Detect desktop environment with better support for KDE, GNOME, and others
        let desktop_environment = Self::detect_desktop_environment();

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

    /// Format memory values with appropriate units (MB or GB)
    /// sysinfo returns memory in bytes
    fn format_memory(used_bytes: u64, total_bytes: u64) -> String {
        let used_mb = used_bytes / (1024 * 1024);
        let total_mb = total_bytes / (1024 * 1024);

        if total_mb >= 1024 {
            format!(
                "{:.1} GB / {:.1} GB",
                used_mb as f64 / 1024.0,
                total_mb as f64 / 1024.0
            )
        } else {
            format!("{} MB / {} MB", used_mb, total_mb)
        }
    }

    /// Detect the running desktop environment
    fn detect_desktop_environment() -> String {
        // Desktop environment name mappings (keyword → display name)
        const DE_MAP: &[(&str, &str)] = &[
            ("kde", "KDE Plasma"),
            ("plasmadesktop", "KDE Plasma"),
            ("gnome", "GNOME"),
            ("xfce", "Xfce"),
            ("lxde", "LXDE"),
            ("lxqt", "LXQt"),
            ("cinnamon", "Cinnamon"),
            ("mate", "MATE"),
            ("budgie", "Budgie"),
            ("deepin", "Deepin"),
            ("sway", "Sway"),
            ("hyprland", "Hyprland"),
            ("i3", "i3"),
            ("cosmic", "COSMIC"),
            ("pantheon", "Pantheon"),
        ];

        // Check XDG_CURRENT_DESKTOP first (most reliable), then DESKTOP_SESSION
        let env_val = std::env::var("XDG_CURRENT_DESKTOP")
            .or_else(|_| std::env::var("DESKTOP_SESSION"))
            .unwrap_or_default();

        if env_val.is_empty() {
            return "Unknown".to_string();
        }

        let lower = env_val.to_lowercase();
        for (keyword, display_name) in DE_MAP {
            if lower.contains(keyword) {
                return display_name.to_string();
            }
        }

        // Return the raw value if no known DE matched
        env_val
    }

    #[allow(dead_code)]
    pub fn refresh(&mut self) {
        self.sys.refresh_all();
    }
}

impl Default for SystemState {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_format_memory_mb() {
        // 512 MB used / 1024 MB total (values in bytes)
        let result = SystemState::format_memory(512 * 1024 * 1024, 900 * 1024 * 1024);
        assert!(result.contains("512 MB"));
        assert!(result.contains("900 MB"));
    }

    #[test]
    fn test_format_memory_gb() {
        // 4 GB used / 16 GB total (values in bytes)
        let result = SystemState::format_memory(4 * 1024 * 1024 * 1024, 16 * 1024 * 1024 * 1024);
        assert!(result.contains("4.0 GB"));
        assert!(result.contains("16.0 GB"));
    }

    #[test]
    fn test_system_info_populated() {
        let state = SystemState::new();
        let info = state.get_system_info();

        // All fields should have non-empty values
        assert!(!info.cpu_name.is_empty());
        assert!(!info.cpu_info.is_empty());
        assert!(!info.memory_info.is_empty());
        assert!(!info.os_name.is_empty());
        assert!(!info.kernel_version.is_empty());
        assert!(!info.hostname.is_empty());
        assert!(info.total_memory > 0);
    }
}
