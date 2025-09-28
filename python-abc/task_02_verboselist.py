#!/usr/bin/env python3

class VerboseList(list):
    """
    Classe qui fonctionne comme une liste normale,
    mais qui affiche un message à chaque ajout ou suppression d'élément.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste et affiche un message.

        Args:
            item: L'élément qu'on veut ajouter.
        """
        super().append(item)  # on utilise append de la classe list
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Ajoute plusieurs éléments d'un coup à la liste et affiche un message.

        Args:
            items: Une séquence (liste, tuple, etc.) d’éléments à ajouter.
        """
        super().extend(items)  # on utilise extend de la classe list
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Supprime la première occurrence d’un élément de la liste
        et affiche un message.

        Args:
            item: L’élément qu’on veut enlever.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)  # on utilise remove de la classe list

    def pop(self, index=-1):
        """
        Supprime et renvoie un élément de la liste à une position donnée.
        Si aucun index n’est donné, supprime le dernier élément.

        Args:
            index (int): Position de l’élément à supprimer
            (par défaut -1 = dernier).

        Returns:
            L’élément qui a été supprimé.
        """
        item = super().pop(index)  # on utilise pop de la classe list
        print(f"Popped [{item}] from the list.")
        return item
