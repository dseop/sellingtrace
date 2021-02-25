from tabulate import tabulate
import sqlite3
import pandas as pd
from pandas import DataFrame as df

# DB connect    
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def print__(df) : # https://pypi.org/project/tabulate/
    print(tabulate(df, headers='keys', showindex=False, tablefmt='plain'))
    return 0

def print_(df) : # https://pypi.org/project/tabulate/
    print(tabulate(df[['rank_var', 'rank_num', 'title_main']], headers='keys', showindex=False, tablefmt='plain'))
    # rank_num, code, collect_date, rank_var, title, au, pu, price, title_main
    return 0

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

# rank_economy rank_economy_invest rank_economy_ebiz rank_humanities
table_name = "rank_economy"

if table_name == "rank_economy" : rank_df = pd.read_sql_query("select * from rank_economy", con)
elif table_name == "rank_economy_invest" : rank_df = pd.read_sql_query("select * from rank_economy_invest", con)
elif table_name == "rank_economy_ebiz" : rank_df = pd.read_sql_query("select * from rank_economy_ebiz", con)
elif table_name == "rank_humanities" : rank_df = pd.read_sql_query("select * from rank_humanities", con)

book = pd.read_sql_query("select * from book_table", con)
rank_df = pd.merge(rank_df, book, on='code', how='left') # rank_table + book_table
rank_df['title_main']  = rank_df['title'].str.split(' : ').str[0] # title_main is 제목, title = 제목+부제
# print(rank_df.dtypes)

print("수집 기간 [ {0} ~ {1} ] / 데이터 길이 [ {2} ]\n".format(\
    pd.unique(rank_df.collect_date)[0], pd.unique(rank_df.collect_date)[-1], len(rank_df.code)))

# set_date_range # 
start_date = '2021-01'
end_date = '2029-02-25'
print("# 데이터 범위 설정 [ {0} ~ {1} ]\n".format(start_date,end_date))
rank_df = rank_df[(rank_df['collect_date'] >= start_date) & (rank_df['collect_date'] <= end_date)]

# last day's best #
last_day = rank_df['collect_date'].unique()[-1] # .unique -> type 'numpy.ndarray' 
# last_day = rank_df.iloc[-1]['collect_date']
last_day_df = rank_df[(rank_df['collect_date'] == last_day)]

# view better : use tabulate #
switch = 1
if switch == 1 :
    top = 100
    move = 5

    print("# {0} 기준".format(last_day))
    up_var_df = last_day_df[(last_day_df['rank_var'] >= move) & (last_day_df['rank_num'] <= top)]
    print("\n▼ {0}위 이상 올라간 책: {1}개".format(move,len(up_var_df)))
    print__(up_var_df[['rank_var', 'rank_num', 'publish_date', 'code', 'title_main']].sort_values(by=['rank_var'],ascending=False))

    down_var_df = last_day_df[(last_day_df['rank_var'] <= -move) & (last_day_df['rank_num'] <= top)]
    print("\n▼ {0}위 이상 내려간 책: {1}개".format(-move,len(down_var_df)))
    print__(down_var_df[['rank_num', 'rank_var', 'title_main']])

# searching keyword #
keyword = "ETF 투자 무작정 따라하기"
code = 97176348

if code != None :
    print("\n▼ 코드 검색 결과 : {0} {1}".format(code, rank_df[(rank_df['code'] == code)]['title_main'].unique()))
    print__(rank_df[(rank_df['code'] == code)][['collect_date', 'rank_num', 'rank_var']])

switch = 1
if switch == 1 :
    search_df_title = last_day_df[last_day_df['title'].str.contains(keyword, regex=False)] # search keyword from today's data
    if len(search_df_title) != 0 : 
        print("\n▼ 제목 검색 결과 : {0}".format(keyword))
        print__(search_df_title[['collect_date','rank_num', 'code', 'au', 'pu', 'price']]) # type(search_df) = df

    search_df_au = last_day_df[last_day_df['au'].str.contains(keyword, regex=False)] # search keyword from today's data
    if len(search_df_au) != 0 :
        print("▼ 저자명 검색 결과 : {0}".format(keyword))
        print(search_df_au)
    
    search_df = rank_df[rank_df['title'].str.contains(keyword, regex=False)] # search keyword
    print("\n▼ 순위 변화")
    print__(search_df[['collect_date', 'rank_num', 'rank_var']])
        
elif switch == 2 :
    # 검색 결과에서 코드 뽑아버리기
    code_list = list(search_df['code'])
    print(code_list)

    # 특정 코드 뽑아서 비교하기
    code = code_list # [88406526] # 85156209 주식투자 무따기
    # spec_df = search_df.where(search_df['code'] == code)
    for c in code :
        spec_df = rank_df[rank_df["code"] == c]
        print(spec_df.title_main.unique())
        rank_list = list(spec_df.rank_num)
        # # type(spec_df.rank_num[72]) # <class 'numpy.int64'>
        # # type(rank_list[0]) # int
        sub_list = [0]
        for i in range(len(rank_list)-1) :
            sub_list.append(rank_list[i]-rank_list[i+1])
        spec_df.loc[:,('sub')] = sub_list
        print(spec_df.loc[:,['collect_date', 'rank_num', 'sub']])

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