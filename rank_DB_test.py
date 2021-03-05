import sqlite3
import crawling as cr
import connect_sheet as cs
import DB_controler as dbc
import sys
from datetime import datetime

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

c.execute("SELECT * FROM {0}".format('book_table'))
before_len = len(c.fetchall())
print(before_len)