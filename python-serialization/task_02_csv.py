#!/usr/bin/python3
'''Convert JSON To CSV'''
# -*- coding: utf-8 -*-
# Ce script permet de convertir un fichier CSV en fichier JSON.
# Il utilise les modules csv et json pour lire et écrire les fichiers.

import csv  # Import du module pour manipuler les fichiers CSV
import json  # Import du module pour manipuler les fichiers JSON


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert CSV to JSON.

    Paramètres :
        csv_filename (str) : Le nom du fichier CSV à convertir.

    Retour :
        bool : True si la conversion s'est bien passée, False sinon.

    Fonctionnement :
        - Lit le fichier CSV en utilisant csv.DictReader
        (chaque ligne devient un dictionnaire).
        - Stocke toutes les lignes dans une liste.
        - Écrit cette liste dans un fichier JSON nommé 'data.json',
        avec une indentation pour plus de lisibilité.
        - Gère les exceptions : fichier non trouvé ou autres erreurs.
    """
    try:
        # Ouverture du fichier CSV en lecture
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Lit le CSV et transforme chaque ligne en dictionnaire
            reader = csv.DictReader(csv_file)
            # Stocke toutes les lignes dans une liste
            data = [row for row in reader]

        # Écriture des données dans un fichier JSON
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            # dump avec indentation de 4 espaces pour lisibilité
            json.dump(data, json_file, indent=4)
        return True  # Conversion réussie
    except FileNotFoundError:
        # Message d'erreur si le fichier CSV n'existe pas
        print("Error: CSV file not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")  # Affiche tout autre type d'erreur
        return False
