#!/usr/bin/env python3
# Cette ligne spéciale (shebang) indique quel interpréteur utiliser.
# Ici, on dit au système d’exécuter le script avec Python 3.
# (Utile surtout sous Linux/Mac, pas nécessaire sous Windows.)


class CountedIterator:
    # Définition d'une classe qui va compter combien d'éléments on a parcourus

    def __init__(self, iterable):
        # Le constructeur prend en paramètre un objet itérable
        # (ex: liste, tuple, etc.)

        # On transforme l'itérable en véritable itérateur
        self.iterator = iter(iterable)
        self.count = 0  # Compteur initialisé à 0

        def __iter__(self):
            # Cette méthode rend l'objet "itérable".
            # Elle doit retourner un itérateur (ici : l'objet lui-même).
            return self

        def __next__(self):
            # Cette méthode définit le comportement à chaque "next()"
            item = next(self.iterator)  # Récupère le prochain élément
            self.count += 1  # Incrémente le compteur
            return item  # Retourne l'élément

        def get_count(self):
            # Méthode pour récupérer la valeur du compteur
            return self.count
