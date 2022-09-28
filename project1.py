#importing webdriver class from selenium library
from selenium import webdriver
#importing time for the maintainence of delay Between the operations/tasks
import time
#connection with chrome browser via webdriver class
browser=webdriver.Chrome("C:/Users/Prashanth K/anaconda3/chromedriver.exe")
#maximising the screen for good display
browser.maximize_window()
#opening the hackveda one2one website with the help of get function/method
browser.get("https://www.hackveda.in/one2one")
#time delay of 3 seconds
time.sleep(3)
#giving the emailaddress with the help of find_element_by_id and send keys functions or methods
username=browser.find_element_by_id("email")
username.send_keys("kadudulaprashanth3@gmail.com")
time.sleep(3)
#giving the password with the help of find_element_by_id and send keys functions or method
password=browser.find_element_by_id("password")
password.send_keys("Pasi9392@")
time.sleep(3)
# enabling the signin button via click function or method
signinbutton=browser.find_element_by_id("login_btn")
signinbutton.click()
