import pyautogui as pag
import clipboard
import time
import os
import random
import win32gui

delay01 = 0.1
interval = 0.01
image_folder = r'C:\Projects\NadoPython\Personal\hayden.park\CodeIt\New_PJT\image'
root_commands = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']

def wait(sec):
    time.sleep(sec)

def init_click():
    pag.click(x=2, y=125)
    time.sleep(delay01)

def open_url(url):
    init_click()
    new_tab()
    hotkey('alt','d')
    typetext(url)
    press_enter()

def open_setting():
    find_image(root_commands,'chrome_setting',delay01*30,True)
    time.sleep(delay01)

def open_extensions():
    init_click() # select chrome window
    find_image(root_commands,'extensions',delay01*30,True)
    time.sleep(delay01)
    
def screen_left():
    pag.hotkey('win','left')
    time.sleep(delay01*5)
    pag.press('esc')
    init_click()
    time.sleep(delay01)

def screen_full():
    find_image(root_commands,'chrome_full_screen',3,True)
    init_click()
    time.sleep(delay01)

def typetext(text):
    wait(delay01*5)
    copy_text(text)
    hotkey('ctrl','v')
    wait(delay01*5)

def new_window():
    pag.hotkey('ctrl','n')
    time.sleep(delay01)

def close_window():
    pag.hotkey('ctrl','w')
    time.sleep(delay01)


def new_tab():
    pag.hotkey('ctrl','t')
    time.sleep(delay01)

def go_homepage():
    pag.press('browserhome')

def press(*key):
    for x in key:
        pag.press(x)
    time.sleep(delay01)

def press_tab(cnt):
    pag.press('tab',presses=cnt,interval=interval)
    time.sleep(delay01)

def press_shifttab(cnt):
    pag.keyDown('shift')
    time.sleep(delay01)
    pag.press('tab',presses=cnt,interval=interval)
    time.sleep(delay01)
    pag.keyUp('shift')
    time.sleep(delay01)

def press_up(cnt):
    pag.press('up', presses=cnt,interval=interval)
    time.sleep(delay01)

def press_down(cnt):
    pag.press('down', presses=cnt,interval=interval)
    time.sleep(delay01)

def press_left(cnt):
    pag.press('left', presses=cnt,interval=interval)
    time.sleep(delay01)

def press_right(cnt):
    pag.press('right', presses=cnt,interval=interval)
    time.sleep(delay01)

def press_space(cnt):
    pag.press('space',presses=cnt,interval=interval)
    time.sleep(delay01)

def press_enter():
    pag.press('enter')
    time.sleep(delay01)

def press_esc():
    pag.press('esc')
    time.sleep(delay01)

def press_alt():
    pag.press('alt')
    time.sleep(delay01)

def hotkey(*key):
    pag.hotkey(key)
    time.sleep(delay01)

def typewrite(text):
    pag.typewrite(text,interval=interval)
    time.sleep(delay01)

def click(x,y):
    pag.click(x,y)
    time.sleep(delay01)

def click_right(x,y):
    pag.rightClick(x,y)
    time.sleep(delay01)

def click_hold(x,y,duration):
    pag.mouseDown(x,y,duration=duration)
    time.sleep(delay01)

def doubleclick(x,y):
    pag.doubleClick(x,y)
    time.sleep(delay01)

def moveRel(x,y,click):
    pag.moveRel(x,y)
    x2,y2 = pag.position()
    if click == True:
        pag.click(x2,y2)

def scroll(num):
    pag.scroll(num)
    time.sleep(delay01)

def point_image(root,filename,timeout):
    found = False
    count = 0
    filepath = os.path.normpath(image_folder+'\\'+root+'\\'+filename+'.png')
    while (found==False) and (count < timeout):
        loc = pag.locateOnScreen(filepath,grayscale=True,confidence=0.9)
        try:
            x,y = pag.center(loc)
            pag.moveTo(x,y)
            found = True
        except:
            x,y = 0,0
            count += 1
            time.sleep(delay01*10)
    if not found:
        print("{} not found".format(filename))
    return found

