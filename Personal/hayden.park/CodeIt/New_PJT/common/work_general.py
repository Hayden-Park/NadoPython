import commands as cmd
import metamask as meta
import galxe as gal
import discord as dico
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

def open_url(url):
    cmd.init_click()
    cmd.new_tab()
    cmd.hotkey('alt','d')
    cmd.copy_text(url)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.wait(delay)


# 230925 PancakeSwap 에서 BNB 를 USDC 로 2$ 스왑 
url1 = 'https://pancakeswap.finance/'
def action1():
    result = 'action1 = '
    open_url(url1)
    cmd.init_click()
    cmd.find_image(root,'action1_wait_loading',delay*60,False)
    if cmd.find_image(root,'action1_connect_wallet',delay*5,True):
        cmd.find_image(root,'action1_connect_metamask',delay*5,True)
        if meta.connect_wallet():
            if not meta.allow_to_add_network():
                meta.allow_switch()
    cmd.find_image(root,'action1_wallet_connected',delay*5,False)
    cmd.wait(delay)
    cmd.point_image(root,'action1_trade',delay*5)
    cmd.find_image(root,'action1_swap',delay*5,True)
    
    # 팝업끄기
    if cmd.find_image(root,'action1_popup_check',delay*5,True):
        cmd.find_image_rate(root,'action1_popup_close',delay*5,True,98.5)
    
    cmd.find_image(root,'action1_swap_cake',delay*5,True)
    cmd.find_image(root,'action1_swap_search',delay*5,True)
    cmd.wait(delay)
    cmd.copy_text('usdc')
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'action1_swap_usdc',delay*5,True)
    
    cmd.find_image(root,'action1_swap_title',delay*5,True)
    cmd.press_tab(17)
    amount = cmd.get_random(2.700,2.750,3)
    cmd.copy_text(amount)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*3)
    cmd.find_image(root,'action1_swap_swap',delay*10,True)
    if cmd.find_image(root,'action1_swap_confirm',delay*10,True):
        meta.mint_confirm()
        cmd.find_image(root,'action1_swap_completed',delay*5,True)
        cmd.wait(delay)
        cmd.press_esc()
        cmd.wait(delay)
        cmd.press_esc()
        cmd.wait(delay)
        cmd.find_image(root,'action1_add_usdc_to_wallet',delay*5,True)
        meta.add_token()
        result += 'pass'
    else:
        result += 'fail'
    return result

