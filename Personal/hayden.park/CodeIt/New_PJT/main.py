import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__))+'\\common')
import time
from common import gologin_profile as profile
from common import metamask as meta
from common import argentX as arg
from common import twitter as twit
from common import google_app as ggl
from common import csv_handling as csv
from common import commands as cmd
from common import win_control as win
from common import account_init as acc_init

####### 실행할 작업파일
# from common import work_gvrt as grvt
from common import work_polyhedra as polyhedra
from common import work_holograph as holograph
from common import work_galxe as galxe
from common import work_zksync as zksync
# from common import work_hytopia as hytopia
from common import work_general as general
from common import work_starknet as stark
from common import work_kroma as kroma
from common import work_scroll as scroll

waiting = False
while waiting:
    
    if time.localtime().tm_hour >= 9 and time.localtime().tm_min >=1:
        waiting = False
        break
    else:
        print('waiting...')
        time.sleep(20)

######## 작업용 변수들 ########
start=2
end=98
autorun = True
# iteration = [i for i in range(start,end+1)]
iteration = [2,38,40,44,45,47]
workname = 'general 12, polyhedra act 6'
##############################
delay = 1
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGY0NzdkMmEyMGI3YTA3NDMyOWY4NmQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGY0OWFhNmM4NzU0ZTdiOWNlZWRlNjEifQ.4lGit8tSoJtk-78jE4CliPx8U0EQkL4TCmMaT5DeLQY"
data = csv.get_csv_data('gmail_list.csv')
path = os.path.dirname(__file__)+"\\"+"result_main.txt"
f = open(path, "a+")
f.write(workname + '\n')

for index in iteration:
    i = index-1
    profile_no = (4 - len(str(data['profile_no'][i])))*'0' + str(data['profile_no'][i])
    profile_id = data['gologin_profile_id'][i]
    email = data['Google Account'][i]
    pw_old = data['PW(Init)'][i]
    pw_new = data['PW(Changed)'][i]
    recovery_email = data['Restore email'][i]
    meta_recovery = data['metamask_recovery'][i]
    meta_wallet = data['metamask_wallet'][i]
    

    print(i+1,"=",email,pw_old,pw_new,recovery_email,profile_id)
    if autorun:
        # gl,driver = profile.open(token,profile_id) # gologin 프로필 실행
        profile.run(profile_no)
    cmd.focus_window(profile_no)
    
    #################### 메인 작업 시작 ############################
    # meta.change_network('polygon')
    # polyhedra.action1()
    # galxe.setting_social_link()

    # step_start = 13
    # step_end = 16
    # zksync.subroutine(data,f,i,step_start,step_end)
    # cmd.wait(delay)

    # step_start = 5
    # step_end = 5
    # stark.subroutine(data,f,i,step_start,step_end)

    # step_start = 1
    # step_end = 1
    # kroma.subroutine(data,f,i,step_start,step_end)

    # step_start = 1
    # step_end = 5
    # scroll.subroutine(data,f,i,step_start,step_end)

    # # 231103 - 구글 새계정 로그인
    # step_start = 1
    # step_end = 1
    # acc_init.subroutine(data,f,i,step_start,step_end)
    
    # step_start = 3
    # step_end = 3
    # holograph.subroutine(data,f,i,step_start,step_end)
    
    meta.run()
    # 매일출첵
    # opBNB NFT 클레임
    step_start = 6
    step_end = 6
    polyhedra.subroutine(data,f,i,step_start,step_end)
    
    step_start = 13
    step_end = 13
    general.subroutine(data,f,i,step_start,step_end)

    # url = 'https://reiki.web3go.xyz/aiweb/home'
    # cmd.open_url(url)

    # meta.change_network('polygon')
    # url = 'https://app.holograph.xyz/'
    # cmd.open_url(url)


    # meta.run()
    
    # urls = []
    # urls.append('https://dropcoin.club/farming')
    # urls.append('https://bags.fm/$l___hm')
    # urls.append('https://viewer.tokenscript.org/')
    # urls.append('https://www.beoble.io/')
    # urls.append('https://www.premint.xyz/GrapeCoin/')
    # urls.append('https://www.premint.xyz/grapecoin2/')

    # # 스타크넷 퀴즈즈
    # arg.run()
    # urls = []
    # urls.append('https://starknet.quest/quest/1')
    # urls.append('https://starknet.quest/quest/9')
    # urls.append('https://starknet.quest/quest/13')
    # urls.append('https://starknet.quest/quest/14')
    # urls.append('https://starknet.quest/quest/15')

    # for url in urls:
    #     cmd.open_url(url)
    

    #################### 메인 작업 종료 ############################
    
    if autorun:
        profile.stop(profile_no)




##### twitter 사용하는 작업
    # check_unlock = twit.check_unlock()
    # if check_unlock:
    #     galxe.setting_social_link()
    #     galxe.action_polyhedra()
    # else:
    #     print('{} twitter blocked'.format(i+1))


### 폴리헤데라 작업
    # result = meta.change_network('polygon')
    # if result == '':
    #     polyhedra.open_url()
    #     polyhedra.connect_wallet()
    #     galxe.setting_social_link()
    #     galxe.action_polyhedra()

f.close()