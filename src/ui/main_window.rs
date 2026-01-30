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
        // Create header bar
        let header = HeaderBar::new();
        header.set_title_widget(Some(&Label::new(Some("Ro-Start"))));

        // Create main content box
        let main_box = GtkBox::new(Orientation::Vertical, 12);
        main_box.set_margin_top(24);
        main_box.set_margin_bottom(24);
        main_box.set_margin_start(24);
        main_box.set_margin_end(24);

        // Get translations
        let t = crate::i18n::t();

        // Welcome title
        let title = Label::new(Some(&format!("🚀 {}", t.home.title)));
        title.add_css_class("title-1");
        main_box.append(&title);

        // Subtitle
        let subtitle = Label::new(Some(&t.home.description));
        subtitle.add_css_class("subtitle");
        subtitle.add_css_class("dim-label");
        main_box.append(&subtitle);

        // System info card
        let info_card = Self::create_system_info_card();
        main_box.append(&info_card);

        // Quick actions
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
                crate::ui::settings::show_settings(Some(&window));
            }
        });
        window.add_action(&settings_action);

        // About action
        let about_action = gio::SimpleAction::new("about", None);
        let window_weak = window.downgrade();
        about_action.connect_activate(move |_, _| {
            if let Some(window) = window_weak.upgrade() {
                crate::ui::about::show_about(Some(&window));
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
        group.set_description(Some("Your system specifications"));

        // Get system info
        let sys_state = SystemState::new();
        let info = sys_state.get_system_info();

        // OS row
        let os_row = adw::ActionRow::new();
        os_row.set_title("Operating System");
        os_row.set_subtitle(&format!("{} {}", info.os_name, info.os_version));
        os_row.set_icon_name(Some("computer-symbolic"));
        group.add(&os_row);

        // Kernel row
        let kernel_row = adw::ActionRow::new();
        kernel_row.set_title("Kernel");
        kernel_row.set_subtitle(&info.kernel_version);
        kernel_row.set_icon_name(Some("settings-symbolic"));
        group.add(&kernel_row);

        // CPU row
        let cpu_row = adw::ActionRow::new();
        cpu_row.set_title("Processor");
        cpu_row.set_subtitle(&info.cpu_name);
        cpu_row.set_icon_name(Some("cpu-symbolic"));
        group.add(&cpu_row);

        // RAM row
        let ram_row = adw::ActionRow::new();
        ram_row.set_title("Memory");
        let ram_gb = info.total_memory / 1024 / 1024 / 1024;
        ram_row.set_subtitle(&format!("{} GB", ram_gb));
        ram_row.set_icon_name(Some("memory-symbolic"));
        group.add(&ram_row);

        group
    }

    fn create_actions_card() -> adw::PreferencesGroup {
        let group = adw::PreferencesGroup::new();
        let t = crate::i18n::t();

        group.set_title(&t.update.title);
        group.set_description(Some("Common tasks to get started"));

        // Update button
        let update_button = Button::builder()
            .label(&t.update.btn_update)
            .css_classes(["suggested-action"])
            .build();

        // Clone all needed values before the closure
        let button_label_default = t.update.btn_update.clone();
        let error_title = t.update.error.clone();
        let update_check_title = "Update Check".to_string();

        update_button.connect_clicked(move |btn| {
            tracing::info!("Checking for updates...");
            btn.set_sensitive(false);
            btn.set_label("Checking...");

            let btn_clone = btn.clone();
            let button_label = button_label_default.clone();
            let error_title_clone = error_title.clone();
            let update_check_title_clone = update_check_title.clone();

            // Spawn async task
            glib::spawn_future_local(async move {
                // Simulate async operation
                let result = tokio::task::spawn_blocking(move || {
                    crate::package_manager::PackageManager::detect()
                        .and_then(|pm| pm.check_updates())
                })
                .await;

                match result {
                    Ok(Ok(info)) => {
                        tracing::info!("Update check result: {:?}", info);

                        // Show notification if updates available
                        if info.available {
                            crate::notifications::notify_updates_available(info.count);
                        }

                        crate::ui::dialogs::show_info(
                            None,
                            &update_check_title_clone,
                            &info.message(),
                        );
                    }
                    Ok(Err(e)) => {
                        tracing::error!("Update check failed: {}", e);
                        crate::ui::dialogs::show_error(
                            None,
                            &error_title_clone,
                            &format!("Failed to check updates: {}", e),
                        );
                    }
                    Err(e) => {
                        tracing::error!("Task failed: {}", e);
                        crate::ui::dialogs::show_error(
                            None,
                            &error_title_clone,
                            &format!("Task execution failed: {}", e),
                        );
                    }
                }

                // Re-enable button
                btn_clone.set_sensitive(true);
                btn_clone.set_label(&button_label);
            });
        });

        let update_row = adw::ActionRow::new();
        update_row.set_title(&t.update.title);
        update_row.set_subtitle(&t.update.description);
        update_row.set_activatable_widget(Some(&update_button));
        update_row.add_suffix(&update_button);
        group.add(&update_row);

        // Software recommendations
        let software_button = Button::with_label(&t.software.btn_install);
        software_button.add_css_class("pill");
        software_button.connect_clicked(|_| {
            tracing::info!("Opening software recommendations...");
        });

        let software_row = adw::ActionRow::new();
        software_row.set_title(&t.software.title);
        software_row.set_subtitle(&t.software.description);
        software_row.set_activatable_widget(Some(&software_button));
        software_row.add_suffix(&software_button);
        group.add(&software_row);

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

    pub fn present(&self) {
        self.window.present();
    }
}
