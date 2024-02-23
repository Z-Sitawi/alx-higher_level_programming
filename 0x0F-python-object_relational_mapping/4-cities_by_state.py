#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
Usage: ./program.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities "
              "INNER JOIN states ON cities.state_id = state.id "
              "ORDER BY cities.id")
    [print(city) for city in c.fetchall()]
