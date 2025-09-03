#!/usr/bin/python3

# Définition de la fonction fizzbuzz
def fizzbuzz():
    # On parcourt les nombres de 1 à 100 inclus
    for i in range(1, 101):
        # Si le nombre est divisible à la fois par 3 et par 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        # Sinon si le nombre est divisible seulement par 3
        elif i % 3 == 0:
            print("Fizz ", end="")
        # Sinon si le nombre est divisible seulement par 5
        elif i % 5 == 0:
            print("Buzz ", end="")
        # Sinon, on affiche simplement le nombre
        else:
            print(i, end=" ")
