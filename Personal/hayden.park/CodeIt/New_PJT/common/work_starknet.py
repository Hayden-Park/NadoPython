import commands as cmd
import metamask as meta
import argentX as arg
import galxe as gal
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

# 230930 스타크넷 브릿지
url1 = 'https://starkgate.starknet.io/'
def action1(data,i):
    result = 'action1 = '
    arg.run()
    cmd.open_url(url1)
    cmd.init_click()
    if cmd.find_image(root,'action1_terms',delay*15,True): #initial
        cmd.scroll(-10000)
        cmd.wait(delay)
        cmd.find_image(root,'action1_accept',delay*5,True)
        cmd.find_image_rate(root,'action1_popup',delay*10,True,98)
    if cmd.find_image(root,'action1_connect_wallets',delay*5,True): #지갑 둘다 연걸
        cmd.find_image(root,'action1_get_started',delay*5,True)
        if cmd.find_image(root,'action1_connect_metamask',delay*5,True):
            meta.connect_wallet()
            cmd.find_image(root,'action1_select_eth',delay*10,True)
            meta.allow_switch()
        cmd.find_image(root,'action1_connect_starknet_wallet',delay*10,True)
        if cmd.find_image(root,'action1_connect_argentx',delay*5,True):
            arg.connect_wallet()
        cmd.find_image(root,'action1_connect_continue',delay*5,True)
        cmd.find_image(root,'action1_deposit',delay*5,True)
        cmd.press_tab(1)
        cmd.press_space(1)
        cmd.wait(delay)
        cmd.find_image(root,'action1_deposit_eth',delay*5,True)
        cmd.press_tab(1)
        cmd.copy_text('0.02')
        cmd.hotkey('ctrl','v')
        cmd.wait(delay)
        cmd.press_tab(1)
        cmd.press_enter()
        if meta.mint(root,None,'action1_deposit_close'):
            cmd.find_image(root,'action1_deposit_close',delay*10,True)
            result += 'pass'
    return result

# 231002 스타크넷 브릿지
url2 = 'https://app.starknet.id/'
def action2(data,i):
    result = 'action2 = '
    username = data['domain_name'][i]
    email = data['Google Account'][i]
    arg.run()
    cmd.open_url(url2)
    cmd.init_click()
    cmd.find_image(root,'action2_wait_loading',delay*30,True)
    cmd.find_image(root,'action2_ok',delay*5,True)
    cmd.find_image(root,'action2_menu',delay*5,True)
    if cmd.find_image(root,'action2_connect_wallet',delay*5,True):
        if cmd.find_image(root,'action2_connect_argentx',delay*5,True):
            arg.connect_wallet()
    if cmd.find_image(root,'action2_connect_finish',delay*5,False):
        cmd.find_image(root,'action2_menu_close',delay*5,True)
    if cmd.find_image(root,'action2_search',delay*5,True):
        cmd.typetext(username)
        cmd.find_image(root,'action2_available',delay*5,True)
    if cmd.find_image(root,'action2_enter_email',delay*10,True):
        cmd.press_tab(1)
        cmd.wait(delay)
        cmd.typetext(email)
        cmd.find_image(root,'action2_no',delay*5,True)
        cmd.scroll(-2000)
        if cmd.find_image(root,'action2_register',delay*5,False):
            arg.mint(root,'action2_register','action2_mint_complete')
            cmd.find_image(root,'action2_mint_complete',delay*5,True)
            result += 'pass'
    return result

# 231002 USDC 4$ 스왑
url3 = 'https://www.myswap.xyz/#/'
def action3(data,i):
    result = 'action3 = '
    arg.run()
    cmd.open_url(url3)
    cmd.init_click()
    if cmd.find_image(root,'action3_connect_wallet',delay*30,True):
        if cmd.find_image(root,'action3_connect_argentx',delay*5,True):
            arg.connect_wallet()
    cmd.find_image(root,'action3_connect_finish',delay*5,True)
    if cmd.find_image(root,'action3_select_token',delay*5,True):
        cmd.find_image(root,'action3_usdc',delay*5,True)
        cmd.wait(delay)
        cmd.press_tab(1)
        amount = cmd.get_random(4.000,4.100,3)
        cmd.typetext(amount)
        if cmd.find_image(root,'action3_swap',delay*5,False):
            arg.mint(root,'action3_swap')
            cmd.find_image(root,'action3_swap_finish',delay*5,False)
            result += 'pass'
    return result

