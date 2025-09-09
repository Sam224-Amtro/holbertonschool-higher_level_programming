#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # parcourt les clés triées du dictionnaire et affiche clé: valeur
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
