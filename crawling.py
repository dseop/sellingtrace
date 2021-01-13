# -* coding : cp949 *-
# -* coding : utf-8 *- 언제 바뀌었지?

from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df
import requests
from datetime import datetime

import csv

now = datetime.now()
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
today = "%s %s %s %s" %(now.year, now.month, now.day, week[now.weekday()])
date = str(now.date())
# print(today)
# print(now.date())
# print(type(now.date()))
date = "%s-%s-%s" %(now.year, now.month, now.day)
# datetype = datetime.strptime(date, '%Y-%m-%d')

def yes24_code_to_url(code_list) :
    url_list = []
    for code in code_list :
        url_list.append("http://www.yes24.com/Product/Goods/"+code)
    return url_list

# html parsing, insert url, return par_url
def makepar(url) :
    if url is None :
        return 0
    else :
        re_url = requests.get(url)
        # re_url.encoding = 'ms949'  # important
        par_url = bs(re_url.text, 'html.parser')
        return par_url

def makeresult(t_list, a_list, pu_list, pr_list, d_list, t_num) :
    raw_data = df({'title': t_list,
                   'author': a_list,
                   'publisher': pu_list,
                   'price': pr_list,
                   'date': d_list,
                   'selling point': t_num})
    return raw_data

def search_key(par_url) :

    t_list, t2_list, a_list, pu_list, pr_list, d_list, sp_list, i_list = [], [], [], [], [], [], [], []

    # title_list = par_url.select('#schMid_wrap > div.goods_list_wrap.mgt30 > div.goodsList.goodsList_img > table > tr > td > div.goods_infogrp > p.goods_name > a') # sector 그대로 가져온 것
    # search = par_url.find('span', 'txt_keyword').text[1:len(par_url.find('span','txt_keyword').text)-1]

    for i in par_url.find_all('td', 'goods_infogrp') :
        url = 'http://www.yes24.com' + i.find('a', href=True)['href']
        tmp_par = makepar(url)
        t_list.append(tmp_par.find('h2', 'gd_name').text)
        t2_list.append(tmp_par.find('h3', 'gd_nameE').text)
        a_list.append(tmp_par.find_all('a')[0].text)
        pu_list.append(tmp.find_all('a')[len(tmp.find_all('a'))-1].text)
        d_list.append(tmp.em.text)
        pr_list.append(i.find('p','goods_price').strong.text)



        if len(i.find('p', 'goods_rating').text) == 1 or len(i.find('p', 'goods_rating').contents) == 17 :
            t_num.append('0')
        else :
            a=next(i.find('p', 'goods_rating').stripped_strings) # strip 된 str 을 찾아서 generator 로 반환, 그 중에 첫번째가 '판매지수 ooo'임
            t_num.append(a.split(' ')[1]) # 그걸 split(' ') 으로 쪼개면 리스트 두번째 문자열이 t_number

    return t_list, a_list, pu_list, pr_list, d_list, t_num

def best_yes24(url, sellpoint=1, tracing_switch=0) : #ts= t num switch

    par_url = makepar(url)

    if 'Search' in url: # Search 따로
        t_list, a_list, pu_list, pr_list, d_list, t_num = search_key(par_url)

    else : # 기본

        t_list, a_list, pu_list, pr_list, d_list, t_num, url_list = [], [], [], [], [], [],[]
        # title, author, publisher, price, published date list, selling point



        for i in par_url.find_all('td', 'goodsTxtInfo') :
            t_list.append(i.find('a',href=True).text)

            temp_list = []
            for k in i.div.find_all('a') :
                temp_list.append(k.text)
            if len(temp_list) < 2 :
                a_list.append(['no author'])
            if len(temp_list) > 10 :
                a_list.append(str(temp_list[0:10]).replace('[','').replace(']','').replace("""'""",''))
            if 2<=len(temp_list)<=10 :
                a_list.append(str(temp_list[0:len(temp_list)-1]).replace('[','').replace(']','').replace("""'""",''))
            pu_list.append(temp_list[len(temp_list)-1])
            pr_list.append(i.find_all('p')[1].span.text)
            q = i.div.get_text(strip=True)
            d_list.append(q[len(q)-9:len(q)].replace('년 ','-').replace('월',''))
            url_list.append('http://www.yes24.com' + par_url.find_all('td', 'goodsTxtInfo').find('a', href=True)['href'])

    return t_list, a_list, pu_list, pr_list, d_list, t_num, url_list

def best_de_yes24(url, lineup) :

    in_url = url
    re_url = requests.get(in_url)
    txt_url = re_url.text
    par_url = bs(txt_url, 'html.parser')

    term = par_url.find('h3', 'cateTit_txt').get_text("", strip=True) # data name
    if lineup == '01' :
        lineup = '기본순'
    if lineup == '05' :
        lineup = '판매량'
    if lineup == '04' :
        lineup = '신상품'
    f_name = "{0}, {1}, {2}.csv".format(term, lineup, today)
    # file name decision

    t_list = [] # title list
    a_list = [] # author list
    pu_list = [] # publisher list
    pr_list = [] # pirce list
    d_list = [] # published date


    for i in par_url.find_all('div', 'goods_name') :
        t_list.append(i.a.text)

    for i in par_url.find_all('span', 'goods_auth') :
        temp_list = []
        for k in i.find_all('a') :
            temp_list.append(k.text)
        a_list.append(temp_list)
    for i in par_url.find_all('span', 'goods_pub') :
        pu_list.append(i.text)
    for i in par_url.find_all('span', 'goods_date') :
        d_list.append((i.text))
    for i in par_url.find_all('div', 'goods_price') :
        pr_list.append(i.em.text)

    return f_name, t_list, a_list, pu_list, pr_list, d_list

def sell_p_cr(url, tracing_switch=0) : # selling point crawler
    re_url = requests.get(url)
    re_url.encoding='ms949' #이게 너무 중요했다..... 하.....
    par_url = bs(re_url.text, 'html.parser')

    selling_point = int(par_url.find('span','gd_sellNum').get_text(' ',strip=True).split(' ')[2])

    if tracing_switch == 1 :
        today2 = '%s-%s-%s' % (now.year, now.month, now.day)
        t = par_url.find('h2', 'gd_name').text
        tmp = (t, today2, selling_point)

        f = open('sellling point taracing.csv', mode='a', newline='')  # 파일명
        csvWriter = csv.writer(f)
        csvWriter.writerow(tmp)
        f.close()

    return selling_point

def add(fn, rd) : # 추가할 때
    rd.to_csv(fn, header=False, index=True, encoding='ms949', mode='a')

def mk(fn, rd) :
    rd.to_csv(fn, header=True, index=True, encoding='ms949')

def tag(fn, rd) :
    rd.to_csv(fn.replace('.csv','tag.csv'), header=['tag','count'], index=False, encoding='ms949')