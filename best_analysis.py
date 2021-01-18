# https://www.notion.so/7cadd2f2f5b64f208fa9cfbde4cfcf30#3c22dc1cd4b74b81a413197381dbec04
# rank analysis

import crawling as cr
import connect_sheet as cs

# from keyword_analysis import get_tags_okt

def yes24(url) :
    
    # URL request possible
    # http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber=1

    doc = cs.open_sheet()
    worksheet = doc.worksheet('RANK_YES_'+url[0]) # select sheet

    print('get daily BEST 320...')

    rank = 0
    row_list = []
    for i in [1, 2, 3, 4, 5] : # 400위까지
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

            info_row = rank,code,title,au,pu,date,price,cr.date,"http://www.yes24.com"+code_url    
            print(info_row)
            # worksheet.append_row(info_row)
            row_list.append(info_row)
    worksheet.append_rows(row_list)

    print(len(row_list), ' data insert complete!') # 1day 320 / 1year 116800 / 2year 233600 (이정도 모으기 전에 그만두지 않을까?)
    # 어쩄거나 데이터를 정리하려면, DB를 만드는 게 좋다.
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