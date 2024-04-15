#!/usr/bin/python3

""" Filter states by name """

import MySQLdb
import sys


def filter_states(username, password, db_name, state_name):
    """ Connects to the database and selects states matching the given name """
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
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username>\
                <password> <db_name> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]
    filter_states(username, password, db_name, state_name)
