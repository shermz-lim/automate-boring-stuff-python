#searches all text files in a folder for user supplied regex
import os
import re 
#getting folder to be searched from user 
folder = None
while folder == None:
	folder = str(raw_input('Enter the absolute path of the folder you want to search: '))
	if not os.path.isdir(folder):
		folder = None
#getting user supplied regex 

UserRegexString = str(raw_input('Enter the expression you want to search in the text: '))
UserRegex = re.compile(UserRegexString, re.IGNORECASE)

#open all text files in a folder and puts matches into a list
totalMatches = []
filesList = os.listdir(folder)
for file in filesList:
	if file[-4:] == '.txt':
		searchfile = open('{}\\{}'.format(folder, file), 'r')
		text = searchfile.read()
		matches = UserRegex.findall(text)
		for match in matches:
			totalMatches.append(match)
		searchfile.close()	

print(totalMatches)
