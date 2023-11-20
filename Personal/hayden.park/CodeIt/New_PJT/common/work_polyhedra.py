# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'\\common')
import commands as cmd
import metamask as meta
import galxe as gal

# 230915_폴리곤체인 민팅
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'




def open_url(url):
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()

url1 = 'https://zkbridge.com/sbt/Lifeform-x-Polyhedra-Avatar'
def action1():
    open_url(url1)
    cmd.find_image(root,'wait_page_loading',delay*20,False)
    cmd.init_click()
    cmd.press_tab(8)
    cmd.press_enter()
    cmd.find_image(root,'connect_metamask',delay*20,True)
    
    meta.connect_wallet()
    meta.connect_wallet_sign()

    cmd.find_image(root,'waiting_birth',delay*30,False)
    cmd.find_image(root,'base',delay*10,False)

    cmd.wait(delay*2)
    cmd.find_image(root,'polygon',delay*30,True)
    if not meta.allow_to_add_network():
        meta.allow_switch()
    meta.mint_confirm()
    cmd.wait(delay*5)
    
    cmd.find_image(root,'core_dao',delay*30,True)
    cmd.press_tab(1)
    cmd.press_enter()
    meta.mint_confirm()
    cmd.find_image(root,'collect_done',delay*60,True)
    cmd.wait(delay*2)

    cmd.find_image(root,'base',delay*30,True)
    cmd.press_tab(1)
    cmd.press_enter()
    meta.mint_confirm()
    cmd.find_image(root,'collect_done',delay*60,True)
    cmd.wait(delay*2)

    cmd.init_click()
    cmd.press_right(10)
    cmd.find_image(root,'mantle',delay*30,True)
    cmd.press_tab(1)
    cmd.press_enter()
    meta.mint_confirm()
    cmd.find_image(root,'collect_done',delay*60,True)

    cmd.find_image(root,'sent_mantle',delay*20,True)

# BNB체인 민팅 # Taiko 브릿지
url2 = 'https://zkbridge.com/gallery/pandra'
def action2():
    open_url(url2)
    cmd.find_image(root,'action2_claim',delay*60,True)
    if cmd.find_image(root,'action2_connect_metamask',delay*5,True):
        meta.connect_wallet()
        meta.connect_wallet_sign()
        cmd.wait(delay*3)
        cmd.find_image(root,'action2_claim',delay*5,True)
        cmd.wait(delay)
    
    if not meta.allow_to_add_network():
        meta.allow_switch()
    meta.mint_confirm()

    cmd.find_image(root,'action2_finish',delay*10,False)
    cmd.find_image(root,'action2_nft',delay*5,True)
    cmd.find_image(root,'action2_confirm_import',delay*10,True)
    cmd.find_image(root,'action2_next',delay*20,True)
    cmd.find_image(root,'action2_select_a_network',delay*5,True)
    cmd.press_down(10)
    cmd.moveRel(0,100,False)
    cmd.scroll(-400)
    cmd.find_image(root,'action2_taiko',delay*5,True)
    cmd.find_image(root,'action2_next',delay*5,True)
    cmd.find_image(root,'action2_approve',delay*5,True)
    cmd.find_image(root,'action2_waiting_for_confirmations',delay*5,False)
    meta.mint_confirm()
    cmd.find_image(root,'action2_transfer',delay*5,True)
    meta.mint_confirm()
    cmd.find_image(root,'action2_completed',delay*60,True)

url3 = 'https://galxe.com/polyhedra/campaign/GCis2U2eve'
def action3():
    open_url(url3)
    if cmd.find_image(root,'action3_follow_taiko',delay*60,False):
        cmd.wait(delay*3)
        gal.twit_follow(root,'action3_follow_taiko')
        gal.twit_repost(root,'action3_retweet')
        cmd.wait(delay)
        gal.refresh()


