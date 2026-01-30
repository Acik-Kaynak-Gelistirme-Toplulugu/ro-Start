// Prevents additional console window on Windows (though we're Linux-focused)
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod ui;
mod system;
mod config;
mod error;
mod package_manager;

use gtk::prelude::*;
use gtk::{Application, ApplicationWindow};
use libadwaita as adw;
use adw::prelude::*;

const APP_ID: &str = "org.osdev.rostart";

fn main() {
    // Initialize tracing
    tracing_subscriber::fmt()
        .with_env_filter("ro_start=debug")
        .init();

    tracing::info!("🚀 Starting Ro-Start v2.0.0");

    // Create GTK application
    let app = Application::builder()
        .application_id(APP_ID)
        .build();

    app.connect_activate(build_ui);

    // Run the application
    app.run();
}

fn build_ui(app: &Application) {
    // Create main window
    let window = ui::MainWindow::new(app);
    
    // Present window
    window.present();
    
    tracing::info!("✅ Application window created");
}
