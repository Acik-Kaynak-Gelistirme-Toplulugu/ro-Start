use crate::system::SystemState;
use adw::prelude::*;
use gio;
use gio::prelude::*;
use glib;
use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Button, HeaderBar, Label};
use gtk::{Box as GtkBox, Orientation};
use libadwaita as adw;

pub struct MainWindow {
    window: ApplicationWindow,
}

impl MainWindow {
    pub fn new(app: &Application) -> ApplicationWindow {
        // Get translations
        let t = crate::i18n::t();

        // Create main container
        let main_box = GtkBox::new(Orientation::Vertical, 24);
        main_box.set_margin_top(24);
        main_box.set_margin_bottom(24);
        main_box.set_margin_start(24);
        main_box.set_margin_end(24);

        // Welcome section
        let welcome_box = GtkBox::new(Orientation::Vertical, 12);
        let welcome_label = Label::new(Some(&t.home.title));
        welcome_label.add_css_class("title-1");
        let desc_label = Label::new(Some(&t.home.description));
        desc_label.add_css_class("dim-label");
        welcome_box.append(&welcome_label);
        welcome_box.append(&desc_label);
        main_box.append(&welcome_box);

        // System info card
        let sys_card = Self::create_system_info_card();
        main_box.append(&sys_card);

        // Quick actions card
        let actions_card = Self::create_actions_card();
        main_box.append(&actions_card);

        // Create header bar with menu
        let header = HeaderBar::new();
        header.set_title_widget(Some(&Label::new(Some("Ro-Start"))));

        // Create menu
        let menu = gio::Menu::new();

        // Settings menu item
        menu.append(Some("_Settings"), Some("win.settings"));

        // About menu item
        menu.append(Some("_About"), Some("win.about"));

        // Separator
        menu.append(None, None);

        // Quit menu item
        menu.append(Some("_Quit"), Some("win.quit"));

        // Menu button
        let menu_button = gtk::MenuButton::new();
        menu_button.set_icon_name("open-menu-symbolic");
        menu_button.set_menu_model(Some(&menu));
        header.pack_end(&menu_button);

        // Create scrolled window for content
        let scrolled = gtk::ScrolledWindow::new();
        scrolled.set_child(Some(&main_box));
        scrolled.set_vexpand(true);

        // Create main window
        let window = ApplicationWindow::builder()
            .application(app)
            .title("Ro-Start")
            .default_width(960)
            .default_height(640)
            .build();

        window.set_titlebar(Some(&header));
        window.set_child(Some(&scrolled));

        // Add actions
        Self::setup_actions(&window, app);

        // Load CSS for styling
        Self::load_css();

        window
    }

    fn setup_actions(window: &ApplicationWindow, app: &Application) {
        // Settings action
        let settings_action = gio::SimpleAction::new("settings", None);
        let window_weak = window.downgrade();
        settings_action.connect_activate(move |_, _| {
            if let Some(window) = window_weak.upgrade() {
                crate::ui::settings::show_settings(Some(window.upcast_ref()));
            }
        });
        window.add_action(&settings_action);

        // About action
        let about_action = gio::SimpleAction::new("about", None);
        let window_weak = window.downgrade();
        about_action.connect_activate(move |_, _| {
            if let Some(window) = window_weak.upgrade() {
                crate::ui::about::show_about(Some(window.upcast_ref()));
            }
        });
        window.add_action(&about_action);

        // Quit action
        let quit_action = gio::SimpleAction::new("quit", None);
        let app_weak = app.downgrade();
        quit_action.connect_activate(move |_, _| {
            if let Some(app) = app_weak.upgrade() {
                app.quit();
            }
        });
        window.add_action(&quit_action);

        // Set up keyboard shortcuts
        app.set_accels_for_action("win.settings", &["<Ctrl>comma"]);
        app.set_accels_for_action("win.about", &["F1"]);
        app.set_accels_for_action("win.quit", &["<Ctrl>Q"]);
    }

