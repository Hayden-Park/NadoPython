import time
import commands as cmd
import win_control as win

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

def run():
    cmd.init_click()
    cmd.open_extensions()
    cmd.find_image(root,'extension_run',delay*5,True)
    if not cmd.find_image(root,'wallet_open_done',delay*3,False):
        if cmd.find_image(root,'welcome_back_password',delay*5,False):
            cmd.copy_text(pw)
            cmd.hotkey('ctrl','v')
            cmd.press_tab(1)
            cmd.press_enter()
            init_popup()
    run_success = cmd.find_image(root,'change_network',delay*5,False)
    return run_success
    
def init_popup():
    if cmd.find_image(root,'whats_new_try_it_out',delay*2,True):
        cmd.find_image(root,'swap_no_thanks',delay*5,True)
        cmd.find_image(root,'swap_backward',delay*2,True)
        cmd.find_image(root,'whats_new_close',delay,True)
        cmd.find_image(root,'protect_your_funds_got_it',delay,True)
        if cmd.find_image(root,'network_switcher_got_it',delay,True):
            cmd.find_image(root,'network_switcher_got_it',delay,True)
            cmd.find_image(root,'network_switcher_got_it',delay,True)
        cmd.find_image(root,'whats_new_close',delay,True)

def import_existing_wallet(recovery_phrase):
    result = ''
    if cmd.find_image(root,'lets_get_started',delay*5,True):
        cmd.press_tab(5)
        cmd.press_space(1)
        cmd.press_tab(3)
        cmd.press_enter()
        cmd.find_image(root,'import_i_agree',delay*3,True)
        cmd.find_image(root,'recovery_first',delay*3,True)
        rec_list = recovery_phrase.split(' ')
        for i,word in enumerate(rec_list):
            cmd.copy_text(word)
            cmd.hotkey('ctrl','v')
            cmd.wait(delay*0.25)
            cmd.press_tab(2)
        cmd.wait(delay*0.25)
        cmd.press_enter()
        cmd.find_image(root,'create_password',delay*5,True)
        cmd.press_tab(2)
        cmd.copy_text(pw)
        cmd.hotkey('ctrl','v')
        cmd.press_tab(1)
        cmd.copy_text(pw)
        cmd.hotkey('ctrl','v')
        cmd.press_tab(1)
        cmd.press_space(1)
        cmd.press_tab(2)
        cmd.press_enter()
        cmd.wait(delay*5)
        cmd.find_image(root,'wallet_creation_successful',delay*5,True)
        cmd.find_image(root,'wallet_creation_got_it',delay*2,True)
        cmd.find_image(root,'wallet_creation_next',delay*3,True)
        cmd.find_image(root,'wallet_creation_done',delay*3,True)
        if cmd.find_image(root,'import_final_whats_new',delay*5,True):
            cmd.find_image(root,'import_try_it_out',delay*3,True)
            cmd.find_image(root,'no_thanks',delay*3,True)
            cmd.close_window()
    else:
        result = 'import failed'
    return result

def expand_view():
    result = False
    if run():
        cmd.wait(delay)
        cmd.press_tab(4)
        cmd.press_enter()
        result = cmd.find_image(root,'expand_view',delay*5,True)
    return result

def change_network(network):
    result = ''
    cnt = 0
    if expand_view():
        cmd.find_image(root,'add_network_logo',delay*10,False)
        cmd.init_click()
        cmd.press_tab(2)
        cmd.press_enter()
        cmd.find_image(root,'select_search',delay*3,False)
        cmd.wait(delay*0.5)
        cmd.typetext(network)
        cmd.press_tab(2)
        cmd.press_enter()
        cmd.find_image(root,'change_network_got_it',delay*2,True)
        cmd.find_image(root,'change_network',delay*5,False) # 완료 대기
        cmd.close_window()
    else:
        result += 'could not run metamask' + '\n' 
    return result

