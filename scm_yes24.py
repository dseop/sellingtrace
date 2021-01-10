# using pyautogui, extract yes24 selling data

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome() # ()에 경로 입력, 현재 스크립트와 같은 폴더에 있다면 경로 필요 없음

scm_url = "https://scm.yes24.com/Login/LogOn?ReturnUrl=%2f"
ID = "gilbut"
PW = "023320931gb#"

driver.get(scm_url)
driver.find_element_by_css_selector('UserName.fm_text.valid').click()
driver.find_element_by_css_selector('UserName.fm_text.valid').send_keys(ID)
