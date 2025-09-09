#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Crée une nouvelle liste
    new_list = []

    # On parcourt chaque élément de la liste d'origine
    for element in my_list:
        if element == search:
            # si l'élément est égal à "search", on met "replace"
            new_list.append(replace)
        else:
            # sinon on garde l'élément tel quel
            new_list.append(element)

    return new_list # on retourne la nouvelle liste
