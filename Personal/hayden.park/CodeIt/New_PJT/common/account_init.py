import commands as cmd

delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]
pw = '12341234'

# 231030 gmail 첫 로그인 & pw 변경
url1 = 'https://accounts.google.com/'
image_path = r'C:\Projects\NadoPython\Personal\hayden.park\CodeIt\New_PJT\image\profile_discord_x'
def action1(data,i):
    result = 'action1 = '
    profile_no = str(data['profile_no'][i])
    email = data['Google Account2'][i]
    pw_old = data['PW(Init)2'][i]
    pw_new = data['PW(Changed)'][i]
    recovery_email = data['Restore email2'][i]
    cmd.open_url(url1)
    cmd.init_click()
    cmd.find_image(root,'action1_wait_loading',delay*30,False)

    # 이미 로그인 되어있는 계정 로그아웃
    if cmd.find_image(root,'action1_already_logged_in',delay*5,False):
        cmd.find_image(root,'action1_search_google_account',delay*5,True)
        cmd.press_tab(3)
        cmd.press_space(1)
        cmd.find_image(root,'action1_sign_out',delay*5,True)
        cmd.find_image(root,'action1_wait_loading',delay*30,False)
        cmd.find_image(root,'action1_another_account',delay*5,True)
        cmd.find_image(root,'action1_wait_loading',delay*30,False)

    if not cmd.find_image(root,'action1_lang_eng_eng',delay*5,False):
        cmd.find_image(root,'action1_btn_lang',delay*5,True)
        cmd.wait(delay)
        cmd.press_down(5)
        cmd.find_image(root,'action1_lang_eng',delay*5,True)
    
    #gmail 입력
    if not cmd.find_image(root,'action1_input_email',delay*5,False):
        cmd.find_image(root,'action1_another_account',delay*5,True)
    cmd.wait(delay*10)
    cmd.find_image(root,'action1_wait_loading',delay*5,True)
    cmd.press_tab(1)
    cmd.typetext(email)
    cmd.find_image(root,'action1_btn_next',delay*5,True)

    #pw_old 입력
    cmd.find_image(root,'action1_input_pw',delay*5,False)
    cmd.find_image(root,'action1_wait_loading',delay*5,True)
    cmd.press_tab(2)
    cmd.typetext(pw_old)
    cmd.find_image(root,'action1_btn_next',delay*5,True)
    cmd.find_image(root,'action1_google_account_loading',delay*30,True)

    #비밀번호 저장
    if cmd.find_image(root,'save_pw_show',delay*10,True):
        cmd.press_tab(1)
        cmd.press_enter()

    #sign up
    if cmd.find_image(root,'action1_signup_to_get',delay*3,True):
        cmd.find_image(root,'action1_keep_me_updated',delay*3,True)
        cmd.find_image(root,'action1_keep_me_updated',delay*3,True)
    
    #프사 업데이트
    if cmd.find_image(root,'action1_add_profile_pic',delay*5,True):
        cmd.find_image(root,'action1_add_profile_pic2',delay*30,True)
        cmd.find_image(root,'action1_profile_from_pc',delay*10,True)
        cmd.find_image(root,'action1_upload_from_pc',delay*5,True)
        cmd.hotkey('alt','d')
        cmd.hotkey('ctrl','a')
        cmd.press('delete')
        cmd.typetext(image_path)
        cmd.press_enter()
        cmd.wait(delay)
        cmd.hotkey('alt','n')
        cmd.typetext(profile_no)
        cmd.press_enter()
        cmd.find_image(root,'action1_profile_rotate',delay*20,False)
        cmd.find_image(root,'action1_profile_next',delay*5,True)
        cmd.find_image(root,'action1_profile_saveas',delay*5,True)
        cmd.find_image(root,'action1_profile_dismiss',delay*5,True)
        cmd.init_click()
    #설정 후 done 및 완료확인
    cmd.find_image(root,'action1_btn_done',delay*10,True)
    cmd.find_image(root,'action1_welcome',delay*30,False)

    #비번바꾸기
    cmd.find_image(root,'action1_security',delay*5,True)
    cmd.wait(delay*5)
    cmd.press_down(5)
    cmd.find_image(root,'action1_security_pw',delay*20,True)
    cmd.find_image(root,'action1_change_pw_loading',delay*30,False)
    cmd.find_image(root,'action1_change_pw_title',delay*5,True)
    cmd.press_tab(3)
    cmd.typetext(pw_new)
    cmd.wait(delay*0.5)
    cmd.press_tab(3)
    cmd.typetext(pw_new)
    cmd.wait(delay*0.5)
    if cmd.find_image(root,'action1_btn_change_pw',delay*5,True):
        result += 'pass'
    #변경완료 후 다시 security 페이지 로딩 대기
    cmd.find_image(root,'action1_security_loading',delay*30,False)
    #비밀번호 저장
    if cmd.find_image(root,'save_pw_show',delay*10,True):
        cmd.press_tab(1)
        cmd.press_enter()
    return result

url2 = ''
def action2(data,i):
    result = 'action2 = '
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

