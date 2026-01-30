#!/bin/bash
# Installation script for Ro-Start (Rust + GTK4)

set -e

echo "🚀 Installing Ro-Start..."

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo "❌ Please do not run as root. Use your regular user account."
   exit 1
fi

# Check if binary exists
if [ ! -f "target/release/ro-start" ]; then
    echo "❌ Binary not found! Please build first:"
    echo "  cargo build --release"
    exit 1
fi

# Install binary
echo "📦 Installing binary..."
sudo install -Dm755 target/release/ro-start /usr/local/bin/ro-start

# Install desktop integration files
echo "🖥️  Installing desktop integration files..."
sudo install -Dm644 data/ro-start.desktop /usr/share/applications/ro-start.desktop
sudo install -Dm644 data/ro-start.png /usr/share/icons/hicolor/512x512/apps/ro-start.png
sudo install -Dm644 data/org.osdev.ro_start.appdata.xml /usr/share/metainfo/org.osdev.ro_start.appdata.xml

# Update icon cache
echo "🎨 Updating icon cache..."
sudo gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true

# Update desktop database
sudo update-desktop-database /usr/share/applications 2>/dev/null || true

echo "✅ Installation complete!"
echo ""
echo "To run Ro-Start:"
echo "  ro-start"
echo ""
echo "Or search for 'Ro-Start' in your application menu."
