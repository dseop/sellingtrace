from tabulate import tabulate
import sqlite3
import pandas as pd
from pandas import DataFrame as df
import connect_sheet as cs

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

# rank_economy rank_economy_invest rank_economy_ebiz rank_humanities
table_name = "rank_economy"

if table_name == "rank_economy" : rank_df = pd.read_sql_query("select * from rank_economy", con)
elif table_name == "rank_economy_invest" : rank_df = pd.read_sql_query("select * from rank_economy_invest", con)
elif table_name == "rank_economy_ebiz" : rank_df = pd.read_sql_query("select * from rank_economy_ebiz", con)
elif table_name == "rank_humanities" : rank_df = pd.read_sql_query("select * from rank_humanities", con)

book_df = pd.read_sql_query("select * from book_table", con)
rank_df = pd.merge(rank_df, book_df, on='code', how='left') # rank_table + book_table
# rank_num, code, collect_date, rank_var, title, au, pu, price, title_main, remarked
rank_df['title_main']  = rank_df['title'].str.split(' : ').str[0] # title_main is 제목, title = 제목+부제
# print(rank_df.dtypes)

print("수집 기간 [ {0} ~ {1} ] / 데이터 길이 [ {2} ]\n".format(\
    pd.unique(rank_df.collect_date)[0], pd.unique(rank_df.collect_date)[-1], len(rank_df.code)))

# set_date_range # 
start_date = '2021-03'
end_date = '2029-02-25'
print("# 데이터 범위 설정 [ {0} ~ {1} ]".format(start_date,end_date))
rank_df = rank_df[(rank_df['collect_date'] >= start_date) & (rank_df['collect_date'] <= end_date)]

# last day's best #
last_day = rank_df['collect_date'].unique()[-1] # .unique -> type 'numpy.ndarray' 

# view better : use tabulate #
switch = 0
if switch == 1 :
    var_setting = (100, 5) # range, var size
    sort = 'rank_num' # sort = 'rank_num' 'rank_var'
    # asc = True # False True
    last_day_df = rank_df[(rank_df['collect_date'] == last_day)]
    print("\n# {0} 기준".format(last_day))
    var_df = last_day_df[(last_day_df['rank_var'] >= var_setting[1]) & (last_day_df['rank_num'] <= var_setting[0])]
    print("\n▼ {0}위 이상 올라간 책: {1}개".format(var_setting[1],len(var_df)))
    print__(var_df[['rank_num', 'rank_var', 'publish_date', 'code', 'title_main']].sort_values(by=[sort],ascending=True))
    # rank down list
    var_df = last_day_df[(last_day_df['rank_var'] <= -var_setting[1]) & (last_day_df['rank_num'] <= var_setting[0])]
    print("\n▼ {0}위 이상 내려간 책: {1}개".format(-var_setting[1],len(var_df)))
    print__(var_df[['rank_num', 'rank_var', 'publish_date', 'code', 'title_main']].sort_values(by=[sort],ascending=True))

if switch == 2 : # last_day
    last_day_df = rank_df[(rank_df['collect_date'] == last_day)]
    print("\n# {0} 기준".format(last_day))
    print__(last_day_df[['rank_num', 'rank_var', 'code', 'title_main']].sort_values(by=['rank_num'],ascending=True))

specific_day = "2021-03-13"
if switch == 3 :
    specific_day_df = rank_df[(rank_df['collect_date'] == specific_day)]
    print("\n# {0} 기준".format(specific_day))
    print__(specific_day_df[['rank_num', 'rank_var', 'code', 'title_main']].sort_values(by=['rank_num'],ascending=True))

# book check #
switch = 0
if switch == 1 : # use if specific code 
    code = 98195271                      
    if code != None :
        url = "http://www.yes24.com/Product/Goods/{0}".format(code)
        title = rank_df[(rank_df['code'] == code)]['title_main'].unique()[0]
        
        # spreadsheet #
        # doc = cs.open_sheet("https://docs.google.com/spreadsheets/d/1f2yScTn1L3POs3slWOkV_QEZoNClrSypUA4roQOl5Gs/edit#gid=0")
        # worksheet = doc.worksheet(table_name)
        # code_list = list(map(int, worksheet.col_values(1)))
        # if code not in code_list :
        #     worksheet.append_row((code, title, url, pd.Timestamp.today()))

        print("\n▼ 코드 검색 결과 : {0} | {1} | {2}".format(code, title, url))
        print__(rank_df[(rank_df['code'] == code)][['collect_date', 'rank_num', 'rank_var']])

        c.execute("UPDATE book_table SET remarked = 1 WHERE code = {0}".format(code))
        c.execute("INSERT OR REPLACE INTO remarked_list VALUES(?,?)", (code, table_name))

        # c.execute("CREATE TABLE book_table('code' int PRIMARY KEY, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text, 'remarked' int)")
        
# delete remarked
if switch == 2 : 
    c.execute("UPDATE book_table SET remarked = 0 WHERE code = {0}".format(code))

# remarked list / view all #
switch = 0
if switch == 1 : # list up
    print("\n▼ 마크된 책 리스트")
    for code in list(book_df[(book_df['remarked'] == 1)]['code']) :
        title = rank_df[(rank_df['code'] == code)]['title_main'].unique()[0]
        print("\n[{0}] {2}\nhttp://www.yes24.com/Product/Goods/{1}\n-".format(code, code, title))
        print__(rank_df[(rank_df['code'] == code)][['collect_date', 'rank_num', 'rank_var']])
    
    # second way for exporting remarked codes
    c.execute("SELECT code FROM remarked_list")
    code_list = c.fetchall()
    for code in code_list :
        code = code[0]
        # print(code)
    
# searching keyword # 수정 많이 필요함
title_keyword = ""
if title_keyword != "" :
    search_df_title = rank_df[rank_df['title'].str.contains(title_keyword, regex=False)] # search keyword from today's data
    if len(search_df_title) != 0 : 
        print("\n▼ 제목 검색 결과 : {0}".format(title_keyword))
        print__(search_df_title[['collect_date','rank_num', 'code', 'au', 'pu', 'price']]) # type(search_df) = df

author_keyword = "박희용"
if author_keyword != "" :
    search_df_au = rank_df[rank_df['au'].str.contains(author_keyword, regex=False)] # search keyword from today's data
    if len(search_df_au) != 0 :
        print("\n▼ 저자명 검색 결과 : {0}".format(author_keyword))
        code_list = list(search_df_au['code'].unique())
        for code in code_list :
            title = search_df_au[(search_df_au['code'] == code)]['title_main'].unique()[0]
            print("\n[{0}] {2}\nhttp://www.yes24.com/Product/Goods/{1}\n-".format(code, code, title))
            print__(search_df_au[(search_df_au['code'] == code)][['collect_date', 'rank_num', 'rank_var']])
        
if switch == 2 :
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


con.commit()
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