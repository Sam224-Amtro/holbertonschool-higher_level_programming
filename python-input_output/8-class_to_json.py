#!/usr/bin/python3
"""Module pour JSON"""
import json


def class_to_json(obj):
    """
    Retourne la description d’un objet sous forme de dictionnaire,
    afin de pouvoir le sérialiser en JSON.

    Arguments :
        obj : Une instance d’une classe avec des attributs sérialisables
              (liste, dictionnaire, chaîne de caractères, entier, booléen).

    Retourne :
        Un dictionnaire contenant tous les attributs sérialisables de l’objet.
    """
    # Utilise l’attribut intégré __dict__ pour récupérer les attributs
    # de l’objet
    # On filtre uniquement les types de base compatibles avec JSON
    if hasattr(obj, "__dict__"):
        return {cle: valeur for cle, valeur in obj.__dict__.items()
                if isinstance(valeur, (list, dict, str, int, bool))}
    else:
        raise TypeError("L’objet fourni ne contient pas d’attributs sérialisables.")
