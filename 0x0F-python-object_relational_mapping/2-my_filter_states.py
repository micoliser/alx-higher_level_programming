#!/usr/bin/python3
"""
    This module filters states from the database
    hbtn_0e_0_usa with name starting with user input argv4
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
            *
        FROM
            states
        WHERE CONVERT
            (`name` USING Latin1)
        COLLATE
            Latin1_General_CS = '{}';
        """.format(sys.argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)
