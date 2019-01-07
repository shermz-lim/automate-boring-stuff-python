#!python
#this programs searches for files with a particular extension (e.g. .jpg, .pdf) and copies them into a new folder

import os, shutil 

def searchFolder(search_folder, extension):
	destination_folder = raw_input('Enter the absolute path of the new folder: ')
	os.mkdir(destination_folder)
	#making sure the folders are in the absolute path
	search_folder = os.path.abspath(search_folder)
	destination_folder = os.path.abspath(destination_folder)
	#make sure that extension is valid 
	valid_extensions = ['.jpg', '.txt', '.pdf', '.docx']
	if not extension in valid_extensions:
		print('Type in a valid extension as the second argument')
		return 
	for folderName, subFolders, filenames in os.walk(search_folder):
		print('Searching for files in {}'.format(folderName))
		for filename in filenames:
			if filename.endswith(extension):
				print('Copying file {} to folder {}'.format(os.path.join(folderName, filename), destination_folder))
				shutil.copy(os.path.join(folderName, filename), destination_folder)	

searchFolder('C:\Users\sherm\OneDrive\Desktop\Documents (self)', '.jpg')

