from bs4 import BeautifulSoup as bs
import pyperclip
url = pyperclip.paste()

print(type(int(url)))
if len(url) == 8 :
    print(len(url))