#!/usr/bin/python3
"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database 
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

dbconfig = {'user':'mySQL_u', 'passwd':'mySQL_p', 'db' :'db_name'}

conn = MySQLdb.connect(**dbconfig)
 cur = conn.cursor()
sql_code = """SELECT * FROM states ORDER BY id"""

    cur.execute(sql_code)
    rows = cur.fetchall()

    for row in rows:
        print(row)
