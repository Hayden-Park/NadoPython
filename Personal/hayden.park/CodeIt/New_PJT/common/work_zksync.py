import commands as cmd
import metamask as meta
import galxe as gal

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

url1 = 'https://owlto.finance/rewards/?ref=0x1667764DD15D6dfaB71fEBfa6D11eaDb7E9BC1ef'
amount = '0.025'
def action1():
    result = 'action1 = '
    open_url(url1)
    cmd.wait(delay)
    cmd.screen_full()
    if cmd.find_image(root,'connect_wallet',delay*10,True):
        cmd.find_image(root,'connect_metamask',delay*5,True)
        cmd.wait(delay*5)
        meta.connect_wallet()
    else:
        meta.connect_wallet_sign()
    cmd.wait(delay*5)
    cmd.screen_full()
    cmd.find_image(root,'bridge',delay*3,True)
    cmd.wait(delay*5)
    cmd.point_image(root,'bridge_to',delay*5)
    cmd.moveRel(80,30,True)
    cmd.find_image(root,'zksync_era',delay*3,True)
    cmd.find_image(root,'value',delay*3,True)
    cmd.copy_text(amount)
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'send_eth_to_zksync_era',delay*10,True)
    cmd.find_image(root,'confirm_and_send',delay*10,True)
    meta.mint_confirm()
    if cmd.find_image(root,'bridge_completed',delay*300,False):
        result += 'pass'
    else:
        result += 'fail'
    cmd.init_click()
    cmd.wait(delay)
    cmd.screen_left()
    return result

url2 = 'https://app.zkex.com/trade/ETH/USD'
amount2 = '0.022'
def action2():
    result = 'action2 = '
    open_url(url2)
    cmd.find_image(root,'wait_loading_2',delay*20,False)
    cmd.wait(delay*3)
    cmd.init_click()
    cmd.wait(delay)
    cmd.press_down(30)
    if cmd.find_image(root,'connect_wallet_2',delay*3,True):
        cmd.find_image(root,'connect_metamask_2',delay*5,True)
        if not cmd.find_image(root,'remember_me',delay*5,False):
            meta.connect_wallet()
        cmd.find_image(root,'remember_me',delay*5,True)
        cmd.find_image(root,'connect_final',delay*5,True)
        meta.connect_wallet_sign()
        meta.connect_wallet_sign()
        cmd.find_image(root,'connected_confirm',delay*10,False)
    cmd.wait(delay*3)
    cmd.find_image(root,'open_my_account',delay*5,True)
    cmd.wait(delay*2)
    cmd.find_image(root,'transfer_crypto',delay*5,True)
    cmd.find_image(root,'select_zksync_era',delay*5,True)
    meta.allow_to_add_network()
    cmd.wait(delay*10)
    cmd.find_image(root,'available_0025',delay*10,True)
    cmd.find_image(root,'enter_amount',delay*5,True)
    cmd.copy_text(amount2)
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'deposit',delay*5,True)
    meta.mint_confirm()
    cmd.find_image(root,'deposit_success',delay*120,True)
    cmd.find_image(root,'activate',delay*120,True)
    meta.connect_wallet_sign()
    cmd.find_image(root,'congratulations',delay*10,False)
    cmd.find_image(root,'start_trading',delay*5,True)
    
    cmd.screen_full()
    cmd.find_image(root,'click_sell',delay*5,True)
    cmd.find_image(root,'limit',delay*5,True)
    cmd.find_image(root,'market',delay*5,True)
    cmd.find_image(root,'amount_usd',delay*5,True)
    cmd.copy_text('10')
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'btn_sell',delay*5,True)
    cmd.find_image(root,'sell_enter_amount',delay*10,False) # sell 완료 확인

    cmd.find_image(root,'click_buy',delay*5,True)
    cmd.find_image(root,'100percent',delay*5,True)
    cmd.find_image(root,'btn_buy',delay*5,True)
    cmd.find_image(root,'buy_enter_amount',delay*10,False) # buy 완료 확인

    cmd.find_image(root,'convert',delay*5,True)
    cmd.find_image(root,'convert_from',delay*5,True)
    cmd.find_image(root,'convert_eth',delay*5,True)
    cmd.find_image(root,'convert_to',delay*5,True)
    cmd.find_image(root,'convert_usd',delay*5,True)

    for i in range(2):
        if i>0:
            cmd.find_image(root,'convert_reverse',delay*5,True)
        cmd.find_image(root,'convert_max',delay*5,True)
        cmd.find_image(root,'preview_conversion',delay*5,True)
        cmd.find_image(root,'convert_convert',delay*5,True)
        while True:
            if cmd.find_image(root,'convert_waiting',delay*10,False):
                break
            else:
                cmd.find_image(root,'convert_refresh',delay*10,True)
                cmd.find_image(root,'preview_conversion',delay*5,True)
                cmd.find_image(root,'convert_convert',delay*5,True)

    cmd.find_image(root,'trade',delay*5,True)
    cmd.wait(delay)
    cmd.screen_left()
    cmd.find_image(root,'balance',delay*5,True)
    cmd.find_image(root,'withdraw',delay*5,True)
    cmd.find_image(root,'send_crypto_back_to',delay*5,True)
    cmd.find_image(root,'withdraw_select',delay*5,True)
    cmd.find_image(root,'withdraw_eth',delay*5,True)
    cmd.find_image(root,'withdraw_zksync_era',delay*5,True)
    cmd.find_image(root,'withdraw_max',delay*5,True)

    cmd.find_image(root,'withdraw_fast',delay*5,True)
    # cmd.find_image(root,'withdraw_standard',delay*5,True)
    cmd.find_image(root,'withdraw_withdraw',delay*5,True)
    meta.connect_wallet_sign()
    return result
    
