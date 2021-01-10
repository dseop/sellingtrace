import gspread
from oauth2client.service_account import ServiceAccountCredentials

import crawling as cr
import get_book_info as gbi

print('open the sheet')
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
json_file_name = 'spreadsheet-301116-287ef71ecaa0.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Mddr6g9Oid4_2R5mwQRC4N8NB05uLaO0jtT7SxTXwZc/edit#gid=0'
doc = gc.open_by_url(spreadsheet_url) # load spread sheet
print('ok')

# # 이런 식으로 불러올 수도 있나봄
    # gc1 = gc.open("python-linkage-sample").worksheet('시트1')
    # gc2 = gc1.get_all_values()
    # print(gc2)

print('make code_list')
worksheet = doc.worksheet('YES24') # select sheet
list_of_lists = worksheet.get_all_values()
# print(list_of_lists)
# list_of_lists = ['날짜', '코드'], ['', '96195306'], ['2021-1-10', '15,414']

# http://www.yes24.com/Product/Goods/96195306
# cell_data = worksheet.acell('B2').value # load 1 cell 
code_list = list_of_lists[1][1:] # list
# values_list = worksheet.row_values(1) # load row
print(code_list)
print('ok')

print('make new data')
raw_data = gbi.yes24(gbi.mak_url_list(code_list)) # raw_data는 모든 yes24의 책 정보를 다 가져옴 # pandas Series type
new_data = list(raw_data['지수']) # list
new_data.insert(0, cr.date) # insert today's date
print(new_data)
worksheet.append_row(new_data) # insert row below end line
print('ok')

# # load row
# row_data = worksheet.row_values(1)
# print(row_data)
# # result # ['a1', 'b1', 'c1', 'd1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# # load column
# column_data = worksheet.col_values(1)
# print(column_data)

# # 범위(셀 위치 리스트) 가져오기
# range_list = worksheet.range('A1:D2')
# print(range_list)
# # result # [<Cell R1C1 'a1'>, <Cell R1C2 'b1'>, <Cell R1C3 'c1'>, <Cell R1C4 'd1'>, <Cell R2C1 'a2'>, <Cell R2C2 'b2'>, <Cell R2C3 'c2'>, <Cell R2C4 'd2'>]

# # 범위에서 각 셀 값 가져오기
# for cell in range_list:
#     print(cell.value) 

# # insert data
# # save cell
# worksheet.update_acell('B1', 'b1 updated')

# worksheet.append_row(['new1','new2','new3','new4'])
# worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 4) # specific line

# # resize sheet size
# worksheet.resize(10,4)

# # create new sheet
# gs = gc.create('새로운 테스트')
# # 시트를 새로 생성하고 싶다면 add_worksheet를 사용해서 시트 이름과 사이즈를 지정해줄 수도 있다.
# worksheet = gs.add_worksheet(title='시트1', rows='1', cols='1') 
# # 아래와 같이 하면 다른 사람에게 그 문서를 공유하고 소유권을 이전한다.
# gs.share('hleecaster@gmail.com', perm_type='user', role='owner')


