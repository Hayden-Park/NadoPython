import time
from sys import platform
from selenium import webdriver
from gologin import GoLogin
from gologin import getRandomPort
from selenium.webdriver.chrome.service import Service
import commands as cmd

chrome_driver_path = r"C:\Projects\NadoPython\Personal\hayden.park\CodeIt\New_PJT\chromedriver.exe"
delay = 1
root = __file__[__file__.rfind('\\')+1:__file__.rfind('.')]

def open(token,profile_id):
	gl = GoLogin({
		"token": token,
		"profile_id": profile_id
		})
	debugger_address = gl.start()
	service = Service(executable_path=chrome_driver_path)

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("debuggerAddress", debugger_address)
	driver = webdriver.Chrome(service=service, options=chrome_options)
	cmd.find_image(root,'chrome_setting_btn',delay*60,False)
	return gl,driver

def terminate(gl,driver):
	driver.quit()
	time.sleep(2)
	gl.stop()

def search_profile(profile_no):
	cmd.focus_window('Browser Profiles')
	cmd.init_click()
	cmd.scroll(6500)
	cmd.find_image(root,'search',delay*3,True)
	if not cmd.find_image(root,'search_profiles',delay,True):
		cmd.find_image_rate(root,'all_profiles',delay*3,True,5)
		cmd.find_image(root,'search',delay*3,True)
		cmd.find_image(root,'search_profiles',delay*3,True)
	cmd.typetext(profile_no)
	cmd.press_enter()

def run(profile_no):
	search_profile(profile_no)
	if cmd.find_image(root,'ready',delay*8,True):
		cmd.find_image(root,'run',delay*5,True)

def stop(profile_no):
	# search_profile(profile_no)
	cmd.focus_window('Browser Profiles')
	cmd.init_click()
	cmd.scroll(6500)
	cmd.find_image(root,'search',delay*3,False)
	if cmd.find_image(root,'running',delay*8,True):
		cmd.wait(delay)
		cmd.find_image(root,'stop',delay*5,True)
		cmd.find_image(root,'ready',delay*30,False)

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGY0NzdkMmEyMGI3YTA3NDMyOWY4NmQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGY0OWFhNmM4NzU0ZTdiOWNlZWRlNjEifQ.4lGit8tSoJtk-78jE4CliPx8U0EQkL4TCmMaT5DeLQY"
# profile_id = '64f5e49a433b174552b97833'




