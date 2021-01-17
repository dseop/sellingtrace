import pyautogui
import pyperclip
import datetime
from dateutil.relativedelta import relativedelta
# pyautogui.mouseInfo()
# pyautogui.sleep(3)
# 492,262
# 603,264
# 1878,293 # 조회
# 266,339 # 엑셀 저장

#pyautogui.click()
#pyautogui.position(100, y)

def excel(search, excel_down) :
    pyautogui.click(search)
    pyautogui.sleep(2)
    pyautogui.moveTo(excel_down)

def start(three_month) :
    pyautogui.click(three_month, duration=0.1)

def copy_pn_xy() : 
    pn = []
    xy = []
    for i in pyautogui.locateAllOnScreen('calendar_button.png') :
        pyautogui.moveTo(i,duration=0.1)
        pyautogui.move(-50, 0,duration=0.1)
        xy.append((pyautogui.position().x, pyautogui.position().y))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'c')
        pn.append(pyperclip.paste())
        # print(pn)
        # print(xy)
    return pn, xy

def go_back_3_month(pn) :
    convert_date = datetime.datetime.strptime(pn[0],"%Y-%m-%d").date()
    pn[0] = (convert_date - relativedelta(months=3)).strftime("%Y-%m-%d")
    convert_date = datetime.datetime.strptime(pn[1],"%Y-%m-%d").date()
    pn[1] = (convert_date - relativedelta(months=3)).strftime("%Y-%m-%d")
    return pn    

def paste_pn(pn, xy) :
    for i in [0, 1] : 
        pyperclip.copy(pn[i])
        pyautogui.moveTo(xy[i][0],xy[i][1], duration=0.1)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')

# 코드를 옆에 켜놓고 하는 게 가장 정확
three_month = pyautogui.locateOnScreen('3month_button.png')
search = pyautogui.locateOnScreen('search_button.png')
excel_down = pyautogui.locateOnScreen('excel_download_button.png')

start(three_month) # 3 month btn
excel(search, excel_down)

pn, xy = copy_pn_xy()
pn = go_back_3_month(pn) # pn_date = date - 3 month
paste_pn(pn, xy)

excel(search, excel_down)