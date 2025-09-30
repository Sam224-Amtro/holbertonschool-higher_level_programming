#!/usr/bin/python3
import sys
from pathlib import Path

# Import des fonctions depuis les fichiers imposés par Holberton
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Charger l’ancienne liste si le fichier existe
if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

# Ajouter les nouveaux arguments
items.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour
save_to_json_file(items, filename)
