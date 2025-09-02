#!/usr/bin/python3

# La boucle for parcourt les nombres de 97 à 122 inclus
# En effet, range(97, 123) génère la séquence 97, 98, ..., 122
for letter in range(97, 123):
    # chr(letter) convertit le code ASCII en caractère correspondant
    # 97 = 'a', 98 = 'b', ..., 122 = 'z'
    # L’argument end='' dans print empêche le saut de ligne automatique
    print(chr(letter), end='')
