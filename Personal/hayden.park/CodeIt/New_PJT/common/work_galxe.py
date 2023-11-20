import commands as cmd
import metamask as meta

# 230916_갤럭시 소셜 링크 설정, 폴리헤데라
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'
url = 'https://galxe.com/polyhedra/campaign/GCMhyUPmDW'

def open_url():
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.find_image(root,'wait_loading',delay*20,False)
    cmd.wait(delay)

def setting_social_link():
    msg = ''
    open_url()
    cmd.find_image(root,'menu',delay*3,True)
    cmd.wait(delay*3)
    if cmd.find_image(root,'connect_wallet',delay*3,True):
        cmd.find_image(root,'connect_metamask',delay*5,True)
        meta.connect_wallet()
        meta.connect_wallet_sign()
    cmd.point_image(root,'bell',delay*5)
    cmd.moveRel(-40,0,True)
    cmd.find_image(root,'settings',delay*5,True)
    cmd.find_image(root,'settings_social_link',delay*5,True)

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
    cmd.find_image(root,'settings_social_link',delay*5,True)
    cmd.close_window()
    if msg == '':
        msg = 'setting_social_link_done'
    print(msg)

def action_polyhedra():
    msg = ''
    open_url()
    cmd.find_image(root,'follow_polyhedra',delay*8,True)
    if cmd.find_image(root,'btn_follow',delay*15,True):
        cmd.find_image(root,'check_following',delay*15,False)
        cmd.close_window()
    elif cmd.find_image(root,'btn_follow_alter',delay*5,True):
        cmd.find_image(root,'check_following',delay*15,False)
        cmd.close_window()
    else:
       cmd.init_click()
       cmd.find_image(root,'follow_polyhedra',delay*5,True) 
       msg = 'polyhedra already done'
    
    cmd.find_image(root,'follow_lifeformcc',delay*8,True)
    if cmd.find_image(root,'btn_follow_2',delay*15,True):
        cmd.wait(delay)
        cmd.close_window()
    else:
        cmd.init_click()
        cmd.find_image(root,'follow_lifeformcc',delay*5,True)
        msg = msg + ' ' + 'lifeformcc already done'

    cmd.find_image(root,'follow_zkbridge',delay*8,True)
    if cmd.find_image(root,'btn_follow',delay*15,True):
        cmd.find_image(root,'check_following',delay*15,False)
        cmd.close_window()
    else:
        cmd.init_click()
        cmd.find_image(root,'follow_zkbridge',delay*5,True)
        msg = msg + ' ' + 'zkbridge already done'

    cmd.find_image(root,'retweet',delay*8,True)
    if cmd.find_image(root,'repost',delay*15,True):
        cmd.wait(delay)
        cmd.close_window()
    else:
        cmd.init_click()
        cmd.find_image(root,'retweet',delay*5,True)
        msg = msg + ' ' + 'retweet already done'
    # cmd.find_image(root,'refresh',delay*15,True)
    if msg == '':
        msg = 'action_done'
    print(msg)

# def check_polyhedra():
#     meta.run()
#     open_url()

  

# cmd.init_click()
# meta.run()
# setting_social_link()
# action_polyhedra()