# 230925 DappOS
url2 = 'https://perp.dappos.com/overview'
amount2 = '0.022'
def action2():
    result = 'action2 = '
    open_url(url2)
    cmd.init_click()
    cmd.find_image(root,'action2_wait_loading',delay*60,False)
    if cmd.find_image(root,'action2_connect_wallet',delay*5,True):
        cmd.find_image(root,'action2_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.find_image(root,'action2_wallet_connected',delay*5,False)
    cmd.wait(delay)
    # deposit
    cmd.find_image(root,'action2_more',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action2_deposit',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action2_deposit_title',delay*5,True)
    cmd.press_tab(2)
    amount = cmd.get_random(0.7000,0.7100,4)
    cmd.copy_text(amount)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*3)
    if cmd.find_image(root,'action2_deposit_approve',delay*30,True):
        meta.liquidity()
        cmd.find_image(root,'action2_deposit_approve_success',delay*30,False)
    if cmd.find_image(root,'action2_deposit_deposit',delay*30,True):
        cmd.find_image(root,'action2_checkout_waiting',delay*30,True)
        cmd.find_image(root,'action2_deposit_confirm',delay*30,True)
        if meta.sign():
            meta.mint_confirm()
            cmd.find_image(root,'action2_finish',delay*20,False)
            cmd.find_image(root,'action2_deposit_close',delay*5,True)
    cmd.wait(delay*3)
    # long 포지션
    cmd.find_image(root,'action2_btc',delay*5,True)
    cmd.find_image(root,'action2_long',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(5)
    amount = cmd.get_random(4.000,4.100,3)
    cmd.copy_text(amount)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay)
    cmd.press_tab(1)
    cmd.find_image(root,'action2_long_confirm',delay*10,True)
    cmd.find_image(root,'action2_checkout_waiting',delay*10,True)
    cmd.find_image(root,'action2_deposit_confirm',delay*5,True)
    if meta.sign():
        meta.mint_confirm()
        cmd.find_image(root,'action2_finish',delay*20,False)
        cmd.find_image(root,'action2_deposit_close',delay*5,True)
    cmd.wait(delay*2)
    # long 취소
    cmd.find_image(root,'action2_long',delay*5,True)
    cmd.press_down(20)
    if cmd.find_image(root,'action2_long_btc_check',delay*20,False):
        cmd.find_image(root,'action2_position',delay*5,True)
        cmd.press_tab(3)
        cmd.press_enter()   
    cmd.find_image(root,'action2_checkout_waiting',delay*10,True)
    cmd.find_image(root,'action2_deposit_confirm',delay*5,True)
    if meta.sign():
        meta.mint_confirm()
        cmd.wait(delay*5)
        cmd.find_image(root,'action2_finish',delay*20,False)
        cmd.find_image(root,'action2_deposit_close',delay*5,True)
        cmd.find_image(root,'action2_no_open_position',delay*60,False)
        
    # withdraw
    cmd.find_image(root,'action2_overview',delay*5,True)
    cmd.find_image(root,'action2_more',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action2_withdraw',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action2_withdraw_title',delay*5,True)
    cmd.find_image_rate(root,'action2_withdraw_metamask',delay*5,True,10)
    cmd.find_image(root,'action2_withdraw_max',delay*5,True)
    cmd.wait(delay*2)
    if cmd.find_image(root,'action2_withdraw_withdraw',delay*5,True):
        cmd.find_image(root,'action2_checkout_waiting',delay*10,True)
        cmd.find_image(root,'action2_deposit_confirm',delay*5,True)
        if meta.sign():
            cmd.find_image(root,'action2_finish',delay*20,False)
            cmd.find_image(root,'action2_deposit_close',delay*5,True)
            result = 'pass'
        else:
            result += 'fail'
    return result

# 230925 mint.fun, 이더필요
url3 = 'https://mint.fun/zora/0x22222222d2B432Ec420032C46fAe3Cda0e029dCc'
def action3():
    result = 'action3 = '
    meta.change_network('eth')
    open_url(url3)
    cmd.init_click()
    cmd.find_image(root,'action3_wait_loading',delay*60,False)
    if cmd.find_image(root,'action3_connect_wallet',delay*15,True):
        cmd.find_image(root,'action3_connect_metamask',delay*5,True)
        meta.connect_wallet()
    if cmd.find_image(root,'action3_mint',delay*10,True):
        meta.mint_confirm()
        cmd.find_image(root,'action3_bridge_close',delay*10,True)
        result += 'pass'
    if cmd.find_image(root,'action3_mint_success',delay*300,True):
        cmd.find_image(root,'action3_bridge_close',delay*10,True)
        result += 'pass'
    else:
        result += 'fail'
    return result

# 230925 mint fundrop
url4 = 'https://mint.fun/fundrop?ref=0x1667764DD15D6dfaB71fEBfa6D11eaDb7E9BC1ef'
def action4():
    result = 'action4 = '
    open_url(url4)
    cmd.init_click()
    cmd.find_image(root,'action4_wait_loading',delay*60,True)
    cmd.find_image(root,'action4_mint_fundrop',delay*10,False)
    cmd.press_tab(2)
    cmd.press_enter()
    cmd.wait(delay)
    meta.mint_confirm()
    cmd.find_image(root,'action4_screen',delay*10,True)
    cmd.press_down(3)
    cmd.find_image(root,'action4_skip',delay*5,True)
    cmd.find_image(root,'action4_game_play',delay*10,True)
    cmd.find_image(root,'action4_game_start',delay*10,True)
    cmd.press_space(1)
    while True:
        if cmd.find_image(root,'action4_game_over',delay,False):
            result += 'pass'
            break
        else:
            cmd.press_space(1)
    return result

# 230930 JeffWorld 민팅
url5 = 'https://puzzlefreemint.jeffprotocol.io/'
def action5():
    result = 'action5 = '
    meta.change_network('polygon')
    open_url(url5)
    cmd.init_click()
    cmd.find_image(root,'action5_wait_loading',delay*60,False)
    if cmd.find_image(root,'action5_connect_wallet',delay*15,True):
        meta.connect_wallet()
    cmd.wait(delay)
    if meta.mint(root,'action5_mint','action5_mint_finished'):
        result += 'pass'
    return result

