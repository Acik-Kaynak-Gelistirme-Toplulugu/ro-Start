use crate::system::SystemState;
use gio::prelude::*;
use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Button, HeaderBar, Label};
use gtk::{Box as GtkBox, Orientation};
use libadwaita as adw;
use libadwaita::prelude::*;

#[allow(dead_code)]
pub struct MainWindow {
    window: ApplicationWindow,
}

impl MainWindow {
    #[allow(clippy::new_ret_no_self)]
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
                crate::ui::settings::show_settings(Some(window.upcast_ref::<gtk::Window>()));
            }
        });
        window.add_action(&settings_action);

        // About action
        let about_action = gio::SimpleAction::new("about", None);
        let window_weak = window.downgrade();
        about_action.connect_activate(move |_, _| {
            if let Some(window) = window_weak.upgrade() {
                crate::ui::about::show_about(Some(window.upcast_ref::<gtk::Window>()));
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

        group.set_title("System Information");

        // Get system info
        let sys_state = SystemState::new();
        let info = sys_state.get_system_info();

        // OS Row
        let os_row = adw::ActionRow::new();
        os_row.set_title("Operating System");
        os_row.set_subtitle(&info.os_name);
        os_row.add_prefix(&gtk::Image::from_icon_name("computer-symbolic"));
        group.add(&os_row);

        // Desktop Row
        let desktop_row = adw::ActionRow::new();
        desktop_row.set_title("Desktop Environment");
        desktop_row.set_subtitle(&info.desktop_environment);
        desktop_row.add_prefix(&gtk::Image::from_icon_name("video-display-symbolic"));
        group.add(&desktop_row);

        // Kernel Row
        let kernel_row = adw::ActionRow::new();
        kernel_row.set_title("Kernel");
        kernel_row.set_subtitle(&info.kernel_version);
        kernel_row.add_prefix(&gtk::Image::from_icon_name("utilities-terminal-symbolic"));
        group.add(&kernel_row);

        // Memory Row
        let memory_row = adw::ActionRow::new();
        memory_row.set_title("Memory");
        memory_row.set_subtitle(&info.memory_info);
        memory_row.add_prefix(&gtk::Image::from_icon_name("drive-harddisk-symbolic"));
        group.add(&memory_row);

        // CPU Row
        let cpu_row = adw::ActionRow::new();
        cpu_row.set_title("CPU");
        cpu_row.set_subtitle(&info.cpu_info);
        cpu_row.add_prefix(&gtk::Image::from_icon_name("cpu-symbolic"));
        group.add(&cpu_row);

        group
    }

    fn create_actions_card() -> adw::PreferencesGroup {
        let group = adw::PreferencesGroup::new();

        group.set_title("Quick Actions");

        // Update System Button
        let update_row = adw::ActionRow::new();
        update_row.set_title("Update System");
        update_row.set_subtitle("Check and install available updates");
        update_row.add_prefix(&gtk::Image::from_icon_name(
            "software-update-available-symbolic",
        ));
        update_row.set_activatable(true);

        let update_button = Button::with_label("Update");
        update_button.set_valign(gtk::Align::Center);
        update_button.add_css_class("suggested-action");
        update_row.add_suffix(&update_button);

        update_button.connect_clicked(|_| {
            tracing::info!("Update button clicked");
            // TODO: Implement update functionality
        });

        group.add(&update_row);

        // Software Center Button
        let software_row = adw::ActionRow::new();
        software_row.set_title("Software Center");
        software_row.set_subtitle("Browse and install applications");
        software_row.add_prefix(&gtk::Image::from_icon_name(
            "system-software-install-symbolic",
        ));
        software_row.set_activatable(true);

        let software_button = Button::with_label("Open");
        software_button.set_valign(gtk::Align::Center);
        software_row.add_suffix(&software_button);

        software_button.connect_clicked(|_| {
            tracing::info!("Software Center button clicked");
            // TODO: Open software center
        });

        group.add(&software_row);

        // Settings Button
        let settings_row = adw::ActionRow::new();
        settings_row.set_title("System Settings");
        settings_row.set_subtitle("Configure your system");
        settings_row.add_prefix(&gtk::Image::from_icon_name("emblem-system-symbolic"));
        settings_row.set_activatable(true);

        let settings_button = Button::with_label("Open");
        settings_button.set_valign(gtk::Align::Center);
        settings_row.add_suffix(&settings_button);

        settings_button.connect_clicked(|_| {
            tracing::info!("Settings button clicked");
            // TODO: Open system settings
        });

        group.add(&settings_row);

        group
    }

    fn load_css() {
        let provider = gtk::CssProvider::new();
        provider.load_from_string(
            r#"
            .title-1 {
                font-size: 24px;
                font-weight: bold;
            }
            .dim-label {
                opacity: 0.7;
            }
            "#,
        );

        gtk::style_context_add_provider_for_display(
            &gtk::gdk::Display::default().expect("Could not connect to display"),
            &provider,
            gtk::STYLE_PROVIDER_PRIORITY_APPLICATION,
        );
    }
}
