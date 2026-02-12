use anyhow::{Context, Result};
use serde::{Deserialize, Serialize};
use std::path::PathBuf;

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(default)]
pub struct AppConfig {
    pub app_name: String,
    pub version: String,
    pub autostart: bool,
    pub language: String,
}

impl Default for AppConfig {
    fn default() -> Self {
        Self {
            app_name: "Ro-Start".to_string(),
            version: "2.0.0".to_string(),
            autostart: false,
            language: "auto".to_string(),
        }
    }
}

impl AppConfig {
    /// Get the config file path
    fn config_path() -> Result<PathBuf> {
        let config_dir = dirs::config_dir().context("Failed to get config directory")?;
        Ok(config_dir.join("ro-start").join("config.toml"))
    }

    /// Load configuration from file, or create default if not exists
    pub fn load() -> Result<Self> {
        let path = Self::config_path()?;

        if path.exists() {
            let contents = std::fs::read_to_string(&path).context("Failed to read config file")?;
            let config: Self = toml::from_str(&contents).context("Failed to parse config file")?;
            Ok(config)
        } else {
            tracing::info!("Config file not found, using defaults");
            Ok(Self::default())
        }
    }

    /// Valid locale values for input validation
    const VALID_LOCALES: &'static [&'static str] = &[
        "auto", "en_US", "tr_TR", "de", "es", "fr", "it", "ja", "ru", "zh",
    ];

    /// Validate configuration values
    fn validate(&self) -> Result<()> {
        if !Self::VALID_LOCALES.contains(&self.language.as_str()) {
            anyhow::bail!(
                "Invalid language '{}'. Valid values: {:?}",
                self.language,
                Self::VALID_LOCALES
            );
        }
        Ok(())
    }

    /// Save configuration to file with secure permissions (0600)
    pub fn save(&self) -> Result<()> {
        // Validate before saving
        self.validate()?;

        let path = Self::config_path()?;

        // Create config directory with restricted permissions
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent).context("Failed to create config directory")?;
        }

        let contents = toml::to_string_pretty(self).context("Failed to serialize config")?;
        std::fs::write(&path, &contents).context("Failed to write config file")?;

        // Set file permissions to 0600 (owner read/write only)
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            let perms = std::fs::Permissions::from_mode(0o600);
            std::fs::set_permissions(&path, perms)
                .context("Failed to set config file permissions")?;
        }

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
        assert_eq!(config.version, "2.0.0");
        assert!(!config.autostart);
        assert_eq!(config.language, "auto");
    }

    #[test]
    fn test_config_path() {
        let result = AppConfig::config_path();
        assert!(result.is_ok());

        let path = result.unwrap();
        let path_str = path.to_str().expect("Valid UTF-8 path");
        assert!(path_str.contains("ro-start"));
        assert!(path_str.contains("config.toml"));
    }

    #[test]
    fn test_valid_locale_passes_validation() {
        for locale in AppConfig::VALID_LOCALES {
            let config = AppConfig {
                language: locale.to_string(),
                ..Default::default()
            };
            assert!(
                config.validate().is_ok(),
                "Locale '{}' should be valid",
                locale
            );
        }
    }

    #[test]
    fn test_invalid_locale_fails_validation() {
        let config = AppConfig {
            language: "invalid_locale".to_string(),
            ..Default::default()
        };
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_config_serialization_roundtrip() {
        let config = AppConfig::default();
        let toml_str = toml::to_string_pretty(&config).unwrap();
        let deserialized: AppConfig = toml::from_str(&toml_str).unwrap();
        assert_eq!(config.app_name, deserialized.app_name);
        assert_eq!(config.version, deserialized.version);
        assert_eq!(config.autostart, deserialized.autostart);
        assert_eq!(config.language, deserialized.language);
    }
}
