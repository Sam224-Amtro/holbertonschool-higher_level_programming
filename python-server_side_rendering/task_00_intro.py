import os

def generate_invitations(template: str, attendees: list, output_dir="invitations"):
    if not isinstance(template, str):
        raise TypeError("Le modèle (template) doit être une chaîne de caractères.")
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Les invités (attendees) doivent être une liste de dictionnaires.")
    if not template.strip() or not attendees:
        return

    os.makedirs(output_dir, exist_ok=True)

    for i, attendee in enumerate(attendees, start=1):
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }

        try:
            invitation_text = template.format(**data)
        except KeyError:
            continue

        with open(os.path.join(output_dir, f"invitation_{i}.txt"), "w", encoding="utf-8") as f:
            f.write(invitation_text)
