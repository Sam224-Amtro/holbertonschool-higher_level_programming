#!/usr/bin/python3
"""Module pour JSON File"""
import json


def load_from_json_file(filename):
    """
    Lit un fichier JSON et crée un objet Python à partir de son contenu.

    Args :
        nom_fichier (str) : Le chemin vers le fichier JSON.

    Retourne :
        objet : L'objet Python créé à partir du fichier JSON.
    """
    # Utilisation de l'instruction 'with' pour ouvrir le fichier
    # et s'assurer qu'il sera correctement fermé
    with open(filename, 'r', encoding='utf-8') as fichier:
        # Analyse le contenu JSON et retourne l'objet Python résultant
        return json.load(fichier)
