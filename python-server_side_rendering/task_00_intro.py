#!/usr/bin/python3
"""
Module task_00_intro

Ce module contient une fonction `generate_invitations`
qui génère des fichiers texte personnalisés à partir d’un modèle
et d’une liste de dictionnaires représentant les invités.
"""

import os

def generate_invitations(template, attendees):
    """
    Génère des invitations à partir d’un modèle texte et d’une liste d'invités.

    Args:
        template (str): Modèle avec les placeholders {name}, {event_title}, {event_date}, {event_location}.
        attendees (list): Liste de dictionnaires contenant les informations des invités.

    Returns:
        None
    """

    # --- Vérification du type de template ---
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    # --- Vérification du type d’attendees ---
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # --- Cas du template vide ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # --- Cas de liste d’invités vide ---
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- Boucle principale : traitement de chaque invité ---
    for i, attendee in enumerate(attendees, start=1):
        # Récupération des données avec valeurs par défaut "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Si une valeur est None, on remplace aussi par "N/A"
        if name is None:
            name = "N/A"
        if event_title is None:
            event_title = "N/A"
        if event_date is None:
            event_date = "N/A"
        if event_location is None:
            event_location = "N/A"

        # Remplacement des placeholders dans le modèle
        content = template.replace("{name}", str(name))
        content = content.replace("{event_title}", str(event_title))
        content = content.replace("{event_date}", str(event_date))
        content = content.replace("{event_location}", str(event_location))

        # Nom du fichier de sortie
        output_filename = f"output_{i}.txt"

        # Écriture du fichier
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
            continue
