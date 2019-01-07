import random 

def getGuess():
	guess = ''
	while guess not in ('heads', 'tails'):
		guess = raw_input('Guess heads or tails: ')
	if guess == 'heads':
		guess = 1
	else:
		guess = 0
	return guess 			

def playHeadsOrTails():
	guess = getGuess()
	toss = random.randint(0, 1) #0 for tails, 1 for heads
	while toss != guess:
		print('You lost! Guess again!')
		guess = getGuess()
	print('Congratulations. You won!')
	
playHeadsOrTails()		

