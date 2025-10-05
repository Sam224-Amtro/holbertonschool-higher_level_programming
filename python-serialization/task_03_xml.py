#!/usr/bin/python3
"""
Module pour la sérialisation et la désérialisation d'un dictionnaire Python en
format XML

Ce module contient deux fonctions principales :
- serialize_to_xml : Sérialise un dictionnaire Python et l'enregistre dans un
fichier XML
- deserialize_from_xml : Charge et désérialise un fichier XML en un
dictionnaire Python
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en fichier XML

    Args:
        dictionary (dict): Le dictionnaire Python à sérialiser
        filename (str): Le nom du fichier XML où les données
                        seront sauvegardées

    Returns:
        None
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Error serializing object: {e}")


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python

    Args:
        filename (str): Le nom du fichier XML à charger et désérialiser

    Returns:
        dict: Le dictionnaire Python contenant les données désérialisées
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError:
        print(f"Error: The file {filename} is not well-formed.")
        return None
