#!/bin/bash
# Installation script for Ro-Start

set -e

echo "🚀 Installing Ro-Start..."
echo ""

# Check if running with sudo/root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ This script must be run as root or with sudo"
    echo "Usage: sudo ./install.sh"
    exit 1
fi

# Check if binary exists
if [ ! -f "target/release/ro-start" ]; then
    echo "❌ Binary not found! Please build first:"
    echo "   ./build.sh"
    exit 1
fi

echo "📦 Installing files..."

# Install binary
install -Dm755 target/release/ro-start /usr/bin/ro-start
echo "  ✅ Binary installed to /usr/bin/ro-start"

# Install desktop files
install -Dm644 data/ro-start.desktop /usr/share/applications/ro-start.desktop
install -Dm644 data/ro-start-autostart.desktop /etc/xdg/autostart/ro-start-autostart.desktop
echo "  ✅ Desktop files installed"

# Install icon
install -Dm644 data/ro-start.png /usr/share/icons/hicolor/512x512/apps/ro-start.png
echo "  ✅ Icon installed"

# Install AppData/MetaInfo
install -Dm644 data/org.osdev.ro_start.appdata.xml /usr/share/metainfo/org.osdev.ro_start.appdata.xml
echo "  ✅ AppData file installed"

# Install man page
install -Dm644 docs/ro-start.1 /usr/share/man/man1/ro-start.1
gzip -f /usr/share/man/man1/ro-start.1
echo "  ✅ Man page installed"

# Install shell completions
install -Dm644 packaging/completions/ro-start.bash /usr/share/bash-completion/completions/ro-start
install -Dm644 packaging/completions/ro-start.zsh /usr/share/zsh/site-functions/_ro-start
install -Dm644 packaging/completions/ro-start.fish /usr/share/fish/vendor_completions.d/ro-start.fish
echo "  ✅ Shell completions installed"

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database /usr/share/applications
    echo "  ✅ Desktop database updated"
fi

# Update icon cache
if command -v gtk-update-icon-cache &> /dev/null; then
    gtk-update-icon-cache -f -t /usr/share/icons/hicolor
    echo "  ✅ Icon cache updated"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "You can now run: ro-start"
echo "Or find it in your application menu"
echo ""
