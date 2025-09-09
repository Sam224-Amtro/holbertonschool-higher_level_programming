#!/usr/bin/python3

def best_score(a_dictionary):
    # si le dictionnaire est vide ou None, on retourne None
    if not a_dictionary:
        return None

    # retourne la clé ayant la plus grande valeur
    return max(a_dictionary, key=a_dictionary.get)
