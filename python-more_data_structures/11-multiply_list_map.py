#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # multiplie chaque élément de la liste par 'number'
    return (list(map(lambda x: x * number, my_list)))
