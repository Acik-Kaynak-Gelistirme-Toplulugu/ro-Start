use gtk::prelude::*;
use libadwaita as adw;
use libadwaita::prelude::*;

/// Show Settings/Preferences window
pub fn show_settings(parent: Option<&gtk::Window>) {
    let window = adw::PreferencesWindow::new();
    window.set_title(Some("Settings"));
    window.set_default_size(600, 400);

    if let Some(parent) = parent {
        window.set_transient_for(Some(parent));
        window.set_modal(true);
    }

    // General page
    let general_page = adw::PreferencesPage::new();
    general_page.set_title("General");
    general_page.set_icon_name(Some("preferences-system-symbolic"));

    // Appearance group
    let appearance_group = adw::PreferencesGroup::new();
    appearance_group.set_title("Appearance");

    // Language selection
    let language_row = adw::ComboRow::new();
    language_row.set_title("Language");
    let languages = gtk::StringList::new(&[
        "English",
        "Türkçe",
        "Deutsch",
        "Español",
        "Français",
        "Italiano",
        "日本語",
        "Русский",
        "中文",
    ]);
    language_row.set_model(Some(&languages));
    language_row.set_selected(0);

    language_row.connect_selected_notify(|row| {
        let locale = match row.selected() {
            0 => "en_US",
            1 => "tr_TR",
            2 => "de",
            3 => "es",
            4 => "fr",
            5 => "it",
            6 => "ja",
            7 => "ru",
            8 => "zh",
            _ => "en_US",
        };
        crate::i18n::set_locale(locale);
        tracing::info!("Language changed to: {}", locale);
    });

    appearance_group.add(&language_row);
    general_page.add(&appearance_group);

    // Startup group
    let startup_group = adw::PreferencesGroup::new();
    startup_group.set_title("Startup");

    // Autostart toggle
    let autostart_row = adw::SwitchRow::new();
    autostart_row.set_title("Launch at login");
    autostart_row.set_subtitle("Automatically start Ro-Start when you log in");

    // Load current autostart setting
    if let Ok(config) = crate::config::AppConfig::load() {
        autostart_row.set_active(config.autostart);
    }

    autostart_row.connect_active_notify(|row| {
        let active = row.is_active();
        tracing::info!("Autostart set to: {}", active);

        // Save to config
        if let Ok(mut config) = crate::config::AppConfig::load() {
            config.autostart = active;
            if let Err(e) = config.save() {
                tracing::error!("Failed to save config: {}", e);
            }
        }
    });

    startup_group.add(&autostart_row);
    general_page.add(&startup_group);

    // Add page to window
    window.add(&general_page);

    window.present();
}
