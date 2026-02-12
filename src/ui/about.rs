use gtk::prelude::*;

/// Show About dialog
pub fn show_about(parent: Option<&gtk::Window>) {
    let about = libadwaita::AboutWindow::builder()
        .application_name("Ro-Start")
        .application_icon("ro-start")
        .version("2.0.0")
        .developer_name("Açık Kaynak Geliştirme Topluluğu")
        .issue_url("https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/issues")
        .website("https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start")
        .copyright("© 2026 Açık Kaynak Geliştirme Topluluğu")
        .license_type(gtk::License::Gpl30)
        .build();

    about.add_credit_section(
        Some("Contributors"),
        &["Açık Kaynak Geliştirme Topluluğu <info@osdev.shop>"],
    );

    about.add_acknowledgement_section(
        Some("Built with"),
        &["Rust Programming Language", "GTK4 Toolkit", "libadwaita"],
    );

    if let Some(parent) = parent {
        about.set_transient_for(Some(parent));
    }

    about.present();
}
