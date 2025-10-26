#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa that belong
to the state name passed as argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cur = db.cursor()

    # Execute query with JOIN (recommended and efficient)
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """, (argv[4],))  # ← tuple, pas dict !

    # Fetch and print results
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
