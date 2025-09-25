#!/usr/bin/env python3
# Cette ligne est un *shebang*. Elle permet d'exécuter directement ce script Python
# dans un environnement Unix/Linux en indiquant d'utiliser l’interpréteur python3.

# Définition d'une première classe représentant un poisson
class Fish:
    def swim(self):
        # Méthode qui décrit l’action de nager
        print("The fish is swimming")

    def habitat(self):
        # Méthode qui décrit l’habitat du poisson
        print("The fish lives in water")

# Définition d'une deuxième classe représentant un oiseau
class Bird:
    def fly(self):
        # Méthode qui décrit l’action de voler
        print("The bird is flying")

    def habitat(self):
        # Méthode qui décrit l’habitat de l’oiseau
        print("The bird lives in the sky")


# Définition d'une classe "FlyingFish" (poisson volant)
# Elle hérite de deux classes : Fish et Bird (héritage multiple).
class FlyingFish(Fish, Bird):
    def fly(self):
        # Redéfinition de la méthode fly() héritée de Bird
        # -> Polymorphisme : le comportement est adapté au FlyingFish
        print("The flying fish is soaring!")

    def swim(self):
        # Redéfinition de la méthode swim() héritée de Fish
        print("The flying fish is swimming!")

    def habitat(self):
        # Redéfinition de la méthode habitat() héritée à la fois de Fish et Bird
        # -> Ici, on combine les deux pour refléter la double nature
        # du poisson volant
        print("The flying fish lives both in water and the sky!")
