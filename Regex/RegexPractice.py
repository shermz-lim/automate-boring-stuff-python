import pyperclip, re

NumWithCommas = re.compile(r'''(
	\'
	(\d{1,3})
	(,\d{3})?
	(,\d{3})?
	(,\d{3})?
	\'
	)''', re.VERBOSE)



LastNameNakamoto = re.compile(r'''(
	\'
	([A-Z][a-zA-Z]*)
	(\s)
	(Nakamoto)
	\'
	)''', re.VERBOSE)	

SentenceRegex = re.compile(r'''(
	\'
	(Alice|Bob|Carol)
	\s
	(eats|pets|throws)
	\s
	(apples|cats|baseballs)
	\.\'
	)''', re.VERBOSE | re.IGNORECASE)

text = str(pyperclip.paste())
for groups in SentenceRegex.findall(text):
	print(groups[0])