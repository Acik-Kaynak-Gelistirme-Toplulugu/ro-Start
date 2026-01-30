#!/bin/bash
# Uninstall script for Ro-Start

set -e

echo "🗑️  Uninstalling Ro-Start..."

# Remove system files
echo "Removing desktop integration files..."
sudo rm -f /usr/share/applications/ro-start.desktop
sudo rm -f /usr/share/icons/hicolor/512x512/apps/ro-start.png
sudo rm -f /usr/share/metainfo/org.osdev.ro_start.appdata.xml
sudo rm -f /usr/local/bin/ro-start

# Update icon cache
sudo gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true

echo ""
echo "✅ Ro-Start has been uninstalled from system directories."
echo ""
echo "To completely remove the project:"
echo "  cd .."
echo "  rm -rf ro-start/"
