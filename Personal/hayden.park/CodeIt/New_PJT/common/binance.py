import time
import commands as cmd
import csv_handling as csv
import random
import os

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

data = csv.get_csv_data('binance.csv')


def add_whitelist(data, start, end):
    for i in range(start - 1, end):
        label = data['Address label'][i]
        coin = data['Coin'][i]
        address = data['Address_Metamask'][i]
        network = data['Network'][i]
        origin = data['Address origin'][i]
        print(i,":",label,coin,address,network,origin)
        cmd.find_image(root,'binance_whitelist_fill_in_label',delay*5,True) # label 탭 클릭
        cmd.scroll(-500)        # 마우스 스크롤 맨 아래로 이동
        cmd.copy_text(label)
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.press_tab(1)        # coin 으로 이동
        cmd.wait(delay)       # coin 목록 로딩 대기
        cmd.copy_text(coin)
        cmd.hotkey('ctrl','v')  # coin 명 검색어 입력
        cmd.press_enter()       # coin 선택
        cmd.wait(delay)       # 선택완료 대기
        cmd.press_tab(1)        # address 입력창 이동
        cmd.copy_text(address)
        cmd.hotkey('ctrl','v')  # address 입력
        cmd.wait(delay)
        cmd.press_tab(1)        # network 이동
        cmd.find_image(root,'binance_whitelist_network_'+network+'',delay*5,True)
        cmd.wait(delay)       # 선택완료 대기
        cmd.find_image(root,'binance_whitelist_address_origin',delay*5,True) # address origin 클릭
        cmd.wait(delay)       # 창 오픈 대기
        cmd.find_image(root,'binance_whitelist_address_origin_wallet_address',delay*5,True)
        cmd.press_tab(1)        # 목록 오픈
        cmd.find_image(root,'binance_whitelist_address_origin_meta_mask',delay*5,True) # metamask 선택
        cmd.find_image(root,'binance_whitelist_address_origin_ok',delay*5,True) # ok 버튼 클릭
        cmd.wait(delay)       # 완료 대기
        cmd.scroll(-500)        # 마우스 스크롤 맨 아래로 이동
        cmd.find_image(root,'binance_whitelist_add',delay*5,True) # add 버튼 클릭
        
def withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower):
    result = ''
    for i in range(start - 1, end):
        label = data['Address label'][i]
        coin = data['Coin'][i]
        address = data['Address_Metamask'][i]
        network = data['Network'][i]
        # amount = round((amount_upper-amount_lower) * random.random() + amount_lower,digit)
        amount = cmd.get_random(amount_lower,amount_upper,digit)
        print(i+1,":",label,coin,address,network,amount)
        cmd.init_click()
        cmd.scroll(2000)
        cmd.find_image(root,'binance_withdraw_select_wallet',delay*10,True)
        cmd.find_image(root,'binance_withdraw_select_from_address_book',delay*5,False)
        cmd.hotkey('ctrl','f')
        cmd.copy_text(label)
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.press_enter()
        cmd.find_image(root,'binance_withdraw_found_address',delay*5,True)
        cmd.wait(delay)
        if coin == 'bnb': # BNB 코인이면 BSC network 선택한 것에 대해 확인창 발생
            cmd.find_image(root,'binance_withdraw_i_understand',delay*5,True)
            cmd.wait(delay)
        cmd.press_esc()
        cmd.find_image(root,'binance_withdraw_amount',delay*5,True)
        cmd.press_tab(1)
        cmd.copy_text(str(amount))
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.scroll(-300)
        cmd.find_image(root,'btn_withdraw',delay*5,True)
        if coin == 'bnb': # BNB 코인이면 BSC network 선택한 것에 대해 확인창 발생
            cmd.find_image(root,'binance_withdraw_bnb_confirm',delay*5,True)
            cmd.wait(delay)
        else:
            cmd.find_image(root,'binance_withdraw_continue_gray',delay*3,True)
        cmd.find_image(root,'binance_withdraw_continue',delay*5,True)
        if not cmd.find_image(root,'binance_withdraw_complete',delay*5,True):
            result += ('{0} withdraw failed'.format(i+1)) + '\n'
        else:
            result += ('{0}:{1}:{2} completed'.format(i+1,label,amount) + '\n')
        if i < end-1:
            term = round((delay_upper - delay_lower) * random.random() + delay_lower,0)
            print('delay {} sec...'.format(term))
            time.sleep(term)
    return result

path = os.path.dirname(__file__)+"\\"+"result_binance.txt"
f = open(path, "a+")


# # # eth_arbitrum 송금_230918
# # 1~100
# workname = 'withdraw - eth_arbitrum'
# f.write(workname + '\n')

# start = 96
# end = 97
# amount_upper = 0.00700
# amount_lower = 0.00650
# digit = 5
# delay_upper = 300
# delay_lower = 180

# result = withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower)
# f.write(result)
# ##########################



# cmd.find_image(root,'select_coin_from_eth',delay*5,True)
# cmd.find_image(root,'select_coin_to_matic',delay*5,True)


# # matic_matic 송금_230914
# 101 ~ 200
workname = 'withdraw - matic'
f.write(workname + '\n')

start = 154  # matic_matic 은 101번부터 시작
end = 200
amount_upper = 15.100
amount_lower = 14.900
digit = 3
delay_upper = 300
delay_lower = 180

result = withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower)
f.write(result)
# ##########################

# # eth_eth 송금_230922
# # 201 ~ 300
# workname = 'withdraw - eth_eth'
# f.write(workname + '\n')

# start = 241  # eth_eth 는 201번부터 시작
# end = 245
# amount_upper = 0.03050
# amount_lower = 0.02950
# digit = 5
# delay_upper = 300
# delay_lower = 180

# result = withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower)
# f.write(result)
# ##########################

# 먼저 이더리움 출금하고 bnb 출금하기 위해 코인 변경
# cmd.find_image(root,'select_coin_from_eth',delay*5,True)
# cmd.find_image(root,'select_coin_to_bnb',delay*5,True)


# # bnb_bsc whitelist 생성_230921
# 301~400
# start = 321
# end = 400

# add_whitelist(data, start, end)
# #################################

# # # bnb_bsc 송금_231023
# workname = 'withdraw - bnb_bsc'
# f.write(workname + '\n')

# start = 351  # bnb_bsc 는 301번부터 시작
# end = 398
# amount_upper = 0.04750
# amount_lower = 0.04650
# digit = 5
# delay_upper = 300
# delay_lower = 180

# result = withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower)
# f.write(result)
# # ##########################

# f.close()


