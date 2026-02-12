#!/bin/bash
# Build .deb package using OrbStack on macOS

set -e

echo "🚀 Building Ro-Start .deb package with OrbStack (x86_64)..."
echo ""

# Check if OrbStack is installed
if ! command -v orbctl &> /dev/null; then
    echo "❌ OrbStack is not installed!"
    echo "Please install OrbStack from: https://orbstack.dev"
    exit 1
fi

echo "✅ OrbStack found"
echo ""

# Container name
CONTAINER_NAME="ro-start-builder-x86"
IMAGE="ubuntu:24.04"

# Check if container already exists
if orbctl list | grep -q "$CONTAINER_NAME"; then
    echo "🔄 Deleting existing container..."
    orbctl delete -f "$CONTAINER_NAME" 2>/dev/null || true
    sleep 2
fi

echo "📦 Creating x86_64 Ubuntu container..."
orbctl create "$IMAGE" "$CONTAINER_NAME" --arch amd64
echo ""

echo "⏳ Waiting for container to start..."
sleep 5
echo ""

# Install dependencies in container
echo "📥 Installing build dependencies in container..."
orb -m "$CONTAINER_NAME" -u root bash -c "
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        pkg-config \
        libgtk-4-dev \
        libadwaita-1-dev \
        curl \
        git \
        ca-certificates \
        && \
    apt-get clean
"
echo ""

echo "🦀 Installing Rust in container (as default user)..."
orb -m "$CONTAINER_NAME" bash -c "
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    source \$HOME/.cargo/env && \
    cargo install cargo-deb
"
echo ""

# Get project directory
PROJECT_DIR=$(pwd)
PROJECT_NAME=$(basename "$PROJECT_DIR")

echo "📂 Copying project to container..."
orb -m "$CONTAINER_NAME" -u root bash -c "mkdir -p /build && chown -R \$(id -un 1000):\$(id -gn 1000) /build"
orb -m "$CONTAINER_NAME" rm -rf "/build/$PROJECT_NAME"

# Copy files using tar to preserve permissions
echo "   Creating tarball..."
tar czf /tmp/ro-start-src.tar.gz \
    --exclude='target' \
    --exclude='.git' \
    --exclude='dist' \
    --exclude='*.deb' \
    -C "$PROJECT_DIR/.." "$PROJECT_NAME"

echo "   Uploading to container..."
cat /tmp/ro-start-src.tar.gz | orb -m "$CONTAINER_NAME" bash -c "cat > /tmp/ro-start-src.tar.gz"
orb -m "$CONTAINER_NAME" tar xzf /tmp/ro-start-src.tar.gz -C /build
rm /tmp/ro-start-src.tar.gz
echo ""

echo "🔨 Building .deb package in container..."
orb -m "$CONTAINER_NAME" bash -c "
    cd /build/$PROJECT_NAME && \
    source \$HOME/.cargo/env && \
    unset PKG_CONFIG_PATH PKG_CONFIG_LIBDIR CARGO_TARGET_X86_64_PC_WINDOWS_GNU_LINKER && \
    export CARGO_BUILD_TARGET=x86_64-unknown-linux-gnu && \
    cargo build --release --target x86_64-unknown-linux-gnu && \
    strip -s target/x86_64-unknown-linux-gnu/release/ro-start && \
    cargo deb --no-build --target x86_64-unknown-linux-gnu
"
echo ""

# Find the .deb package
DEB_FILE=$(orb -m "$CONTAINER_NAME" bash -c "find /build/$PROJECT_NAME/target/debian -name '*.deb' -type f | head -n 1")

if [ -z "$DEB_FILE" ]; then
    echo "❌ Failed to create .deb package!"
    exit 1
fi

# Get just the filename
DEB_FILENAME=$(basename "$DEB_FILE")

echo "📤 Copying .deb package from container..."
mkdir -p "$PROJECT_DIR/dist"
orb -m "$CONTAINER_NAME" cat "$DEB_FILE" > "$PROJECT_DIR/dist/$DEB_FILENAME"
echo ""

# Get architecture info
ARCH=$(orb -m "$CONTAINER_NAME" dpkg --print-architecture)
echo "📊 Package architecture: $ARCH"
echo ""

# Cleanup
echo "🧹 Cleaning up container..."
orbctl delete -f "$CONTAINER_NAME"
echo ""

# Display result
if [ -f "$PROJECT_DIR/dist/$DEB_FILENAME" ]; then
    SIZE=$(du -h "$PROJECT_DIR/dist/$DEB_FILENAME" | cut -f1)
    echo "✅ Package created successfully!"
    echo "📦 Package: dist/$DEB_FILENAME"
    echo "📏 Size: $SIZE"
    echo ""
    echo "🎉 Done! Package is ready for distribution."
    echo ""
    echo "To test the package on a Debian/Ubuntu system:"
    echo "  scp dist/$DEB_FILENAME user@linux-machine:"
    echo "  ssh user@linux-machine"
    echo "  sudo dpkg -i $DEB_FILENAME"
    echo ""
else
    echo "❌ Failed to copy package from container!"
    exit 1
fi
