#!/usr/bin/python3

# Définition de la fonction uppercase
def uppercase(str):
    result = "" # on prépare une chaîne vide qui va contenir le résultat final

    # On parcourt chaque caractère de la chaîne donnée en paramètre
    for c in str:
        # Vérifie si le caractère est une lettre minuscule
        if 'a' <= c <= 'z':
            # Si c'est une minuscule, on la convertit en majuscule
            # Comment ? On prend son code ASCII avec ord(), on soustrait 32
            # puis on retransforme en caractère avec chr()
            result += chr(ord(c) - 32)
        else:
            # Si ce n'est pas une minuscule (ex: majuscule, chiffre, espace, accent...),
            # on le laisse tel quel
            result += c
    # On affiche la chaîne finale transformée
    print(result)
