import commands as cmd
import metamask as meta
import galxe as gal
import twitter as twit

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

# 231105 bags 클레임
url1 = 'https://bags.fm/$l___hm'
def action1(data,i):
    result = 'action1 = '
    cmd.open_url(url1)
    cmd.find_image(root,'action1_wait_loading',delay*60,False)
    cmd.init_click()
    cmd.press_tab(1)
    cmd.press_enter()
    while True:
        if twit.authorize_app():
            break
    # 아직 에러남, 추후 업데이트
    result += 'pass'
    result += 'fail'
    return result

# 231105 스마트레이어 작업
url2 = 'https://www.smartlayer.network/referral/3589864032'
def action2(data,i):
    result = 'action2 = '
    if i<50:
        email = data['Google Account2'][i]
    else:
        email = data['Google Account'][i]
    cmd.open_url(url2)
    cmd.init_click()
    cmd.find_image(root,'action2_input_email',delay*60,True)
    cmd.typetext(email)
    cmd.wait(delay)
    cmd.find_image(root,'action2_checkbox',delay*5,True)
    cmd.press_tab(2)
    cmd.press_enter()
    
    result += 'pass'
    result += 'fail'
    return result

def subroutine(data,f,i,start,end):
    result = str(i+1)+'\n'
    f.write(result)

    step = 1
    if start <= step and end >= step:
        result = action1(data,i) + '\n'
        f.write(result)    
    
    step = 2
    if start <= step and end >= step:
        result = action2(data,i) + '\n'
        f.write(result)    
    
    