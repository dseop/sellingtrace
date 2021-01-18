import sqlite3
import pandas as pd

def open_db() :
    con = sqlite3.connect("rank_DB.db")
    c = con.cursor()
    return con, c

def close_db(con) :
    con.commit()
    con.close()

con, c = open_db()

c.execute("CREATE TABLE rank_table('rank' int, code int, today text)")

c.execute("INSERT INTO test VALUES('title1', 10, 'no data', 'auth1')")
c.execute("SELECT * FROM test")
c.fetchone()
c.fetchall()

