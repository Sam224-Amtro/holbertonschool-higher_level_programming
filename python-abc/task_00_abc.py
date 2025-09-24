#!/usr/bin/python3

# On importe ABC et abstractmethod depuis le module abc
# ABC : permet de créer des classes abstraites
# abstractmethod : permet de définir une méthode abstraite
from abc import ABC, abstractmethod

# Définition d'une classe abstraite Animal
class Animal(ABC):
    # Méthode abstraite : toutes les classes filles doivent l'implémenter
    @abstractmethod
    def sound(self):
        pass  # Ici on ne met rien, car ce sera défini par les sous-classes

# Classe Dog qui hérite de Animal
class Dog(Animal):
    # Implémentation concrète de la méthode sound
    def sound(self):
        return "Bark"

# Classe Cat qui hérite aussi de Animal
class Cat(Animal):
    # Implémentation concrète de la méthode sound
    def sound(self):
        return "Meow"
