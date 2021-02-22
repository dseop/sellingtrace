from datetime import datetime
import crawling as cr
import connect_sheet as cs

today = datetime.today().date()
url = ("부동산","http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06&FetchSize=80")
print(url)

rank = 0
row_list = []
rank_db_list = [] # make DB list
book_db_list = []
collect_date = cr.date

for i in [1, 2, 3, 4, 5] :
    tmp_url = url[1]+('&PageNumber={0}'.format(i))
    par_url = cr.makepar(tmp_url)
    for good_info in par_url.find_all('td', 'goodsTxtInfo') :
            
        # variable definition
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


        # make row_list for spreadsheet data
        info_row = rank,code,title,au,pu,publish_date,price,collect_date,"http://www.yes24.com"+code_url    
        row_list.append(info_row)
    print(i, "page")
print("DONE! number of data: {0}".format(len(row_list)))
    
doc = cs.open_sheet("https://docs.google.com/spreadsheets/d/1RHrnaXg636ARmBnwzEVmTsgp721lMvqWZMyOKg3hnTA")
worksheet = doc.worksheet(url[0]) # select sheet
worksheet.append_rows(row_list) # insert into spreadsheet