import gspread
from oauth2client.service_account import ServiceAccountCredentials

def open_sheet(spreadsheet_url) :
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    json_file_name = 'spreadsheet-301116-287ef71ecaa0.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)

    doc = gc.open_by_url(spreadsheet_url) # load spread sheet
    print('spreadsheet_url:', spreadsheet_url)
    return doc