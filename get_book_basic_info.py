# get info about 1book

from bs4 import BeautifulSoup as bs
import requests
import pyperclip
from selenium import webdriver

# https://chromedriver.chromium.org/downloads 
    
# naver url
def from_naver_url(driver) :
    html = driver.page_source
    url = driver.current_url
    driver.close()

    par = bs(html, "html.parser")

    t = par.find("div","gd_titArea") # .get_text(" ", strip=True) # title
    t1 = t.h2.get_text(" ", strip=True) # title
    if t.h3 is not None :
        t2 = t.h3.get_text(" ", strip=True) # title_2
    else : t2 = ""
    apd = par.find("span", "gd_pubArea").get_text(" ", strip=True) # author / publisher / date
    p = par.find("div", "gd_infoTb").tr.td.span.text # price
    if par.find("span", "gd_sellNum") is None : # point
        s = "0"
    else : s = par.find("span", "gd_sellNum").get_text(" ", strip=True).split(" ")[2] # point
    i = par.findAll("td", "txt lastCol")[1].get_text(" ", strip=True).replace("*","x")
    isbn = par.findAll("td", "txt lastCol")[2].get_text(" ", strip=True) # = par.find(text="ISBN13").parent.parent.td.text
    
    raw = str("{0} : {1}\n\n{2} | {3}\n\n{4} | {5}\n\n{6}".format(t1, t2, apd, s, i, p, url))
    print(raw)

    pyperclip.copy(raw)

def gbbi():
    url = pyperclip.paste()

    if "http://" not in url : # search by title
        driver = webdriver.Chrome()
        driver.get("http://www.yes24.com/Main/default.aspx")
        driver.find_element_by_name("query").send_keys(url)
        driver.find_element_by_css_selector("#yesSForm .schBtn button").click()
        driver.find_element_by_css_selector("#schMid_wrap .goodsList_list .goods_img a.img_bdr").click()
        from_naver_url(driver)

    elif "Product/Goods/" in url :
        # driver = webdriver.Chrome()
        # driver.get(url)
        # from_naver_url(driver)
        url_list = [url]
        from_url_list(url_list)

    else : 
        driver = webdriver.Chrome()
        driver.get(url) # "http://www.yes24.com/Cooperate/Naver/welcomeNaver.aspx?pageNo=1&goodsNo="+"95612811"
        driver.switch_to.frame("shopping_mall")
        from_naver_url(driver)

def from_url_list(url_list):
    raw_list = []
    for url in url_list : 
        
        html = requests.get(url)
        par = bs(html.text, "html.parser")

        t = par.find("div","gd_titArea") # .get_text(" ", strip=True) # title
        t1 = t.h2.get_text(" ", strip=True) # title
        if t.h3 is not None :
            t2 = t.h3.get_text(" ", strip=True) # title_2
        else : t2 = ""
        apd = par.find("span", "gd_pubArea").get_text(" ", strip=True) # author / publisher / date
        p = par.find("div", "gd_infoTb").tr.td.span.text # price
        if par.find("span", "gd_sellNum") is None : # point
            s = "0"
        else : s = par.find("span", "gd_sellNum").get_text(" ", strip=True).split(" ")[2] # point
        i = par.findAll("td", "txt lastCol")[1].get_text(" ", strip=True).replace("*","x")
        isbn = par.findAll("td", "txt lastCol")[2].get_text(" ", strip=True) # = par.find(text="ISBN13").parent.parent.td.text
        
        raw = str("{0} : {1}\n\n{2} | {3}\n\n{4} | {5}\n\n{6}".format(t1, t2, apd, s, i, p, url))
        raw_list.append(raw)
        print(raw)
    pyperclip.copy("\n\n".join(raw_list))


url_list = [
    "http://www.yes24.com/Product/Goods/101889359?OzSrank=84",
    "http://www.yes24.com/Product/Goods/102087412?OzSrank=85",
    "http://www.yes24.com/Product/Goods/102237481?OzSrank=88",
    "http://www.yes24.com/Product/Goods/78142995?OzSrank=90"
]

gbbi()