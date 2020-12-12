#!/usr/bin/python3
""" Task 3 """
import MySQLdb
from sys import argv


def Task3():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    point = db.cursor()
    point.execute("SELECT * from states WHERE name LIKE %s\
            ORDER BY states.id", str(argv[4]))
    for state in point.fetchall():
        print(state)
    point.close()
    db.close()

if __name__ == "__main__":
    Task3()
