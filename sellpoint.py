from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df
import requests
from urllib.request import urlopen
from datetime import datetime

# import url_list as

# with open('G:/내 드라이브/070392_경제 용어 도감/url.txt') as data:
#    url=data.read().split()

url = ['http://www.yes24.com/Product/Goods/61556029?scode=032&OzSrank=2',
       'http://www.yes24.com/Product/Goods/70834009?Acode=101',
       'http://www.yes24.com/Product/Goods/63470144?Acode=101',
       'http://www.yes24.com/Product/Goods/24338420',
       'http://www.yes24.com/Product/Goods/70812322?scode=032&OzSrank=2',
       'http://www.yes24.com/Product/Goods/15281236',
       'http://www.yes24.com/Product/Goods/67536495',
       'http://www.yes24.com/Product/Goods/71538793?scode=032&OzSrank=5',
       'http://www.yes24.com/Product/Goods/59734176?Acode=101'
       ]


# 내가 추적하고 싶은 도서의 주소를 집어 넣는다.
# put the URL of the book that you want to trace

def makepar(url) :
    re_url = requests.get(url)
    # re_url.encoding = 'ms949'
    # 2019.03.27. I think yes24 changed the charset to utf-8 from euc-kr. euc-kr maybe will be same with 'ms949'
    par_url = bs(re_url.text, 'html.parser')
    return par_url

today = datetime.today()


def essencial_function(par_url) :
    selling_point = par_url.find('span', 'gd_sellNum').get_text(' ',strip=True).split(' ')[2]
    print('ing ', selling_point)
    if par_url.find('a', 'formatA formatLnk') != None:
        if par_url.find('a', 'formatA formatLnk').get('onclick').split("""'""")[1] != 'Pcode':
            a = par_url.find('a', 'formatA formatLnk').get('onclick').split("""'""")[1]
            ebook_re_url = requests.get('http://www.yes24.com'+a)
            ebook_par_url = bs(ebook_re_url.text, 'html.parser')
            ebook_selling_point = ebook_par_url.find('span', 'gd_sellNum').get_text(' ',strip=True).split(' ')[2]
            return selling_point, ebook_selling_point
        else: return selling_point
    else: return selling_point

t_list, a_list, pu_list, po_list, d_list = [],[],[],[],[]


for tem_url in url :
    par_url = makepar(tem_url)
    title = par_url.find('h2', 'gd_name').text
    t_list.append(title)
    auth = par_url.find('span', 'gd_auth').a.text
    a_list.append(auth)
    publisher = par_url.find('span', 'gd_pub').a.text
    pu_list.append(publisher)
    pub_date = par_url.find('span', 'gd_date').text
    d_list.append(pub_date)
    basic_info = title, auth, publisher, pub_date
    po_list.append(essencial_function(par_url))

raw_data = df({'title': t_list,
               'author': a_list,
               'publisher': pu_list,
               'point': po_list,
               'date': d_list})
rd = raw_data

print(today.date(), po_list)
# get parsed html text from url
#divFormatInfo > ul > li:nth-child(1) > a

def add(fn, rd) : # 추가할 때
    rd.to_csv(fn, header=False, index=True, encoding='ms949', mode='a')

def mk(fn, rd) :
    rd.to_csv(fn, header=True, index=True, encoding='ms949')

def tag(fn, rd) :
    rd.to_csv(fn.replace('.csv','tag.csv'), header=['tag','count'], index=False, encoding='ms949')
# selling_point = par_url.find('span', 'gd_sellNum').get_text(',',strip=True).split(',')[1].split(' ')[1]



#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum > em