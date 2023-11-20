# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'\\common')
import commands as cmd
import metamask as meta

# 230915_홀로그래프 민팅
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

url1 = 'https://app.holograph.xyz/'

def action1():
    cmd.screen_full()
    cmd.init_click()
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url1)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.find_image(root,'connect_wallet',delay*120,True)
    cmd.find_image(root,'connect_metamask',delay*10,True)
    cmd.find_image(root,'metamask_notification',delay*30,True)
    cmd.screen_left()
    cmd.find_image(root,'connect_next',delay*5,True)
    cmd.find_image(root,'connect_connect',delay*5,True)
    cmd.find_image(root,'connect_sign',delay*10,True)
    cmd.find_image(root,'free',delay*10,True)
    cmd.find_image(root,'mint',delay*10,True)
    cmd.find_image(root,'metamask_notification',delay*30,True)
    cmd.screen_left()
    cmd.find_image(root,'mint_confirm',delay*10,True)
    cmd.find_image(root,'mint_successful',delay*60,False)
    cmd.find_image(root,'mint_close',delay*5,True)
    cmd.find_image(root,'bridge',delay*5,True)
    cmd.find_image(root,'nft_bridge',delay*5,True)
    cmd.find_image(root,'fees',delay*10,True)
    cmd.find_image(root,'eth',delay*10,True)
    cmd.find_image(root,'avalanche',delay*10,True)
    cmd.find_image(root,'add_nft',delay*30,True)
    cmd.find_image(root,'choose_a_collection',delay*5,True)
    cmd.find_image(root,'available',delay*5,True)
    cmd.find_image(root,'available_2',delay*30,True)
    cmd.press_tab(1)
    cmd.press_enter()
    cmd.press_tab(1)
    cmd.press_enter()
    cmd.find_image(root,'bridge_run',delay*60,True)
    cmd.find_image(root,'metamask_notification',delay*30,True)
    cmd.screen_left()
    cmd.find_image(root,'mint_confirm',delay*10,True)
    cmd.find_image(root,'bridge_completed',delay*120,False)

url2 = 'https://app.holograph.xyz/'
def action2():
    result = ''
    meta.change_network('polygon')
    cmd.open_url(url2)
    cmd.find_image(root,'action2_wait_loading',delay*60,False)
    if not cmd.find_image(root,'action2_connect_wallet_1',delay*10,True):
        cmd.find_image(root,'action2_connect_wallet_2',delay*5,True)
    if cmd.find_image(root,'action2_connect_metamask',delay*10,True):
        if not meta.connect_wallet():
            result += 'wallet failed'
        meta.sign()
    if cmd.find_image(root,'action2_free',delay*10,True):
        if cmd.find_image(root,'action2_mint',delay*10,True):
            if not meta.mint():
                result += 'mint failed'
    else:
        result += 'mint failed'
    return result

# 231117 NFT 민팅 & 브릿지
url3='https://app.holograph.xyz/'
def action3(data,i):
    result = 'action3 = '
    meta.change_network('polygon')
    cmd.open_url(url3)
    cmd.init_click()
    cmd.find_image(root,'action3_wait_loading',delay*60,False)
    if cmd.find_image(root,'action3_connect_wallet2',delay*10,True):
        if cmd.find_image(root,'action3_connect_metamask',delay*30,True):
            meta.connect_wallet()
            meta.sign()
    elif cmd.find_image(root,'action3_connect_wallet',delay*10,True):
        if cmd.find_image(root,'action3_connect_metamask',delay*30,True):
            meta.connect_wallet()
            meta.sign()
    else:
        if not cmd.find_image(root,'action3_1',delay*5,False):
            if cmd.find_image(root,'action3_connect_wallet',delay*60,True):
                if cmd.find_image(root,'action3_connect_metamask',delay*5,True):
                    meta.connect_wallet()
                    meta.sign()
    if cmd.find_image(root,'action3_1',delay*5,True):
        cmd.wait(delay)
        cmd.press_tab(2)
        cmd.press_enter()
        if cmd.find_image(root,'action3_mint',delay*30,True):
            meta.mint()
        if cmd.find_image(root,'action3_mint_successful',delay*30,True):
            cmd.find_image(root,'action3_menu',delay*5,True)
            cmd.find_image(root,'action3_bridge',delay*5,True)
            cmd.find_image(root,'action3_nft_bridge',delay*5,True)
            cmd.find_image(root,'action3_eth',delay*20,True)
            cmd.find_image(root,'action3_aval',delay*5,True)
            cmd.find_image(root,'action3_select_nft',delay*5,True)
            cmd.find_image(root,'action3_choose',delay*5,True)
            cmd.find_image(root,'action3_choose_nft',delay*5,True)
            if cmd.find_image(root,'action3_available',delay*30,True):
                cmd.wait(delay)
                cmd.press_tab(1)
                cmd.press_enter()
            if cmd.find_image(root,'action3_nft_selected',delay*5,True):
                cmd.find_image(root,'action3_bridge_continue',delay*5,True)
                if cmd.find_image(root,'action3_bridge_confirm',delay*60,True):
                    meta.mint()
    if cmd.find_image(root,'action3_bridge_in_progress',delay*30,True):
        result += 'Pass'
        cmd.close_window()
    else:
        result += 'Fail'
    return result

def subroutine(data,f,i,start,end):
    result = str(i+1)+'\n'
    f.write(result)

    step = 1
    if start <= step and end >= step:
        result = action1() + '\n'
        f.write(result)    
    
    step = 2
    if start <= step and end >= step:
        result = action2() + '\n'
        f.write(result)    
    
    step = 3
    if start <= step and end >= step:
        result = action3(data,i) + '\n'
        f.write(result)    
    
    # step = 4
    # if start <= step and end >= step:
    #     result = action4() + '\n'
    #     f.write(result)    

    # step = 5
    # if start <= step and end >= step:
    #     result = action5() + '\n'
    #     f.write(result)    

    # step = 6
    # if start <= step and end >= step:
    #     result = action6() + '\n'
    #     f.write(result)    

    # step = 7
    # if start <= step and end >= step:
    #     result = action7() + '\n'
    #     f.write(result)    

    # step = 8
    # if start <= step and end >= step:
    #     result = action8() + '\n'
    #     f.write(result)    
    
    # step = 9
    # if start <= step and end >= step:
    #     result = action9() + '\n'
    #     f.write(result)    
    
    # step = 10
    # if start <= step and end >= step:
    #     result = action10() + '\n'
    #     f.write(result)


    # step = 1
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action1() + '\n'
    #         f.write(result)    
    
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
    #         result = action5() + '\n'
    #         f.write(result)    

    # step = 6
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action6() + '\n'
    #         f.write(result)    

    # step = 7
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action7() + '\n'
    #         f.write(result)    

    # step = 8
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action8() + '\n'
    #         f.write(result)    
    
    # step = 9
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action9() + '\n'
    #         f.write(result)    
    
    # step = 10
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action10() + '\n'
    #         f.write(result)    
    
    # step = 11
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action11() + '\n'
    #         f.write(result) 

    # step = 12
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action12() + '\n'
    #         f.write(result)    

    # step = 13
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action13() + '\n'
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



    