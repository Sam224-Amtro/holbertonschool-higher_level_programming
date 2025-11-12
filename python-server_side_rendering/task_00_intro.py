import os

def generate_invitations(template: str, attendees: list, output_dir="invitations"):
    # --- Validation des entrées ---
    if not isinstance(template, str):
        raise TypeError("Le modèle (template) doit être une chaîne de caractères.")
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Les invités (attendees) doivent être une liste de dictionnaires.")
    if not template.strip():
        print("⚠️  Le modèle est vide, aucun fichier généré.")
        return
    if not attendees:
        print("⚠️  Aucun invité fourni, aucun fichier généré.")
        return

    # --- Création du dossier de sortie ---
    os.makedirs(output_dir, exist_ok=True)

    # --- Génération des invitations ---
    for i, attendee in enumerate(attendees, start=1):
        # Fournit des valeurs par défaut "N/A" pour les clés manquantes
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }

        try:
            invitation_text = template.format(**data)
        except KeyError as e:
            print(f"⚠️  Clé manquante dans le modèle : {e}")
            continue

        # Écriture du fichier
        output_file = os.path.join(output_dir, f"invitation_{i}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(invitation_text)

        print(f"✅ Invitation générée : {output_file}")
