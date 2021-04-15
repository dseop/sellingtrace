# get info about 1book

from bs4 import BeautifulSoup as bs
import pyperclip
from selenium import webdriver

# https://chromedriver.chromium.org/downloads 
    
# naver url
def from_naver_url(driver) :
    html = driver.page_source
    url = driver.current_url
    driver.close()

    par = bs(html, "html.parser")

    t = par.find("div","gd_titArea").get_text(" ", strip=True) # title
    apd = par.find("span", "gd_pubArea").get_text(" ", strip=True) # author / publisher / date
    p = par.find("div", "gd_infoTb").tr.td.span.text # price
    if par.find("span", "gd_sellNum") is None : # point
        s = "0"
    else : s = par.find("span", "gd_sellNum").get_text(" ", strip=True).split(" ")[2] # point
    i = par.findAll("td", "txt lastCol")[1].get_text(" ", strip=True).replace("*","x")
    isbn = par.findAll("td", "txt lastCol")[2].get_text(" ", strip=True) # = par.find(text="ISBN13").parent.parent.td.text
    
    raw = str(t+"\n"+apd+" | "+s+"\n"+i+" | "+p+"\n"+url)
    print(raw)

    pyperclip.copy(raw)

driver = webdriver.Chrome()
url = pyperclip.paste()

if "http://" not in url : # search by title
    driver.get("http://www.yes24.com/Main/default.aspx")
    driver.find_element_by_name("query").send_keys(url)
    driver.find_element_by_css_selector("#yesSForm .schBtn button").click()
    driver.find_element_by_css_selector("#schMid_wrap .goodsList_list .goods_img a.img_bdr").click()
    from_naver_url(driver)

elif "Product/Goods/" in url :
    driver.get(url)
    from_naver_url(driver)

else : 
    driver.get(url) # "http://www.yes24.com/Cooperate/Naver/welcomeNaver.aspx?pageNo=1&goodsNo="+"95612811"
    driver.switch_to.frame("shopping_mall")
    from_naver_url(driver)