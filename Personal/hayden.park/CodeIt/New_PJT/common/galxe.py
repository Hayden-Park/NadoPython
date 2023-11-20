import commands as cmd
import metamask as meta
import twitter as twit
import google_app as ggl
import discord as dico

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

def open_url(url):
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    wait_loading()


def setting_social_link(email):
    msg = ''
    cmd.find_image(root,'menu',delay*3,True)
    cmd.wait(delay*3)
    if cmd.find_image(root,'login',delay*3,True):
        cmd.find_image(root,'metamask',delay*5,True)
        meta.connect_wallet()
        meta.connect_wallet_sign()
    cmd.point_image(root,'bell',delay*5)
    cmd.moveRel(-40,0,True)
    cmd.find_image(root,'settings',delay*5,True)
    cmd.find_image(root,'settings_social_accounts',delay*5,True)

    if cmd.find_image(root,'settings_enter_email',delay*5,True):
        cmd.copy_text(email)
        cmd.hotkey('ctrl','v')
        cmd.wait(delay)
        cmd.find_image(root,'settings_email_send',delay*5,True)
        cmd.find_image(root,'settings_email_timer',delay*5,False)
        ### gmail 에서 값 읽어오기 필요
        code = ''
        cmd.find_image(root,'settings_email_enter_code',delay*5,True)
        cmd.copy_test(code)
        cmd.hotkey('ctrl','v')
        cmd.wait(delay)
        cmd.find_image(root,'settings_email_verify',delay*5,True)
        cmd.find_image(root,'settings_email_done',delay*10,True)

    if cmd.find_image(root,'connect_discord',delay*5,True):    # 디스코드 연결
        if not cmd.find_image(root,'discord_authorize',delay*15,True):
            cmd.find_image(root,'discord_authorize_kr',delay*15,True)
        cmd.wait(delay*10)
    else:
        msg = 'discord already done'

    if cmd.find_image(root,'connect_twitter',delay*15,True):    # 트위터 포스트 및 링크 인증
        cmd.find_image(root,'connect_twitter_step1',delay*5,True)
        cmd.find_image(root,'twitter_maybe_later',delay*15,True)
        cmd.wait(delay*3)
        cmd.find_image(root,'twitter_post',delay*5,True)
        cmd.find_image(root,'twitter_got_it',delay*5,True)
        cmd.find_image(root,'twitter_share',delay*5,True)
        cmd.find_image(root,'twitter_copy_link',delay*5,True)
        cmd.wait(delay)
        cmd.close_window()
        cmd.find_image(root,'connect_twitter_paste_link_here',delay*5,True)
        cmd.hotkey('ctrl','v')
        cmd.press_tab(1)
        cmd.press_enter()
        cmd.find_image(root,'link_success',delay*10,False)
    else:
        msg = msg +' ' + 'twitter already done'
    cmd.find_image(root,'settings_social_accounts',delay*5,True)
    cmd.close_window()
    if msg == '':
        msg = 'settings_social_accounts_done'
    print(msg)

def wait_loading(sec):
    cmd.find_image(root,'wait_loading',delay*sec,False)
    cmd.wait(delay)

def switch():
    if cmd.find_image(root,'switch',delay*5,True):
        cmd.wait(delay)
        meta.allow_switch()
        cmd.wait(delay)

def twit_follow(root,filename):
    cmd.find_image(root,filename,delay*5,True)
    result = twit.follow()
    if result == '':
        cmd.close_window()
        cmd.wait(delay*2)
    if refresh(root,filename):
        twit.authorize_app()
    return result

def twit_retweet(root,filename):
    cmd.find_image(root,filename,delay*5,True)
    result = twit.repost()
    if result == '':
        cmd.close_window()
        cmd.wait(delay*2)
    if refresh(root,filename):
        twit.authorize_app()
    return result

def twit_like(root,filename):
    cmd.find_image(root,filename,delay*5,True)
    result = twit.like()
    if result == '':
        cmd.close_window()
        cmd.wait(delay*2)
    if refresh(root,filename):
        twit.authorize_app()
    return result

def twit_quote(root,filename):
    cmd.find_image(root,filename,delay*5,True)
    result = twit.post()
    if result == '':
        cmd.close_window()
        cmd.wait(delay*2)
    if refresh(root,filename):
        twit.authorize_app()
    return result

def visit(root_work,filename):
    result = False
    cmd.find_image(root_work,filename,delay*5,True)
    if cmd.find_image(root,'visit_warning',delay*60,False):
        cmd.find_image(root,'visit_continue',delay*30,True)
        cmd.wait(delay*10)
        cmd.close_window()
        result = refresh(root_work,filename)
    return result

def claim():
    count = 0
    result = False
    while True and count < 6:
        if cmd.find_image(root,'claim',delay*10,True) or count >= 6:
            result = True
            break
        else:
            cmd.init_click()
            cmd.press('f5')
            count += 1
    return result    

def discord_join(root_work,filename):
    result = False
    cmd.find_image(root_work,filename,delay*5,True)
    if dico.accept_invite() == '':
        result = cmd.find_image_rate(root_work,filename,delay*5,True,98)
    return result           

def refresh(root,filename):
    result = False
    if cmd.find_image_rate(root,filename,delay*5,True,98): #Refresh
        result = True
        cmd.wait(delay*2)
    return result

def check_coin(name):
    result = False
    msg = ''
    coin_name = 'coin_' + name
    if not cmd.find_image(root,coin_name,delay*2,False):
        if meta.change_network(name) =='':
            result = True
    return result

    

