#!/usr/bin/python3
"""Class Student"""

# Définition d'une classe "Student" qui représente un étudiant
class Student:
    def __init__(self, first_name, last_name, age):
        """
        Constructeur de la classe Student.
        Initialise les attributs publics :
        - first_name : prénom de l'étudiant
        - last_name  : nom de l'étudiant
        - age        : âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne une représentation sous forme de dictionnaire
        des attributs de l'objet Student.

        - Si attrs est une liste de chaînes de caractères, on ne
          retourne que les attributs dont les noms figurent dans
          cette liste (et qui existent vraiment dans l'objet).

        - Si attrs est None (valeur par défaut), on retourne
          tous les attributs de l'objet (équivalent à __dict__).
        """
        if isinstance(attrs, list):
            # On construit un dictionnaire avec uniquement les
            # attributs demandés et existants
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        # Sinon, on retourne directement tout le dictionnaire des attributs
        return self.__dict__
