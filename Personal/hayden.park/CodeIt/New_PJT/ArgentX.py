import time
import commands as cmd

delay = 1

def run(operating_delay):
    cmd.open_extensions()
    cmd.press_tab(2) # select Argent X
    cmd.press_enter()
    time.sleep(operating_delay) # wait 2sec for running

def unlock(pw):
    cmd.typewrite(pw)
    cmd.press_tab(1)
    cmd.press_enter()

def create_wallet(pw):
    run(delay*3)            # wait for 3sec
    cmd.init_click()
    cmd.press_tab(1)
    cmd.press_enter() # Create a new wallet
    cmd.click(89,552) # check 1
    cmd.click(81,655) # check 2
    cmd.press_tab(1)
    cmd.press_enter() # continue
    time.sleep(delay*2)
    cmd.typewrite(pw) # password
    cmd.press_tab(1)
    cmd.typewrite(pw) # repeat password
    cmd.press_tab(1)
    cmd.press_enter() # create wallet
    time.sleep(delay*3)
    cmd.init_click()
    cmd.press_tab(3)
    time.sleep(delay)
    cmd.press_enter() # finish
    time.sleep(delay)

def pin_to_extensions():
    cmd.open_extensions()
    cmd.press_tab(3)
    cmd.press_enter() # pin ArgentX to extensions
    cmd.press_esc()
    time.sleep(delay)

def init_recovery_phrase():
    run(delay*3)              # wait for 3sec
    cmd.press_tab(5)
    cmd.press_enter()
    time.sleep(delay*2) # wait 2sec
    cmd.find_image('argentx_copy_phrase.png',delay*5,True)
    cmd.find_image('argentx_phrase_confirm.png',delay*5,True)
    cmd.press_tab(1)
    cmd.press_enter()
    cmd.press_esc()
    time.sleep(delay)
    return cmd.paste()

def get_recovery_phrase(pw):
    run(delay*3)        # wait for 3sec
    cmd.press_tab(3)
    cmd.press_enter()
    time.sleep(delay)
    cmd.press_tab(8)
    cmd.press_enter()
    cmd.typewrite(pw)
    cmd.press_enter()
    time.sleep(delay*2.5) # wait 2sec
    cmd.click(640,500) # copy recovery phrase
    cmd.press_esc()
    time.sleep(delay)
    return cmd.paste()

    
def get_wallet_address():
    run(delay*3)        # wait for 3sec
    cmd.press_tab(4)
    cmd.press_enter()
    cmd.press_esc()
    time.sleep(delay)
    return cmd.paste()

