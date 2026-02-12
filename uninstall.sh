#!/bin/bash
# Uninstallation script for Ro-Start

set -e

echo "🗑️  Uninstalling Ro-Start..."
echo ""

# Check if running with sudo/root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ This script must be run as root or with sudo"
    echo "Usage: sudo ./uninstall.sh"
    exit 1
fi

echo "📦 Removing files..."

# Remove binary
rm -f /usr/bin/ro-start
echo "  ✅ Binary removed"

# Remove desktop files
rm -f /usr/share/applications/ro-start.desktop
rm -f /etc/xdg/autostart/ro-start-autostart.desktop
echo "  ✅ Desktop files removed"

# Remove icon
rm -f /usr/share/icons/hicolor/512x512/apps/ro-start.png
echo "  ✅ Icon removed"

# Remove AppData/MetaInfo
rm -f /usr/share/metainfo/org.osdev.ro_start.appdata.xml
echo "  ✅ AppData file removed"

# Remove man page
rm -f /usr/share/man/man1/ro-start.1.gz
echo "  ✅ Man page removed"

# Remove shell completions
rm -f /usr/share/bash-completion/completions/ro-start
rm -f /usr/share/zsh/site-functions/_ro-start
rm -f /usr/share/fish/vendor_completions.d/ro-start.fish
echo "  ✅ Shell completions removed"

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
echo "✅ Uninstallation complete!"
echo ""