def add_network(networks):
    result = ''
    if expand_view():
        cmd.find_image(root,'add_network_logo',delay*10,False)
        for network in networks:
            name = 'add_' + network
            cmd.init_click()
            cmd.press_tab(2)
            cmd.press_enter()
            if not cmd.find_image(root,'add_network',delay*2,True):
                cmd.find_image(root,'add_network_2',delay*2,True)
            
            if cmd.find_image(root,name,delay*2,True):
                cmd.press_tab(1)
                cmd.press_enter()
                cmd.find_image(root,'add_approve',delay*3,True)
                cmd.find_image(root,'add_success',delay*5,False)
                cmd.find_image(root,'add_dismiss',delay*3,True)
            else:
                result += '{0} not added'.format(network) + '\n'
        cmd.wait(delay)
        cmd.close_window()
    else:
        result += 'could not run metamask' + '\n' 
    return result



def unlock(pw):
    cmd.typewrite(pw)
    cmd.press_tab(1)
    cmd.press_enter()

def create_wallet(pw):
    run()       # wait for 10sec, page loading
    cmd.init_click()
    cmd.press_tab(8)
    cmd.press_space(1) # check 'I agree'
    cmd.press_tab(2)
    cmd.press_enter() # create a new wallet
    cmd.press_tab(3)
    cmd.press_enter() # I agree
    cmd.typewrite(pw) # password
    cmd.press_tab(1)
    cmd.typewrite(pw) # repeat password
    cmd.press_tab(1)
    cmd.press_space(1) # check 'I understand'
    cmd.press_tab(2)
    cmd.press_enter() # create a new wallet
    time.sleep(delay*2)
    cmd.press_tab(9)
    cmd.press_enter() # secure my wallet
    cmd.init_click()
    cmd.press_tab(3)
    cmd.press_enter() # Reveal secret recovery phrase
    cmd.init_click()
    cmd.press_tab(4)
    cmd.press_enter() # copy to clipboard
    cmd.press_tab(1)
    cmd.press_enter() # next
    phrase = cmd.paste()
    rec_list = phrase.split(' ')
    pos_list = [[318,498],[482,498],[653,498],[318,545],[482,545],[653,545],[318,594],[482,594],[653,594],[318,638],[482,638],[653,638]]
    for i,word in enumerate(rec_list):
        cmd.click(x=pos_list[i][0],y=pos_list[i][1])
        cmd.typewrite(word)
        time.sleep(delay*0.25)
    cmd.init_click()
    cmd.press_tab(6)
    cmd.press_enter()   # phrase confirm
    cmd.init_click()
    cmd.press_tab(5)
    cmd.press_enter()   # successful got it
    cmd.init_click()
    cmd.press_tab(6)
    cmd.press_enter()   # next
    time.sleep(delay)
    cmd.click(291,862)  # try it out
    time.sleep(delay*2)
    cmd.click(478,785)  # no thanks
    cmd.hotkey('ctrl','w')
    run(delay*5)
    cmd.find_image(root,'metamask_whats_new_x',delay*5,True) # what's new close
    cmd.press_tab(1)
    cmd.press_enter()   # what's new got it
    # close initial popup
    for i in range(3):
        cmd.find_image(root,'metamask_network_switcher_got_it',delay*5,True)
    cmd.press_esc()

def pin_to_extensions():
    cmd.open_extensions()
    cmd.press_tab(11)
    cmd.press_enter() # pin MetaMask to extensions
    cmd.press_esc()
    time.sleep(delay)

def get_recovery_phrase(pw):
    run()        
    cmd.wait(delay*5)   # wait for 5sec
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.click(690,418) # settings
    cmd.press_tab(5)
    cmd.press_enter() # security & privacy
    cmd.press_tab(1)
    cmd.press_enter() # reveal secret recovery phrase
    cmd.press_tab(1)
    cmd.press_enter() # get started
    cmd.press_tab(2)
    cmd.press_enter() # can't help you
    cmd.press_tab(1)
    cmd.press_enter() # continue
    cmd.press_tab(1)
    cmd.press_enter() # you're being scammed
    cmd.press_tab(1)
    cmd.press_enter() # continue
    cmd.typewrite(pw)
    cmd.press_enter() # enter password and next
    cmd.click_hold(640,395,2) # click and hold to reveal SRP
    time.sleep(delay*2)
    cmd.press_tab(9)
    cmd.press_enter() # copy to clipboard
    cmd.press_tab(1)
    cmd.press_enter() # close
    cmd.press_esc()
    time.sleep(delay)
    return cmd.paste()
    
