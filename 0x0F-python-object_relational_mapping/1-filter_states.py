#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_states(username, password, database):
    """
    Lists all states from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database.

    Returns:
        None
    """
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        c = db.cursor()
        c.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY id ASC")
        # Fetch all rows
        states = c.fetchall()
        # Display results
        for state in states:
            print(state)
        c.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> "
              "<database name>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
