#!/usr/bin/env python3
# ↑ Indique à l'interpréteur de lancer ce script avec Python 3

# Définition d'un "mixin" qui ajoute une capacité de nager
class SwimMixin:
    def swim(self):
        # Méthode qui affiche que la créature nage
        print("The creature swims!")

# Définition d'un "mixin" qui ajoute une capacité de voler
class FlyMixin:
    def fly(self):
        # Méthode qui affiche que la créature vole
        print("The creature flies!")

# Classe Dragon qui hérite de SwimMixin et FlyMixin
# → cela permet au dragon de nager ET de voler
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")  # Méthode spécifique au dragon : il rugit
