# 투고 원고를 자동으로 정리해주는 프로그램
# not use requests, chromedriver
# have no authority from home

# so use just 1 html copy&paste -> make 1 row summary

from bs4 import BeautifulSoup as bs
import pyperclip
import codecs

# pyperclip.paste()

f = codecs.open("test.html", 'r', 'utf-8')
par_url = bs(f, 'html.parser')

content = par_url.find('table').find_all('tr')
au = content[0].find_all('td')[0].text
c_date = content[0].find_all('td')[1].text
title = content[6].get_text("",strip=True)
concept = content[18].get_text("\n",strip=True)
sp_au = content[28].get_text("\n",strip=True)
print()
par_url.find('table').find_all('tr')

row = (c_date, "홈페이지", title, au, sp_au, concept).join()
print(str(row))

pyperclip.copy(str(row))