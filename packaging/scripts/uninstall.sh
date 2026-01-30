#!/bin/bash
# Uninstall script for Ro-Start

set -e

echo "🗑️  Uninstalling Ro-Start..."

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo "❌ Please do not run as root. Use your regular user account."
   exit 1
fi

# Remove binary
echo "📦 Removing binary..."
sudo rm -f /usr/local/bin/ro-start

# Remove desktop integration files
echo "🖥️  Removing desktop integration files..."
sudo rm -f /usr/share/applications/ro-start.desktop
sudo rm -f /usr/share/icons/hicolor/512x512/apps/ro-start.png
sudo rm -f /usr/share/metainfo/org.osdev.ro_start.appdata.xml

# Update icon cache
echo "🎨 Updating icon cache..."
sudo gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true

# Update desktop database
sudo update-desktop-database /usr/share/applications 2>/dev/null || true

echo "✅ Uninstallation complete!"
