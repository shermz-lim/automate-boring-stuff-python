#python2
#saves and loads pieces of text onto the clipboard 
#Usage: python mcb.pyw save <keyword> : saves clipboard to keyword
#		python mcb.pyw <keyword> : input text saved on keyword to clipboarb
#		python mcb.pyw list : input list of keywords onto clipboard 	

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#saves clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]]	
#loads text saved on keyword or loads list of keywords
elif len(sys.argv) == 2: 	
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	elif sys.argv[1].lower() == 'delete':
		for keys in mcbShelf.keys():
			del mcbShelf[keys]	 

mcbShelf.close()		

