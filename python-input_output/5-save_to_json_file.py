#!/usr/bin/python3
"""Module pour JSON File"""
import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier texte en utilisant sa représentation JSON.

    Args:
        my_obj: L'objet à sérialiser et à écrire dans le fichier.
        filename: Le nom du fichier dans lequel la représentation
        JSON sera enregistrée.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
