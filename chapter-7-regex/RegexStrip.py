import re

def RegexStrip(string, rm_string = None):
	if rm_string == None:
		return string.strip()
	else:
		string = string.strip()
		string_regex = re.compile(rm_string)
		new_string = string_regex.sub('', string)
		return new_string


string = input('Enter a string: ')
rm_str = input('Enter the str you want to remove from the string or just click enter: (Optional)')
string = RegexStrip(string, rm_str)
print (string)