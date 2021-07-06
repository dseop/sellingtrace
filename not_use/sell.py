from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time

url = 'https://www.instagram.com/cultured_consumers/'
driver = webdriver.Chrome('D:/')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('/Applications/chromedriver', options=options)

driver.implicitly_wait(5)



# 5초간 대기한다
time.sleep(5)

driver.get(url)
totalCount = driver.find_element_by_class_name('C4VMK').text
print(totalCount)