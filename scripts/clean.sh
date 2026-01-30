#!/bin/bash
# Clean development artifacts

echo "🧹 Cleaning development artifacts..."

# Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete

# Build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info
rm -rf .eggs/

# Frontend build artifacts
rm -rf frontend/node_modules/
rm -rf frontend/dist/
rm -rf frontend/.vite/

# Virtual environment
rm -rf venv/
rm -rf .venv/

# IDE artifacts
rm -rf .idea/
rm -rf .vscode/
rm -rf *.swp
rm -rf *.swo
rm -rf *~

# Logs
rm -rf *.log

echo "✅ Cleanup complete!"
