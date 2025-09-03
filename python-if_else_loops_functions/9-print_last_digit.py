#!/usr/bin/python3

# Fonction qui affiche et retourne le dernier chiffre d'un nombre
def print_last_digit(number):
    # On prend la valeur absolue (abs) pour gérer aussi les nombres négatifs
    # Puis on fait % 10 pour récupérer uniquement le dernier chiffre
    last_digit = abs(number) % 10

    # On affiche ce dernier chiffre, sans saut de ligne
    print(last_digit, end="")

    # La fonction retourne aussi le dernier chiffre (utile si on veut l'utiliser après)
    return last_digit
