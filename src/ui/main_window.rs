use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Box as GtkBox, Label, Button, Orientation, HeaderBar};
use libadwaita as adw;
use adw::prelude::*;
use crate::system::SystemState;

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
        
        // Welcome title
        let title = Label::new(Some("🚀 Welcome to Linux"));
        title.add_css_class("title-1");
        main_box.append(&title);
        
        // Subtitle
        let subtitle = Label::new(Some("Modern welcome application built with Rust + GTK4"));
        subtitle.add_css_class("subtitle");
        subtitle.add_css_class("dim-label");
        main_box.append(&subtitle);
        
        // System info card
        let info_card = Self::create_system_info_card();
        main_box.append(&info_card);
        
        // Quick actions
        let actions_card = Self::create_actions_card();
        main_box.append(&actions_card);
        
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
        
        // Load CSS for styling
        Self::load_css();
        
        window
    }
    
    fn create_system_info_card() -> adw::PreferencesGroup {
        let group = adw::PreferencesGroup::new();
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
        group.set_title("Quick Actions");
        group.set_description(Some("Common tasks to get started"));
        
        // Update system button
        let update_button = Button::with_label("Check for Updates");
        update_button.add_css_class("pill");
        update_button.add_css_class("suggested-action");
        
        update_button.connect_clicked(move |btn| {
            tracing::info!("Checking for updates...");
            btn.set_sensitive(false);
            btn.set_label("Checking...");
            
            // Spawn async task
            glib::spawn_future_local(async move {
                match crate::package_manager::PackageManager::detect() {
                    Ok(pm) => {
                        match pm.check_updates() {
                            Ok(info) => {
                                tracing::info!("Update check result: {:?}", info);
                                crate::ui::dialogs::show_info(
                                    None,
                                    "Update Check",
                                    &info.message()
                                );
                            }
                            Err(e) => {
                                tracing::error!("Update check failed: {}", e);
                                crate::ui::dialogs::show_error(
                                    None,
                                    "Update Check Failed",
                                    &format!("Failed to check for updates: {}", e)
                                );
                            }
                        }
                    }
                    Err(e) => {
                        tracing::error!("Package manager detection failed: {}", e);
                        crate::ui::dialogs::show_error(
                            None,
                            "Package Manager Not Found",
                            "Could not detect your package manager. Please check updates manually."
                        );
                    }
                }
                
                btn.set_sensitive(true);
                btn.set_label("Check for Updates");
            });
        });
        
        let update_row = adw::ActionRow::new();
        update_row.set_title("System Updates");
        update_row.set_subtitle("Keep your system up to date");
        update_row.set_activatable_widget(Some(&update_button));
        update_row.add_suffix(&update_button);
        group.add(&update_row);
        
        // Software recommendations
        let software_button = Button::with_label("Browse");
        software_button.add_css_class("pill");
        software_button.connect_clicked(|_| {
            tracing::info!("Opening software recommendations...");
        });
        
        let software_row = adw::ActionRow::new();
        software_row.set_title("Recommended Software");
        software_row.set_subtitle("Discover essential applications");
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
