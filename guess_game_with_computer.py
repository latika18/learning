#make a guess against the computer guessed number
#! /usr/bin/python
import random
#GET GUESS
def get_guess():
	guess = list(str(input("What is your guess?")))
	return guess

#Generate Code
def generate_code():
	code = []
	for i in range(3):
		code.append(str(random.randint(1,9)))
	return code


#Generate Clue
def generate_clue(user_guess,code):
	if user_guess == code:
		return "Code Cracked!"
	clues = []

	for i,num in enumerate(user_guess):
		if num==code[i]:
			clues.append("match")
		elif num in code:
			clues.append("close")
	
	if clues==[]:
		return ["Nope"]
	else:
		return clues




#final logic

secret_code = generate_code()
clue_report = []

while clue_report!= "Code Cracked!":
	guess = get_guess()
	print(guess,secret_code)
	clue_report = generate_clue(guess,secret_code)
	print("Here is the result of your guess:")
	for clue in clue_report:
		print(clue)
