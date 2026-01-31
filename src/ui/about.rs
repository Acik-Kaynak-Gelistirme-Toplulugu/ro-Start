use adw::prelude::*;
use gtk::prelude::*;
use libadwaita as adw;

/// Show About dialog
pub fn show_about(parent: Option<&gtk::Window>) {
    let about = libadwaita::AboutWindow::builder()
        .application_name("Ro-Start")
        .application_icon("ro-start")
        .version("1.0.0")
        .developer_name("ro-repo")
        .issue_url("https://github.com/ro-repo/ro-start/issues")
        .website("https://github.com/ro-repo/ro-start")
        .copyright("© 2026 ro-repo")
        .license_type(gtk::License::Gpl30)
        .build();

    about.add_credit_section(Some("Contributors"), &["ro-repo <project.roasd@gmail.com>"]);

    about.add_acknowledgement_section(
        Some("Built with"),
        &["Rust Programming Language", "GTK4 Toolkit", "libadwaita"],
    );

    if let Some(parent) = parent {
        about.set_transient_for(Some(parent));
    }

    about.present();
}
