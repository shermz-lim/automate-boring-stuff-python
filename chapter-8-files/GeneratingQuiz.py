#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

import random

   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

capitalsKeys = capitals.keys()

for quizNum in range(1,36):
	quizFile = open('capitalQuiz{}.txt'.format(quizNum), 'w')
 	quizFile.write('Name:\nClass:\nPeriod:\n')
 	quizFile.write((' ' * 20) + 'State Capital Quiz (Form: {})'.format(quizNum))
 	quizFile.write('\n\n')
 	quizFile.close()
 	answerFile = open('capitalQuizAnswer{}.txt'.format(quizNum), 'w')
 	answerFile.write('Answer key for the quiz: \n \n')
 	answerFile.close()
 	quizFile = open('capitalQuiz{}.txt'.format(quizNum), 'a')
 	answerFile = open('capitalQuizAnswer{}.txt'.format(quizNum), 'a')
 	random.shuffle(capitalsKeys)
 	for i in range(len(capitalsKeys)):
 		quizFile.write('Question {}: \nThe capital of {} is: \n'.format(i + 1, capitalsKeys[i]))
 		answerFile.write('The answer for question {} is: \n{} \n \n'.format(i + 1, capitals[capitalsKeys[i]]))
 		answerLstIndex = [i]
 		while len(answerLstIndex) < 4:
 			index = random.randint(0, 49)
 			if not index in answerLstIndex:
 				answerLstIndex.append(index)
 		random.shuffle(answerLstIndex)
 		for index in answerLstIndex:
 			quizFile.write('{}: {}\n'.format('ABCD'[index], capitals[capitalsKeys[index]]))
 		quizFile.write('\n')	
 	quizFile.close()
 	answerFile.close()		



