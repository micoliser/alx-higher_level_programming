#!/usr/bin/python3
"""
    This module lists all cities from the
    database hbtn_0e_4_usa based on user input
"""

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
    cur.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name = '{}';
        """.format(sys.argv[4]))

    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))
