#!/usr/bin/python3

def safe_print_integer(value):
    """
    Essaie d'imprimer la valeur passée en argument comme un entier.
    Retourne True si l'impression réussit, False sinon.
    """
    try:
        # Tente de formater et d'imprimer la valeur en tant qu'entier
        print("{:d}".format(value))
        # Si cela réussit, on retourne True
        return True
    except (ValueError, TypeError):
        # Si la valeur n'est pas un entier ou ne peut pas être formatée
        # on attrape l'exception et on retourne False
        return False