# 230930 thetanuts galxe
url6 = 'https://galxe.com/thetanuts/campaign/GCLEeUsGvE?referral_code=GRFr2JPvbqH-nnNiZtaFJ2hg72MGV0WPgKXCkOTFIWIZNBk'
def action6():
    result = 'action6 = '
    open_url(url6)
    cmd.init_click()
    if meta.sign():
        meta.sign()
    gal.wait_loading(delay*60)
    cmd.find_image(root,'action6_wait_loading',delay*5,False)
    gal.check_coin('polygon')
    gal.twit_follow(root,'action6_follow')
    if cmd.find_image(root,'action6_quiz_start',delay*10,True):
        cmd.init_click()
        cmd.press_down(7)
        cmd.find_image(root,'action6_quiz_answer',delay*10,True)
        cmd.wait(delay*1.5)
        cmd.find_image(root,'action6_quiz_submit',delay*10,True)
        cmd.wait(delay*5)
    if gal.claim():
        cmd.find_image(root,'action6_claim_finish',delay*10,True)
        cmd.find_image(root,'action6_claim_close',delay*3,True)
        cmd.find_image(root,'action6_claim_close',delay*3,True)
        cmd.find_image(root,'action6_claimed',delay*5,True)
        result += 'pass'
    else:
        result += 'fail'
    return result

# 230930 OAT galxe
url7 = 'https://galxe.com/orderlynetwork/campaign/GCi49UB4Qa?referral_code=GRFr2JqzOaHywrqrZtaFJ2hg70ET5YqZ0QIw8SyiL2JPFsW'
def action7():
    result = 'action7 = '
    open_url(url7)
    cmd.init_click()
    gal.wait_loading(delay*60)
    if cmd.find_image(root,'action7_wait_loading',delay*5,False):
        gal.check_coin('polygon')
        gal.twit_follow(root,'action7_follow')
        if gal.discord_join(root,'action7_discord'):
            gal.switch()
            gal.claim()
            cmd.find_image(root,'action7_waiting_for_confirmation',delay*30,True)
            meta.mint(root,None,'action7_mint_finish')
            cmd.find_image(root,'action7_mint_finish',delay*5,True)
            cmd.press_esc()
            if cmd.find_image(root,'action7_claimed',delay*5,False):
                result += 'pass'
        else:
            result += 'fail'
    return result

url8 = 'https://galxe.com/orderlynetwork/campaign/GC92yUPbhQ?referral_code=GRFr2I6yqaH2VzTnZtaFJ2hg1b50yLc9OgFCYuzL4PXHy1k'
def action8():
    result = 'action8 = '
    open_url(url8)
    cmd.init_click()
    gal.wait_loading(delay*60)
    if cmd.find_image(root,'action8_wait_loading',delay*5,False):
        gal.check_coin('polygon')
        gal.twit_like(root,'action8_like')
        cmd.wait(delay*3)
        gal.twit_quote(root,'action8_quote')
        cmd.init_click()
        cmd.press_down(5)
        gal.visit(root,'action8_visit')
        if gal.discord_join(root,'action8_discord'):
            gal.switch()
            gal.claim()
            cmd.find_image(root,'action7_waiting_for_confirmation',delay*30,True)
            meta.mint(root,None,'action7_mint_finish')
            cmd.find_image(root,'action7_mint_finish',delay*5,True)
            cmd.press_esc()
            if cmd.find_image(root,'action7_claimed',delay*5,False):
                result += 'pass'
        else:
            result += 'fail'
    return result
    
