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
# print(len(con_df.code))

print("[", pd.unique(con_df.collect_date)[0],"~",pd.unique(con_df.collect_date)[-1],"] \n")

# 오늘 베스트 검색 #
today = pd.Timestamp.today().strftime("%Y-%m-%d").replace("30","29") # 임시로 날짜 변경
# print("today:", today)
today_df = con_df[con_df['collect_date'] == today]
# print("today's data:", today_df)

# print(type(today_df))
# print(type(con_df['collect_date'] == today))
# print(type(con_df['collect_date']))

# 키워드 검색 #
keyword = "무작정 따라하기"
# search_df = con_df[con_df['title'].str.contains(keyword, regex=False)] # search keyword
# print(search_df.sort_values('code'))

# now only for today, but should be changed
# find on book table? find on rank table by specific date?
search_df_title = today_df[today_df['title'].str.contains(keyword, regex=False)] # search keyword from today's data
if len(search_df_title) == 0 : print("> 제목 검색 결과 없음")
else :
    print("▼ 제목 검색 결과 : {0}".format(keyword))
    print(search_df_title) # type(search_df) = df
    search_df = search_df_title

search_df_au = today_df[today_df['au'].str.contains(keyword, regex=False)] # search keyword from today's data
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
    print(pd.unique(spec_df.title))
    rank_list = list(spec_df.rank_num)
    # type(spec_df.rank_num[72]) # <class 'numpy.int64'>
    # type(rank_list[0]) # int
    sub_list = [0]
    for i in range(len(rank_list)-1) :
        sub_list.append(rank_list[i+1]-rank_list[i])
    spec_df['sub'] = sub_list
    print(spec_df[['collect_date', 'rank_num', 'sub']])

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