    fn create_system_info_card() -> adw::PreferencesGroup {
        let group = adw::PreferencesGroup::new();
        let t = crate::i18n::t();

        group.set_title("System Information");

        // Get system info
        let sys_state = SystemState::new();
        let info = sys_state.get_system_info();

        // CPU row
        let cpu_row = adw::ActionRow::new();
        cpu_row.set_title("CPU");
        cpu_row.set_subtitle(&info.cpu_name);
        group.add(&cpu_row);

        // Memory row
        let memory_row = adw::ActionRow::new();
        memory_row.set_title("Memory");
        let mem_text = format!(
            "{:.1} GB / {:.1} GB",
            info.used_memory as f64 / 1024.0 / 1024.0 / 1024.0,
            info.total_memory as f64 / 1024.0 / 1024.0 / 1024.0
        );
        memory_row.set_subtitle(&mem_text);
        group.add(&memory_row);

        // OS row
        let os_row = adw::ActionRow::new();
        os_row.set_title("Operating System");
        os_row.set_subtitle(&format!("{} {}", info.os_name, info.os_version));
        group.add(&os_row);

        group
    }

    fn create_actions_card() -> adw::PreferencesGroup {
        let group = adw::PreferencesGroup::new();
        let t = crate::i18n::t();

        group.set_title(&t.update.title);
        group.set_description(Some("Common tasks to get started"));

        // Update button with proper lifetime handling
        let update_button = Button::builder()
            .label(&t.update.btn_update)
            .css_classes(["suggested-action"])
            .build();

        // Clone values for the outer closure
        let button_label = t.update.btn_update.clone();
        let error_title = t.update.error.clone();

        update_button.connect_clicked(move |btn| {
            tracing::info!("Checking for updates...");

            // Clone btn for inner async block
            let btn_weak = btn.downgrade();
            let button_label = button_label.clone();
            let error_title = error_title.clone();

            // Disable button
            btn.set_sensitive(false);
            btn.set_label("Checking...");

            // Spawn async task
            glib::spawn_future_local(async move {
                // Run blocking operation in thread pool
                let result = tokio::task::spawn_blocking(|| {
                    crate::package_manager::PackageManager::detect()
                        .and_then(|pm| pm.check_updates())
                })
                .await;

                // Handle result
                match result {
                    Ok(Ok(info)) => {
                        tracing::info!("Update check result: {:?}", info);

                        if info.available {
                            crate::notifications::notify_updates_available(info.count);
                        }

                        crate::ui::dialogs::show_info(None, "Update Check", &info.message());
                    }
                    Ok(Err(e)) => {
                        tracing::error!("Update check failed: {}", e);
                        crate::ui::dialogs::show_error(
                            None,
                            &error_title,
                            &format!("Failed to check updates: {}", e),
                        );
                    }
                    Err(e) => {
                        tracing::error!("Task failed: {}", e);
                        crate::ui::dialogs::show_error(
                            None,
                            &error_title,
                            &format!("Task execution failed: {}", e),
                        );
                    }
                }

                // Re-enable button
                if let Some(btn) = btn_weak.upgrade() {
                    btn.set_sensitive(true);
                    btn.set_label(&button_label);
                }
            });
        });

        let button_row = adw::ActionRow::new();
        button_row.set_title(&t.update.btn_update);
        button_row.add_suffix(&update_button);
        button_row.set_activatable_widget(Some(&update_button));

        group.add(&button_row);

        group
    }

    fn load_css() {
        let provider = gtk::CssProvider::new();
        provider.load_from_data(include_str!("../../resources/style.css"));

        gtk::style_context_add_provider_for_display(
            &gtk::gdk::Display::default().expect("Could not connect to display"),
            &provider,
            gtk::STYLE_PROVIDER_PRIORITY_APPLICATION,
        );
    }
}
