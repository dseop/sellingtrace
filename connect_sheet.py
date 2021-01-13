import gspread
from oauth2client.service_account import ServiceAccountCredentials

def open_sheet() :
    print('open the sheet')
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    json_file_name = 'spreadsheet-301116-287ef71ecaa0.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)

    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Mddr6g9Oid4_2R5mwQRC4N8NB05uLaO0jtT7SxTXwZc/edit#gid=0'
    doc = gc.open_by_url(spreadsheet_url) # load spread sheet
    print('ok')

    return doc