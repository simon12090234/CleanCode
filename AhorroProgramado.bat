@echo off
setlocal

set VENV_DIR=kivy_env
set VENV_PATH=%~dp0%VENV_DIR%

where python >nul 2>nul
if errorlevel 1 (
    echo ❌ Python no está instalado.
    pause
    exit /b 1
)

if not exist "%VENV_PATH%\Scripts\activate.bat" (
    echo 📦 Creando entorno virtual...
    python -m venv "%VENV_PATH%"
)

call "%VENV_PATH%\Scripts\activate.bat"

pip install --upgrade pip
pip install "kivy[base]" pyinstaller

pyinstaller --noconfirm --onefile --windowed KivyApp.py

if exist dist\KivyApp.exe (
    move /Y dist\KivyApp.exe dist\MiAppKivy.exe >nul
    echo ✅ Ejecutable creado: dist\MiAppKivy.exe
) else (
    echo ❌ Error al generar el ejecutable
)

endlocal
pause
