# Specification - markdown\_to\_textbundle.py

## ✅ Objectif

Transformer un ou plusieurs fichiers **Markdown** (`.md`) en fichiers **TextBundle compressés** (`.textpack`), incluant automatiquement :

- Les **images liées** dans le fichier Markdown
- La **réécriture des chemins d’image** dans le Markdown (`assets/`)
- Un fichier `info.json` pour la compatibilité avec le format [TextBundle](https://textbundle.org)

---

## 📆 Fonctionnalités principales

| Fonction                                | Description                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------- |
| 🔄 Conversion `.md` → `.textpack`       | Crée un fichier compressé `.textpack` contenant `text.md`, `info.json`, `assets/` |
| 📸 Inclusion des images                 | Les images locales utilisées dans le Markdown sont copiées dans `assets/`         |
| 🔍 Prise en charge des chemins          | Supporte les **chemins relatifs** et **absolus** vers les images                  |
| 📝 Réécriture des chemins d’image       | Les chemins d’image dans le Markdown sont modifiés pour pointer vers `assets/`   |
| 🎨 Extensions d’images supportées       | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.jxl`                         |
| 🗂️ Traitement d’un dossier             | Peut traiter tous les `.md` dans un répertoire donné                              |
| 📁 Répertoire de sortie personnalisable | Peut enregistrer les `.textpack` dans un dossier spécifique (`--output-dir`)      |
| 🧠 Nom de sortie intelligent            | Par défaut, le nom du `.textpack` correspond au nom du fichier `.md`              |
| ⚙️ Ligne de commande complète           | Avec `-o` pour forcer un nom, `--output-dir` pour la destination, et `-h/--help`  |

---

## 💻 Exemples d'utilisation

```bash
# 1. Convertir un seul fichier (sortie = ./fichier.textpack)
./markdown_to_textbundle.py fichier.md

# 2. Convertir avec un nom personnalisé
./markdown_to_textbundle.py fichier.md -o MonExport

# 3. Spécifier le dossier de sortie
./markdown_to_textbundle.py fichier.md --output-dir ./out/

# 4. Convertir tous les .md dans un dossier
./markdown_to_textbundle.py ./notes/ --output-dir ./archives/
```

---

## 🔧 Structure du `.textpack` généré

```
NomDuFichier.textpack/
├── text.md          # le contenu markdown avec liens images modifiés
├── info.json        # métadonnées TextBundle (type/version)
└── assets/          # les images liées
    ├── img1.jpg
    └── image.avif
```

---


