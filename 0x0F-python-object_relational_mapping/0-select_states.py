#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa:
takes 3 arguments:mysql username, mysql password and database name
"""
import MySQLdb
import sys


if __name__ == "main":
    db_name = input("Enter database name: ")
    user = input("Enter username: ")
    password = input("Enter password: ")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cursor.fetchall()

    cursor.close()
    db.close()
