#!/usr/bin/python3
import random # On importe le module random pour générer un nombre aléatoire
number = random.randint(-10000, 10000) # Génère un nombre aléatoire entre -10000 et 10000

lastdigit = number % -10 if number < 0 else number % 10
# Si le nombre est négatif → on prend number % -10 (donne un dernier chiffre négatif)
# Sinon → on prend number % 10 (dernier chiffre positif)

str = "Last digit of" # Stocke le début du message à afficher

if lastdigit > 5: # Si le dernier chiffre est supérieur à 5
    print(f"{str} {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0: # Si le dernier chiffre est égal à 0
    print(f"{str} {number} is {lastdigit} and is 0")
else: # Sinon (dernier chiffre < 6 et ≠ 0)
    print(f"{str} {number} is {lastdigit} and is less than 6 and not 0")