url9 = 'https://testnet-dex-evm.woo.org/en/trade'
def action9():
    result = 'action9 = '
    open_url(url9)
    cmd.init_click()
    cmd.find_image(root,'action9_wait_loading',delay*60,False)
    if cmd.find_image(root,'action9_connect_wallet',delay*10,True):
        cmd.find_image(root,'action9_connect_check',delay*5,True)
        cmd.find_image(root,'action9_connect_metamask',delay*5,True)
        if meta.connect_wallet():
            cmd.find_image(root,'action9_connect_finish',delay*5,True)
            cmd.init_click()
            cmd.press_esc()
    cmd.find_image(root,'action9_testnet',delay*5,True)
    if cmd.find_image(root,'action9_arbitrum',delay*5,True):
        meta.allow_to_add_network()
    cmd.init_click()
    cmd.find_image(root,'action9_get_test',delay*5,True)
    if cmd.find_image(root,'action9_sign_in',delay*5,True):
        meta.sign()
    if cmd.find_image(root,'action9_enable',delay*5,True):
        meta.sign()
    cmd.find_image(root,'action9_get_test',delay*5,True)
    cmd.find_image(root,'action9_get_confirm',delay*5,True)
    if cmd.find_image(root,'action9_free_collat',delay*180,False):
        amount = float(cmd.get_random(17,23,2))
        cmd.find_image_rate(root,'action9_percent',delay*5,True,amount)
        cmd.press_tab(3)
        cmd.find_image(root,'action9_order_confirm',delay*5,True)
        for i in range(3):
            cmd.find_image(root,'action9_buy',delay*5,True)
            cmd.wait(delay*3)
            cmd.find_image(root,'action9_portfolio_close',delay*5,True)
            cmd.find_image(root,'action9_confirm',delay*5,True)
        result += 'pass'
    return result

url10 = 'https://galxe.com/orderlynetwork/campaign/GCiLaU2YJm'
def action10():
    result = 'action10 = '
    meta.change_network('arbitrum')
    open_url(url10)
    cmd.init_click()
    gal.wait_loading(delay*60)
    if cmd.find_image(root,'action10_wait_loading',delay*5,False):
        gal.twit_follow(root,'action10_follow')
        cmd.wait(delay*3)
        gal.twit_retweet(root,'action10_retweet')
        cmd.wait(delay*3)
        cmd.find_image_rate(root,'action10_testnet_refresh',delay*5,True,98)
        gal.switch()
        if gal.claim():
            cmd.find_image(root,'action10_waiting_for_confirmation',delay*30,True)
            meta.mint(root,None,'action10_mint_finish')
            cmd.find_image(root,'action10_mint_finish',delay*5,True)
            cmd.press_esc()
            if cmd.find_image(root,'action10_claimed',delay*5,False):
                result += 'pass'
        else:
            result += 'fail'
    return result

url11 = 'https://app.kiloex.io/trade?sCode=jj5ksimdj'
def action11():
    result = 'action11 = '
    meta.run()
    open_url(url11)
    cmd.init_click()
    cmd.find_image(root,'action11_wait_loading',delay*60,False)
    if cmd.find_image(root,'action11_connect_wallet',delay*5,True):
        cmd.find_image(root,'action11_connect_metamask',delay*5,True)
        meta.connect_wallet()
        meta.allow_switch()
        cmd.find_image(root,'action11_okay',delay*5,True)
    cmd.find_image(root,'action11_airdrop',delay*5,True)
    if cmd.find_image(root,'action11_signed_in',delay*5,False):
        result += 'pass'
        cmd.close_window()
    else:
        if cmd.find_image(root,'action11_signin',delay*3,True):
            if not cmd.find_image(root,'action11_signed_in',delay*7,False):
                meta.sign()
            if cmd.find_image(root,'action11_signed_in',delay*30,False):
                result += 'pass'
                cmd.close_window()            
        else:
            result += 'fail'
    return result

# 231103_테넷이더 수령
url12 = 'https://goerlifaucet.com/'
def action12(data,i):
    result = 'action12 = '
    metamask_wallet = data['metamask_wallet'][i]
    meta.run()
    open_url(url12)
    cmd.init_click()
    if not cmd.find_image(root,'action12_main_logo',delay*30,False):
        if cmd.find_image(root,'action12_check_human',delay*5,False):
            cmd.find_image(root,'action12_check_human_checkbox',delay*5,True)
    if cmd.find_image(root,'action12_enter',delay*60,True):
        cmd.typetext(metamask_wallet)
        cmd.find_image(root,'action12_checkbox',delay*5,False)
        cmd.find_image(root,'action12_checkbox',delay*5,True)
        if not cmd.find_image(root,'action12_captcha_complete',delay*5,True):
            if cmd.find_image(root,'action12_captcha_bypass',delay*10,True):
                if cmd.find_image(root,'action12_captcha_play',delay*5,False):
                    cmd.find_image(root,'action12_captcha_bypass',delay*10,True)
                cmd.find_image(root,'action12_captcha_complete',delay*10,False)
        cmd.find_image(root,'action12_send',delay*10,True)
        result += 'pass'
    else:
        result += 'fail'
    return result

