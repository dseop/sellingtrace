# https://www.notion.so/7cadd2f2f5b64f208fa9cfbde4cfcf30#3c22dc1cd4b74b81a413197381dbec04
# rank analysis

import sqlite3
import crawling as cr
import connect_sheet as cs

def yes24(url) :
    # DB connect    
    con = sqlite3.connect("rank_DB.db")
    c = con.cursor()
    
    # Spreadsheet connect
    doc = cs.open_sheet()
    worksheet = doc.worksheet('RANK_YES_'+url[0]) # select sheet

    # start
    print('get daily BEST 320...')

    rank = 0
    row_list = []
    rank_db_list = [] # make DB list
    book_db_list = []

    # page 1~5, get bestseller list
    for i in [1] : # , 2, 3, 4, 5] : # 400위까지
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

            # into DB data
            rank_db_row = rank, code, cr.date
            rank_db_list.append(rank_db_row)

            book_db_row = code, title, au, pu, date, price
            book_db_list.append(book_db_row)
            
        print(i, "page complete!")
    # insert into Spreadsheet
    # worksheet.append_rows(row_list)

    # insert into rank_DB
    # print(rank_db_list) # check DB
    # c.execute("CREATE TABLE rank_table_"+url[0]+"('rank' int, code int, today text)")
    # sql_insert_rank = "INSERT INTO rank_table_"+url[0]+" VALUES (?,?,?)"
    # c.executemany(sql_insert_rank, rank_db_list)

    print(book_db_list)
    # insert into book_DB
    # 중복처리 해결 필요 #
    # c.execute("CREATE TABLE book_table('code' int, 'title' text, 'au' text, 'pu' text, 'date' text, 'price' text)")
    # c.executemany("INSERT INTO book_table VALUES (?,?,?,?,?,?)", book_db_list)
    
    #con.commit()
    con.close()

    print(len(row_list), ' data insert complete! - ', url[0])
    
    # 320위에서 벗어나버리면 점점 안 보게 될 것. 내가 선택적으로 그 때 그 때 데이터를 보는 게 낫다.
    # 일단은 스프레드시트? 피봇테이블로 감당할 수 있을까..?
    return 0

def kyobo() : return 0
    # URL request impossible(responsive web)
    # 경제경영 전체로 볼 때는 150위까지 제공, 반응형 → use pyautogui
    # 세부 분야로 들어가면 전체 도서 제공, url request possible
    # http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1323&mallGb=KOR&orderClick=JAR

def aladin() : return 0
    # https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=170&page=1&cnt=1000&SortOrder=1