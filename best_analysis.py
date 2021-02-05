# https://www.notion.so/7cadd2f2f5b64f208fa9cfbde4cfcf30#3c22dc1cd4b74b81a413197381dbec04
# rank analysis

import sqlite3
import crawling as cr
import connect_sheet as cs
import DB_controler as dbc
from datetime import datetime
# doc = cs.open_sheet("url") / worksheet = doc.worksheet("sheet_name")

# DB connect    
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

def yes24(url) :

    print("get rank data from YES24... / {0}".format(url[0]))
    rank = 0
    row_list = []
    rank_db_list = [] # make DB list
    book_db_list = []
    collect_date = cr.date
    
    # page 1~5, get bestseller list #
    for i in [1, 2, 3, 4, 5] : # 400위까지 # row_list, rank_db_list, book_db_list
        tmp_url = url[1]+('&PageNumber=%s' %i)
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
            
            publish_date = good_info.find('div', 'aupu').get_text('',strip=True).split('| ')[-1]
            price = int(good_info.find_all('p')[1].get_text().split('원')[0].replace(',',''))

            # make row_list for Spreadsheet data
            info_row = rank,code,title,au,pu,publish_date,price,collect_date,"http://www.yes24.com"+code_url    
            row_list.append(info_row)

            # make db_list for DB(rank_DB, book_DB)
            rank_db_row = rank, code, collect_date
            rank_db_list.append(rank_db_row)

            book_db_row = code, title, au, pu, publish_date, price
            book_db_list.append(book_db_row)    
        print(i, "page")
    print("DONE!")
    # processing table name #
    now_table = "rank_"+url[0] # str
    print("now table name: {0} / number of data: {1}".format(now_table, len(row_list)))

    # spreadsheet connect #
    doc = cs.open_sheet("https://docs.google.com/spreadsheets/d/1Mddr6g9Oid4_2R5mwQRC4N8NB05uLaO0jtT7SxTXwZc/edit#gid=0")
    worksheet = doc.worksheet('RANK_YES_'+url[0]) # select sheet

    # insert into Spreadsheet #
    if collect_date != worksheet.col_values(8)[-1] : # collect_date column last data
        worksheet.append_rows(row_list)
        print("complete insert to spreadsheet")
    else : print("already inserted : spreadsheet")
    
    # check / create rank table & insert data #
    if dbc.check_table_in_db(c, now_table) == 0 : # 있으면 1, 없으면 0 / return 0 or 1
        print("create new table...", now_table)
        print("[before table list]\n", dbc.get_table_list(c))
        c.execute("CREATE TABLE {0}('rank_num' int, 'code' int, 'collect_date' text)".format(now_table))
        print("[after table list]\n:", dbc.get_table_list(c))
    
    if dbc.get_last_date(c, now_table) != collect_date :
        before_len = len(dbc.get_table(c, 'book_table'))
        dbc.insert_book_data(c, book_db_list) # insert into book_table
        after_len = len(dbc.get_table(c, 'book_table'))
        print("book_table before_len: {0} / after_len: {1}".format(before_len, after_len))

        before_len = len(dbc.get_table(c, now_table))
        dbc.insert_rank_data(c, now_table, rank_db_list)
        after_len = len(dbc.get_table(c, now_table))
        print("rank_table before_len: {0} / after_len: {1}".format(before_len, after_len))
    else :
        print("already inserted : DB")
    
    con.commit()

    return row_list, rank_db_list, book_db_list

# main #

url_list = [
    ("economy", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80"), # 경제경영
    ("economy_invest", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010&sumgb=06&FetchSize=80"), # 경제경영 > 투자/재테크
    ("economy_ebiz", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025011&sumgb=06&FetchSize=80"), # 경제경영 > 인터넷 비즈니스
    ("humanities", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001019&sumgb=06&FetchSize=80") # 인문    
]

for url in url_list :
    yes24(url)

def kyobo() : return 0
    # URL request impossible(responsive web)
    # 경제경영 전체로 볼 때는 150위까지 제공, 반응형 → use pyautogui
    # 세부 분야로 들어가면 전체 도서 제공, url request possible
    # http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1323&mallGb=KOR&orderClick=JAR

def aladin() : return 0
    # https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=170&page=1&cnt=1000&SortOrder=1