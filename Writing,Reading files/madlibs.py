import re
import os  

file_name = raw_input('Enter the name of the file you wish to open: ')
file = open('{}\\{}.txt'.format(os.getcwd(), file_name))
text = file.read()

madlib_regex = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)', re.IGNORECASE)
matches = madlib_regex.findall(text)
if matches:
	for match in matches:
		replacement = str(raw_input('Enter a {}: '.format(match)))
		text = text.replace(match, replacement, 1)

print(text)		