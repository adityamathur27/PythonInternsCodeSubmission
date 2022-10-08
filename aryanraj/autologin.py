from selenium import webdriver
import time

browser=webdriver.Chrome(executable_path="/Users/holeshsharma/Desktop/web/hackveda_project/drive/chromedriver")

browser.get("https://www.hackveda.in/one2one")
time.sleep(3)

username=browser.find_element_by_id("email")
username.send_keys("holes@gmail.com")
time.sleep(3)

password=browser.find_element_by_id("password")
password.send_keys("1935**04")
time.sleep(3)

btn=browser.find_element_by_id("login_btn")
btn.click()