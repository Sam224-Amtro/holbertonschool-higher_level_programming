#!/usr/bin/python3
'''Student to JSON'''


# Définition de la classe Student pour représenter un étudiant
class Student:
    """Classe représentant un étudiant avec des attributs de base."""

    def __init__(self, first_name, last_name, age):
        """Constructeur de la classe.

        Args:
            first_name (str): Prénom de l'étudiant
            last_name (str): Nom de l'étudiant
            age (int): Âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Renvoie un dictionnaire représentant l'instance.

        Si 'attrs' est fourni et contient une liste de noms d'attributs,
        seuls ces attributs seront inclus dans le dictionnaire. Sinon,
        tous les attributs de l'objet sont retournés.

        Args:
            attrs (list, optional): Liste de noms d'attributs à inclure.

        Returns:
            dict: Dictionnaire des attributs de l'objet.
        """
        # Vérifie si attrs est une liste de chaînes de caractères
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            # Retourne uniquement les attributs présents dans attrs
            # et existants dans l'objet
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        # Sinon, retourne tous les attributs de l'objet
        return self.__dict__

    def reload_from_json(self, json):
        """Met à jour les attributs de l'objet à partir d'un dictionnaire.

        Args:
            json (dict): Dictionnaire contenant les attributs à mettre à jour
        """
        # Parcourt le dictionnaire et met à jour/ajoute les attributs
        for key, value in json.items():
            setattr(self, key, value)
