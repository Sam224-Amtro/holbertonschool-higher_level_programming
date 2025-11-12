import os  # Module standard pour manipuler les fichiers et dossiers

def generate_invitations(template: str, attendees: list, output_dir="invitations"):
    """
    Génère des fichiers d'invitation personnalisés à partir d'un modèle de texte.

    Paramètres :
    - template (str) : le modèle de texte contenant des variables comme {name}, {event_title}, etc.
    - attendees (list) : une liste de dictionnaires contenant les informations des invités.
    - output_dir (str) : le nom du dossier où les fichiers seront créés (par défaut : "invitations").
    """

    # --- Étape 1 : Validation des entrées ---
    # Vérifie que le modèle est bien une chaîne de caractères
    if not isinstance(template, str):
        raise TypeError("Le modèle (template) doit être une chaîne de caractères.")

    # Vérifie que attendees est une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Les invités (attendees) doivent être une liste de dictionnaires.")

    # Si le modèle est vide ou la liste d'invités est vide, on ne fait rien
    if not template.strip() or not attendees:
        return  # Rien à générer, on quitte la fonction

    # --- Étape 2 : Création du dossier de sortie ---
    # Crée le dossier s’il n’existe pas encore
    os.makedirs(output_dir, exist_ok=True)

    # --- Étape 3 : Génération des invitations ---
    # On parcourt la liste des invités
    for i, attendee in enumerate(attendees, start=1):
        # Fournit des valeurs par défaut "N/A" pour éviter les erreurs de clé manquante
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }

        try:
            # On remplace les variables {name}, {event_title}, etc. dans le modèle
            invitation_text = template.format(**data)
        except KeyError:
            # Si une clé manque dans le modèle, on passe à l’invité suivant
            continue

        # --- Étape 4 : Écriture du fichier ---
        # Nom du fichier, par exemple "invitation_1.txt"
        output_file = os.path.join(output_dir, f"invitation_{i}.txt")

        # On ouvre le fichier en écriture et on enregistre le texte de l’invitation
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(invitation_text)

    # La fonction ne retourne rien (None par défaut),
    # mais les fichiers sont bien générés dans le dossier choisi.
