from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

usernameElem = browser.find_element_by_name('username')
usernameElem.send_keys('sherman1237@gmail.com')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('654561112672')
passwordElem.send_keys(Keys.ENTER)