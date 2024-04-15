#!/usr/bin/python3

""" Lists all cities from the database """

import MySQLdb
import sys

def list_cities(username, password, db_name):
    """ Connects to the database and lists all cities """
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
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    list_cities(username, password, db_name)
