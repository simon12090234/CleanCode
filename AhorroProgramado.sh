#!/bin/bash

# Nombre del entorno virtual
VENV_DIR="kivy_env"

# Ruta absoluta del script
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado. Instálalo y vuelve a intentar."
    exit 1
fi

if [ ! -d "$BASE_DIR/$VENV_DIR" ]; then
    echo "📦 Creando entorno virtual en $VENV_DIR..."
    python3 -m venv "$BASE_DIR/$VENV_DIR"
fi

source "$BASE_DIR/$VENV_DIR/bin/activate"

if ! python -c "import kivy" &> /dev/null; then
    echo "⬇ Instalando Kivy en el entorno virtual..."
    pip install --upgrade pip
    pip install "kivy[base]"
fi

APP="$BASE_DIR/KivyApp.py"
if [ -f "$APP" ]; then
    echo "🚀 Ejecutando KivyApp.py..."
    python "$APP"
else
    echo "❌ No se encontró el archivo KivyApp.py en $BASE_DIR"
    exit 1
fi
