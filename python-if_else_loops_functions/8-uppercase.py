#!/usr/bin/python3

# Définition de la fonction uppercase
def uppercase(str):
    # On parcourt chaque caractère de la chaîne passée en argument
    for c in str:
        # Vérifie si le caractère est une lettre minuscule
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            # Conversion en majuscule :
            # ord(c) donne le code ASCII de la minuscule
            # on soustrait 32 pour obtenir le code de la majuscule
            # chr() transforme ce code en caractère
            c = chr(ord(c) - 32)

        # Affiche le caractère (modifié ou non) sans retour à la ligne
        print("{}".format(c), end='')

    # Après la boucle, on ajoute un retour à la ligne
    print()
