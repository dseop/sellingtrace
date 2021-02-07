import sqlite3
import pandas as pd
from pandas import DataFrame as df

# DB connect    
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

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
# rank_economy_invest = pd.read_sql_query("select * from rank_economy_invest", con)
# rank_economy_ebiz = pd.read_sql_query("select * from rank_economy_ebiz", con)
# rank_humanities = pd.read_sql_query("select * from rank_humanities", con)

# print(len(rank_economy_ebiz.code))
# rank_df['code'] = rank_df['code'].apply('str') 
# rank_df['rank_num'] = rank_df['rank_num'].apply('str') 

book = pd.read_sql_query("select * from book_table", con)
# book['code'] = book['code'].apply('str')

con_df = pd.merge(rank_df, book, on='code', how='left')
con_df['title_main']  = con_df['title'].str.split(' : ').str[0]
print(con_df[['rank_num','title_main','rank_var']][-80:])
# print(len(con_df.code))
print("[", pd.unique(con_df.collect_date)[0],"~",pd.unique(con_df.collect_date)[-1],"] \n")

# today's best #
#today = pd.Timestamp.today().strftime("%Y-%m-%d").replace("06","05")
#print(today)
#today_df = con_df[con_df['collect_date'] == today]

# pd.set_option('display.max_row', 400)
# pd.set_option('display.max_columns', 100)

# last day's best #
last_day = con_df['collect_date'].unique()[-1] # .unique -> type 'numpy.ndarray' 
# last_day = con_df.iloc[-1]['collect_date']
last_day_df = con_df[(con_df['collect_date'] == last_day)]
last_day_df_left = last_day_df.style.set_properties(**{'text-align': 'left'})
last_day_df_left.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])

################ 여기서부터
# print(last_day_df.loc[:,['rank_num', 'title_main']])
# display(last_day_df_left)

# memo #
'''
좌로 정렬 문제, 리스트가 다 안 보이는 문제 해결 필요(400위는 쭉 훑어야지..?) -> 필요없다고 판단 시 아래 문제 해결
랭크를 빼기한 데이터, 저장할 것인지? -> 특정 한 권에 대한 랭크를 쭉 불러와서 더하고 뺴는 일은 가능
이거 돌린 다음 데이터 베이스에 집어 넣어야 겠다. 아니면 계산량이 너무 많아짐
책 마다 불러와서 전체 시기에 대해서 계산하고, 이걸 전체 책에 반복하려면 굉장히 작업이 많아짐. 일수가 늘어날 수록 더 더욱 심해짐
1) 한번 쭉 정리하는 과정에서는 전체를 계산하도록 스크립트 짜야겠지만
2) db 입력을 위한 row를 정리하기 전에 전날 db를 불러와서 대기해
2-2) row에서 code, title 등이 입력되고, sub(빼기) 데이터 하나를 리스트 끝에 추가하는데, 이 때 전날 db에서 이 데이터의 code를 검색해보고 데이터가 있으면 그 rank_num 에서 row의 rank_num을 빼서 값을 입력해
2-3) 그럼 db 상에서 'sub' 열 데이터가 자연스럽게 입력된다

- db 파일 각 rank 테이블 별로 sub 열을 입력해야 함(비교적 간단)
- db에 들어가 있는 기존 데이터들의 sub를 한번 싹 입력해야 함
- 

3) 선택한 도서들의 rank 추이를 그래프로 그려볼 수 있으면 좋겠다
'''

# 키워드 검색 #
keyword = "ETF 투자 무작정 따라하기"
# search_df = con_df[con_df['title'].str.contains(keyword, regex=False)] # search keyword
# print(search_df.sort_values('code'))
def search_keyword(keyword) :
    # now only for today, but should be changed
    # find on book table? find on rank table by specific date?
    search_df_title = last_day_df[last_day_df['title'].str.contains(keyword, regex=False)] # search keyword from today's data
    if len(search_df_title) == 0 : print("> 제목 검색 결과 없음")
    else :
        print("▼ 제목 검색 결과 : {0}".format(keyword))
        print(search_df_title) # type(search_df) = df
        search_df = search_df_title

    search_df_au = last_day_df[last_day_df['au'].str.contains(keyword, regex=False)] # search keyword from today's data
    if len(search_df_au) == 0 : print("> 저자 검색 결과 없음")
    else :
        print("▼ 저자명 검색 결과 : {0}".format(keyword))
        print(search_df_au)
        search_df = search_df_au

    # 검색 결과에서 코드 뽑아버리기
    code_list = list(search_df['code'])
    print(code_list)

    # 특정 코드 뽑아서 비교하기
    code = code_list # [88406526] # 85156209 주식투자 무따기
    # spec_df = search_df.where(search_df['code'] == code)
    for c in code :
        spec_df = con_df[con_df["code"] == c]
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