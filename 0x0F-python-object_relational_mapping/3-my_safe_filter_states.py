#!/usr/bin/python3
"""
This script is safe from MySQL injections:
Displays all values in the states table of hbtn_0e_0_usa
where name matches the 4th argument.
Usage: ./0-select_states.py
Usage: ./program.py <mysql username> <mysql password> <database name>
<state name searched>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute a parameterized query
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    search_query = (sys.argv[4],)
    c.execute(sql_query, search_query)

    states = c.fetchall()
    for state in states:
        print(state)
