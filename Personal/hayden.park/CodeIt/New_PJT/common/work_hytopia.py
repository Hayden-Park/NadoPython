import commands as cmd

# 230917_email 입력
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'
url = 'https://preregister.hytopia.com/Lminol'

def open_url(url):
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.wait(delay)

def action1(index, username, email):
    result = ''
    open_url(url)
    cmd.find_image(root,'wait_loading',delay*20,False)
    cmd.init_click()
    cmd.press_tab(2)
    cmd.copy_text(username)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*0.5)
    cmd.press_tab(1)
    cmd.copy_text(email)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*0.5)
    cmd.press_tab(1)
    cmd.press_enter()
    if cmd.find_image(root,'success',delay*30,True):
        cmd.close_window()
        result = "{0} {1} : done".format(index,username)
    else:
        result = "{0} {1} : not finished".format(index,username)
    return result
    
# cmd.init_click()
# action1(2,'aggievaggno','aggievaggno@gmail.com')
