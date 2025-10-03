#!/usr/bin/python3

import pickle

class customObjet:
    def __init__(self, name, age, is_student):
        """
        Initialisez le CustomObject avec les attributs nom, âge et est_étudiant.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")
    def serialize(self, flamme: str):
        """Serialize this objet"""
        try:
            with open(flamme, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization Error: {e}")
    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize this objet"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization Error: {e}")
            return None
