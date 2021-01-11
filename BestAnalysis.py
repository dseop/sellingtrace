# https://www.notion.so/7cadd2f2f5b64f208fa9cfbde4cfcf30#3c22dc1cd4b74b81a413197381dbec04
# rank analysis

from pandas import DataFrame as df
import time
from datetime import datetime as dt

import crawling as cr
from get_book_info import gbi_yes
# from keyword_analysis import get_tags_okt

def yes24() :
    # URL request possible
    # http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber=1
    url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber="
    for i in [1,2,3,4] :
        tmp_url = url+('%s' %i)
        par_url = cr.makepar(tmp_url)
        pritn(par_url)

def kyobo() :
    # URL request impossible(responsive web)
    # 경제경영 전체로 볼 때는 150위까지 제공, 반응형 → use pyautogui
    # 세부 분야로 들어가면 전체 도서 제공, url request possible
    # http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1323&mallGb=KOR&orderClick=JAR
def aladin() :
    # URL request possible
    # https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=170&page=1&cnt=1000&SortOrder=1

yes24()

