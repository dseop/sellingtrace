from pandas import DataFrame as df
import time
from datetime import datetime as dt

import crawling as cr
from get_book_info import gbi_yes
# from keyword_analysis import get_tags_okt

# &ParamSortTp=%s # sort '05':판매량 '04':신상품 '01':기본순(사용x)

# copy the url of specific category and paste to here
#url = str(input('url?\n'))
url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06&ParamSortTp=04'
url += '&FetchSize=%s&GS=03' %(80) #int(input('fetchsize? 20/40/80')))  # 80개씩, 품절제외
#p = list(range(1, int(input('which page?'))+1))
p = [1]

fn = str(dt.today().date())

starttime = time.time()

idx = 1
tmp_par = cr.makepar(url)
url_list = []
idx_list = []
for page in p :
    tmpurl = url + '&PageNumber=%s' % (page)
    for i in tmp_par.find_all('td', 'goodsTxtInfo'):
        idx_list.append(idx)
        idx += 1
        url_list.append('http://www.yes24.com' + i.find('a', href=True)['href'])

rd = gbi_yes(url_list)
rd.to_csv('C:/Users/gilbut/Desktop/getinfo.csv', header=True, encoding='ms949')

print('running time ', int((time.time() - starttime) / 60), 'm', round((time.time() - starttime) % 60, 2), 's')

def main_sear(url) :

    result_data = df()
    url += '&page_size=120'
    url += '&stat_gb=0&scode=006_002'  # 품절제외

    par_url = cr.makepar(url)
    t_list, a_list, pu_list, pr_list, d_list, t_num = cr.search_key(par_url)

    rd = cr.makeresult(t_list, a_list, pu_list, pr_list, d_list, t_num)
    result_data.append(rd, ignore_index=True)

    inl = " ".join(result_data['title'])
    tag_list = get_tags_okt(inl)
    tag_list = df(tag_list)

    return result_data, tag_list

input()
