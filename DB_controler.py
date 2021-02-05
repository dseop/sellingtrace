def get_table_list(c) :
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_list =[]
    temp_list = c.fetchall()
    for i in temp_list :
        table_list.append(i[0])
    return table_list
    
def check_table_in_db(c, table_name) :
    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='{0}'""".format(table_name))
    check = c.fetchall()
    count_check = check[0][0] # 있으면 1, 없으면 0
    return count_check

def get_last_date(c, table_name) :
    c.execute("""SELECT * FROM {0} ORDER BY collect_date DESC LIMIT 1""".format(table_name))
    data = c.fetchall()
    return data[0][-1]

def insert_rank_data(c, table_name, db_list) :
    insert_rank_sql = "INSERT INTO {0} VALUES (?,?,?)".format(table_name)
    c.executemany(insert_rank_sql, db_list)

def insert_book_data(c, db_list) :
    insert_book_sql = "INSERT OR REPLACE INTO book_table VALUES (?,?,?,?,?,?)"
    c.executemany(insert_book_sql, db_list)

def get_table(c, table_name) :
    c.execute("SELECT * FROM {0}".format(table_name))
    data = c.fetchall()
    return data