url3 = 'https://galxe.com/zkLink/campaign/GCti5UjiD1'
def action3():
    result = 'action3 = '
    open_url(url3)
    gal.wait_loading(delay*60)
    cmd.wait(delay*10)
    result += gal.twit_follow(root,'zklink_follow')
    cmd.wait(delay*3)
    result += gal.twit_like(root,'zklink_like')
    cmd.wait(delay*3)
    result += gal.twit_quote(root,'zklink_quote')
    return result

url4 = 'https://galxe.com/zkLink/campaign/GCXM4Uivsa'
def action4():
    result = 'action4 = '
    open_url(url4)
    cmd.init_click()
    cmd.find_image(root,'switch_to_polygon',delay*30,True)
    cmd.wait(delay)
    meta.allow_switch()
    cmd.find_image(root,'claim_1_nft',delay*10,True)
    cmd.find_image(root,'waiting_for_confirmation',delay*15,False)
    meta.mint_confirm()
    if cmd.find_image(root,'transaction_completed',delay*10,True):
        cmd.press_esc()
        result += 'pass'
    else:
        result += 'fail'
    return result

url5 = 'https://app.zkns.domains/'
def action5(domain_name):
    result = 'action5 = '
    meta.change_network('zksync_era')
    open_url(url5)
    cmd.init_click()
    if cmd.find_image(root,'connect_action5',delay*60,True):
        cmd.find_image(root,'connect_metamask_action5',delay*5,True)
        meta.connect_wallet()
    cmd.find_image(root,'enter_domain',delay*5,True)
    cmd.copy_text(domain_name)
    cmd.hotkey('ctrl','v')
    cmd.press_enter()
    cmd.find_image(root,'domain_available',delay*5,True)
    if cmd.find_image(root,'domain_fee',delay*60,True):
        cmd.press_down(5)
        cmd.find_image(root,'domain_request',delay*5,True)
        cmd.wait(delay)
        meta.allow_to_add_network()
        cmd.wait(delay*5)
        cmd.find_image(root,'domain_request',delay*5,True)
        meta.mint_confirm()
        cmd.find_image(root,'domain_registered',delay*10,True)
        result += 'pass'
    else:
        result += 'fail'
    return result

