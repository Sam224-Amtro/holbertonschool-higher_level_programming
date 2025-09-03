#!/usr/bin/python3
# On démarre une boucle qui parcourt les nombres de 0 à 99
for i in range(100):
    # Si le nombre n’est pas encore 99 (c’est-à-dire pas le dernier)
    if i < 99:
        # On affiche le nombre sur deux chiffres, suivi de ", "
        # end="" permet de rester sur la même ligne
        print(f"{i:02d}, ", end="")
    else:
        # Si c’est le dernier nombre (99), on l’affiche
        # mais sans ajouter de virgule à la fin
        print(f"{i:02d}")
