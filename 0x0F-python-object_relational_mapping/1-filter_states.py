#!/usr/bin/python3


""" Select states starting with 'N' from database """
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """ Connects to the database and selects
    states starting with 'N' """
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
        cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY id ASC")
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
        print("Usage: ./1-filter_states.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    filter_states(username, password, db_name)
