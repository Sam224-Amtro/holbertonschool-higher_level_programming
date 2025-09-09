#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # crée un nouveau dictionnaire vide
    new_dictionary = {}

    # parcourt chaque clé du dictionnaire
    for key in a_dictionary:
        # multiplie chaque valeur par 2
        new_dictionary[key] = a_dictionary[key] * 2

    # retourne le nouveau dictionnaire
    return new_dictionary