url4 = 'https://zkbridge.com/zknft'
image_path = r'C:\Projects\NadoPython\Personal\hayden.park\CodeIt\New_PJT\image\profile_discord_x'
def action4(data,i):
    result = 'action4 = '
    profile_no = str(data['profile_no'][i])
    domain_name = data['domain_name'][i]
    meta.run()
    open_url(url4)
    cmd.init_click()
    cmd.find_image(root,'action4_transfer',delay*60,True)
    cmd.find_image(root,'action4_select_a_network',delay*5,True)
    if cmd.find_image(root,'action4_select_bnb',delay*5,True):
        if cmd.find_image(root,'action4_connect_metamask',delay*5,True):
            meta.connect_wallet()
            cmd.wait(delay*3)
            meta.sign()
            cmd.wait(delay*3)
            meta.allow_to_add_network()
            cmd.press('f5')
            cmd.wait(delay*3)
            cmd.find_image(root,'action4_select_a_network',delay*10,True)
            cmd.find_image(root,'action4_select_bnb',delay*5,True)
        else:
            meta.allow_switch()
        cmd.find_image(root,'action4_bnb_confirm',delay*10,False)
    if cmd.find_image(root,'action4_import_nft',delay*5,True):
        if cmd.find_image(root,'action4_create_nft',delay*10,True):
            cmd.find_image(root,'action4_nft_browse',delay*5,True)
            cmd.find_image(root,'action4_browse_window',delay*5,True)
            cmd.hotkey('alt','d')
            cmd.hotkey('ctrl','a')
            cmd.press('delete')
            cmd.typetext(image_path)
            cmd.press_enter()
            cmd.wait(delay)
            cmd.hotkey('alt','n')
            cmd.typetext(profile_no)
            cmd.press_enter()
    if cmd.find_image(root,'action4_image_added',delay*20,False):
        cmd.find_image(root,'action4_nft_name',delay*5,True)
        cmd.press_tab(1)
        cmd.typetext(domain_name)
        cmd.press_tab(1)
        cmd.typetext(domain_name)
        cmd.press_tab(1)
        cmd.find_image(root,'action4_select_a_network',delay*5,True)
        cmd.find_image(root,'action4_select_bnb',delay*5,True)
        cmd.find_image(root,'action4_nft_create',delay*5,True)
        meta.mint()
        cmd.find_image(root,'action4_create_nft_done',delay*30,True)
    cmd.find_image(root,'action4_opbnb',delay*5,True)
    cmd.find_image(root,'action4_nft_bridge',delay*5,True)
    cmd.find_image(root,'action4_transfer',delay*5,True)
    if cmd.find_image(root,'action4_import_nft',delay*5,True):
        cmd.find_image(root,'action4_import_nft_address',delay*30,True)
        cmd.find_image(root,'action4_import_nft_confirm',delay*5,True)
        cmd.find_image(root,'action4_nft_bridge_confirm_import',delay*5,True)
        cmd.find_image(root,'action4_nft_bridge_next',delay*5,True)
        cmd.find_image(root,'action4_select_a_network',delay*5,True)
        cmd.find_image(root,'action4_opbnb_mainnet',delay*5,True)
        cmd.find_image(root,'action4_nft_bridge_next',delay*5,True)
        cmd.find_image(root,'action4_nft_bridge_approve',delay*5,True)
        meta.mint()
    if cmd.find_image(root,'action4_nft_bridge_approved',delay*10,False):
        cmd.find_image(root,'action4_nft_bridge_transfer',delay*5,True)
        meta.mint()
    if cmd.find_image(root,'action4_nft_bridge_completed',delay*30,False):
        cmd.find_image(root,'action4_token_bridge',delay*5,True)
        cmd.find_image(root,'action4_token_bridge_enter',delay*5,True)
        amount = cmd.get_random(0.00480,0.00520,5)
        cmd.typetext(amount)
        cmd.find_image(root,'action4_token_bridge_transfer',delay*5,True)
        meta.mint()
    if cmd.find_image(root,'action4_token_bridge_completed',delay*20,False):
        result += 'pass'
    else:
        result += 'fail'
    return result

url5 = 'https://premium.lifeform.cc/event_detail/5'
def action5(data,i):
    result = 'action5 = '
    meta.run()
    open_url(url5)
    cmd.init_click()
    cmd.find_image(root,'action5_wait_loading',delay*60,False)
    if cmd.find_image(root,'action5_connect_wallet',delay*10,True):
        cmd.find_image(root,'action5_connect_metamask',delay*5,True)
        meta.connect_wallet()
        meta.sign()
    if cmd.find_image(root,'action5_wallet_connected',delay*10,False):
        cmd.press_down(13)
        cmd.find_image(root,'action5_verify',delay*5,True)
        if cmd.find_image(root,'action5_verified',delay*10,True):
            result += 'Pass'
        else:
            result += 'Fail'
    return result

url6 = 'https://star.legend.game/mint/ticket'
def action6(data,i):
    result = 'action6 = '
    open_url(url6)
    cmd.init_click()
    cmd.find_image(root,'action6_wait_loading',delay*60,False)
    cmd.wait(delay*3)
    if cmd.find_image(root,'action6_connect_wallet',delay*5,True):
        if cmd.find_image(root,'action6_connect_metamask',delay*5,True):
            meta.connect_wallet()
            meta.sign()
            meta.allow_to_add_network()
            cmd.press('f5')
            cmd.wait(delay*3)
    if cmd.find_image(root,'action6_switch_network',delay*5,True):
        meta.allow_switch()
        cmd.press('f5')
        cmd.wait(delay*3)
    cmd.init_click()
    if cmd.find_image(root,'action6_claim1_after',delay*3,False):
        result += 'Pass'
        cmd.close_window()
    else:
        if cmd.find_image(root,'action6_claim1',delay*7,True):
            meta.mint()
            cmd.find_image(root,'action6_claim1_done',delay*30,True)
            if cmd.find_image(root,'action6_claim1_after',delay*3,False):
                result += 'Pass'
                cmd.close_window()
        else:
            result += 'Fail'
    # if not cmd.find_image(root,'action6_claim2_claimed',delay*3,False):
    #     if cmd.find_image(root,'action6_claim2',delay*5,True):
    #         meta.mint()
    #         cmd.find_image(root,'action6_claim2_done',delay*10,True)
    
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
        result = action3() + '\n'
        f.write(result)    
    
    step = 4
    if start <= step and end >= step:
        result = action4(data,i) + '\n'
        f.write(result)    

    step = 5
    if start <= step and end >= step:
        result = action5(data,i) + '\n'
        f.write(result)    

    step = 6
    if start <= step and end >= step:
        result = action6(data,i) + '\n'
        f.write(result)    

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