url13 = 'https://reiki.web3go.xyz/aiweb/home'
def action13(data,i):
    firsttime = False
    result = 'action13 = '
    email = data['Google Account2'][i]
    open_url(url13)
    cmd.init_click()
    cmd.find_image(root,'action13_wait_loading',delay*60,False)
    if not cmd.find_image(root,'action13_connected',delay*10,False):
        firsttime = True
        if not cmd.find_image(root,'action13_connect_metamask',delay*5,True):
            if cmd.find_image(root,'action13_connect_wallet',delay*5,True):
                cmd.find_image(root,'action13_connect_metamask',delay*5,True)
        meta.allow_switch()
        meta.connect_wallet()
        meta.sign()
        cmd.wait(delay*3)
        cmd.init_click()
        cmd.press('f5')
        cmd.find_image(root,'action13_connected',delay*10,False)
    cmd.init_click()
    cmd.press_esc()
    cmd.find_image(root,'action13_golden',delay*15,True)
    if not cmd.find_image(root,'action13_daily_check_in',delay*5,True):
        cmd.find_image(root,'action13_golden',delay*15,True)
        if cmd.find_image(root,'action13_need_passport',delay*3,True):
            firsttime = True
    if firsttime:
        if cmd.find_image(root,'action13_passport',delay*10,False):
            if cmd.find_image(root,'action13_passport_mint',delay*3,True):
                meta.mint()
                cmd.find_image(root,'action13_wait_loading',delay*60,False)
                cmd.find_image(root,'action13_golden',delay*15,True)
    cmd.find_image(root,'action13_daily_check_in',delay*20,True)
    if not cmd.find_image(root,'action13_collect',delay*3,True):
        cmd.find_image(root,'action13_scroll',delay*5,True)
        cmd.press_right(10)
        cmd.find_image(root,'action13_collect',delay*3,True)
    if cmd.find_image(root,'action13_collected',delay*5,True):
        result += 'Pass'
        cmd.close_window()
    else:
        result += 'Fail'

    return result

