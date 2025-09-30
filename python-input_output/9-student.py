#!/usr/bin/python3
"""Class pour Student"""

class Student:
    def __init__(self, first_name, last_name, age):
        """Initialisation de l'etudiant"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        Retourne un dictionnaire contenant les informations de l'étudiant
        """
        return self.__dict__
