import bestsellers_yes24 as bl
import mkcsvfile as mkc
from importlib import reload as re
# 검색을 한 경우 '국내도서' 꼭 고르기
url = 'http://www.yes24.com/SearchCorner/Search?domain=BOOK&query=%b0%a1%b0%e8%ba%ce&page_size=120&sort_gb=POPULAR&scode=009_001'
# 전체 url을 집어넣어 줘야함

result_data, tag_list = bl.main_ca(url, y=2019, m=2, p=[1,2,3], sellpoint=1, tsw=0)

# url += '&domain=BOOK' # 국내도서

def cate_best(url) :

    if '&sumgb=06' in url:
        url = url.replace('&sumgb=06', '&sumgb=09')

    f_name = '경제경영 2019 02 best 240.csv'
    b = []
    a = []
    for m in range(1,13) :
        result_data, tag_list = bl.main_ca(url, y=2019, m=m, p=[1], sellpoint=0, tsw=0)
        b.append(result_data)
        a.append(tag_list)
    mkc.mk(f_name, result_data)
    mkc.tag(f_name, tag_list)

def search_best(url) :

    if '&sumgb=06' in url:
        url = url.replace('&sumgb=06', '&sumgb=09')

    fn = '길벗 인기 품절제외 97.csv'  # %len(rd)# file name
    rd, tl = bl.main_sear(url, p=[1]) # return result_data, tag_list

    mkc.mk(fn, rd)
    mkc.tag(fn, tl)
