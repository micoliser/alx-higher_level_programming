#!/usr/bin/python3
""" This module lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    hb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="{}".format(sys.argv[1]),
            passwd="{}".format(sys.argv[2]),
            db="{}".format(sys.argv[3]))

    cur = hb.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
