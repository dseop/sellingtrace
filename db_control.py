import sqlite3
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def get_table_list() :
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_list =[]
    temp_list = c.fetchall()
    for i in temp_list :
        table_list.append(i[0])
    return table_list

table_list = get_table_list()


def check_table_list(table_name) :
    c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name="+"'"+table_name+"'")
    check = c.fetchall()
    check = check[0][0]
    print(table_name+": ", check)
    return check


def create_table(count_check, table_name) : 
    if count_check == 0 :
        c.execute("CREATE TABLE "+table_name+"('rank' int, 'code' int, 'today' text)")


def insert_data(table_name) :
    insert_rank_sql = "INSERT INTO "+table_name+" VALUES (?,?,?)"
    c.executemany(insert_rank_sql, rank_db_list)


def check_table(table_name) :
    c.execute("SELECT * FROM "+table_name)
    check = c.fetchall()
    print(len(check))

def get_table(table_name) :
    c.execute("SELECT * FROM "+table_name)
    data = c.fetchall()
    return data


'''
select date('now','-1 month') as before_1_month ; # 오늘부터 한 달 전
select * from rank_table_economy join book_table on rank_table_economy.code = book_table.code;
'''

select code, title from book_table where title like '%무작정 따라하기%';
join rank_table_economy on book_table.code = rank_table_economy.code;

# 컬럼 제목 함께 보이게 하려면
.headers on

# 스키마 전체 보기
.schema

# 무작정 따라하기 이름을 가진 애들 골라서 rank join 하는 것까지 완료
query = """select book_table.code, book_table.title, rank_table_economy.rank 
from book_table join rank_table_economy on book_table.code = rank_table_economy.code 
where book_table.title like '%무작정 따라하기%';
"""

