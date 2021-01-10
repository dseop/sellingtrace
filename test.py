import gspread
from oauth2client.service_account import ServiceAccountCredentials
print('ok')

import crawling as cr
import get_book_info as gbi

list_of_lists = ['날짜', '코드'], ['', '96195306'], ['2021-1-10', '15,414']

code_list = list_of_lists[1][1:] # list
# values_list = worksheet.row_values(1) # load row
print(code_list)

raw_data = gbi.yes24(gbi.mak_url_list(code_list)) # raw_data는 모든 yes24의 책 정보를 다 가져옴 # pandas Series type
new_data = list(raw_data['지수']) # list
new_data.insert(0, cr.date)

print(new_data)