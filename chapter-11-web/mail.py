#this program allows you to send a string to an email address via gmail on the command line
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time 
import sys 
import re 

#getting email address and string from command line
#2nd argument - email address
#3rd argument and beyond: string to send to above email address
assert len(sys.argv) >= 3

#create email address Regex
emailRegex = re.compile(r'''
	(.)+
	\@
	(\w)+
	\.
	(com|sg)
	''', re.VERBOSE)
email = sys.argv[1]
emailMatch = emailRegex.search(email)
if emailMatch:
	email = emailMatch.group(0)
else:
	raise Exception('2ndArgumentNotEmailError')

message = ' '.join(sys.argv[2:])
print("Sending message '{}' to email address: {}".format(message, email))		

my_email = input("What is your email? ")
my_password = input("What is your password? ")

#Opening gmail
print('Opening gmail...')
browser = webdriver.Chrome()
browser.get('https://mail.google.com/mail/u/0/#inbox')

#Keying in username and click next
print('Keying in username...')
usernameElem = browser.find_element_by_tag_name('input')
usernameElem.send_keys(my_email)
usernameElem.send_keys(Keys.ENTER)
time.sleep(1.5) #loading
#Keying in password and click next
print('Keying in password...')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(my_password)
passwordElem.send_keys(Keys.ENTER)
time.sleep(3.0)
#clicking on compose button
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(3.0)
#Entering email
recipientElem = browser.find_element_by_xpath("//textarea[@aria-label='To']")	
recipientElem.send_keys(email)
time.sleep(2.0)	
#Entering subject
browser.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Hi!")

messageElem = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
messageElem.send_keys(message) 
time.sleep(1.0)
#//*[@id=":py"]

ActionChains(browser) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .key_up(Keys.ENTER) \
    .key_up(Keys.CONTROL) \
    .perform()
