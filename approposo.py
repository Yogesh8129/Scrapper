import sys

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login():
        user_name = "aashi@desertsundesigns.com"
        user_pw = "hTm[aCoWYwKL!1"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("https://app.roposoclout.com/staff-login")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email-input')))
        user_name_ip = browser.find_element(By.ID, 'email-input')
        user_name_ip.clear()
        user_name_ip.send_keys(user_name)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'login-page-get-otp-button')))
        submit = browser.find_element('id','login-page-get-otp-button')
        submit.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'password-input')))
        pw_ip = browser.find_element('id','password-input')
        pw_ip.clear()
        pw_ip.send_keys(user_pw)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'login-page-proceed-button')))
        submit = browser.find_element('id','login-page-proceed-button')
        submit.click()
        # browser.switch_to.window(browser.window_handles[0])


#region browser_setup
chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=3")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#endregion

#region main code
login_page = 'https://app.roposoclout.com/staff-login'
browser = webdriver.Chrome()
browser.get(login_page)
time.sleep(1)
current_url = browser.current_url
print(browser.current_url)

def main_code():
    print("Successful")


while current_url == login_page:
	login()
	browser.implicitly_wait(1)
	new_current_url = browser.current_url
	while new_current_url == "https://app.roposoclout.com/":
		print("Login Successful")
		main_code()
		sys.exit("Successful")
#endregion