#!/usr/bin/env python3
import os
import json
import shutil
import re
import argparse

def create_textbundle_with_assets(markdown_path, output_base):
    bundle_dir = "temp_bundle.textbundle"
    text_path = os.path.join(bundle_dir, "text.md")
    info_path = os.path.join(bundle_dir, "info.json")
    assets_dir = os.path.join(bundle_dir, "assets")

    os.makedirs(assets_dir, exist_ok=True)

    # Lire le contenu du fichier markdown
    with open(markdown_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Repérer les liens d'image
    image_paths = re.findall(r'!\[.*?\]\((/.*?\.(?:png|jpg|jpeg|gif|webp))\)', content, re.IGNORECASE)

    for img_path in image_paths:
        img_name = os.path.basename(img_path)
        new_path = f"assets/{img_name}"

        try:
            shutil.copy(img_path, os.path.join(assets_dir, img_name))
            print(f"📸 Image copiée : {img_path}")
        except Exception as e:
            print(f"⚠️ Erreur lors de la copie de {img_path} : {e}")

        content = content.replace(img_path, new_path)

    # Écriture du markdown modifié
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Fichier info.json
    info_data = {
        "type": "net.daringfireball.markdown",
        "version": 2
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, indent=4)

    # Création archive .textpack
    shutil.make_archive(output_base, 'zip', bundle_dir)
    os.rename(output_base + ".zip", output_base + ".textpack")

    shutil.rmtree(bundle_dir)
    print(f"✅ Fichier généré : {output_base}.textpack")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="📦 Convertir un fichier Markdown en TextBundle compressé (.textpack) avec les images liées."
    )
    parser.add_argument("markdown", help="Chemin du fichier Markdown (.md)")
    parser.add_argument(
        "-o", "--output",
        help="Nom du fichier de sortie (sans extension). Par défaut : même nom que le fichier Markdown",
        default=None
    )

    args = parser.parse_args()

    # Déduire le nom de sortie si non précisé
    output_name = args.output or os.path.splitext(os.path.basename(args.markdown))[0]

    create_textbundle_with_assets(args.markdown, output_name)

