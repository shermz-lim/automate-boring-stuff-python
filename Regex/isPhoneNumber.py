import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

def isPhoneNumber(text):
    match = phoneNumRegex.search(text)
    if match != None:
    	return True 

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(0, len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print ('The phone number found is: ' + chunk)