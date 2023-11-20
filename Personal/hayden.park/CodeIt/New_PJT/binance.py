import time
import commands as cmd
import csv_handling as csv
import random

delay = 1

data = csv.get_csv_data('whitelist.csv')


def add_whitelist(data, start, end):
    for i in range(start - 1, end):
        label = data['Address label'][i]
        coin = data['Coin'][i]
        address = data['Address'][i]
        network = data['Network'][i]
        origin = data['Address origin'][i]
        print(i,":",label,coin,address,network,origin)
        cmd.find_image('binance_whitelist_fill_in_label.png',delay*10,True) # label 탭 클릭
        cmd.scroll(-500)        # 마우스 스크롤 맨 아래로 이동
        cmd.copy_text(label)
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.press_tab(1)        # coin 으로 이동
        time.sleep(delay)       # coin 목록 로딩 대기
        cmd.copy_text(coin)
        cmd.hotkey('ctrl','v')  # coin 명 검색어 입력
        cmd.press_enter()       # coin 선택
        time.sleep(delay)       # 선택완료 대기
        cmd.press_tab(1)        # address 입력창 이동
        cmd.copy_text(address)
        cmd.hotkey('ctrl','v')  # address 입력
        time.sleep(delay*1.5)
        cmd.press_tab(1)        # network 이동
        cmd.find_image('binance_whitelist_network_'+network+'.png',delay*5,True)
        cmd.find_image('binance_whitelist_address_origin.png',delay*5,True) # address origin 클릭
        cmd.find_image('binance_whitelist_address_origin_wallet_address.png',delay*5,True)
        cmd.press_tab(1)        # 목록 오픈
        cmd.find_image('binance_whitelist_address_origin_meta_mask.png',delay*5,True) # metamask 선택
        cmd.find_image('binance_whitelist_address_origin_ok.png',delay*5,True) # ok 버튼 클릭
        cmd.scroll(-500)        # 마우스 스크롤 맨 아래로 이동
        cmd.find_image('binance_whitelist_add.png',delay*5,True) # add 버튼 클릭
        
def withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower):
    for i in range(start - 1, end):
        label = data['Address label'][i]
        coin = data['Coin'][i]
        address = data['Address'][i]
        network = data['Network'][i]
        amount = round((amount_upper-amount_lower) * random.random() + amount_lower,digit)
        print(i+1,":",label,coin,address,network,amount)
        cmd.init_click()
        cmd.scroll(2000)
        cmd.find_image('binance_withdraw_select_wallet.png',delay*10,True)
        cmd.find_image('binance_withdraw_select_from_address_book.png',delay*5,True)
        cmd.hotkey('ctrl','f')
        cmd.copy_text(label)
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.press_enter()
        cmd.find_image('binance_withdraw_found_address.png',delay*10,True)
        time.sleep(delay)
        cmd.press_esc()
        time.sleep(delay)
        cmd.find_image('binance_withdraw_amount.png',delay*5,True)
        cmd.press_tab(1)
        cmd.copy_text(str(amount))
        cmd.hotkey('ctrl','v')  # address label 입력
        cmd.press_tab(3)
        cmd.press_enter()
        cmd.find_image('binance_withdraw_continue.png',delay*5,True)
        cmd.find_image('binance_withdraw_complete.png',delay*5,True)
        if i < end-1:
            term = round((delay_upper - delay_lower) * random.random() + delay_lower,0)
            print('delay {} sec...'.format(term))
            time.sleep(term)

# # eth_arbitrum 송금_230914
# start = 1
# end = 17
# amount_upper = 0.03010
# amount_lower = 0.02900
# digit = 5
# delay_upper = 300
# delay_lower = 180
# ##########################

# # matic_matic 송금_230914
start = 102  # matic_matic 은 101번부터 시작
end = 117
amount_upper = 15.100
amount_lower = 14.900
digit = 3
delay_upper = 300
delay_lower = 180
# ##########################


withdraw(data,start,end,amount_upper,amount_lower,digit,delay_upper,delay_lower)
