import time
from sys import platform
from selenium import webdriver
from gologin import GoLogin
from gologin import getRandomPort
from selenium.webdriver.chrome.service import Service

import MetaMask as meta


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGY0NzdkMmEyMGI3YTA3NDMyOWY4NmQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGY0OWFhNmM4NzU0ZTdiOWNlZWRlNjEifQ.4lGit8tSoJtk-78jE4CliPx8U0EQkL4TCmMaT5DeLQY"
profile_id = "64f5e49a433b174552b97833"

gl = GoLogin({
	"token": token,
	"profile_id": profile_id
	})

chrome_driver_path = r"C:\Projects\NadoPython\Personal\hayden.park\CodeIt\New_PJT\chromedriver.exe"

debugger_address = gl.start()
service = Service(executable_path=chrome_driver_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://www.python.org")

meta.pin_to_extensions()



time.sleep(5)
driver.quit()
time.sleep(3)
gl.stop()