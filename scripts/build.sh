#!/bin/bash
# Build script for creating distribution packages

set -e

VERSION=$(grep "version" pyproject.toml | head -1 | cut -d'"' -f2)
echo "📦 Building Ro-Start v${VERSION}..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info

# Build frontend
echo "⚛️  Building frontend..."
cd frontend
npm ci
npm run build
cd ..

# Build Python package
echo "🐍 Building Python package..."
python3 -m pip install --upgrade build
python3 -m build

echo "✅ Build complete!"
echo "📦 Packages created in dist/"
ls -lh dist/
