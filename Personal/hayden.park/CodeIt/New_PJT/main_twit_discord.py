import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__))+'\\common')
import time
from common import gologin_profile as profile
from common import csv_handling as csv
from common import commands as cmd
from common import win_control as win

####### 실행할 작업파일
from common import twitter as twit
from common import discord as dico

######## 작업용 변수들 ########
start=2
end=15
iteration = [i for i in range(start,end+1)]
# iteration = [1,2,3,4,5,6,7,8,61,62,63,64,65]
workname = 'add friend twit, discord'
##############################
delay = 1
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGY0NzdkMmEyMGI3YTA3NDMyOWY4NmQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGY0OWFhNmM4NzU0ZTdiOWNlZWRlNjEifQ.4lGit8tSoJtk-78jE4CliPx8U0EQkL4TCmMaT5DeLQY"
data = csv.get_csv_data('gmail_list.csv')
path = os.path.dirname(__file__)+"\\"+"result_main_twit.txt"
f = open(path, "a+")
f.write(workname + '\n')

# 231002 트윗 디코 친구추가 작업

id_start = 12
id_end = 69
# id_twit = list(data['ID_twit'][id_start-1:ex_start-1]) + list(data['ID_twit'][ex_end:id_end])
# id_discord = list(data['ID_discord'][id_start-1:ex_start-1]) + list(data['ID_discord'][ex_end:id_end])
id_twit = data['ID_twit'][id_start-1:id_end]
id_discord = data['ID_discord'][id_start-1:id_end]

for n in range(id_start-1,id_end): # 트윗, 디스코드 친구목록 갯수
    for index in iteration: # 실행중인 프로필 갯수
        i = index-1
        print(time.strftime('%H:%M:%S'))
        print("Profile: {0} / twit:{1}-{2} / discord:{3}-{4}".format(i+1,n+1,id_twit[n],n+1,id_discord[n]))
        # if n!=i:
        if n!=i and type(id_twit[n]) == str: # 올바른 아이디만 실행
            profile_no = (4 - len(str(data['profile_no'][i])))*'0' + str(data['profile_no'][i])
            cmd.focus_window(profile_no)
            cmd.wait(delay*1)
            cmd.hotkey('ctrl','2') # 트위터를 두번째 창에 켜놓을 것
            if twit.add_friend(id_twit[n]):
                # 계정간 interval 시간을 랜덤으로 조절
                var = cmd.get_random(40,60,2)
                print('twit wait {0} secs...'.format(var))
                cmd.wait(delay*float(var))
            else:
                print('{0} already following'.format(id_twit[n]))
            # if type(id_discord[n]) == str: # 올바른 아이디만 실행
            #     cmd.hotkey('ctrl','3') # 디스코드를 세번째 창에 켜놓을 것
            #     if dico.add_friend(id_discord[n]):
            #         # 계정간 interval 시간을 랜덤으로 조절
            #         var = cmd.get_random(60,65,2)
            #         print('discord wait {0} secs...'.format(var))
            #         cmd.wait(delay*float(var))
            #     else:
            #         print('{0} already friend'.format(id_discord[n]))
                

# ## 신청들어온 친구신청 수락하기
# for j in range(start-1,end):
#     profile_no = (4 - len(str(data['profile_no'][i])))*'0' + str(data['profile_no'][i])
#     hwnd = win.wait_for_window_hwnd(profile_no)
#     win.focus_window_hwnd(hwnd)
#     cmd.screen_left()
#     cmd.wait(delay*2)
#     cmd.hotkey('ctrl','2') # 트위터를 두번째 창에 켜놓을 것
#     twit.accept_friend(interval=30)
#     cmd.hotkey('ctrl','3') # 디스코드를 세번째 창에 켜놓을 것
#     dico.accept_friend(interval=30)


f.close()