#!/usr/bin/python3
"""
Script that takes a state name as an argument
and displays all values in the states table of hbtn_0e_0_usa
where the name matches the argument (safe from SQL injection).
"""

import MySQLdb
import sys


def safe_filter_states_by_name(username, password, database, state_name):
    """
    Displays all values in the states table

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    safe_filter_states_by_name(username, password, database, state_name)
