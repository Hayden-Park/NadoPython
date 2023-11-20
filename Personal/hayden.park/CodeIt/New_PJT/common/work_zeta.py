import commands as cmd
import metamask as meta
import galxe as gal
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

def open_url(url):
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.wait(delay)


# 230925 zeta 포인트 획득 -> 트위터 1개월 이상, 10 팔로워 필요
url1 = 'https://labs.zetachain.com/leaderboard?code=ID4WUVFGY3_d9YlxzOWL1'
def action1():
    result = 'action1 = '
    open_url(url1)
    if cmd.find_image(root,'action1_twit_verify',delay*60,False):
        twit.authorize_app()
    cmd.find_image(root,'action1_continue',delay*20,True)
    cmd.wait(delay)
    cmd.find_image(root,'action1_continue',delay*10,True)
    cmd.find_image(root,'action1_get_started',delay*10,True)
    if cmd.find_image(root,'action1_twit_follow',delay*10,True):
        if twit.follow():
            cmd.close_window()
    if cmd.find_image(root,'action1_connect_wallet',delay*10,True):
        cmd.find_image(root,'action1_connect_metamask',delay*10,True)
        meta.mint_confirm()
        meta.allow_switch()
    cmd.find_image(root,'action1_menu',delay*10,True)
    cmd.find_image(root,'action1_earn_point',delay*10,True)
    # 여기서 중단함


def subroutine(data,f,i,start,end):
    result = str(i+1)+'\n'
    f.write(result)
    # total_liq = data['zksync_total'][i]
    # liq8 = data['zksync_8'][i]
    # liq9 = data['zksync_9'][i]
    # liq10 = data['zksync_10'][i]
    # liq11 = data['zksync_11'][i]
    # liq13 = data['zksync_13'][i]
    # domain_name = data['domain_name'][i]
    
    step = 1
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action1() + '\n'
            f.write(result)    
    
    # step = 2
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action2() + '\n'
    #         f.write(result)    
    
    # step = 3
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action3() + '\n'
    #         f.write(result)    
    
    # step = 4
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action4() + '\n'
    #         f.write(result)    

    # step = 5
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action5(domain_name) + '\n'
    #         f.write(result)    

    # step = 6
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action6() + '\n'
    #         f.write(result)    

    # step = 7
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         meta.change_network('zksync_era')
    #         result = action7(domain_name) + '\n'
    #         f.write(result)    

    # step = 8
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action8(total_liq,liq8) + '\n'
    #         f.write(result)    
    
    # step = 9
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action9(liq9) + '\n'
    #         f.write(result)    
    
    # step = 10
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action10(liq10) + '\n'
    #         f.write(result)    
    
    # step = 11
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action11(liq11) + '\n'
    #         f.write(result) 

    # step = 13
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action13(liq13) + '\n'
    #         f.write(result)    

    # step = 14
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action14() + '\n' 
    #         f.write(result)    
    
    # step = 15
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action15() + '\n' 
    #         f.write(result)    

    # step = 16
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action16() + '\n' 
    #         f.write(result)    