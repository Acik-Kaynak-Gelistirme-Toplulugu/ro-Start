#!/bin/bash
# Build .deb package for Ro-Start

set -e

echo "🚀 Building Ro-Start .deb package..."
echo ""

# Check if cargo-deb is installed
if ! cargo install --list | grep -q "cargo-deb"; then
    echo "📦 cargo-deb not found, installing..."
    cargo install cargo-deb
    echo ""
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
cargo clean
echo ""

# Build release binary
echo "🔨 Building release binary..."
cargo build --release
echo ""

# Strip binary for smaller size
echo "🎨 Stripping binary..."
strip -s target/release/ro-start || true
echo ""

# Create .deb package
echo "📦 Creating .deb package..."
cargo deb --no-build
echo ""

# Find and display the package
DEB_FILE=$(find target/debian -name "*.deb" -type f | head -n 1)

if [ -f "$DEB_FILE" ]; then
    SIZE=$(du -h "$DEB_FILE" | cut -f1)
    echo "✅ Package created successfully!"
    echo "📦 Package: $DEB_FILE"
    echo "📏 Size: $SIZE"
    echo ""
    
    # Display package info
    echo "📋 Package information:"
    dpkg-deb --info "$DEB_FILE" 2>/dev/null || echo "  (dpkg not available for package info)"
    echo ""
    
    echo "🎉 Done! You can install the package with:"
    echo "   sudo dpkg -i $DEB_FILE"
    echo ""
else
    echo "❌ Package creation failed!"
    exit 1
fi