url6 = 'https://market.tevaera.com/'
def action6():
    result = 'action6 = '
    open_url(url6)
    cmd.init_click()
    cmd.find_image(root,'action6_menu',delay*60,True)
    if cmd.find_image(root,'action6_connect_wallet',delay*30,True):
        cmd.find_image(root,'action6_connect_metamask',delay*5,True)
        meta.connect_wallet()
    if cmd.find_image(root,'action6_sign_in',delay*10,True):
        meta.connect_wallet_sign()
        cmd.press_esc()
    cmd.wait(delay*5)
    cmd.find_image(root,'action6_button',delay*10,True)
    cmd.find_image(root,'action6_button',delay*10,True)
    if cmd.find_image(root,'action6_mint_citizen_id',delay*300,True):
        meta.mint_confirm()
        cmd.find_image(root,'action6_mint_citizen_ok',delay*10,True)
    cmd.wait(delay*5)
    cmd.find_image(root,'action6_button',delay*10,True)
    cmd.find_image(root,'action6_button',delay*10,True)
    if cmd.find_image(root,'action6_mint_onft',delay*300,True):
        meta.mint_confirm()
        cmd.find_image(root,'action6_mint_onft_ok',delay*10,True)
        cmd.press_esc()
    cmd.wait(delay*5)
    cmd.find_image(root,'action6_button',delay*10,True)
    cmd.find_image(root,'action6_button',delay*10,True)
    if cmd.find_image(root,'action6_bridge',delay*300,True):
        cmd.find_image(root,'action6_bridge_bridge',delay*30,True)
        cmd.find_image(root,'action6_bridge_confirm',delay*30,True)
        cmd.wait(delay*5)
        meta.mint_confirm()
        if cmd.find_image(root,'action6_completed',delay*600,True):
            cmd.press_esc()
            result += 'pass'
        else:
            result += 'fail'
    return result

# 230921 - 멀티시그
url7 = 'https://app.safe.global/welcome'
def action7(name):
    result = 'action7 = '
    open_url(url7)
    cmd.init_click()
    cmd.find_image(root,'action7_wait_loading',delay*60,False)
    cmd.find_image(root,'action7_accept_selection',delay*5,True)
    if cmd.find_image(root,'action7_connect_wallet',delay*5,True):
        cmd.find_image(root,'action7_connect_metamask',delay*5,True)
        meta.connect_wallet()
        cmd.find_image(root,'action7_create_new_account',delay*5,True)
        cmd.find_image(root,'action7_create_name',delay*10,True)
        cmd.copy_text(name)
        cmd.hotkey('ctrl','v')
        cmd.press_enter()
        cmd.wait(delay)
        cmd.find_image(root,'action7_create_next',delay*10,True)
        cmd.wait(delay)
        cmd.find_image(root,'action7_create_next',delay*10,True)
        if cmd.find_image(root,'action7_create_next',delay*60,False):
            if meta.mint_confirm():
                result += 'pass'
                cmd.find_image(root,'action7_start_using_safe',delay*120,True)
                cmd.find_image(root,'action7_got_it',delay*5,True)
            else:
                result += 'fail'
        else:
            result += 'fail'
    else:
        result += 'already done'
    return result
    
import random

def random_liq():
    total_upper = 6
    total_lower = 5.5
    total_digit = 2
    total_liq = round((total_upper-total_lower) * random.random() + total_lower,total_digit)
    liq = [0 for i in range(5)]

    liq_upper = total_liq* 21.5 /100
    liq_lower = total_liq* 18.5 /100
    liq_digit = 2
    temp = total_liq
    for i in range(5):
        if i<4:
            liq[i] = round((liq_upper-liq_lower) * random.random() + liq_lower,liq_digit)    
            temp -= liq[i]
        else:
            liq[i] = round(temp,liq_digit)
    return str(round(total_liq+0.01,2)), list(map(str,liq))

