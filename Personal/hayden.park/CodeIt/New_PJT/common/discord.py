import commands as cmd

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

def run():
    cmd.new_tab()
    cmd.open_setting()
    cmd.press('b','d')  # open bookmarks tree and discord
    cmd.wait(delay)

def add_friend(id):
    result = False
    cmd.find_image(root,'friends',delay*10,True)
    cmd.find_image(root,'btn_add_friend',delay*5,True)
    cmd.find_image(root,'add_friend',delay*5,True)
    cmd.press_tab(1)
    cmd.typetext(id)
    cmd.wait(delay*0.5)
    cmd.find_image(root,'send_friend_request',delay*5,True)
    if not cmd.find_image(root,'add_friend_success',delay*5,True):
        if not cmd.find_image(root,'already_friends',delay*5,True):
            result = True
        cmd.find_image(root,'friend_request_failed',delay*5,True)
        cmd.find_image(root,'okay',delay*5,True)    
    else:
        result = True
    return result

def accept_friend(interval=10):
    cmd.find_image(root,'friends',delay*10,True)
    cmd.find_image(root,'pending',delay*5,True)
    found = True
    while found:
        found = cmd.find_image(root,'accept_friend',delay*5,True)
        if found:
            interval = float(cmd.get_random(interval*0.7,interval*1.3,2))
            print('wait {0} secs for next friend...'.format(interval))
            cmd.wait(delay*interval)

def accept_invite():
    result = ''
    if cmd.find_image(root,'accept_invite_en',delay*30,True):
        if cmd.find_image(root,'setting',delay*30,True):
            cmd.close_window()
    elif cmd.find_image(root,'accept_invite_kr',delay*3,True):
        if cmd.find_image(root,'setting',delay*30,True):
            cmd.close_window()
    else:
        result = 'follow failed' + '\n'
    return result

def authorize():
    result = False
    cmd.focus_window('Authorize')
    if cmd.find_image(root,'authorize',delay*30,True):
        result = True
    return result
