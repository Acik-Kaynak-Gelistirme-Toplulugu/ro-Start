use serde::{Deserialize, Serialize};
use std::path::PathBuf;
use anyhow::{Context, Result};

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
#[serde(default)]
pub struct AppConfig {
    #[serde(default = "default_app_name")]
    pub app_name: String,
    #[serde(default = "default_version")]
    pub version: String,
    #[serde(default)]
    pub autostart: bool,
    #[serde(default = "default_language")]
    pub language: String,
}

fn default_app_name() -> String {
    "Ro-Start".to_string()
}

fn default_version() -> String {
    "1.0.0".to_string()
}

fn default_language() -> String {
    "auto".to_string()
}

impl AppConfig {
    /// Get the config file path
    fn config_path() -> Result<PathBuf> {
        let config_dir = dirs::config_dir()
            .context("Failed to get config directory")?;
        Ok(config_dir.join("ro-start").join("config.toml"))
    }
    
    /// Load configuration from file, or create default if not exists
    pub fn load() -> Result<Self> {
        let path = Self::config_path()?;
        
        if path.exists() {
            let contents = std::fs::read_to_string(&path)
                .context("Failed to read config file")?;
            let config: Self = toml::from_str(&contents)
                .context("Failed to parse config file")?;
            Ok(config)
        } else {
            tracing::info!("Config file not found, using defaults");
            Ok(Self::default())
        }
    }
    
    /// Save configuration to file
    pub fn save(&self) -> Result<()> {
        let path = Self::config_path()?;
        
        // Create config directory if it doesn't exist
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent)
                .context("Failed to create config directory")?;
        }
        
        let contents = toml::to_string_pretty(self)
            .context("Failed to serialize config")?;
        std::fs::write(&path, contents)
            .context("Failed to write config file")?;
        
        tracing::info!("Config saved to {:?}", path);
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_app_config_default() {
        let config = AppConfig::default();
        assert_eq!(config.app_name, "Ro-Start");
        assert_eq!(config.version, "1.0.0");
        assert_eq!(config.autostart, false);
    }

    #[test]
    fn test_config_path() {
        let result = AppConfig::config_path();
        assert!(result.is_ok());
        let path = result.unwrap();
        assert!(path.to_str().unwrap().contains("ro-start"));
        assert!(path.to_str().unwrap().contains("config.toml"));
    }
}
