use lazy_static::lazy_static;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::sync::RwLock;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Translations {
    pub app: AppTranslations,
    pub sidebar: SidebarTranslations,
    pub home: HomeTranslations,
    pub update: UpdateTranslations,
    pub drivers: DriversTranslations,
    pub software: SoftwareTranslations,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AppTranslations {
    pub title: String,
    pub version: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SidebarTranslations {
    pub welcome: String,
    pub home: String,
    pub update: String,
    pub drivers: String,
    pub software: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HomeTranslations {
    pub title: String,
    pub description: String,
    pub website: String,
    pub docs: String,
    pub forum: String,
    pub github: String,
    pub links_title: String,
    pub autostart_label: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UpdateTranslations {
    pub title: String,
    pub description: String,
    pub status_unknown: String,
    pub status_uptodate: String,
    pub status_need_update: String,
    pub btn_update: String,
    pub log_title: String,
    pub status_started: String,
    pub success: String,
    pub error: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DriversTranslations {
    pub title: String,
    pub description: String,
    pub detecting: String,
    pub detected: String,
    pub unknown_gpu: String,
    pub driver_installed: String,
    pub driver_not_found: String,
    pub driver_current: String,
    pub btn_launch: String,
    pub session_type: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SoftwareTranslations {
    pub title: String,
    pub description: String,
    pub btn_install: String,
}

lazy_static! {
    static ref CURRENT_LOCALE: RwLock<String> = RwLock::new("en_US".to_string());
    static ref TRANSLATIONS: RwLock<HashMap<String, Translations>> = RwLock::new(HashMap::new());
}

/// Initialize i18n system and load all available translations
pub fn init() -> anyhow::Result<()> {
    let locales = vec!["en_US", "tr_TR", "de", "es", "fr", "it", "ja", "ru", "zh"];

    for locale in locales {
        if let Ok(trans) = load_locale(locale) {
            let mut translations = TRANSLATIONS.write().map_err(|e| {
                anyhow::anyhow!("Failed to acquire write lock on translations: {}", e)
            })?;
            translations.insert(locale.to_string(), trans);
            tracing::debug!("Loaded locale: {}", locale);
        }
    }

    // Detect system locale
    detect_system_locale();

    Ok(())
}

/// Load translations from JSON file
fn load_locale(locale: &str) -> anyhow::Result<Translations> {
    let json_path = format!("assets/locales/{}.json", locale);

    // Try to load from file
    match std::fs::read_to_string(&json_path) {
        Ok(content) => match serde_json::from_str(&content) {
            Ok(trans) => {
                tracing::debug!("Loaded locale {} from {}", locale, json_path);
                return Ok(trans);
            }
            Err(e) => {
                tracing::warn!("Failed to parse locale {}: {}", locale, e);
            }
        },
        Err(e) => {
            tracing::debug!("Locale file {} not found: {}", json_path, e);
        }
    }

    // Fallback to embedded translations for en_US
    if locale == "en_US" {
        tracing::debug!("Using embedded fallback for en_US");
        return Ok(get_fallback_en());
    }

    anyhow::bail!("Locale {} not found and no fallback available", locale)
}

/// Detect system locale from environment
fn detect_system_locale() {
    let locale = std::env::var("LANG")
        .or_else(|_| std::env::var("LC_ALL"))
        .unwrap_or_else(|_| "en_US.UTF-8".to_string());

    // Extract locale code (e.g., "tr_TR" from "tr_TR.UTF-8")
    let locale_code = locale.split('.').next().unwrap_or("en_US");

    // Check if we have this locale
    if let Ok(translations) = TRANSLATIONS.read() {
        if translations.contains_key(locale_code) {
            set_locale(locale_code);
            tracing::info!("System locale detected: {}", locale_code);
            return;
        }

        // Try language code only (e.g., "tr" from "tr_TR")
        let lang_code = locale_code.split('_').next().unwrap_or("en");
        if translations.contains_key(lang_code) {
            set_locale(lang_code);
            tracing::info!("Using language code: {}", lang_code);
            return;
        }
    } else {
        tracing::warn!("Failed to read translations lock during locale detection");
    }

    tracing::info!("Using default locale: en_US");
}

/// Set current locale
pub fn set_locale(locale: &str) {
    match TRANSLATIONS.read() {
        Ok(translations) => {
            if translations.contains_key(locale) {
                if let Ok(mut current) = CURRENT_LOCALE.write() {
                    *current = locale.to_string();
                    tracing::info!("Locale set to: {}", locale);
                } else {
                    tracing::error!("Failed to write current locale");
                }
            } else {
                tracing::warn!("Locale {} not available, keeping current", locale);
            }
        }
        Err(e) => tracing::error!("Failed to read translations: {}", e),
    }
}

/// Get current locale code
pub fn get_locale() -> String {
    CURRENT_LOCALE
        .read()
        .map(|locale| locale.clone())
        .unwrap_or_else(|_| {
            tracing::warn!("Failed to read current locale, using default");
            "en_US".to_string()
        })
}

/// Get translations for current locale
pub fn t() -> Translations {
    let locale = CURRENT_LOCALE
        .read()
        .map(|l| l.clone())
        .unwrap_or_else(|_| "en_US".to_string());

    TRANSLATIONS
        .read()
        .ok()
        .and_then(|translations| translations.get(&locale).cloned())
        .unwrap_or_else(get_fallback_en)
}

/// Fallback English translations (embedded)
fn get_fallback_en() -> Translations {
    Translations {
        app: AppTranslations {
            title: "Welcome to Linux".to_string(),
            version: "v2.0.0".to_string(),
        },
        sidebar: SidebarTranslations {
            welcome: "Welcome".to_string(),
            home: "Home".to_string(),
            update: "Update System".to_string(),
            drivers: "Drivers".to_string(),
            software: "Software".to_string(),
        },
        home: HomeTranslations {
            title: "Welcome to Your System".to_string(),
            description: "Essential tools to configure and prepare your computer.".to_string(),
            website: "Website".to_string(),
            docs: "Documentation".to_string(),
            forum: "Community Forum".to_string(),
            github: "Source Code (GitHub)".to_string(),
            links_title: "Useful Links".to_string(),
            autostart_label: "Show at startup".to_string(),
        },
        update: UpdateTranslations {
            title: "System Updates".to_string(),
            description: "Keep your system up to date".to_string(),
            status_unknown: "Status: Waiting for check...".to_string(),
            status_uptodate: "System is up to date!".to_string(),
            status_need_update: "Updates available".to_string(),
            btn_update: "Check for Updates".to_string(),
            log_title: "Process Log".to_string(),
            status_started: "Starting update process...".to_string(),
            success: "Update completed successfully!".to_string(),
            error: "Update check failed".to_string(),
        },
        drivers: DriversTranslations {
            title: "Hardware Drivers".to_string(),
            description: "Manage hardware drivers for optimal performance".to_string(),
            detecting: "Detecting hardware...".to_string(),
            detected: "Detected GPU:".to_string(),
            unknown_gpu: "Graphics card not detected".to_string(),
            driver_installed: "Installed Driver:".to_string(),
            driver_not_found: "Driver Not Installed".to_string(),
            driver_current: "Active".to_string(),
            btn_launch: "Open Settings".to_string(),
            session_type: "Session Type".to_string(),
        },
        software: SoftwareTranslations {
            title: "Recommended Software".to_string(),
            description: "Install popular applications to get started quickly".to_string(),
            btn_install: "Install".to_string(),
        },
    }
}

/// Get available locales
#[allow(dead_code)]
pub fn available_locales() -> Vec<String> {
    TRANSLATIONS
        .read()
        .ok()
        .map(|t| t.keys().cloned().collect())
        .unwrap_or_default()
}

/// Get locale display name
#[allow(dead_code)]
pub fn locale_name(locale: &str) -> &str {
    match locale {
        "en_US" => "English",
        "tr_TR" => "Türkçe",
        "de" => "Deutsch",
        "es" => "Español",
        "fr" => "Français",
        "it" => "Italiano",
        "ja" => "日本語",
        "ru" => "Русский",
        "zh" => "中文",
        _ => "Unknown",
    }
}
