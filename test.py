import sqlite3

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
all_table = c.fetchall()
print(all_table)

for i in all_table () :
    