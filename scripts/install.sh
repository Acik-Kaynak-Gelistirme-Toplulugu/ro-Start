#!/bin/bash
# Installation script for Ro-Start

set -e

echo "🚀 Installing Ro-Start..."

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo "❌ Please do not run as root. Use your regular user account."
   exit 1
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv nodejs npm
elif command -v dnf &> /dev/null; then
    sudo dnf install -y python3 python3-pip nodejs npm
elif command -v pacman &> /dev/null; then
    sudo pacman -S --noconfirm python python-pip nodejs npm
else
    echo "⚠️  Unsupported package manager. Please install dependencies manually."
fi

# Create virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install --upgrade pip
pip install -e .

# Build frontend
echo "⚛️  Building frontend..."
cd frontend
npm install
npm run build
cd ..

echo "✅ Installation complete!"
echo ""
echo "To run Ro-Start:"
echo "  source venv/bin/activate"
echo "  ro-start"
