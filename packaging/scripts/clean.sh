#!/bin/bash
# Clean build artifacts

set -e

echo "🧹 Cleaning build artifacts..."

# Remove Cargo build artifacts
if [ -d "target" ]; then
    echo "📦 Removing target directory..."
    cargo clean
fi

# Remove any leftover files
echo "🗑️  Removing temporary files..."
find . -type f -name "*.swp" -delete 2>/dev/null || true
find . -type f -name "*.swo" -delete 2>/dev/null || true
find . -type f -name "*~" -delete 2>/dev/null || true

# Remove package artifacts
echo "📦 Removing package artifacts..."
rm -f *.deb 2>/dev/null || true
rm -f *.rpm 2>/dev/null || true
rm -f *.tar.gz 2>/dev/null || true

echo "✅ Clean complete!"
