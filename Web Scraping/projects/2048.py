from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')
while True:
	try:
		tryElem = browser.find_element_by_link_text('Try again')
		tryElem.click()
	except NoSuchElementException:	
		htmlElem.send_keys(Keys.UP)
		htmlElem.send_keys(Keys.RIGHT)
		htmlElem.send_keys(Keys.DOWN)
		htmlElem.send_keys(Keys.LEFT)


