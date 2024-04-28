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
    mySQL_usr = sys.argv[1]
    mySQL_pwd = sys.argv[2]
    db_name = sys.argv[3]



conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8", user=mySQL_usr, passwd=mySQL_pwd, db=db_name)
cursor = conn.cursor()
conn.commit()

sq_code = """SELECT * FROM states ORDER BY id ASC"""
cursor.execute(sq_code)
rows = cur.fetchall()

for row in rows:
     print(row)
cursor.close()
conn.close()
