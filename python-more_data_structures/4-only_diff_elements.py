#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # renvoie les éléments qui sont dans set_1 OU dans set_2
    # mais pas dans les deux en même temps
    return set_1.symmetric_difference(set_2)
