#!/usr/bin/python3
# Indique que le script doit être exécuté avec Python 3

# Permet d'accéder aux arguments du script et à certaines fonctionnalités système
import sys
# Permet de manipuler les fichiers et vérifier leur existence
import os

# Import dynamique de fonctions depuis d'autres fichiers Python

# Fonction pour sauvegarder une liste dans un fichier JSON
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Fonction pour charger une liste depuis un fichier JSON
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Vérifie si le fichier add_item.json existe
if os.path.exists("add_item.json"):
    # Charge le contenu existant du fichier dans my_list
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []  # Initialise une liste vide si le fichier n'existe pas

# Ajoute tous les arguments passés au script (sauf le nom du script lui-même)
# à la liste
my_list.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans add_item.json
save_to_json_file(my_list, "add_item.json")

