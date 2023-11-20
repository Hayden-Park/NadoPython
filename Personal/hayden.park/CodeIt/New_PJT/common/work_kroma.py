import commands as cmd
import metamask as meta
import argentX as arg
import galxe as gal
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

# 231004 kroma 민팅
url1 = 'https://kroma.network/ecosystem/experience/nft'
def action1(data,i):
    result = 'action1 = '
    meta.change_network('eth')
    cmd.open_url(url1)
    cmd.init_click()
    cmd.find_image(root,'action1_wait_loading',delay*60,True)
    cmd.find_image(root,'action1_menu',delay*5,True)
    if cmd.find_image(root,'action1_connect_wallet',delay*5,True):
        if cmd.find_image(root,'action1_connect_metamask',delay*5,True):
            meta.connect_wallet()
        cmd.find_image(root,'action1_connect_finish',delay*10,True)    
    cmd.find_image(root,'action1_menu_close',delay*5,True)
    cmd.press_down(5)
    cmd.find_image(root,'action1_mint_kroma',delay*5,True)
    cmd.find_image(root,'action1_accept_cookies',delay*3,True)
    cmd.find_image(root,'action1_minting_now',delay*10,True)
    cmd.press_down(20)
    cmd.find_image(root,'action1_mint',delay*30,True)
    if cmd.find_image(root,'action1_bridge',delay*30,False):
        meta.mint(root,img_request='action1_bridge')
        cmd.find_image(root,'action1_bridge_finish',delay*300,False)
        cmd.find_image(root,'action1_go_to_mint',delay*30,True)
        cmd.find_image(root,'action1_switch_to_kroma',delay*30,True)
        meta.allow_to_add_network()
        cmd.find_image(root,'action1_mint_mint',delay*30,False)
        meta.mint(root,img_request='action1_mint_mint')
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
    
    # step = 2
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action2(data,i) + '\n'
    #         f.write(result)    
    
    # step = 3
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action3(data,i) + '\n'
    #         f.write(result)    
    
    # step = 4
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action4(data,i) + '\n'
    #         f.write(result)    

    # step = 5
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action5(data,i) + '\n'
    #         f.write(result)    

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
