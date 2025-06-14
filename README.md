# markdown_to_textbundle.py

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
python3 markdown_to_textbundle.py fichier.md

# Nom de sortie personnalisé
python3 markdown_to_textbundle.py fichier.md -o MonExport

# Sortie dans un dossier spécifique
python3 markdown_to_textbundle.py fichier.md --output-dir ./out/

# Tous les fichiers .md d’un dossier
python3 markdown_to_textbundle.py ./docs/ --output-dir ./archives/

