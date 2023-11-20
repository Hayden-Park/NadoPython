import time
import commands as cmd


delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

def run_gmail():
    cmd.init_click()
    cmd.new_tab()       # open new tab
    cmd.init_click()
    cmd.press_alt() 
    cmd.press_down(1)   # open setting menus
    cmd.press('b','i','i')  # open bookmarks tree and inbox gmail
    cmd.press_enter() 
    cmd.find_image(root,'gmail_main_logo',delay*30,False)
    

def signin(email,pw,recovery_email):
    if cmd.find_image(root,'google_login_box_border',delay*10,False):
        cmd.init_click()
        cmd.press_tab(1)
        cmd.copy_text(email)
        cmd.hotkey('ctrl','v')  # type email address
        cmd.press_tab(3)
        cmd.press_enter()
        cmd.find_image(root,'google_login_box_border',delay*10,True)
        cmd.copy_text(pw)
        cmd.hotkey('ctrl','v')  # type pw
        cmd.press_tab(2)
        cmd.press_enter()
        if cmd.find_image(root,'google_login_recovery_email_icon',delay*10,False):
            cmd.press_tab(5)
            cmd.press_enter()   # confirm your recovery email
            cmd.find_image(root,'google_login_enter_recovery',delay*10,False)
            cmd.init_click()
            cmd.press_tab(3)
            cmd.copy_text(recovery_email)
            cmd.hotkey('ctrl','v')  # type recovery email
            cmd.press_tab(1)
            cmd.press_enter()
        else:
            print('"{}" is not first login, recovery email not required.'.format(email))
        print('{} login completed.'.format(email))
        time.sleep(delay)

    
def popup_save_pw():
    cmd.find_image(root,'chrome_popup_save_password',delay*20,True)
    cmd.press_tab(1)
    cmd.press_enter()
    time.sleep(delay)


def signin_first(email,pw,recovery_email):
    cmd.init_click()
    cmd.new_tab()
    time.sleep(delay*5)
    cmd.init_click()
    cmd.press_tab(1)    
    cmd.press_enter()   # click gmail button
    time.sleep(delay*5)
    # cmd.init_click()
    # cmd.press_tab(3)    
    # cmd.press_enter()   # click login button
    # time.sleep(delay*5)
    signin(email,pw,recovery_email)

def change_password(email,pw_old,pw_new,recovery_email):
    cmd.init_click()
    time.sleep(delay)
    cmd.new_tab()
    cmd.find_image(root,'google_apps',delay*20,False)
    cmd.init_click()
    cmd.press_tab(3)
    cmd.press_enter()       # google menus
    cmd.find_image(root,'google_apps_wait_loading',delay*20,False)
    cmd.press_enter()       # google account

    if not cmd.find_image(root,'google_account_security',delay*10,False): # not logged in
        if cmd.find_image(root,'google_goto_account_btn',delay*5,False):
            cmd.init_click()
            cmd.press_tab(7)
            cmd.press_enter()       # google 계정으로 이동
            if cmd.find_image(root,'google_login_previous_gmail',delay*5,False):
                cmd.find_image(root,'google_login_previous_gmail',delay*5,True)
                if cmd.find_image(root,'google_login_box_border_filled',delay*20,False):
                    cmd.init_click()
                    cmd.press_tab(4)
                    cmd.press_enter()   # next
            else:
                signin(email,pw_old,recovery_email)
        else:
            print('Already logged in')       
    cmd.find_image(root,'google_account_security',delay*20,True)
    cmd.find_image(root,'google_password_change',delay*20,True) # password 변경
    
    if not cmd.find_image(root,'google_security_password_unhidden',delay*5,False):
        cmd.find_image(root,'google_login_box_border_filled',delay*5,False)
        cmd.init_click()
        cmd.press_tab(4)
        cmd.press_enter()   # next
    cmd.find_image(root,'google_security_password_unhidden',delay*5,False)
    cmd.copy_text(pw_new)
    cmd.hotkey('ctrl','v')  # type pw
    cmd.press_tab(3)
    cmd.hotkey('ctrl','v')  # type pw confirm
    cmd.press_tab(2)
    cmd.press_enter()
    popup_save_pw()
    cmd.find_image(root,'google_password_change',delay*20,False)
    cmd.close_window()
    print('{} password changed.'.format(email))

def security_alert():
    run_gmail()
    if cmd.find_image(root,'gmail_security_alert',delay*5,True):
        cmd.find_image(root,'gmail_check_activity',delay*10,True)
        if cmd.find_image(root,'gmail_already_checked_ok',delay*5,False):
            cmd.find_image(root,'gmail_already_checked_ok',delay*5,True)
        else:
            cmd.find_image(root,'gmail_yes_it_was_me',delay*10,True)
        time.sleep(delay)
        cmd.close_window()
        cmd.find_image(root,'gmail_notifications_no_thanks',delay*5,True)
        cmd.close_window()
        time.sleep(delay)
        print('Security alert email checked.')
    else:
        print('Security alert email already checked.')

def get_vericode_twitter():
    run_gmail()                  
    cmd.find_image(root,'gmail_is_your_x',delay*5,True)
    time.sleep(delay)
    cmd.find_image(root,'gmail_please_enter_this_verification_codes',delay*5,True)
    x,y = cmd.get_position()
    cmd.doubleclick(x,y)
    cmd.copy()
    cmd.close_window()
    return cmd.paste()

