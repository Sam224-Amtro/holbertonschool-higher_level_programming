#!/usr/bin/python3
"""Liste tous les enregistrements d'un état dans la base de données"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cur = db.cursor()  # Création du curseur pour exécuter des requêtes

    # Exécution de la requête pour récupérer l'état passé en argument
    cur.execute("""SELECT *
                   FROM states
                   WHERE name = %(state)s
                   ORDER BY id ASC""", {'state': argv[4]})

    rows = cur.fetchall()  # Récupère toutes les lignes

    # Affiche les lignes correspondant exactement au nom de l'état
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
