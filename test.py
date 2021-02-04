import sqlite3
import crawling as cr
from datetime import datetime

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

url = ("economy", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80")
now_table = "rank_"+url[0] # str

# def get_table(table_name) :
#     c.execute("SELECT * FROM "+table_name)
#     data = c.fetchall()
#     return data

# db_data = get_table(now_table) 
# print(len(db_data))
# print(db_data[-1])

test_data = (400, 91363446, '2021-02-04')

c.execute("""SELECT * FROM {0} ORDER BY collect_date DESC LIMIT 1""".format(now_table))
data = c.fetchall()
print(data[0][-1])