#231111_퀴즈 푸는 일회성 작업만, 원래 action13 에서 분리했기 때문에 사진 이름은 action13
url14 = 'https://reiki.web3go.xyz/aiweb/home'
def action14(data,i):
    result = 'action14 = '
    email = data['Google Account2'][i]
    if cmd.find_image(root,'action13_quiz_yuliverse',delay*20,False):
        cmd.find_image(root,'action13_start_quiz',delay*5,True)
        cmd.find_image(root,'action13_quiz1-1',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz1-2',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz1-3',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz1-4',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz1-5',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_back_to',delay*5,True)

    if cmd.find_image(root,'action13_quiz_lifeform',delay*20,False):
        cmd.find_image(root,'action13_start_quiz',delay*5,True)
        cmd.find_image(root,'action13_quiz2-1',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz2-2',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz2-3',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz2-4',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz2-5',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_back_to',delay*5,True)

    if cmd.find_image(root,'action13_quiz_manta',delay*20,False):
        cmd.find_image(root,'action13_start_quiz',delay*5,True)
        cmd.find_image(root,'action13_quiz3-1',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz3-2',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz3-3',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz3-4',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz3-5',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_back_to',delay*5,True)

    if cmd.find_image(root,'action13_quiz_secondlive',delay*20,False):
        cmd.find_image(root,'action13_start_quiz',delay*5,True)
        cmd.find_image(root,'action13_quiz4-1',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz4-2',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz4-3',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz4-4',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz4-5',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_back_to',delay*5,True)

    if cmd.find_image(root,'action13_quiz_map',delay*20,False):
        cmd.find_image(root,'action13_start_quiz',delay*5,True)
        cmd.find_image(root,'action13_quiz5-1',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz5-2',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz5-3',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz5-4',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_quiz5-5',delay*5,True)
        cmd.find_image(root,'action13_awesome',delay*5,False)
        cmd.find_image(root,'action13_next',delay*5,True)
        cmd.find_image(root,'action13_back_to',delay*5,True)

    if cmd.find_image(root,'action13_share_conversation',delay*5,True):
        cmd.press_down(10)
    if cmd.find_image(root,'action13_referral',delay*5,True):
        cmd.press_down(10)
    if cmd.find_image(root,'action13_connect_email',delay*5,True):
        cmd.wait(delay)
        cmd.find_image(root,'action13_enter_email',delay*5,True)
        cmd.typetext(email)
        cmd.press_enter()
    # if cmd.find_image(root,'action13_connect_discord',delay*5,True):
    #     cmd.find_image(root,'action13_btn_connect',delay*5,True)
    #     dico.authorize()
        if cmd.find_image(root,'action13_share_conversation',delay*30,True):
            result += 'Pass'
        else:
            result += 'Fail'
        # cmd.press_down(20)
    # if cmd.find_image(root,'action13_connect_twit',delay*5,True):
    #     cmd.find_image(root,'action13_btn_connect',delay*5,True)
    #     twit.authorize_app()
    #     cmd.find_image(root,'action13_referral',delay*30,True)
    #     cmd.press('f5')
    # if cmd.find_image(root,'action13_quiz_litentry',delay*30,True):
    #     result += 'Pass'
    # else:
    #     result += 'Fail'
    return result

url15 = 'https://www.beoble.io/'
def action15(data,i):
    result = 'action15 = '
    wallet = data['metamask_wallet'][i]
    email = data['Google Account2'][i]
    id_twit = data['ID_twit'][i]
    id_dico = data['ID_discord'][i]
    # meta.run()
    open_url(url15)
    cmd.init_click()
    cmd.find_image(root,'action15_wait_loading',delay*60,False)
    cmd.find_image(root,'action15_signup',delay*5,True)
    cmd.find_image(root,'action15_welcome',delay*60,False)
    cmd.find_image(root,'action15_start',delay*5,True)
    if cmd.find_image(root,'action15_wallet',delay*10,False):
        cmd.wait(delay)
        # cmd.press_tab(1)
        cmd.typetext(wallet)
        cmd.press_enter()
    if cmd.find_image(root,'action15_email',delay*10,False):
        cmd.wait(delay)
        # cmd.press_tab(1)
        cmd.typetext(email)
        cmd.press_enter()
    if cmd.find_image(root,'action15_twitter',delay*10,False):
        cmd.wait(delay)
        # cmd.press_tab(2)
        cmd.typetext(id_twit)
        cmd.press_enter()
    if cmd.find_image(root,'action15_telegram',delay*10,False):
        cmd.wait(delay)
        # cmd.press_tab(1)
        cmd.typetext(id_dico)
        cmd.press_tab(1)
        cmd.press_enter()
    if cmd.find_image(root,'action15_thanks',delay*10,True):
        result += 'Pass'
    else:
        result += 'Fail'
    return result
    
url16='https://www.premint.xyz/GrapeCoin/'
def action16(data,i):
    result = 'action16 = '
    email = data['Google Account2'][i]
    # meta.run()
    open_url(url16)
    cmd.init_click()
    cmd.find_image(root,'action16_wait_loading',delay*60,False)
    cmd.find_image(root,'action16_login',delay*5,True)
    if cmd.find_image(root,'action16_login_ready',delay*30,False):
        if cmd.find_image(root,'action16_login_to_premint',delay*5,True):
            cmd.wait(delay*3)
            cmd.press_tab(1)
            cmd.press_enter()
            meta.connect_wallet()
            meta.sign()
            cmd.find_image(root,'action16_wait_loading',delay*20,True)
    if cmd.find_image(root,'action16_twit_connect',delay*5,True):
        cmd.find_image(root,'action16_authorize',delay*30,True) 
        cmd.find_image(root,'action16_wait_loading',delay*20,True)
    if cmd.find_image(root,'action16_follow1',delay*5,True):
        cmd.find_image(root,'action16_btn_follow',delay*10,True)
        cmd.init_click()
        if cmd.find_image(root,'action16_btn_following',delay*5,False):
            cmd.wait(delay)
            cmd.close_window()
    if cmd.find_image(root,'action16_follow2',delay*5,True):
        cmd.find_image(root,'action16_btn_follow',delay*10,True)
        cmd.init_click()
        if cmd.find_image(root,'action16_btn_following',delay*5,False):
            cmd.wait(delay)
            cmd.close_window()
    if cmd.find_image(root,'action16_thistweet',delay*5,True):
        cmd.find_image(root,'action16_like',delay*30,True)
        cmd.wait(delay)
        cmd.find_image(root,'action16_repost',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action16_repost_repost',delay*5,True)
        cmd.wait(delay)
        cmd.close_window()
    if cmd.find_image(root,'action16_twitter',delay*5,True):
        cmd.press_tab(5)
    if cmd.find_image(root,'action16_email',delay*5,True):
        cmd.wait(delay)
        cmd.typetext(email)
        cmd.press_tab(2)
        cmd.press_enter()
    if cmd.find_image(root,'action16_registered',delay*20,False):
        result += 'Pass'
    else:
        result += 'Fail'
    return result

url17='https://www.premint.xyz/grapecoin2/'
def action17(data,i):
    result = 'action17 = '
    email = data['Google Account2'][i]
    # meta.run()
    open_url(url17)
    cmd.init_click()
    cmd.find_image(root,'action17_wait_loading',delay*60,False)
    if cmd.find_image(root,'action17_connect_dico',delay*5,True):
        dico.authorize()
    if cmd.find_image(root,'action17_discord',delay*60,True):
        cmd.press_tab(3)
        cmd.press_enter()
    if cmd.find_image(root,'action17_registered',delay*20,False):
        result += 'Pass'
    else:
        result += 'Fail'
    return result

url18='https://viewer.tokenscript.org/'
def action18(data,i):
    result = 'action18 = '
    email = data['Google Account2'][i]
    # meta.run()
    open_url(url18)
    cmd.init_click()
    cmd.find_image(root,'action18_wait_loading',delay*60,False)
    if cmd.find_image(root,'action18_connect_wallet',delay*5,True):
        cmd.find_image(root,'action18_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.find_image(root,'action18_connected',delay*5,True)
    cmd.find_image(root,'action18_smartcat',delay*5,True)
    if cmd.find_image(root,'action18_1token',delay*5,True):
        cmd.find_image(root,'action18_smartcat_success',delay*30,False)
    # if cmd.find_image(root,'action18_adopt',delay*5,True):
    #     if cmd.find_image(root,'action18_adopt_confirm',delay*30,True):
    #         meta.allow_switch()
    #         meta.mint()

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
        result = action4() + '\n'
        f.write(result)    

    step = 5
    if start <= step and end >= step:
        result = action5() + '\n'
        f.write(result)    

    step = 6
    if start <= step and end >= step:
        result = action6() + '\n'
        f.write(result)    

    step = 7
    if start <= step and end >= step:
        result = action7() + '\n'
        f.write(result)    

    step = 8
    if start <= step and end >= step:
        result = action8() + '\n'
        f.write(result)    
    
    step = 9
    if start <= step and end >= step:
        result = action9() + '\n'
        f.write(result)    
    
    step = 10
    if start <= step and end >= step:
        result = action10() + '\n'
        f.write(result)
    
    step = 11
    if start <= step and end >= step:
        result = action11() + '\n'
        f.write(result)    
    
    step = 12
    if start <= step and end >= step:
        result = action12(data,i) + '\n'
        f.write(result)

    step = 13
    if start <= step and end >= step:
        result = action13(data,i) + '\n'
        f.write(result)  

    step = 14
    if start <= step and end >= step:
        result = action14(data,i) + '\n'
        f.write(result)      

    step = 15
    if start <= step and end >= step:
        result = action15(data,i) + '\n'
        f.write(result)
        
    step = 16
    if start <= step and end >= step:
        result = action16(data,i) + '\n'
        f.write(result)  
        
    step = 17
    if start <= step and end >= step:
        result = action17(data,i) + '\n'
        f.write(result) 

    step = 18
    if start <= step and end >= step:
        result = action18(data,i) + '\n'
        f.write(result)  