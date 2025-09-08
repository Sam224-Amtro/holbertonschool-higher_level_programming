#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    liste_vide = []

    for k in my_list:
        if k % 2 == 0:
            liste_vide.append(True)
        else:
            liste_vide.append(False)
    return (liste_vide)
