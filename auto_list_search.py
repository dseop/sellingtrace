# search book title list #

import pyautogui
# pyautogui.mouseInfo()
# import pyperclip

# title_list = []
# pyautogui.mouseInfo()
# pyautogui.sleep(2)

og_point = pyautogui.position()
pyautogui.click(1340, 261, duration=0.25)
# pyautogui.mouseDown()
# pyautogui.mouseUp()

pyautogui.hotkey('ctrl', 'a', duration=0.25)
pyautogui.hotkey('ctrl', 'v')
# pyautogui.keyDown('ctrl') # 위와 같은 동작
# pyautogui.press('v')
# pyautogui.keyUp('ctrl')

# pyautogui.press('enter')
# pyautogui.locateOnScreen()

pyautogui.keyDown('ctrl')
pyautogui.click(1462, 299, duration=0.25)
pyautogui.keyUp('ctrl')

pyautogui.moveTo(og_point, duration=0.25)
# pyautogui.moveTo(432, 136, duration=0.25)
# pyautogui.hotkey('alt', 'tab', duration=0.25)

# pyautogui.press('down')
# pyautogui.hotkey('ctrl', 'c')

# title1 = pyperclip.paste()
# if title2 != title1 :
#     title2 = title1
# else if title2 == title1 :
    
# python auto_list_search.py