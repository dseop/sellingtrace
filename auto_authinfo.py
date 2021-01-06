from bs4 import BeautifulSoup as bs
import requests
import pyautogui
import pyperclip

og_point = pyautogui.position()

pyautogui.click(1772, 22, duration=0.25)
pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'c')
url = pyperclip.paste()

# pyautogui.hotkey('ctrl', 'pagedown')

re_url = requests.get(url)
#re_url.encoding = 'ms949'
par_url = bs(re_url.text, 'html.parser')

# print(par_url)
# print(par_url.find('span','author_info info_origin').text)
authinfo = par_url.find('span','author_info info_origin').get_text("",strip=True)
pyperclip.copy(authinfo)

pyautogui.moveTo(og_point, duration=0.25)
# python auto_authinfo.py