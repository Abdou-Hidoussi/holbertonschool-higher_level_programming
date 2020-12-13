#!/usr/bin/python3
""" Task 5 """
import MySQLdb
from sys import argv


def Task5():
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    point = db.cursor()
    point.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4], ))
    ls = []
    for cities in point.fetchall():
        for name in cities:
            ls.append(name)
    print(', '.join(ls))
    point.close()
    db.close()

if __name__ == "__main__":
    Task5()