def get_wallet_address():
    run()
    cmd.wait(delay*5)   # wait for 5sec
    cmd.press_tab(5)
    cmd.press_enter() # copy wallet
    cmd.press_esc()
    time.sleep(delay)
    return cmd.paste()

def export_txn():
    run()
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.find_image(root,'setting_view_on_explorer',delay*5,True)
    cmd.find_image(root,'log_tab_transactions',delay*5,True)
    cmd.scroll(-1500)
    cmd.find_image(root,'log_csv_export',delay*5,True)
    cmd.find_image(root,'not_robot',delay*5,True)
    cmd.find_image(root,'not_robot_confirm',delay*5,False)
    cmd.find_image(root,'log_download',delay*5,True)

def mint_confirm():
    cnt = 0
    found = False
    if select_metamask():
        while found==False and cnt < 20:
            cmd.find_image(root,'mint_confirm',delay,True)
            found = cmd.find_image(root,'confirmed_transaction',delay,False)
            if not found:
                if cmd.find_image(root,'failed_transaction',delay,False):
                    cnt = 20
            cnt +=1
        if cnt >= 20:
            print('transaction failed')
    return found

# 230930_신규 mint 기능 추가, 시작/완료 사진 입력으로 받기
def mint(root_work=None,img_request=None,img_complete=None,time_request=5,time_complete=60):
    cnt = 0
    found = False
    if img_request is not None:
        cmd.find_image(root_work,img_request,delay*time_request,True)
    if select_metamask():
        while found==False and cnt < 20:
            cmd.find_image(root,'mint_confirm',delay,True)
            found = cmd.find_image(root,'confirmed_transaction',delay,False)
            if not found:
                if cmd.find_image(root,'failed_transaction',delay,False):
                    cnt = 20
            cnt +=1
        if cnt >= 20:
            print('transaction failed')
    if img_complete is not None and found == False:
        found = cmd.find_image(root_work,img_complete,delay*time_complete,False)    
        if found == False:
            mint(root_work,img_request,img_complete,time_request,time_complete)
    return found


def connect_wallet():
    result = False
    if select_metamask():
        cmd.find_image(root,'connect_next',delay*10,True)
        cmd.wait(delay*0.5)
        result = cmd.find_image(root,'connect_connect',delay*10,True)
    return result

def connect_wallet_sign():
    repeat = 0
    while repeat < 60:
        if cmd.find_image(root,'connect_sign',delay*3,True):
            repeat = 60
        else:
            repeat += 1
    cmd.wait(delay)

def sign():
    result = False
    if select_metamask():
        cmd.find_image(root,'sign_arrow',delay*3,True)
        cmd.find_image(root,'scroll_down',delay*3,True)
        cmd.press_down(5)
        cmd.wait(delay)
        result = cmd.find_image(root,'connect_sign',delay*5,True)
    return result

def add_token():
    result = False
    if select_metamask():
        result = cmd.find_image(root,'add_token',delay*30,True)
    return result

def allow_to_add_network():
    result = False
    if select_metamask():
        cmd.find_image(root,'add_approve',delay*10,True)
        result = cmd.find_image(root,'switch_network',delay*10,True)
    return result

def allow_switch():
    result = False
    if select_metamask():
        if cmd.find_image(root,'switch_network',delay*10,True):
            result = True
    return result

def liquidity():
    result = False
    if select_metamask():
        cmd.wait(delay*3)
        if cmd.find_image(root,'liquidity_max',delay*30,True):
            cmd.wait(delay*3)
            cmd.find_image(root,'liquidity_next',delay*5,True)
            cmd.wait(delay)
            cmd.find_image(root,'liquidity_approve',delay*5,True)
            result = cmd.find_image(root,'confirmed_transaction',delay*60,False)
    return result

def select_metamask():
    cmd.find_image(root,'wait_popup',delay*5,False)
    result = cmd.focus_window('MetaMask Notification')
    return result
