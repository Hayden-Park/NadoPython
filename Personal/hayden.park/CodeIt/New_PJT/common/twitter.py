import time
import commands as cmd
import google_app as gmail

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

def run():
    cmd.new_tab()
    cmd.open_setting()
    cmd.press('b','t')  # open bookmarks tree and twitter
    cmd.wait(delay)

def sign_in():
    run()
    if cmd.find_image(root,'sign_in',delay*8,True):
        cmd.find_image(root,'sign_in_next',delay*10,True)
        cmd.find_image(root,'sign_in_login',delay*10,True)

def add_friend(id):
    result = False
    cmd.find_image(root,'btn_explore',delay*10,True)
    cmd.find_image(root,'explore_search',delay*5,True)
    cmd.wait(delay*0.5)
    cmd.hotkey('ctrl','a')
    cmd.press('delete')
    cmd.wait(delay*0.5)
    cmd.typetext(id)
    cmd.find_image(root,'search_btn',delay*5,True)
    if cmd.find_image(root,'goto_id',delay*5,True):
        cmd.init_click()
        if cmd.find_image(root,'btn_follow_alter',delay*5,True):
            result = True
    else:
        result = False
    return result

def accept_friend(interval=10):
    cmd.find_image(root,'profile',delay*10,True)
    cmd.find_image(root,'follower',delay*5,True)
    cmd.find_image(root,'followers',delay*5,True)
    found = True
    while found:
        found = cmd.find_image(root,'people_follow',delay*5,True)
        if found:
            interval = float(cmd.get_random(interval*0.7,interval*1.3,2))
            print('wait {0} secs for next follow...'.format(interval))
            cmd.wait(delay*interval)

def create_account(email, birth, pw):
    run()             # run and wait 10 sec
    cmd.init_click()
    cmd.press_tab(3)
    cmd.press_enter()   # create account
    time.sleep(delay*4)
    cmd.init_click()
    cmd.find_image(root,'twitter_use_email_instead',delay*5,True) # use email instead
    cmd.press_shifttab(2)
    name = email.split('@')[0]
    cmd.typewrite(name) # type name
    cmd.press_tab(1)
    time.sleep(delay)
    cmd.typewrite(email) # type email
    time.sleep(delay)
    cmd.press_tab(2)
    y,m,d = list(map(int,birth.split('-')))
    cmd.press_down(m)   # select month
    cmd.press_tab(1)
    cmd.press_down(d)   # select date
    cmd.press_tab(1)
    cmd.typewrite(str(y))
    time.sleep(delay)
    cmd.press_tab(1)
    cmd.press_enter()   # next
    time.sleep(delay)
    cmd.press_tab(7)
    cmd.press_enter()   # next
    time.sleep(delay)
    cmd.press_tab(10)
    cmd.press_enter()   # next
    time.sleep(delay*10)    # delay waiting for email
    # verification code by email
    vericode = gmail.get_vericode_twitter()
    time.sleep(delay)
    cmd.init_click()
    cmd.press_tab(4)
    cmd.typewrite(vericode)
    # cmd.press('backspace')  # trim blank space
    # cmd.press_tab(2)
    # cmd.press_enter()
    # time.sleep(delay*2)
    # cmd.init_click()
    # cmd.press_tab(3)
    # cmd.typewrite(pw)
    # time.sleep(delay*5) # wait for next button activation
    # cmd.press_tab(2)
    # cmd.press_enter()   # next
    # time.sleep(delay*2)
    # cmd.press_alt()
    # cmd.press_tab(5)
    # cmd.press_enter()   # save password pop-up
    # time.sleep(delay*2)
    # cmd.close_window()
    # time.sleep(delay)

def get_username():
    run()           # wait for 10sec
    cmd.init_click()
    cmd.press_tab(10)
    cmd.press_enter()
    time.sleep(delay*3)     # wait for profile page
    cmd.doubleclick(254,483)
    cmd.copy()
    username = "@"+cmd.paste()
    return username

def check_unlock():
    run()
    if cmd.find_image(root,'home',delay*20,False):
        cmd.close_window()
        return True
    else:
        if cmd.find_image(root,'locked_start',delay*5,False):
            print('twitter blocked')
        return False

def follow():
    result = ''
    if cmd.find_image(root,'btn_follow',delay*30,True):
        cmd.find_image(root,'check_following',delay*5,False)
    elif cmd.find_image(root,'btn_follow_alter',delay*5,True):
        cmd.find_image(root,'check_following',delay*5,False)
    else:
        result = 'follow failed' + '\n'
    return result

def repost():
    result = ''
    if cmd.find_image(root,'repost',delay*30,True):
        cmd.wait(delay)
    else:
        result = 'repost failed' + '\n'
    return result


def like():
    result = ''
    if cmd.find_image(root,'like',delay*30,True):
        cmd.wait(delay)
    else:
        result = 'like failed' + '\n'
    return result

def post():
    result = ''
    cmd.find_image(root,'some_updates_got_it',delay*5,True)
    if cmd.find_image(root,'post',delay*20,True):
        if not cmd.find_image(root,'post_already',delay*3,False):
            cmd.find_image(root,'post_done',delay*5,False)
        cmd.find_image(root,'got_it',delay*3,True)
        cmd.wait(delay)
    else:
        result = 'post failed' + '\n'
    return result

def authorize_app():
    result = False
    cmd.focus_window('X')
    if cmd.find_image(root,'authorize_app',delay*5,True):
        result = True
    return result

def copy_link():
    result = False
    if cmd.find_image(root,'share',delay*5,True):
        result = cmd.find_image(root,'copy_link',delay*3,True)
    return result

