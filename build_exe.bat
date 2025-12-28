@echo off
REM Build script for imgdedup Windows executable
REM Run on Windows with: python build_exe.py or build_exe.bat

setlocal enabledelayedexpansion

echo Building imgdedup Windows executable...
echo.

REM Check if pyinstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install PyInstaller
)

REM Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__

REM Build the executable
echo Building executable with PyInstaller...
pyinstaller imgdedup.spec

REM Create releases directory
if not exist releases mkdir releases

REM Move the executable
if exist dist\imgdedup.exe (
    copy dist\imgdedup.exe releases\imgdedup.exe
    echo.
    echo Build successful!
    echo Windows executable: releases\imgdedup.exe
    echo.
    echo Usage:
    echo   imgdedup.exe C:\Users\YourName\Pictures --remove
    echo.
) else (
    echo Build failed - executable not found
    exit /b 1
)

endlocal
