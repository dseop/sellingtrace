import sqlite3
import test_db_list as tdl
import best_analysis

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def get_table_list() : # show table list
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_list = c.fetchall()
    print(table_list)

get_table_list()

def get_table(table_name) : # get specific table data
    c.execute("SELECT * FROM "+table_name)
    check_data = c.fetchall() # type(check_data) : list
    return check_data

################### make rank table ###################
# c.execute("CREATE TABLE rank_table_economy('rank' int, 'code' int, 'today' text)")
# c.execute("INSERT INTO test VALUES('title1', 10, 'no data', 'auth1')")
#######################################################

# insert_rank_sql = "INSERT INTO rank_table_economy VALUES (?,?,?)"
# c.executemany(insert_rank_sql, tdl.rdl_e)

print("rank data")
check_data = get_table("rank_table_economy")
print(check_data[0:10])
print(len(check_data))

################### make book table ###################
# c.execute("""CREATE TABLE book_table(
#     'code' int PRIMARY KEY, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text
# )""")

# sql_insert_book = "INSERT INTO book_table VALUES (?,?,?,?,?,?)"
# c.executemany(sql_insert_book, tdl.bdl_e)
#######################################################

print("before update book data")
check_data = get_table("book_table")
print(check_data[0:10])
print(len(check_data))

# insert_replace_sql = "INSERT OR REPLACE INTO book_table VALUES (?,?,?,?,?,?)"
# c.executemany(insert_replace_sql, tdl.bdl_e) # collected book data

print("after update book data")
check_data = get_table("book_table")
print(check_data[0:10])
print(len(check_data))

# c.execute("DROP TABLE rank_table_economy")
# "SELECT 컬럼명1, 컬럼명2, ... FROM 테이블명"

# con.commit()
con.close()