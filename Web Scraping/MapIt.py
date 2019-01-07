#this program opens up the address on either the command line/clipboard
#if there's an address in the command line, it will be used. 
#else, the address on the clipboard will be used. 
#google maps will be opened to show the address

import sys, webbrowser, pyperclip 

if len(sys.argv) == 1:
	address = pyperclip.paste()
	address = address.split(' ')
else:
	address = sys.argv[1:]	

address = '+'.join(address)
url = 'https://www.google.com/maps/place/{}/'.format(address)
webbrowser.open(url)		