def copy():
    pag.hotkey('ctrl','c')
    time.sleep(delay01)

def copy_text(text):
    clipboard.copy(text)

def paste():
    return clipboard.paste()

def find_image(root,filename,timeout=5,click=True):
    found = False
    count = 0
    filepath = os.path.normpath(image_folder+'\\'+root+'\\'+filename+'.png')
    while (found==False) and (count < timeout):
        loc = pag.locateOnScreen(filepath,grayscale=True,confidence=0.87)
        try:
            cntr = pag.center(loc)
            found=True
            pag.moveTo(cntr)
            if click == True:
                time.sleep(delay01*5)
                pag.click(cntr)
        except:
            count += 1
            time.sleep(delay01*10)
    if not found:
        print("{} not found".format(filename))
    time.sleep(delay01*5)
    return found

def find_image_rate(root,filename,timeout=5,click=True,rate=50):
    found = False
    count = 0
    filepath = os.path.normpath(image_folder+'\\'+root+'\\'+filename+'.png')
    rate = rate/100
    while (found==False) and (count < timeout):
        loc = pag.locateOnScreen(filepath,grayscale=True,confidence=0.87)
        try:
            pos = (loc.left+loc.width*rate,loc.top+loc.height/2)
            found=True
            pag.moveTo(pos)
            if click == True:
                time.sleep(delay01*5)
                pag.click(pos)
        except:
            count += 1
            time.sleep(delay01*10)
    if not found:
        print("{} not found".format(filename))
    time.sleep(delay01*10)
    return found

def get_position():
    x,y = pag.position()
    return x,y

def get_random(lower,upper,digit):
    amount = round((upper-lower) * random.random() + lower,digit)
    return str(amount)

# 현재 실행중인 윈도우 핸들 목록 가져오기
def get_window_hwnd_list():
    def callback(_hwnd, _result: list):
        title = win32gui.GetWindowText(_hwnd)
        if win32gui.IsWindowEnabled(_hwnd) and win32gui.IsWindowVisible(_hwnd) and title is not None and len(title) > 0:
            _result.append(_hwnd)
        return True
    result = []
    win32gui.EnumWindows(callback, result)
    return result

# 타이틀 일부 문자열을 기준으로, 특정 윈도우 핸들을 찾을 때까지 대기하기
def wait_for_window_hwnd(_part_of_title: str):
    result = None
    cnt = 0
    while result is None and (cnt < 30): # timeout 30초
        hwnd_list = get_window_hwnd_list()
        for hwnd in hwnd_list:
            title = win32gui.GetWindowText(hwnd)
            if title is not None and len(title) > 0:
                if title.find(_part_of_title) > -1:
                    result = hwnd
                    break
        time.sleep(1)        # 1초 대기
        cnt += 1
    return result

# 특정 윈도우 핸들을 포커스/포커싱 처리하기
def focus_window_hwnd(_hwnd):
    result = False
    if _hwnd is not None:
        while True:
            win32gui.ShowWindow(_hwnd, 3) # 최대화
            win32gui.SetForegroundWindow(_hwnd)
            if str(_hwnd) == str(win32gui.GetForegroundWindow()):
                break
            else:
                time.sleep(1)
        result = True
    return result

# 현재 실행중인 윈도우 핸들 타이틀 가져오기
def get_foreground_window_text():
    title = ""
    current_hwnd = win32gui.GetForegroundWindow()
    if current_hwnd is not None:
        title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return title

def focus_window(title):
    result = False
    hwnd = wait_for_window_hwnd(title)
    if hwnd is not None:
        focus_window_hwnd(hwnd)
        time.sleep(delay01*5)
        screen_left()
        time.sleep(delay01*5)
        result = True
    else:
        print(title,'not found')
    return result
