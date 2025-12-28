#!/bin/bash
# Build script for imgdedup Windows executable
# 
# This script creates a standalone Windows .exe using PyInstaller.
# Note: Must be run on Windows or in a Windows-compatible Python environment.
#
# Prerequisites:
#   pip install PyInstaller
#
# Usage on Windows:
#   py build_exe.bat
# 
# Or manually:
#   pyinstaller imgdedup.spec

set -e

echo "🔨 Building imgdedup Windows executable..."
echo ""
echo "⚠️  This script requires PyInstaller on Windows."
echo "   If on Windows, run: python build_exe.py"
echo ""

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "❌ PyInstaller not found. Install it with: pip install PyInstaller"
    echo "   Then run this script on Windows."
    exit 1
fi

# Build the executable
echo "🏗️  Building executable with PyInstaller..."
pyinstaller imgdedup.spec

# Create releases directory if it doesn't exist
mkdir -p releases

# Move the executable to releases folder
if [ -f "dist/imgdedup.exe" ]; then
    cp dist/imgdedup.exe releases/imgdedup.exe
    echo ""
    echo "✅ Build successful!"
    echo "📦 Windows executable: releases/imgdedup.exe"
    echo ""
    echo "Usage on Windows:"
    echo "  imgdedup.exe C:\\Users\\YourName\\Pictures --remove"
    echo ""
else
    echo "⚠️  Build may need to be run on Windows directly."
    echo "   PyInstaller requires a Python installation with shared libraries."
fi

