#This program find phone and email addresses from texts on a clipboard and pastes it on the clipboard

import pyperclip, re 


phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?  	
	(\s|-|\.)?				
	(\d{3})					
	(\s|-|\.)			    	
	(\d{4})					  
	(\s*(ext|x|ext.)\s*(\d{2,5}))?   
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._+%-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

#find matches in clipboard text. pyperclip.paste() get a string value of text on the clipboard  
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
	
for groups in emailRegex.findall(text):		
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard: ')
	print('\n'.join(matches))
else:
	print('No phone number or email addresses found in the text!')
