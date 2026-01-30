use notify_rust::Notification;

/// Show a desktop notification
pub fn show_notification(title: &str, body: &str) {
    if let Err(e) = Notification::new()
        .summary(title)
        .body(body)
        .icon("ro-start")
        .timeout(5000)
        .show()
    {
        tracing::warn!("Failed to show notification: {}", e);
    }
}

/// Show update notification
pub fn notify_updates_available(count: usize) {
    let title = "Updates Available";
    let body = format!("{} update(s) are ready to install", count);
    show_notification(title, &body);
}

/// Show success notification
pub fn notify_success(message: &str) {
    show_notification("Success", message);
}

/// Show error notification
pub fn notify_error(message: &str) {
    show_notification("Error", message);
}
