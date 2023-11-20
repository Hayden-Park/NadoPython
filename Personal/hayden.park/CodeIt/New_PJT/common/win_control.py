import time
import win32gui

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

# hwnd_list = get_window_hwnd_list()

# index = 0
# for hwnd in hwnd_list:
#     print("index : " + str(index) + " / hwnd : " + str(hwnd) + " / title : " + win32gui.GetWindowText(hwnd))
#     index += 1
