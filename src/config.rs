use serde::{Deserialize, Serialize};
use std::path::PathBuf;
use anyhow::{Context, Result};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AppConfig {
    pub app_name: String,
    pub version: String,
    pub autostart: bool,
    pub theme: String,
    pub language: String,
}

impl Default for AppConfig {
    fn default() -> Self {
        Self {
            app_name: "Ro-Start".to_string(),
            version: "2.0.0".to_string(),
            autostart: false,
            theme: "default".to_string(),
            language: "auto".to_string(),
        }
    }
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
