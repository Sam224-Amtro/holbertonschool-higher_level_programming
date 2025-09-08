#!/usr/bin/python3

def no_c(my_string):
    # Créez une nouvelle chaîne en itérant à travers la chaîne d'origine
    # et incluant uniquement des personnages qui ne sont pas «C» ou «C»
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'c':
            new_string += char
    return new_string
