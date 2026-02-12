// Prevents additional console window on Windows (though we're Linux-focused)
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
#![allow(dead_code)]

mod config;
mod error;
mod i18n;
mod notifications;
mod package_manager;
mod system;
mod ui;

use clap::Parser;
use gio::prelude::*;
use gtk::prelude::*;
use gtk::Application;
// use adw::prelude::*;

const APP_ID: &str = "org.osdev.rostart";

#[derive(Parser, Debug)]
#[command(name = "ro-start")]
#[command(version = "2.0.0")]
#[command(about = "Fast, safe, and beautiful Linux welcome application", long_about = None)]
struct Cli {
    /// Don't show at startup
    #[arg(long)]
    no_startup: bool,

    /// Set locale (e.g., en_US, tr_TR)
    #[arg(long)]
    locale: Option<String>,

    /// Enable debug logging
    #[arg(short, long)]
    debug: bool,
}

fn main() {
    // Parse CLI arguments
    let cli = Cli::parse();

    // Initialize tracing
    let log_level = if cli.debug {
        "ro_start=debug"
    } else {
        "ro_start=info"
    };
    tracing_subscriber::fmt().with_env_filter(log_level).init();

    tracing::info!("🚀 Starting Ro-Start v2.0.0");

    // Initialize i18n
    if let Err(e) = i18n::init() {
        tracing::warn!("Failed to initialize i18n: {}", e);
    }

    // Set custom locale if provided
    if let Some(locale) = cli.locale {
        i18n::set_locale(&locale);
    }

    tracing::info!("📖 Locale: {}", i18n::get_locale());

    // Create GTK application
    let app = Application::builder().application_id(APP_ID).build();

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
