import re
def isStrongPassword(password):
	if not len(password) >= 8:
		return False 
	if not TestUpperCase.search(password):
		return False 
	if not TestLowerCase.search(password):
		return False
	if not TestDigit.search(password):
		return False 
	return True 


TestUpperCase = re.compile(r'[A-Z]')

TestLowerCase = re.compile(r'[a-z]')

TestDigit = re.compile(r'[0-9]')

print(isStrongPassword('Sherman123'))