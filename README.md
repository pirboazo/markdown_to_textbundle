# markdown_to_textbundle

Un utilitaire CLI Python pour convertir un ou plusieurs fichiers Markdown (.md) en TextBundle compressé (.textpack), avec prise en charge des images liées.

## 📦 Fonctionnalités

- Conversion `.md` → `.textpack`
- Inclusion automatique des images locales (relatives et absolues)
- Réécriture des chemins d’image vers `assets/`
- Prise en charge des extensions : `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.jxl`
- Traitement d’un fichier ou d’un dossier complet
- Support des options `--output`, `--output-dir`, `-h`

## 🔧 Utilisation

```bash
# Fichier unique
markdown_to_textbundle fichier.md

# Nom de sortie personnalisé
markdown_to_textbundle fichier.md -o MonExport

# Sortie dans un dossier spécifique
markdown_to_textbundle fichier.md --output-dir ./out/

# Tous les fichiers .md d’un dossier
markdown_to_textbundle ./docs/ --output-dir ./archives/

A Python CLI utility to convert one or more Markdown (.md) files to compressed TextBundle (.textpack), with support for linked images.

## 📦 Features

- Conversion `.md` → `.textpack`
- Automatic inclusion of local images (relative and absolute)
- Rewrites image paths to `assets/`
- Supported extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.jxl`
- Processes a single file or an entire folder
- Supports options `--output`, `--output-dir`, `-h`

## 🔧 Usage

```bash
# Single file
markdown_to_textbundle file.md

# Custom output name
markdown_to_textbundle file.md -o MyExport

# Output to a specific folder
markdown_to_textbundle file.md --output-dir ./out/

# All .md files in a folder
markdown_to_textbundle ./docs/ --output-dir ./archives/
