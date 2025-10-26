#!/usr/bin/python3
"""Module listing all cities from the state passed in argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution de la requête SQL (avec JOIN au lieu de sous-requête)
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %(state)s
        ORDER BY cities.id ASC;
    """, {"state": argv[4]})

    # Récupération et affichage des résultats
    rows = [row[0] for row in cur.fetchall()]
    print(', '.join(rows))

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
