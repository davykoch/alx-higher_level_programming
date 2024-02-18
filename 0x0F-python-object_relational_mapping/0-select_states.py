#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa:
takes 3 arguments: mysql username, mysql password, and database name
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_name = sys.argv[3]
    user = sys.argv[1]
    password = sys.argv[2]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
