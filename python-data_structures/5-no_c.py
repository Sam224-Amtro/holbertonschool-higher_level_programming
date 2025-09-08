#!/usr/bin/python3

def no_c(my_string):
    # Créez une nouvelle chaîne en itérant à travers la chaîne d'origine
    # et incluant uniquement des personnages qui ne sont pas «C» ou «C»
    new_string = ""
    for alphabet in my_string:
        if alphabet != 'c' and alphabet != 'c':
            new_string += alphabet
    return new_string
