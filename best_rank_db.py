import sqlite3
import test_db_list as tdl

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

# c.execute("CREATE TABLE rank_table('rank' int, code int, today text)")
# c.execute("INSERT INTO test VALUES('title1', 10, 'no data', 'auth1')")

# c.execute("SELECT * FROM test")
# c.fetchall()

c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(c.fetchall())

def check_rte() :
    c.execute("SELECT * FROM rank_table_economy")
    print(c.fetchall())

# print("no rank data table...")
# check_rte()

sql_insert_rank = "INSERT INTO rank_table_economy VALUES (?,?,?)"
c.executemany(sql_insert_rank, tdl.rdl_e)

# print("now? rank data inserted")
# check_rte()

def check_bt() :
    c.execute("SELECT * FROM book_table")
    print(c.fetchall())

# c.execute("CREATE TABLE book_table('code' int, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text)")
# c.execute("""CREATE TABLE book_table(
#     'code' int PRIMARY KEY, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text
# )""")

sql_insert_book = "INSERT INTO book_table VALUES (?,?,?,?,?,?)"
c.executemany(sql_insert_book, tdl.bdl_e)

sql = """INSERT INTO book_table VALUES (?,?,?,?,?,?)
           ON DUPLICATE KEY UPDATE address = VALUES(address)"""

           ########################### 이거 해결해야 함

print("book data table...")
check_bt()

# print("now? book data inserted")
# check_bt()

# c.execute("DROP TABLE book_table")

# con.commit()
con.close()