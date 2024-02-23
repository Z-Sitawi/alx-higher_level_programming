#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
Usage: ./program.py <mysql username> <mysql password> <database name> <state name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT DISTINCT cities.name FROM cities "
              "INNER JOIN states ON cities.state_id = states.id "
              "WHERE states.name = 'Texas'")
    [print(city) for city in c.fetchall()]
