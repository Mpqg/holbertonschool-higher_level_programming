#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], database=argv[3], charset="utf8")
states = database.states()
states.execute("SELECT * FROM states ORDER id ASC")
rows = states.fetchall()
for row in rows:
    print(row)
states.close()
database.close()