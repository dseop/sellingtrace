import sqlite3

# DB connect    
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def get_table_list() :
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_list =[]
    temp_list = c.fetchall()
    for i in temp_list :
        table_list.append(i[0])
    return table_list
    
def check_table_in_db(table_name) :
    c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name="+"'"+table_name+"'")
    check = c.fetchall()
    count_check = check[0][0] # 있으면 1, 없으면 0
    print(table_name+": ", count_check)
    return count_check

def check_len_table(table_name) :
    c.execute("SELECT * FROM "+table_name)
    check = c.fetchall()
    print(len(check))

def insert_rank_data(table_name, db_list) :
    insert_rank_sql = "INSERT INTO "+table_name+" VALUES (?,?,?)"
    c.executemany(insert_rank_sql, db_list)

def insert_book_data(table_name, db_list) :
    insert_book_sql = "INSERT OR REPLACE INTO book_table VALUES (?,?,?,?,?,?)"
    c.executemany(insert_book_sql, db_list)

def get_table(table_name) :
    c.execute("SELECT * FROM "+table_name)
    data = c.fetchall()
    return data