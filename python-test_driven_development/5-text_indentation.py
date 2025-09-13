#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string): contient un texte

    Raises:
        TypeError: le texte doit être de type string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    caractere = ""

    for char in text:
        caractere += char

        if char in '.?:':
            print(caractere.strip(), end="\n\n")
            caractere = ""

    if caractere:
        print(caractere.strip())
