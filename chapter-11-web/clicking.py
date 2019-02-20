from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

email = input()
password = input()

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')



usernameElem = browser.find_element_by_name('username')
usernameElem.send_keys(email)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(password)
passwordElem.send_keys(Keys.ENTER)