url8 = 'https://swap-zksync.spacefi.io/#/swap'

def action8(total_liq,liq):
    result = 'action8 = '
    open_url(url8)
    cmd.init_click()
    cmd.find_image(root,'action8_wait_loading',delay*60,False)
    if cmd.find_image(root,'action8_connect_wallet',delay*5,True):
        cmd.find_image(root,'action8_connect_metamask',delay*5,True)
        meta.connect_wallet()
    
    # swap
    cmd.find_image(root,'action8_swap',delay*5,True)
    cmd.find_image(root,'action8_select_token',delay*5,True)
    cmd.find_image(root,'action8_usdc',delay*5,True)
    cmd.find_image(root,'action8_swap_to',delay*5,True)
    cmd.press_tab(1)
    cmd.copy_text(total_liq)
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'action8_swap_swap',delay*5,True)
    cmd.find_image(root,'action8_swap_confirm',delay*5,True)
    if cmd.find_image(root,'action8_waiting_for_confirmation',delay*30,False):
        meta.mint_confirm()
        cmd.find_image(root,'action8_swap_close',delay*5,True)
        result += 'swap pass / '
    else:
        result += 'swap fail / '
    
    # pool
    cmd.find_image(root,'action8_pool',delay*5,True)    
    cmd.find_image(root,'action8_add_liquidity',delay*5,True)
    cmd.find_image(root,'action8_select_token',delay*5,True)
    cmd.find_image(root,'action8_usdc',delay*5,True)
    cmd.find_image(root,'action8_add_liquidity_title',delay*5,True)
    cmd.wait(delay*0.5)
    cmd.press_tab(4)
    cmd.copy_text(liq)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay)
    cmd.find_image(root,'action8_add_liquidity_approve',delay*5,True)
    cmd.wait(delay*5)
    meta.liquidity()
    cmd.wait(delay*5)
    cmd.find_image(root,'action8_add_liquidity_title',delay*5,True)
    cmd.wait(delay*0.5)
    while True:
        cmd.find_image(root,'action8_pool_supply',delay*5,True)
        if cmd.find_image(root,'action8_pool_confirm_supply',delay*5,True):
            break
    if cmd.find_image(root,'action8_waiting_for_confirmation',delay*30,False):
        meta.mint_confirm()
        if cmd.find_image(root,'action8_swap_close',delay*5,True):
            result += 'pool pass / '
            cmd.wait(delay*3)
        else:
            result += 'pool fail / '
    else:
        result += 'pool fail / '

    # farm
    cmd.find_image(root,'action8_farm',delay*30,True)
    if cmd.find_image(root,'action8_farm_connect',delay*60,True):
        cmd.find_image(root,'action8_farm_connect_zksync',delay*5,True)
        cmd.find_image(root,'action8_farm_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.wait(delay*8)
    cmd.find_image(root,'action8_farm_single_pool',delay*10,True)
    cmd.wait(delay*0.5)
    cmd.press_down(35)
    cmd.find_image(root,'action8_farm_eth_usdc',delay*5,True)
    cmd.wait(delay*0.5)
    cmd.press_down(25)
    if cmd.find_image(root,'action8_farm_enable_contract',delay*10,True):
        meta.liquidity()
        cmd.find_image(root,'action8_farm_success',delay*5,True)
        cmd.wait(delay*5)
        cmd.find_image(root,'action8_farm_stake',delay*5,True)
        cmd.wait(delay*5)
        cmd.find_image(root,'action8_farm_stake_max',delay*5,True)
        if cmd.find_image(root,'action8_farm_stake_confirm',delay*5,True):
            meta.mint_confirm()
            if cmd.find_image(root,'action8_farm_stake_success',delay*5,True):
                cmd.find_image(root,'action8_farm_stake_ok',delay*5,True)
                result += 'farm pass'
            else:
                result += 'farm fail'
        else:
            result += 'farm fail'
    else:
        result += 'farm fail'
    return result

url9 = 'https://syncswap.xyz/'
def action9(liq):
    result = 'action9 = '
    open_url(url9)
    cmd.init_click()
    if cmd.find_image(root,'action9_start',delay*15,True):
        cmd.wait(delay*2)
        cmd.find_image(root,'action9_explore',delay*5,True)
        cmd.find_image(root,'action9_explore_next',delay*5,True)
        cmd.wait(delay*2)
        cmd.find_image(root,'action9_explore_next',delay*5,True)
        cmd.wait(delay*2)
        cmd.find_image(root,'action9_explore_done',delay*5,True)
        cmd.wait(delay*2)
    if cmd.find_image(root,'action9_connect_wallet',delay*15,True):
        cmd.find_image(root,'action9_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.wait(delay*2)
    cmd.find_image(root,'action9_menu',delay*5,True)
    cmd.find_image(root,'action9_pools',delay*5,True)
    cmd.wait(delay*5)
    cmd.find_image(root,'action9_pools_all_pools',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(1)
    cmd.copy_text('usdc')
    cmd.hotkey('ctrl','v')
    cmd.find_image(root,'action9_pools_usdc_eth',delay*5,True)
    cmd.find_image(root,'action9_pools_enter',delay*5,True)
    cmd.find_image(root,'action9_pools_deposit',delay*5,True)
    cmd.find_image(root,'action9_pools_deposit_usdc',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(2)
    cmd.wait(delay)
    cmd.copy_text(liq)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay)
    cmd.press_tab(4)
    cmd.press_space(1)
    cmd.wait(delay)
    cmd.press_tab(1)
    cmd.press_enter()
    meta.liquidity()
    cmd.find_image(root,'action9_pools_unlocked',delay*10,True)
    cmd.press_esc()
    cmd.find_image(root,'action9_pools_deposit_deposit',delay*5,True)
    if cmd.find_image(root,'action9_pools_deposit_sign_in',delay*5,True):
        meta.mint_confirm()
        if cmd.find_image(root,'action9_pools_confirmed',delay*5,True):
            result += 'pass'
            cmd.press_esc()
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result

url10 = 'https://app.mute.io/swap'
def action10(liq):
    result = 'action10 = '
    open_url(url10)
    cmd.init_click()
    cmd.find_image(root,'action10_wait_loading',delay*60,False)
    if cmd.find_image(root,'action10_connect_wallet',delay*5,True):
        cmd.find_image(root,'action10_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.wait(delay*2)
    cmd.find_image(root,'action10_menu',delay*5,True)
    cmd.find_image(root,'action10_pool',delay*5,True)
    cmd.find_image(root,'action10_add_liquidity',delay*5,True)
    cmd.find_image(root,'action10_add_liquidity_title',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(2)
    cmd.press_enter()
    cmd.wait(delay)
    cmd.find_image(root,'action10_add_liquidity_eth',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action10_add_liquidity_title',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(3)
    cmd.press_enter()
    cmd.wait(delay)
    cmd.find_image(root,'action10_add_liquidity_usdc',delay*5,True)
    cmd.wait(delay)
    cmd.find_image(root,'action10_add_liquidity_title',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(6)
    cmd.press_enter() # manage
    cmd.wait(delay)
    cmd.find_image(root,'action10_deposit',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(5)
    cmd.wait(delay)
    cmd.copy_text(liq)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*0.5)
    cmd.press_tab(3)
    cmd.press_enter() # approve
    if cmd.find_image(root,'action10_wait_transaction',delay*30,True):
        meta.liquidity()
        if meta.mint_confirm():
            cmd.find_image(root,'action10_successful',delay*30,True)
            result += 'pass'
            cmd.press_esc()
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result
    
url11 = 'https://app.mav.xyz/?chain=324'
def action11(liq):
    result = 'action11 = '
    open_url(url11)
    cmd.init_click()
    cmd.find_image(root,'action11_wait_loading',delay*60,False)
    if cmd.find_image(root,'action11_connect_wallet',delay*5,True):
        cmd.find_image(root,'action11_by_checking',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action11_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.wait(delay*2)
    cmd.find_image(root,'action11_pools',delay*10,True)
    cmd.find_image(root,'action11_pools_search',delay*20,True)
    cmd.copy_text('usdc-eth')
    cmd.hotkey('ctrl','v')
    cmd.wait(delay)
    cmd.press_enter()
    cmd.find_image(root,'action11_pools_usdc_eth',delay*10,True)
    cmd.wait(delay*3)
    cmd.find_image(root,'action11_select_pool',delay*10,True)
    cmd.wait(delay)
    cmd.press_tab(4)
    cmd.find_image(root,'action11_select_next',delay*10,True)
    cmd.wait(delay)
    cmd.find_image(root,'action11_select_mode',delay*10,True)
    cmd.wait(delay)
    cmd.press_tab(4)
    cmd.find_image(root,'action11_select_next2',delay*10,True)
    cmd.wait(delay)
    cmd.find_image(root,'action11_pools_usdc',delay*10,True)
    cmd.wait(delay)
    cmd.press_tab(1)
    cmd.wait(delay)
    cmd.copy_text(liq)
    cmd.hotkey('ctrl','v')
    cmd.wait(delay*2)
    cmd.press_tab(5)
    cmd.press_enter()
    cmd.wait(delay)
    if cmd.find_image(root,'action11_pools_approve',delay*10,True):
        cmd.wait(delay*5)
        meta.liquidity()
    repeat = True
    while repeat:
        cmd.find_image(root,'action11_pools_confirm_amount',delay*2,True)
        success = meta.mint_confirm()
        if success and cmd.find_image(root,'action11_pools_done',delay*5,True):
            repeat = False
            result += 'pass'
        else:
            cmd.wait(delay)
            cmd.init_click()
            cmd.press_down(10)
            cmd.find_image(root,'action11_pools_confirm',delay*5,True)
    return result

# url12 = 'https://zksync-v2.velocore.xyz/swap'
def action12(liq):
    pass

url13 = 'https://app.xy.finance/'
def action13(liq):
    result = 'action13 = '
    open_url(url13)
    cmd.init_click()
    cmd.find_image(root,'action13_wait_loading',delay*60,False)
    if cmd.find_image(root,'action13_connect_wallet',delay*5,True):
        cmd.find_image(root,'action13_connect_metamask',delay*5,True)
        meta.connect_wallet()
        if meta.allow_switch():
            meta.allow_switch()
        else:
            cmd.find_image(root,'action13_select',delay*5,True)
            cmd.find_image(root,'action13_select_zksync',delay*5,True)
    cmd.wait(delay*3)
    cmd.find_image(root,'action13_pool',delay*5,True)
    cmd.find_image(root,'action13_pool_usdc',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(1)
    cmd.press_enter()
    cmd.find_image(root,'action13_pool_usdc_pool',delay*5,True)
    cmd.wait(delay)
    cmd.press_down(15)
    cmd.find_image(root,'action13_pool_deposit',delay*5,True)
    cmd.wait(delay)
    cmd.press_tab(2)
    cmd.wait(delay)
    cmd.typewrite(str(liq))
    cmd.wait(delay)
    if cmd.find_image(root,'action13_pool_approve',delay*15,True):
        cmd.wait(delay*5)
        if meta.liquidity():
            cmd.wait(delay*2)
        if cmd.find_image(root,'action13_pool_deposit_deposit',delay*30,True):
            cmd.find_image(root,'action13_pool_deposit_confirm',delay*10,True)
            if cmd.find_image(root,'action13_pool_waiting',delay*10,False):
                meta.mint_confirm()
                if cmd.find_image(root,'action13_pool_dismiss',delay*5,True):
                    result += 'pass'
                else:
                    result += 'fail'
            else:
                result += 'fail'
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result

url14 = 'https://l2marathon.com/'
def action14():
    result = 'action14 = '
    meta.change_network('zksync_era')
    open_url(url14)
    cmd.init_click()
    cmd.find_image(root,'action14_wait_loading',delay*60,False)
    if cmd.find_image(root,'action14_connect_wallet',delay*5,True):
        meta.connect_wallet()
    cmd.wait(delay*2)
    
    if cmd.find_image(root,'action14_mint',delay*5,True):
        meta.mint_confirm()
    if cmd.find_image(root,'action14_mint_check',delay*10,False):
        cmd.find_image(root,'action14_mara',delay*5,True)
    if cmd.find_image(root,'action14_claim_ready',delay*10,False):
        if cmd.find_image(root,'action14_claim_mara',delay*5,True):
            meta.mint_confirm()
    if cmd.find_image(root,'action14_claim_success',delay*30,True):
        cmd.press_down(20)
        cmd.find_image(root,'action14_send_bnb',delay*5,True)
        cmd.find_image(root,'action14_send_optimism',delay*5,True)
        cmd.find_image(root,'action14_send_arbitrum',delay*5,True)
        cmd.find_image(root,'action14_send_polygon',delay*5,True)
        cmd.find_image(root,'action14_send_avalanche',delay*5,True)
        if cmd.find_image(root,'action14_send',delay*5,True):
            meta.mint_confirm()
            if cmd.find_image(root,'action14_send_finish',delay*5,True):
                result += 'pass'
            else:
                result += 'fail'
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result

url15 = 'https://mailzero.network/stamp?earneth=806975'
# zksync era 로 시작필요
def action15():
    result = 'action15 = '
    meta.change_network('zksync_era')
    open_url(url15)
    cmd.init_click()
    cmd.find_image(root,'action15_wait_loading',delay*60,False)
    if cmd.find_image(root,'action15_connect_wallet',delay*5,True):
        cmd.find_image(root,'action15_connect_metamask',delay*5,True)
        meta.connect_wallet()
    cmd.find_image(root,'action15_close',delay*5,True)
    cmd.find_image(root,'action15_connect_wallet_done',delay*10,False)
    
    if cmd.find_image(root,'action15_free_mint',delay*10,True):
        meta.mint_confirm()
        cmd.find_image(root,'action15_popup_close',delay*5,True)
    if cmd.find_image(root,'action15_dropbox',delay*10,True):
        cmd.wait(delay*3)
        cmd.find_image(root,'action15_dropbox_open',delay*10,True)
        cmd.find_image(root,'action15_dropbox_unlock',delay*10,True)
        cmd.wait(delay*3)
        if meta.mint_confirm():
            result += 'pass'
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result

url16 = 'https://element.market/invite?ref=U6DU'
def action16():
    result = 'action16 = '
    meta.change_network('zksync_era')
    open_url(url16)
    cmd.init_click()
    cmd.find_image(root,'action16_wait_loading',delay*60,False)
    cmd.wait(delay*2)
    cmd.find_image(root,'action16_language',delay*10,True)
    cmd.find_image(root,'action16_language_english',delay*10,True)
    cmd.find_image(root,'action16_accept',delay*10,True)
    if cmd.find_image(root,'action16_connect_metamask',delay*10,True):
        meta.connect_wallet()
        cmd.wait(delay)
        meta.allow_switch()
        sign_in = meta.sign()
        if not sign_in:
            cmd.init_click()
            cmd.press('f5')
            cmd.find_image(root,'action16_wait_loading',delay*60,False)
            cmd.wait(delay*3)
            cmd.find_image(root,'action16_accept',delay*10,True)
            meta.sign()
        meta.sign()
        cmd.wait(delay*5)
        cmd.init_click()
        cmd.press('f5')
        cmd.find_image(root,'action16_wait_loading',delay*60,False)
        cmd.wait(delay*3)
        cmd.find_image(root,'action16_accept',delay*10,True)
        if cmd.find_image(root,'action16_popup_confirm',delay*10,True):
            if cmd.find_image(root,'action16_popup_finish',delay*10,True):
                cmd.find_image(root,'action16_popup_done',delay*10,True)
            else:
                result += 'fail'
        else:
            result += 'fail'
    
    cmd.find_image(root,'action16_coin',delay*10,True)
    cmd.find_image(root,'action16_coin_zksync',delay*10,True)
    if cmd.find_image(root,'action16_popup2',delay*10,True):
        cmd.wait(delay)
        cmd.press_esc()
    cmd.wait(delay)
    cmd.find_image(root,'action16_ranking',delay*10,True)
    cmd.wait(delay)
    cmd.find_image(root,'action16_ranking_top',delay*10,True)
    cmd.wait(delay*3)
    cmd.init_click()
    cmd.press_down(10)
    cmd.wait(delay*3)
    if cmd.find_image(root,'action16_zk_dagger',delay*60,True):
        while True:
            if cmd.point_image(root,'action16_zk_dagger_item',delay*60):
                cmd.wait(delay*2)
                cmd.find_image(root,'action16_zk_dagger_buy',delay*10,True)
                if cmd.find_image(root,'action16_change_network',delay*5,True):
                    cmd.find_image(root,'action16_change_network_button',delay*10,True)
                    meta.allow_switch()
                cmd.find_image(root,'action16_checkout',delay*10,False)                
                if meta.mint_confirm():
                    break
                else:
                    cmd.find_image(root,'action16_zk_dagger_popup_close',delay*10,True)
                    cmd.init_click()
                    cmd.press('f5')
            else:
                cmd.init_click()
                cmd.press('f5')
        if cmd.find_image(root,'action16_buy_success',delay*10,True):
            cmd.find_image(root,'action16_zk_dagger_ok',delay*10,True)
            result += 'pass'
        else:
            result += 'fail'
    else:
        result += 'fail'
    return result




def subroutine(data,f,i,start,end):
    result = str(i+1)+'\n'
    f.write(result)
    total_liq = data['zksync_total'][i]
    liq8 = data['zksync_8'][i]
    liq9 = data['zksync_9'][i]
    liq10 = data['zksync_10'][i]
    liq11 = data['zksync_11'][i]
    liq13 = data['zksync_13'][i]
    domain_name = data['domain_name'][i]
    
    step = 1
    if start <= step and end >= step:
        if 'fail' not in result:
            meta.change_network('arbitrum')
            result = action1() + '\n'
            f.write(result)    
    
    step = 2
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action2() + '\n'
            f.write(result)    
    
    step = 3
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action3() + '\n'
            f.write(result)    
    
    step = 4
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action4() + '\n'
            f.write(result)    

    step = 5
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action5(domain_name) + '\n'
            f.write(result)    

    step = 6
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action6() + '\n'
            f.write(result)    

    step = 7
    if start <= step and end >= step:
        if 'fail' not in result:
            meta.change_network('zksync_era')
            result = action7(domain_name) + '\n'
            f.write(result)    

    step = 8
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action8(total_liq,liq8) + '\n'
            f.write(result)    
    
    step = 9
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action9(liq9) + '\n'
            f.write(result)    
    
    step = 10
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action10(liq10) + '\n'
            f.write(result)    
    
    step = 11
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action11(liq11) + '\n'
            f.write(result) 

    step = 13
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action13(liq13) + '\n'
            f.write(result)    

    step = 14
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action14() + '\n' 
            f.write(result)    
    
    step = 15
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action15() + '\n' 
            f.write(result)    

    step = 16
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action16() + '\n' 
            f.write(result)    