#!/bin/bash
# Build script for Ro-Start

set -e

echo "🚀 Building Ro-Start..."
echo ""

# Check Rust installation
if ! command -v cargo &> /dev/null; then
    echo "❌ Rust is not installed!"
    echo "Please install Rust from https://rustup.rs/"
    exit 1
fi

echo "✅ Rust $(rustc --version)"
echo ""

# Check GTK4 dependencies
if ! pkg-config --exists gtk4; then
    echo "❌ GTK4 development files not found!"
    echo "Please install: sudo apt install libgtk-4-dev libadwaita-1-dev"
    exit 1
fi

echo "✅ GTK4 $(pkg-config --modversion gtk4)"

if ! pkg-config --exists libadwaita-1; then
    echo "⚠️  libadwaita not found, install: sudo apt install libadwaita-1-dev"
    exit 1
fi

echo "✅ libadwaita $(pkg-config --modversion libadwaita-1)"
echo ""

# Build
echo "🔨 Building release binary..."
cargo build --release

echo ""
echo "🎨 Stripping binary..."
strip -s target/release/ro-start

# Print size
SIZE=$(du -h target/release/ro-start | cut -f1)
echo ""
echo "✅ Build complete!"
echo "📦 Binary size: $SIZE"
echo "📍 Location: target/release/ro-start"
echo ""
echo "Run with: ./target/release/ro-start"
