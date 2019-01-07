#this program opens multiple tabs of the search results of the search term keyed into the command line 
import requests, sys, bs4, webbrowser

assert len(sys.argv) >= 2

search_phrase = sys.argv[1:]
search_phrase = '+'.join(search_phrase)

#searching term on google and opening page of search results 
google_search_url = 'https://www.google.com.sg/search?q={}'.format(search_phrase) 
webbrowser.open(google_search_url)

#creating response object of downloading search results page and BS4 object of search results page 
res = requests.get(google_search_url)
res.raise_for_status()
searchSoup = bs4.BeautifulSoup(res.text, features = 'html.parser')

searchResultsTag = searchSoup.select('.r a')
for i in range(min(5, len(searchResultsTag))):
	print(searchResultsTag[i].get('href'))
	webbrowser.open('http://google.com' + searchResultsTag[i].get('href'))
