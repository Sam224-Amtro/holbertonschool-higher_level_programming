#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # supprime la clé si elle existe dans le dictionnaire
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
