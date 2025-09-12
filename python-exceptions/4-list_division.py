#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divise les éléments de deux listes, un par un.
    """
    results = []  # Liste pour stocker les résultats

    for i in range(list_length):  # On parcourt chaque position
        try:
            # On essaie de diviser les deux nombres
            result = my_list_1[i] / my_list_2[i]

        except (TypeError, ValueError):
            # Si ce n'est pas des nombres
            print("wrong type")
            result = 0

        except ZeroDivisionError:
            # Si on divise par 0
            print("division by 0")
            result = 0

        except IndexError:
            # Si on dépasse la taille d'une liste
            print("out of range")
            result = 0

        finally:
            # On ajoute le résultat (ou 0) à la liste
            results.append(result)

    return results  # On renvoie la liste finale
