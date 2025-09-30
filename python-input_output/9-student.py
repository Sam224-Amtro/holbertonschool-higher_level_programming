#!/usr/bin/python3
"""Class pour Student"""

class Student:
    def __init__(self, first_name, last_name, age):
        """Initialisation de student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        Retourne la description de dictionnaire.
        """
        return self.__dict__
