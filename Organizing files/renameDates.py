#renameDates.py - Rename filenames with American date formats MM-DD-YYYY to the European date formats DD-MM-YYYY
import shutil, os, re

#creates a regex that can identify the American date format MM-DD-YYYY
DatePattern = re.compile(r"""
	^(.*?)
	((0|1)\d)-
	((0|1|2|3)\d)-
	((19|20)\d\d)
	(.*?)$
	""", re.VERBOSE)

#loops over file in directory
folder = raw_input('Enter the absolute path of the folder you want to search: ')
if os.path.isabs(folder):
	for amerFilename in os.listdir(folder):
		mo = DatePattern.search(amerFilename)
		if mo == None:
			continue
		else:
			beforePart = mo.group(1)
			dayPart = mo.group(4)
			monthPart = mo.group(2)
			yearPart = mo.group(6)
			afterPart = mo.group(8)
			eurFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
			amerFilename = os.path.join(folder, amerFilename)
			eurFilename = os.path.join(folder, eurFilename)
			print('Renaming {} to {}.'.format(amerFilename, eurFilename))
			shutil.move(amerFilename, eurFilename)	


