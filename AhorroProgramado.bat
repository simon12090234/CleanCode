@echo off
REM This script builds the Kivy application executable for Windows using PyInstaller.

REM Navigate to the project directory
cd /d "%~dp0"

REM Install required packages
pip install -r requirements.txt

REM Build the executable using PyInstaller
pyinstaller --onefile --windowed KivyApp.py

REM Move the executable to the desired location
move dist\main.exe .

REM Clean up build files
rmdir /s /q build
rmdir /s /q dist
del main.spec

echo Build complete! The executable is located in the project root directory.