import time
import commands as cmd
import win_control as win
import csv_handling as csv

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
data = csv.get_csv_data('gmail_list.csv')
pw = '12341234'

def run():
    cmd.init_click()
    cmd.open_extensions()
    cmd.find_image(root,'extension_run',delay*5,True)
    restore()
    if cmd.find_image(root,'welcome_back_password',delay*3,False):
        cmd.copy_text(pw)
        cmd.hotkey('ctrl','v')
        cmd.press_tab(1)
        cmd.press_enter()
    show_recovery_init()
    if not cmd.find_image(root,'setting',delay*3,False):
        cmd.find_image(root,'enjoying_close',delay*2,True)
    run_success = cmd.find_image(root,'setting',delay*3,False)
    return run_success

def show_recovery_init():
    phrase = ''
    if cmd.find_image(root,'show_recovery_phrase',delay*3,True):
        cmd.find_image(root,'click_to_reveal',delay*5,True)
        cmd.find_image(root,'recovery_copy',delay*5,True)
        cmd.find_image(root,'recovery_confirm',delay*5,True)
        cmd.wait(delay)
        cmd.press_tab(1)
        cmd.press_enter()
        phrase = cmd.paste()
    return phrase
        
def connect_wallet():
    result = False
    if select_argentx():
        result = cmd.find_image(root,'connect',delay*10,True)
    return result

def select_argentx():
    result = False
    hwnd = win.wait_for_window_hwnd('ArgentX')
    if hwnd is not None:
        win.focus_window_hwnd(hwnd)
        result = True
        cmd.wait(delay*0.5)
        cmd.screen_left()
    else:
        print('ArgentX not found')
    return result

def restore():
    if cmd.find_image(root,'welcome_to_argentx',delay*5,True):
        cmd.find_image(root,'restore',delay*3,True)
        i = int(win.get_foreground_window_text().split(' - ')[0]) - 1
        arg_recovery = data['argentx_recovery'][i].split(" ")
        cmd.find_image(root,'restore_1st',delay*5,True)
        for text in arg_recovery:
            cmd.typewrite(text)
            cmd.wait(delay*0.5)
            cmd.press_tab(1)
            cmd.wait(delay*0.5)
        cmd.find_image(root,'restore_continue',delay*5,True)
        if cmd.find_image(root,'restore_new_password',delay*5,True):
            cmd.press_tab(1)
            cmd.wait(delay*0.5)
            cmd.typewrite(pw)
            cmd.wait(delay*0.5)
            cmd.press_tab(1)
            cmd.wait(delay*0.5)
            cmd.typewrite(pw)
            cmd.find_image(root,'restore_continue',delay*5,True)
            cmd.find_image(root,'restore_finish',delay*20,True)

def mint(root_work=None,img_request=None,img_complete=None,time_request=5,time_complete=60):
    cnt = 0
    found = False
    # msg_success = ['mint_approve','confirmed_transaction','swap_approve','mint_succeeded']
    msg_success = ['transaction_popup']
    if img_request is not None:
        cmd.find_image(root_work,img_request,delay*time_request,True)
    if select_argentx():
        cmd.wait(delay)
        while found==False and cnt < 60:
            cmd.find_image(root,'mint_confirm',delay,True)
            for msg in msg_success:
                found = cmd.find_image(root,msg,delay*0.1,False)
                if found:
                    break
            # if not found:
            #     if cmd.find_image(root,'failed_transaction',delay,False):
            #         cnt = 30
            cnt +=1
        if cnt >= 60:
            print('transaction failed')
    if img_complete is not None and found == False:
        found = cmd.find_image(root_work,img_complete,delay*time_complete,False)    
    if found == False:
        mint(root_work,img_request,img_complete,time_request,time_complete)
    return found



# 초반에 만든부분들
def unlock(pw):
    cmd.typewrite(pw)
    cmd.press_tab(1)
    cmd.press_enter()

def create_wallet(pw):
    run()
    cmd.init_click()
    cmd.press_tab(1)
    cmd.press_enter() # Create a new wallet
    cmd.click(89,552) # check 1
    cmd.click(81,655) # check 2
    cmd.press_tab(1)
    cmd.press_enter() # continue
    cmd.wait(delay*2)
    cmd.typewrite(pw) # password
    cmd.press_tab(1)
    cmd.typewrite(pw) # repeat password
    cmd.press_tab(1)
    cmd.press_enter() # create wallet
    cmd.wait(delay*3)
    cmd.init_click()
    cmd.press_tab(3)
    cmd.wait(delay)
    cmd.press_enter() # finish
    cmd.wait(delay)

def pin_to_extensions():
    cmd.open_extensions()
    cmd.press_tab(3)
    cmd.press_enter() # pin ArgentX to extensions
    cmd.press_esc()
    cmd.wait(delay)

def init_recovery_phrase():
    run()
    cmd.press_tab(5)
    cmd.press_enter()
    cmd.find_image(root,'argentx_copy_phrase',delay*5,True)
    cmd.find_image(root,'argentx_phrase_confirm',delay*5,True)
    cmd.press_tab(1)
    cmd.press_enter()
    cmd.press_esc()
    cmd.wait(delay)
    return cmd.paste()

def get_recovery_phrase(pw):
    run()
    cmd.press_tab(3)
    cmd.press_enter()
    cmd.wait(delay)
    cmd.press_tab(8)
    cmd.press_enter()
    cmd.typewrite(pw)
    cmd.press_enter()
    cmd.wait(delay*2.5)
    cmd.click(640,500) # copy recovery phrase
    cmd.press_esc()
    cmd.wait(delay)
    return cmd.paste()

    
def get_wallet_address():
    run()
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.press_esc()
    cmd.wait(delay)
    return cmd.paste()

