#!/usr/bin/env python3
# Shebang : utile sous Linux/Mac pour lancer directement le script avec Python 3

class CountedIterator:
    # Classe qui permet d’itérer en comptant combien d’éléments on parcourt

    def __init__(self, iterable):
        # On transforme l’itérable en itérateur
        self.iterator = iter(iterable)
        self.count = 0  # Compteur initialisé à 0

    def __iter__(self):
        # L’objet est lui-même un itérateur
        return self

    def __next__(self):
        # Retourne l’élément suivant et incrémente le compteur
        item = next(self.iterator)  # Peut lever StopIteration quand fini
        self.count += 1
        return item

    def get_count(self):
        # Retourne combien d’éléments ont été parcourus
        return self.count
