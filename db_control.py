import sqlite3
import pandas as pd
from pandas import DataFrame as df

con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def get_table_list() :
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_list =[]
    temp_list = c.fetchall()
    for i in temp_list :
        table_list.append(i[0])
    return table_list

def check_table_list(table_name) :
    c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name="+"'"+table_name+"'")
    check = c.fetchall()
    check = check[0][0]
    print(table_name+": ", check)
    return check


def create_table(count_check, table_name) : 
    if count_check == 0 :
        c.execute("CREATE TABLE "+table_name+"('rank_num' int, 'code' int, 'today' text)")


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

def search(keyword) :
    c.execute("select book_table.code, book_table.title from book_table \
                where book_table.title like '% {} %';")
    data = c.fetchall()
    print(data)
    return data

# keyword = "무작정 따라하기" 
# sql = "select book_table.code, book_table.title, rank_economy.rank, rank_economy.today from book_table \
# join rank_economy on book_table.code = rank_economy.code \
# where book_table.title like '%{}%'\
# order by book_table.code;".format(keyword)

# c.execute(sql)
# data = c.fetchall()

rank_humanities = pd.read_sql_query("select * from rank_humanities", con)
rank_ebiz = pd.read_sql_query("select * from rank_ebiz", con)
# print(len(rank_ebiz.code))
rank_economy = pd.read_sql_query("select * from rank_economy", con)
# rank_economy['code'] = rank_economy['code'].apply('str') 
# rank_economy['rank_num'] = rank_economy['rank_num'].apply('str') 


book = pd.read_sql_query("select * from book_table", con)
# book['code'] = book['code'].apply('str')

new_df = pd.merge(rank_economy, book, on='code', how='left')
# print(len(new_df.code))
 
print("[", pd.unique(new_df.today)[0],"~",pd.unique(new_df.today)[-1],"]")

# 오늘자 베스트 검색 
today = pd.Timestamp.today().strftime("%Y-%m-%d")
print("today:", today)
today_df = new_df[new_df['today'] == today]
print("today's data:", today_df)

# 키워드로 검색
print("<제목 검색 결과>")
keyword = "무작정 따라하기" 
search_df = new_df[new_df['title'].str.contains(keyword, regex=False)]
print(search_df.sort_values('code'))

# 특정 코드 뽑아보기
code = 85156209, 45008491
# spec_df = search_df.where(search_df['code'] == code)
for c in code :
    spec_df = new_df[new_df["code"] == c]
    print(pd.unique(spec_df.title))
    print(spec_df)


con.close()

'''
select date('now','-1 month') as before_1_month ; # 오늘부터 한 달 전
select * from rank_economy join book_table on rank_economy.code = book_table.code;


select code, title from book_table where title like '%무작정 따라하기%';
join rank_economy on book_table.code = rank_economy.code;

.open rank_DB.db
.headers on # 컬럼 제목 함께 보이게 하려면
.schema # 스키마 전체 보기


# 무작정 따라하기 이름을 가진 애들 골라서 rank join 하는 것까지 완료
query = """
select book_table.code, book_table.title, rank_economy.rank, rank_economy.today from book_table 
join rank_economy on book_table.code = rank_economy.code
where book_table.title like '%무작정 따라하기%'
order by book_table.code;

select book_table.code, book_table.title, rank_economy.rank, rank_economy.today from book_table 
join rank_economy on book_table.code = rank_economy.code
where book_table.code like '%aaaaaaaaaaaaaaaa%'
order by book_table.code;

select book_table.title, rank_economy.rank from book_table
join rank_economy on book_table.code = rank_economy.code
where book_table.title like '%무작정 따라하기%';

group by book_table.title

select book_table.code, book_table.title, rank_economy.rank, rank_economy.today from book_table 
join rank_economy on book_table.code = rank_economy.code

select rank_economy.code, rank_economy.rank, rank_economy.today from rank_economy 
group by rank_economy.code;
"""

select * from rank_economy join book_table on rank_economy.code = book_table.code where rank < 20 and today = '2021-1-22';

'''