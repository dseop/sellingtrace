import pyperclip
import crawling as cr
import get_book_basic_info as gbbi

url = pyperclip.paste()
# url = "http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=130721&barcode=9791189249519"
# url = "http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791185553597&orderClick=LAG&Kc="

if 'Click' in url:
    barcode = url.split("&")[2].split("=")[1]

else:
    barcode = url.split("=")[4]

tmp_par = cr.makepar(url)

# get article #
# article_list = tmp_par.find_all('div', 'box_detail_article')
# print(article_list)
article = tmp_par.find_all('div', 'box_detail_article')[2].get_text('\n',strip=True).replace(".","")

# get basic info - just title #
# title = tmp_par.find('h1', 'title').get_text('\n',strip=True)

# get basic info - use gbbi #
# pyperclip.copy(barcode)
# gbbi.gbbi()
# basic_info = pyperclip.paste()

# get basic info - from yes24 #
url = "http://www.yes24.com/SearchCorner/Search?domain=BOOK&query={0}".format(barcode)
tmp_par = cr.makepar(url)
infogrp = tmp_par.find('td','goods_infogrp')
title = infogrp.find('p').a.text
stitle = infogrp.p.span.get_text(' ',strip=True)

info_list = infogrp.find_all('div')
info1 = info_list[0].get_text(' ',strip=True)
info2 = info_list[1].get_text('|',strip=True).split('|')[0]
info3 = info_list[2].get_text('|',strip=True).split('|')[0]

basic_info = title+' '+stitle+'\n'+info1+' | '+info2+' | '+info3

# result print #
print(basic_info+"\n\n"+article)
pyperclip.copy("{0}\n\n{1}".format(basic_info, article))