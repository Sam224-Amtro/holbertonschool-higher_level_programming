#!/usr/bin/python3
'''Basic Serialization'''

# On importe le module json qui permet de convertir
# des objets Python (ex: dictionnaire, liste) en texte JSON et inversement.
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialiser un dictionnaire Python et l'enregistrer dans un fichier JSON.

    data : dictionnaire Python (par ex. {"nom": "Alice", "age": 25})
    filename : nom du fichier dans lequel sauvegarder
    les données (ex. "data.json")
    """
    # On ouvre le fichier en mode écriture ('w')
    # Si le fichier existe, il sera écrasé.
    with open(filename, 'w') as file:
        # On convertit le dictionnaire en JSON et on l'écrit dans le fichier
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charger un fichier JSON et le désérialiser en dictionnaire Python.

    filename : nom du fichier JSON à lire (ex. "data.json")
    Retourne : un dictionnaire Python issu du fichier JSON
    """
    # On ouvre le fichier en mode lecture ('r')
    with open(filename, 'r') as file:
        # On lit le contenu JSON et on le reconvertit en objet Python
        return json.load(file)
