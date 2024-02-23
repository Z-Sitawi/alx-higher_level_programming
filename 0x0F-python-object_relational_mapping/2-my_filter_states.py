#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the 4th argument.
Usage: ./program.py <mysql username> <mysql password> <database name>
<state name searched>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` "
              "WHERE BINARY `name` = '{}' ORDER BY `id`".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        print(state)
