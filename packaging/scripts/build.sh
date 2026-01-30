#!/bin/bash
# Build script for Ro-Start

set -e

echo "🔨 Building Ro-Start..."

# Check Rust installation
if ! command -v cargo &> /dev/null; then
    echo "❌ Rust is not installed!"
    echo "Install from: https://rustup.rs/"
    exit 1
fi

# Check GTK4 dependencies
echo "🔍 Checking dependencies..."
if ! pkg-config --exists gtk4; then
    echo "❌ GTK4 development files not found!"
    echo ""
    echo "Install with:"
    echo "  Ubuntu/Debian: sudo apt install libgtk-4-dev libadwaita-1-dev"
    echo "  Fedora:        sudo dnf install gtk4-devel libadwaita-devel"
    echo "  Arch:          sudo pacman -S gtk4 libadwaita"
    exit 1
fi

# Build release
echo "🚀 Building release binary..."
cargo build --release

# Strip binary
echo "✂️  Stripping binary..."
strip -s target/release/ro-start

# Show results
SIZE=$(du -h target/release/ro-start | cut -f1)
echo ""
echo "✅ Build complete!"
echo "📦 Binary size: $SIZE"
echo "📍 Location: target/release/ro-start"
echo ""
echo "To install system-wide, run:"
echo "  ./packaging/scripts/install.sh"
