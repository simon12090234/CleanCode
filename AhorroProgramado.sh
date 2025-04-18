#!/bin/bash

# Vérifiez si PyInstaller est installé
if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller n'est pas installé. Veuillez l'installer en exécutant 'pip install pyinstaller'."
    exit 1
fi

# Créez l'exécutable avec PyInstaller
pyinstaller --onefile --windowed main.py

# Déplacez l'exécutable dans le répertoire de distribution
mkdir -p dist
mv dist/main dist/mon_projet_kivy

echo "L'exécutable a été créé avec succès dans le répertoire 'dist'."