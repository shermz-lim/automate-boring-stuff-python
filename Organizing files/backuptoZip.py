#!python
#backuptoZip.py - copies an entire folder and its files to a zip file whoes file name increments 

import zipfile, os 

def backuptoZip(folder):
	#back up the entire contents of zipfile into a folder 
	if not os.path.exists(folder):		#checks whether folder exists
		print('Folder does not exist.')
		return 
	
	folder = os.path.abspath(folder)	#ensures that the folder path is absolute 

	file_number = 1
	while True:
		zipfileName = os.path.basename(folder) + str(file_number) + '.zip'

		if not os.path.exists(zipfileName):
			break 
		file_number = file_number + 1 
	
	print(zipfileName)
	#create the zip file 
	print('Creating {}...'.format(zipfileName))
	backupZip = zipfile.ZipFile(zipfileName, 'w')

	#walk the entire folder tree and compress the files in each folder 
	for folderName, subfolders, filenames in os.walk(folder):
		print('Adding files in {}...'.format(folderName))
		backupZip.write(folderName)
		for filename in filenames:
			if filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(folderName, filename), compress_type = zipfile.ZIP_DEFLATED)
	backupZip.close()
	print('Done')
	

backuptoZip('C:\Users\sherm\OneDrive\Desktop\Documents (self)')