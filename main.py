
from selenium import webdriver
from user_config import USERNAME, PASSWORD
import time
import random

timeDelay = random.randrange(2, 6)


with open('all_followers.txt') as f:
    contents = f.read()
    users = contents.split()


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

browser.get("https://www.instagram.com/")

time.sleep(3)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)
time.sleep(2)
password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()
a = 0
time.sleep(5)
file = open("users.txt", "w")
for user in users:
    browser.get(f"https://www.instagram.com/{user}")

    if len(browser.find_elements_by_class_name("yLUwa")) > 0:
        link = browser.find_element_by_class_name("yLUwa")
        follow = browser.find_elements_by_class_name("g47SY")
        file.write(user + " " + (link.text) + " " + (follow[1].text) + "\n")
        a = a+1
        time.sleep(timeDelay)
    else:
        print("asdadas")
        time.sleep(timeDelay)

file.close()

