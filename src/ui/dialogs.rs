use gtk::glib;
use gtk::prelude::*;
use libadwaita as adw;

/// Show an error dialog
pub fn show_error<W: IsA<gtk::Window>>(parent: Option<&W>, title: &str, message: &str) {
    let dialog = adw::MessageDialog::builder()
        .heading(title)
        .body(message)
        .build();

    dialog.add_response("ok", "OK");
    dialog.set_default_response(Some("ok"));
    dialog.set_close_response("ok");

    if let Some(parent) = parent {
        dialog.set_transient_for(Some(parent.upcast_ref::<gtk::Window>()));
    }

    dialog.present();
}

/// Show an info dialog
pub fn show_info<W: IsA<gtk::Window>>(parent: Option<&W>, title: &str, message: &str) {
    let dialog = adw::MessageDialog::builder()
        .heading(title)
        .body(message)
        .build();

    dialog.add_response("ok", "OK");
    dialog.set_default_response(Some("ok"));
    dialog.set_close_response("ok");

    if let Some(parent) = parent {
        dialog.set_transient_for(Some(parent.upcast_ref::<gtk::Window>()));
    }

    dialog.present();
}

/// Show a confirmation dialog
pub fn show_confirm<W: IsA<gtk::Window>>(
    parent: Option<&W>,
    title: &str,
    message: &str,
    confirm_label: &str,
    callback: Box<dyn Fn() + 'static>,
) {
    let dialog = adw::MessageDialog::builder()
        .heading(title)
        .body(message)
        .build();

    dialog.add_response("cancel", "Cancel");
    dialog.add_response("confirm", confirm_label);
    dialog.set_default_response(Some("confirm"));
    dialog.set_close_response("cancel");
    dialog.set_response_appearance("confirm", adw::ResponseAppearance::Suggested);

    if let Some(parent) = parent {
        dialog.set_transient_for(Some(parent.upcast_ref::<gtk::Window>()));
    }

    dialog.connect_response(None, move |_, response| {
        if response == "confirm" {
            callback();
        }
    });

    dialog.present();
}
