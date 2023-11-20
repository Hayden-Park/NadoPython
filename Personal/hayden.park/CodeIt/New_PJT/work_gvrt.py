import commands as cmd
import time

# 230911_gmail 입력하기 작업
delay = 1

def enter_gmail(url,gmail):
    cmd.init_click()
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.waiting_for_image('grvt_main.png',30)
    cmd.init_click()
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.waiting_for_image('grvt_email_address.png',30)
    cmd.click_image('grvt_email_address.png')
    cmd.copy_text(gmail)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.waiting_for_image('grvt_thank_you.png',30)
    cmd.close_window()

# url = 'https://grvt.io'
# gmail = 'ad8428903@gmail.com'
# enter_gmail(url,gmail)
