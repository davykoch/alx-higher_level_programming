#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT cities.name FROM cities \
             LEFT JOIN states \
			 ON states_id = cities.state_id \
             WHERE states.name LIKE BINARY %s \
             ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    if rows:
        cities = ', '.join(row[0] for row in rows)
        print(cities)

    cursor.close()
    db.close()
