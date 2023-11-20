import commands as cmd
import metamask as meta
import argentX as arg
import galxe as gal
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

# 231028 rhino 브릿지
url1 = 'https://app.rhino.fi/bridge'
def action1(data,i):
    result = 'action1 = '
    meta.run()
    cmd.open_url(url1)
    cmd.init_click()
    cmd.find_image(root,'action1_wait_loading',delay*30,False)
    if not cmd.find_image(root,'action1_wallet_connected',delay*5,False):
        cmd.find_image(root,'action1_connect_wallet',delay*5,True)
        cmd.find_image(root,'action1_connect_metamask',delay*10,True)
        if not cmd.find_image(root,'action1_wallet_connected',delay*5,False):
            meta.connect_wallet()
    cmd.init_click()
    cmd.find_image(root,'action1_token',delay*5,True)
    cmd.press_tab(2)
    cmd.press_enter()
    cmd.wait(delay)
    cmd.typetext('eth')
    cmd.find_image(root,'action1_select_eth',delay*5,True)
    cmd.press_tab(1)
    amount = '0.0015'
    cmd.typetext(amount)
    cmd.wait(delay)
    cmd.press_tab(7)
    cmd.press_enter()
    # cmd.find_image(root,'action1_review_bridge',delay*5,True)
    cmd.wait(delay*3)
    cmd.press_tab(3)
    cmd.press_enter()
    # cmd.find_image(root,'action1_bridge_funds',delay*5,True)
    if cmd.find_image(root,'action1_switch',delay*5,True):
        meta.allow_switch()
    meta.mint()
    result += 'pass'
    return result

# 231028 scroll 네트워크 지갑에 추가
url2 = 'https://scroll.io/bridge'
def action2(data,i):
    result = 'action2 = '
    meta.run()
    cmd.open_url(url2)
    cmd.init_click()
    cmd.find_image(root,'action2_wait_loading',delay*30,False)
    if not cmd.find_image(root,'action2_select_scroll_done',delay*5,False):
        if cmd.find_image(root,'action2_connect_wallet',delay*10,True):
            cmd.find_image(root,'action2_connect_metamask',delay*5,True)
            meta.connect_wallet()
            meta.allow_switch()
        
        cmd.find_image(root,'action2_select_eth',delay*5,True)
        if cmd.find_image(root,'action2_select_scroll',delay*5,True):
            meta.allow_to_add_network()
            result += 'pass'
    else:
        result += 'pass'
    return result

# 231028 컨트랙 배포
script = '''pragma solidity 0.8.17;

// SPDX-License-Identifier: MIT

contract JEZFinance {
  string public name = "Jez Finance";
  string public symbol = "JEZ";
  uint8 public decimals = 18;
  uint256 public totalSupply = 10000000000;

  mapping (address => uint256) public balances;
  address public owner;

  constructor() {
    owner = msg.sender;
    balances[owner] = totalSupply;
  }

  function transfer(address recipient, uint256 amount) public {
    require(balances[msg.sender] >= amount, "Insufficient balance.");
    balances[msg.sender] -= amount;
    balances[recipient] += amount;
  }
}'''
url3 = 'https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js&lang=en'
def action3(data,i):
    result = 'action3 = '
    cmd.open_url(url3)
    cmd.init_click()
    if cmd.find_image(root,'action3_accept',delay*20,True):
        cmd.find_image(root,'action3_next',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action3_next',delay*5,True)
        cmd.wait(delay)
        cmd.find_image(root,'action3_done',delay*5,True)
    cmd.find_image(root,'action3_menu',delay*5,True)
    cmd.find_image(root,'action3_create',delay*5,True)
    cmd.find_image(root,'action3_create_workspace',delay*5,True)
    cmd.press_tab(2)
    cmd.typetext('scroll')
    cmd.press_enter()
    cmd.wait(delay*2)
    cmd.find_image(root,'action2_new_file',delay*5,True)
    cmd.typetext('scroll.sol')
    cmd.press_enter()
    cmd.wait(delay)
    cmd.find_image(root,'action3_scroll_sol',delay*5,True)
    cmd.press_tab(1)
    cmd.typetext(script)
    cmd.find_image(root,'action3_paste_ok',delay*5,True)
    cmd.find_image(root,'action3_compiler',delay*5,True)
    cmd.find_image(root,'action3_compile',delay*5,True)
    cmd.wait(delay*5)
    if cmd.find_image(root,'action3_compile_done',delay*20,False):
        cmd.find_image(root,'action3_deploy_menu',delay*5,True)
        cmd.find_image(root,'action3_environment',delay*5,True)
        cmd.press_tab(2)
        cmd.press_down(1)
        if cmd.find_image(root,'action3_select_metamask',delay*5,True):
            meta.connect_wallet()
            cmd.find_image(root,'action3_deploy',delay*5,False)
            meta.mint(root,img_request='action3_deploy',img_complete='action3_deploy_done')
            if cmd.find_image(root,'action3_deploy_done',delay*5,False):
                result += 'pass'
    return result

# 231028 action2,3 대신 머클리에서 scroll 추가하고 deploy
url4 = 'https://minter.merkly.com/deploy/erc20'
def action4(data,i):
    result = 'action4 = '
    meta.run()
    cmd.open_url(url4)
    cmd.init_click()
    cmd.find_image(root,'action4_wait_loading',delay*30,False)
    cmd.find_image(root,'action4_name',delay*5,True)
    cmd.typetext('scroll')
    cmd.press_tab(1)
    cmd.wait(delay)
    cmd.typetext('scroll')
    cmd.find_image(root,'action4_deploy',delay*5,True)
    meta.allow_to_add_network()
    meta.connect_wallet()
    meta.mint()
    if cmd.find_image(root,'action4_mint_finish',delay*5,False):
        result += 'pass'
    return result

# 231028 mint 가능여부 확인
url5 = 'https://scroll.io/developer-nft/check-eligibility'
def action5(data,i):
    result = 'action5 = '
    cmd.open_url(url5)
    cmd.init_click()
    cmd.find_image(root,'action5_wait_loading',delay*30,True)
    if cmd.find_image(root,'action5_connect_wallet',delay*5,True):
        cmd.find_image(root,'action5_connect_metamask',delay*5,True)
        meta.connect_wallet()
        cmd.find_image(root,'action5_wait_loading',delay*5,True)
    cmd.scroll(-10000)
    cmd.find_image(root,'action5_check_eligibility',delay*5,True)
    if cmd.find_image(root,'action5_eligible',delay*5,True):
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
    
    # step = 4
    # if start <= step and end >= step:
    #     if 'fail' not in result:
    #         result = action4(data,i) + '\n'
    #         f.write(result)    

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

