#!/usr/bin/python3
""" Task 4 """
import MySQLdb
from sys import argv


def Task4():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    point = db.cursor()
    point.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    for state in point.fetchall():
        print(state)
    point.close()
    db.close()

if __name__ == "__main__":
    Task4()
