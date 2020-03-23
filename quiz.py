#!/usr/bin/python3

print("Welcome to Siraiya's Multiplication quiz ")
print("\n")
print("Today we will go over our multiples of 2 ")
print("\n")
print("RULES:")
print("\n")
rules = "•Only type the lowercase letter of your answer\n•You cannot enter anything else other than what is presented\n•If you get it wrong or enter the wrong answer,you will have to input it again."
print(rules)
print("\n")
print('Question one:')
print('--------------------')
print("What is 2 * 2")
print("a)4\nb)7\nc)5\nd)2")
answer = "a"
while True:
	try:
		player_answer = input(":")
	except ValueError:
		pass
	else:
		if player_answer == answer:
			break
	print("Please try again")
	
print("Well done")
print("\n")
print("Question Two:")
print('--------------------')
print("What is 2 * 8")
answer_2 = input("a)67\nb)7\nc)16\nd)17\n:")
if answer_2.lower() == 'c' or answer_2.lower == '16':
	print("You're on a roll ")
else:
	print('Please try again')

