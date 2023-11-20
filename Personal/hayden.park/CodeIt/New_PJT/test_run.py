from common import commands as cmd
import pyautogui as pag
import time
from common import csv_handling as csv

# while True:
#     pos = pag.position()
#     print(pos)
#     time.sleep(1)

# data = csv.get_csv_data('gmail_list.csv')

# start = 1
# end = 100
# idlist = data['ID_twit'][start-1:end]
# print(idlist)
# print(idlist[49])
# var = cmd.get_random(180,300,2)
# print(float(var))

#랜덤사진 저장하기
# url = 'https://picsum.photos/250/250'
# for i in range(31,101):
#     cmd.init_click()
#     cmd.hotkey('alt','d')
#     cmd.typetext(url)
#     cmd.press_enter()
#     cmd.wait(2)
#     cmd.click_right(480,570)

#     filepath = r'C:\Users\Min-Lenovo\OneDrive - Atlas Copco Vacuum Technique\Desktop\image_saveas.png'
#     loc = pag.locateOnScreen(filepath,grayscale=True,confidence=0.87)
#     cntr = pag.center(loc)
#     pag.moveTo(cntr)
#     pag.click(cntr)
#     cmd.wait(2)
#     cmd.hotkey('alt','n')
#     cmd.hotkey('ctrl','a')
#     cmd.press('del')
#     cmd.typetext(str(i))
#     cmd.press_enter()
#     cmd.wait(2)

