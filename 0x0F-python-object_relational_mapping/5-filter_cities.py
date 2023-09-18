#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Lists all cities of a specific state from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(state_name)s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, {'state_name': state_name})

    cities = cursor.fetchone()[0]

    if cities:
        print(cities)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(username, password, database, state_name)
