#this function deletes all files in the folder above the file size (in bytes)

import os, shutil, send2trash

def delFiles(folder, size):
	folder = os.path.abspath(folder)
	if os.path.exists(folder):
		print('Looking into {} for files greater than {} bytes'.format(folder, size))
		for filename in os.listdir(folder):
			file = os.path.join(folder, filename)
			if os.path.isfile(file):
				if os.path.getsize(file) > size:
					print('The file {} in the folder is greater than {} bytes.'.format(filename, size))
					print('Deleting {} from folder...'.format(filename))
					#send2trash.send2trash(file)

delFiles('C:\Users\sherm\OneDrive\Desktop\Tuition', 15*1000)