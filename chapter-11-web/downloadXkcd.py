import bs4, requests, os

url = 'https://xkcd.com'
while not url.endswith('#'):
	print('Downloading page: {}'.format(url))
	res = requests.get(url)
	res.raise_for_status()
	pageSoup = bs4.BeautifulSoup(res.text, features = 'html.parser')
	comicTag = pageSoup.select('#comic img')
	if comicTag == []:
		print('Could not find the comic image.')
	else:	
		try:
			comicUrl = comicTag[0].get('src')
			comicUrl = 'http:' + comicUrl
			print('Downloading image {}'.format(comicUrl))
			comicRes = requests.get(comicUrl)
			comicRes.raise_for_status()
		except requests.exceptions.MissingSchema:
			prevLink = pageSoup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prevLink.get('href')
			continue 	
	imageFile = open(os.path.join('.\\comicXkcd', os.path.basename(comicUrl)), 'wb')
	for chunk in comicRes.iter_content(100000):
		imageFile.write(chunk)
	prevLink = pageSoup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')	

		
