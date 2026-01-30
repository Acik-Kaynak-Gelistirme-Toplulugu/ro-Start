use std::process::Command;
use crate::error::{Result, RoStartError};

#[derive(Debug, Clone)]
pub enum PackageManager {
    Apt,
    Dnf,
    Pacman,
    Zypper,
}

impl PackageManager {
    /// Detect the system's package manager
    pub fn detect() -> Result<Self> {
        if Command::new("apt").arg("--version").output().is_ok() {
            Ok(Self::Apt)
        } else if Command::new("dnf").arg("--version").output().is_ok() {
            Ok(Self::Dnf)
        } else if Command::new("pacman").arg("--version").output().is_ok() {
            Ok(Self::Pacman)
        } else if Command::new("zypper").arg("--version").output().is_ok() {
            Ok(Self::Zypper)
        } else {
            Err(RoStartError::PackageManagerNotFound)
        }
    }
    
    /// Get the update check command
    pub fn update_check_command(&self) -> Vec<String> {
        match self {
            Self::Apt => vec!["apt", "list", "--upgradable"],
            Self::Dnf => vec!["dnf", "check-update"],
            Self::Pacman => vec!["checkupdates"],
            Self::Zypper => vec!["zypper", "list-updates"],
        }
        .iter()
        .map(|s| s.to_string())
        .collect()
    }
    
    /// Check for available updates
    pub fn check_updates(&self) -> Result<UpdateInfo> {
        let cmd = self.update_check_command();
        let output = Command::new(&cmd[0])
            .args(&cmd[1..])
            .output()
            .map_err(|e| RoStartError::UpdateCheckFailed(e.to_string()))?;
        
        let stdout = String::from_utf8_lossy(&output.stdout);
        let update_count = match self {
            Self::Apt => stdout.lines()
                .filter(|line| line.contains("upgradable"))
                .count(),
            Self::Dnf | Self::Zypper => stdout.lines()
                .filter(|line| !line.is_empty() && !line.starts_with('#'))
                .count(),
            Self::Pacman => stdout.lines().count(),
        };
        
        Ok(UpdateInfo {
            available: update_count > 0,
            count: update_count,
            package_manager: self.clone(),
        })
    }
}

#[derive(Debug, Clone)]
pub struct UpdateInfo {
    pub available: bool,
    pub count: usize,
    pub package_manager: PackageManager,
}

impl UpdateInfo {
    pub fn message(&self) -> String {
        if self.available {
            format!("{} update(s) available", self.count)
        } else {
            "System is up to date!".to_string()
        }
    }
}
