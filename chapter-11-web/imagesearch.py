#this program takes in search argument for the command line and downloads either all/5 of the images searched on google image, whichever is lesser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys, time, requests, os, bs4

os.chdir('C:\\Users\\sherm\\OneDrive\\Desktop\our-adventure')
#Obtaining search argument from command line
assert len(sys.argv) >= 2
search_object = ' '.join(sys.argv[1:])
try:
	os.mkdir('.\\{}-images'.format(search_object))
except WindowsError:
	print('Folder for the search image already exists.')

#Opening google image browser and searching for search argument
browser = webdriver.Chrome()
print('Opening google images...')
browser.get('https://images.google.com/')
searchElem = browser.find_element_by_xpath("//input[@aria-label='Search']")
searchElem.send_keys(search_object)
searchElem.send_keys(Keys.ENTER)
print('Searching for {}...'.format(search_object))
time.sleep(1.5)

#Arrive at search results page
searchURL = browser.current_url
print('At {}'.format(searchURL))

#Downloading search results page using requests module
print('Downloading search results page {}'.format(searchURL))
res = requests.get(searchURL)
res.raise_for_status()

#Converting search results page to bs4 for identification of results image elements
resultsSoup = bs4.BeautifulSoup(res.text, features = 'html.parser')
searchResultsTags = resultsSoup.select("img[alt='Image result for {}']".format(search_object))
#Determining number of search results image to download
numberofImgs = min(len(searchResultsTags), 10)
print('Downloading {} search results images...'.format(numberofImgs))

#Downloading image from each image element's source
for index in range(numberofImgs):
	imgURL = searchResultsTags[index].get('src')
	print('Downloading image result for {}'.format(imgURL))
	res = requests.get(imgURL)
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem: {}'.format(exc))
		print('Image cannot be downloaded. Moving on the next image...')
		continue
	print('Saving download to file...')
	imgFile = open('.\\{}-images\\img{}.jpg'.format(search_object, index), 'wb')
	for chunk in res.iter_content(100000):
		imgFile.write(chunk)
	imgFile.close()
	print('Download successful!')
print('Done!')
