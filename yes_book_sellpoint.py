num_code = """
96195306
"""
url ="""
http://www.yes24.com/Product/Goods/96195306
"""

bookcode = []
bookcode.append(num_code)

# load spreadsheet data

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'vast-ethos-251302-b8a92651b359.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1j83Zex9AdiHad-LkmnndHdvZdu25KupZCmMdtqwCjCY/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('시트1')