# 231002 유동성 1$
url4 = 'https://app.ekubo.org/'
def action4(data,i):
    result = 'action4 = '
    arg.run()
    cmd.open_url(url4)
    cmd.init_click()
    cmd.find_image(root,'action4_wait_loading',delay*60,True)
    if cmd.find_image(root,'action4_connect_wallet',delay*5,True):
        if cmd.find_image(root,'action4_connect_argentx',delay*5,True):
            arg.connect_wallet()
            cmd.find_image(root,'action4_connect_finish',delay*5,True)
            cmd.find_image_rate(root,'action4_connect_close',click=True,rate=98)
    if cmd.find_image(root,'action4_liq',delay*5,True):
        cmd.wait(delay*2)
        cmd.find_image(root,'action4_liq_new',delay*5,True)
        cmd.find_image(root,'action4_liq_to',delay*5,True)
        cmd.wait(delay)
        cmd.press_enter()
        cmd.find_image(root,'action4_liq_usdc',delay*5,True)
        cmd.find_image(root,'action4_liq_next',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action4_liq_next',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action4_liq_enter_usdc',delay*5,True)
        cmd.wait(delay)
        cmd.hotkey('ctrl','a')
        cmd.press('delete')
        amount = cmd.get_random(1.000,1.050,3)
        cmd.typetext(amount)
        cmd.wait(delay)
        if cmd.find_image(root,'action4_liq_add',delay*5,False):
            arg.mint(root,'action4_liq_add','action4_liq_success')
            if cmd.find_image(root,'action4_liq_success',delay*5,True):
                cmd.press_esc()
                result += 'pass'
    return result

# 231005 NFT Claim
url5 = 'https://spok.xyz/claim/ef590275-dc77-459e-aed0-f6b2cc4ee439'
def action5(data,i):
    result = 'action5 = '
    arg.run()
    cmd.open_url(url5)
    cmd.init_click()
    cmd.find_image(root,'action5_wait_loading',delay*60,False)
    cmd.find_image(root,'action5_check',delay*5,True)
    if cmd.find_image(root,'action5_connect_argentx',delay*10,True):
        arg.connect_wallet()
    if cmd.find_image(root,'action5_claim',delay*10,False):
        arg.mint(root,'action5_claim','action5_claim_finish')
        result += 'pass'
    return result


def subroutine(data,f,i,start,end):
    result = str(i+1)+'\n'
    f.write(result)

    step = 1
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action1(data,i) + '\n'
            f.write(result)    
    
    step = 2
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action2(data,i) + '\n'
            f.write(result)    
    
    step = 3
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action3(data,i) + '\n'
            f.write(result)    
    
    step = 4
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action4(data,i) + '\n'
            f.write(result)    

    step = 5
    if start <= step and end >= step:
        if 'fail' not in result:
            result = action5(data,i) + '\n'
            f.write(result)    

    # step = 6
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action6(data,i) + '\n'
    #         f.write(result)    

    # step = 7
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action7(data,i) + '\n'
    #         f.write(result)    

    # step = 8
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action8(data,i) + '\n'
    #         f.write(result)    
    
    # step = 9
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action9(data,i) + '\n'
    #         f.write(result)    
    
    # step = 10
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action10(data,i) + '\n'
    #         f.write(result)    
    
    # step = 11
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action11(data,i) + '\n'
    #         f.write(result) 

    # step = 12
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action12(data,i) + '\n'
    #         f.write(result)    

    # step = 13
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action13(data,i) + '\n'
    #         f.write(result)    

    # step = 14
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action14(data,i) + '\n' 
    #         f.write(result)    
    
    # step = 15
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action15(data,i) + '\n' 
    #         f.write(result)    

    # step = 16
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action16(data,i) + '\n' 
    #         f.write(result) 
