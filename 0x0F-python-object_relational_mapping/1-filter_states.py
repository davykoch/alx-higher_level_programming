#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
takes 3 arguments: mysql username, mysql password, and database name
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    database = sys.argv[3]
    user = sys.argv[1]
    password = sys.argv[2]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
