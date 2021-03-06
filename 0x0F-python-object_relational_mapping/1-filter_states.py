#!/usr/bin/python3
""" Task 1 """
import MySQLdb
from sys import argv


def Task1():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    point = db.cursor()
    point.execute("SELECT * FROM states WHERE name LIKE\
        BINARY 'N%' ORDER BY states.id")
    for state in point.fetchall():
        print(state)
    point.close()
    db.close()

if __name__ == "__main__":
    Task1()
