from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

email = input()
password = input()

usernameElem = browser.find_element_by_name('username')
usernameElem.send_keys(email)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(password)
passwordElem.send_keys(Keys.ENTER)
