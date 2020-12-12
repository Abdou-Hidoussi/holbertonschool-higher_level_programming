#!/usr/bin/python3
""" Task 0 """
import MySQLdb
import sys

def Task0():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    point = db.cursor()
    point.execute("SELECT * from states ORDER BY id ASC")
    for state in point.fetchall():
        print(state)
    point.close()
    db.close()

if __name__ == "__main__":
    Task0()