#!/usr/bin/python3

def roman_to_int(roman_string):
    # Vérifier que l'entrée est bien une chaîne de caractères
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Tableau de correspondance chiffres romains → entiers
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Résultat final

    # On parcourt chaque lettre de gauche à droite
    for k in range(len(roman_string)):
        current = values.get(roman_string[k], 0)  # valeur actuelle

        # Si la valeur actuelle est plus petite que la prochaine → on soustrait
        if (k + 1 < len(roman_string) and
                current < values.get(roman_string[k + 1], 0)):
            total -= current
        # Sinon → on additionne
        else:
            total += current

    return total
