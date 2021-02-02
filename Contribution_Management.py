# 투고 원고를 자동으로 정리해주는 프로그램
# not use requests, chromedriver
# have no authority from home

# so use just 1 html copy&paste -> make 1 row summary

from bs4 import BeautifulSoup as bs
import pyautogui
import pyperclip
import codecs

import connect_sheet as cs

pyautogui.click(3240,147)
pyautogui.press('f12')

pyautogui.sleep(0.5)

pyautogui.click(3240,147)
pyautogui.hotkey('ctrl','c')
pyautogui.press('f12')

html = pyperclip.paste()
# html = codecs.open("test.html", 'r', 'utf-8')

par_url = bs(html, 'html.parser')

content = par_url.find('table').find_all('tr')
au = content[0].find_all('td')[0].text
c_date = content[0].find_all('td')[1].text
title = content[6].get_text("",strip=True)
concept = content[18].get_text("\n",strip=True)
sp_au = content[28].get_text("\n",strip=True)

new_data = c_date, "홈페이지", title, au, sp_au, concept
print(str(new_data))

# pyperclip.copy(str(new_data))

doc = cs.open_sheet("https://docs.google.com/spreadsheets/d/1069FVllXbd48V12VGamqVwoXwliyyXZeIru6FeQ-Eq4/edit#gid=2081027927") # 투고 원고 정리 파일
worksheet = doc.worksheet('contribution') # select sheet, sheetname is YES24

worksheet.append_row(new_data) # insert row below end line

pyautogui.hotkey('alt','left')