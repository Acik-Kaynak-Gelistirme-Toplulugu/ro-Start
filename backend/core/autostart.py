import os
import sys


def get_autostart_file_path():
    # Standard XDG autostart path
    return os.path.expanduser("~/.config/autostart/ro-start.desktop")


def is_autostart_enabled():
    return os.path.exists(get_autostart_file_path())


def set_autostart(enable=True):
    path = get_autostart_file_path()

    if enable:
        # Create directory if missing
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Determine the command to run
        # In this environment, we are running 'python3 src/main.py'
        # We'll use absolute paths.

        python_exe = sys.executable
        # Get path to src/main.py. We are in src/core/autostart.py
        script_dir = os.path.dirname(os.path.abspath(__file__))  # backend/core
        src_dir = os.path.dirname(script_dir)  # backend
        main_script = os.path.join(src_dir, "main.py")

        # Determine icon path if possible, or use a generic one
        # icon_path = os.path.join(os.path.dirname(src_dir), "assets", "logo.png")

        desktop_entry = f"""[Desktop Entry]
Type=Application
Name=Ro-Start
Comment=Welcome Screen
Exec="{python_exe}" "{main_script}"
Icon=utilities-terminal
Terminal=false
Categories=Utility;
X-GNOME-Autostart-enabled=true
"""
        try:
            with open(path, "w") as f:
                f.write(desktop_entry)
            # Make it executable just in case
            os.chmod(path, 0o755)
            return True
        except Exception as e:
            print(f"Error creating autostart entry: {e}")
            return False
    else:
        if os.path.exists(path):
            try:
                os.remove(path)
                return True
            except Exception as e:
                print(f"Error removing autostart entry: {e}")
                return False
        return True
