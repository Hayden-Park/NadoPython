# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'\\common')
import commands as cmd

# 230911_gmail 입력하기 작업
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

def enter_gmail(url,gmail):
    cmd.init_click()
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.find_image(root,'grvt_main',delay*30,False)
    cmd.init_click()
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.find_image(root,'grvt_email_address',delay*30,True)
    cmd.copy_text(gmail)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.find_image(root,'grvt_thank_you',delay*30,False)
    cmd.close_window()

# url = 'https://grvt.io'
# gmail = 'ad8428903@gmail.com'
# enter_gmail(url,gmail)
