# https://www.notion.so/7cadd2f2f5b64f208fa9cfbde4cfcf30#3c22dc1cd4b74b81a413197381dbec04
# rank analysis

import sqlite3
import crawling as cr
import connect_sheet as cs

# DB connect    
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def yes24(url) :

    # Spreadsheet connect
    doc = cs.open_sheet()
    worksheet = doc.worksheet('RANK_YES_'+url[0]) # select sheet
    
    print('get daily %s BEST 400' % (url[0]))

    rank = 0
    row_list = []
    rank_db_list = [] # make DB list
    book_db_list = []

    # page 1~5, get bestseller list
    for i in [1, 2, 3, 4, 5] : # 400위까지 # row_list, rank_db_list, book_db_list
        tmp_url = url[1]+('%s' %i)
        par_url = cr.makepar(tmp_url)
        for good_info in par_url.find_all('td', 'goodsTxtInfo') :
            
            rank = rank+1
            code_url = good_info.find('a', href=True)['href']
            code = int(code_url.split('/')[-1]) # id
            title = good_info.find_all('p')[0].get_text(' ',strip=True).replace('[도서] ', '')
            
            aupu_list = []
            for aupu in good_info.find('div', 'aupu').find_all('a') : # author list
                aupu_list.append(aupu.get_text())
            if len(aupu_list) > 1 :
                au = aupu_list[0] # aupu_list[0:-1]
                pu = aupu_list[-1]
            else :
                au = 'need check'
                pu = 'need check'
            
            date = good_info.find('div', 'aupu').get_text('',strip=True).split('| ')[-1]
            price = int(good_info.find_all('p')[1].get_text().split('원')[0].replace(',',''))

            # into Spreadsheet data
            info_row = rank,code,title,au,pu,date,price,cr.date,"http://www.yes24.com"+code_url    
            row_list.append(info_row)

            # into DB data(rank_DB, book_DB)
            rank_db_row = rank, code, cr.date
            rank_db_list.append(rank_db_row)

            book_db_row = code, title, au, pu, date, price
            book_db_list.append(book_db_row)
            
        print(url[0], i, "page complete!")
    
    # insert into Spreadsheet #
    worksheet.append_rows(row_list)

    
    # insert into rank_table #
    now_table = "rank_table_"+url[0] # str

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
        count_check = check[0][0] # 있으면 1, 없으면 0
        print(table_name+": ", count_check)
        return count_check

    def create_table(count_check, table_name) : 
        if count_check == 0 :
            c.execute("CREATE TABLE "+table_name+"('rank' int, 'code' int, 'today' text)")

    def insert_data(table_name, db_list) :
        insert_rank_sql = "INSERT INTO "+table_name+" VALUES (?,?,?)"
        c.executemany(insert_rank_sql, db_list)

    def check_table(table_name) :
        c.execute("SELECT * FROM "+table_name)
        check = c.fetchall()
        print(len(check))

    def get_table(table_name) :
        c.execute("SELECT * FROM "+table_name)
        data = c.fetchall()
        return data
    
    print("before")
    get_table_list()
    check_table(now_table)

    count_check = check_table_list(now_table) # 있으면 1, 없으면 0
    create_table(count_check, now_table)

    insert_data(now_table, rank_db_list)

    print("after")
    check_table(now_table)

    # insert into book_table #
    
    if check_table_list("book_table") == 0 :
        c.execute("""CREATE TABLE book_table(
        'code' int PRIMARY KEY, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text
        )""")

    insert_book_sql = "INSERT OR REPLACE INTO book_table VALUES (?,?,?,?,?,?)"
    c.executemany(insert_book_sql, book_db_list)
    
    con.commit()

    print(len(row_list), ' data insert complete! - ', url[0])

    return row_list, rank_db_list, book_db_list

url = "economy", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber=" # 경제경영
yes24(url)

url = "humanities", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001019&sumgb=06&FetchSize=80&PageNumber=" # 인문
yes24(url)

url = "ebiz", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025011&sumgb=06&FetchSize=80&PageNumber=" # 인터넷 비즈니스
yes24(url)

def kyobo() : return 0
    # URL request impossible(responsive web)
    # 경제경영 전체로 볼 때는 150위까지 제공, 반응형 → use pyautogui
    # 세부 분야로 들어가면 전체 도서 제공, url request possible
    # http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1323&mallGb=KOR&orderClick=JAR

def aladin() : return 0
    # https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=170&page=1&cnt=1000&SortOrder=1