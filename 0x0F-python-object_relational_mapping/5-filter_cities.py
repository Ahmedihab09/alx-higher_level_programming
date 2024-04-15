#!/usr/bin/python3

""" Filter cities by state name """

import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """ Connects to the database and lists cities of the given state """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            charset="utf8",
            user=username,
            passwd=password,
            db=db_name
        )
        cur = conn.cursor()
        query = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        cur.execute(query, (state_name,))
        query_row = cur.fetchone()
        cities = query_row[0] if query_row else None
        if cities:
            print(cities)
        else:
            print("No cities found for the given state.")
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username>\
                <password> <db_name> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:]
    filter_cities(username, password, db_name, state_name)
