#!/bin/bash
# Syntax Checker - Run before pushing to GitHub

set -e

echo "🔍 Checking Rust syntax..."

# Check all Rust files
if cargo check --quiet 2>&1 | grep -q "error"; then
    echo "❌ Syntax errors found!"
    cargo check
    exit 1
fi

echo "✅ All syntax checks passed!"

echo ""
echo "🎨 Checking formatting..."
if ! cargo fmt -- --check; then
    echo "⚠️  Code needs formatting. Run: cargo fmt"
    exit 1
fi

echo "✅ Formatting is correct!"

echo ""
echo "🔍 Running clippy..."
if ! cargo clippy --quiet -- -D warnings; then
    echo "⚠️  Clippy found issues"
    exit 1
fi

echo "✅ Clippy passed!"

echo ""
echo "🎉 All checks passed! Safe to push to GitHub."
