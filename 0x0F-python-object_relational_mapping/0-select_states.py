#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa:
"""

if __name__ == '__main__':
    """ Module to select states"""
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id ASC"

    cursor.execute(sql)
    rows = cursor.fetchall()

    for i in rows:
        print(i)
