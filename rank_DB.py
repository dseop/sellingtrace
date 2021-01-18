con, c = open_db()

c.execute("CREATE TABLE rank_table('rank' int, code int, today text)")

c.execute("INSERT INTO test VALUES('title1', 10, 'no data', 'auth1')")
c.execute("SELECT * FROM test")
c.fetchone()
c.fetchall()

import sqlite3
con = sqlite3.connect("rank_DB.db")
c = con.cursor()
c.execute("SELECT * FROM rank_table")
c.fetchall()