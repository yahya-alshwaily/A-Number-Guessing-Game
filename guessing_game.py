import random

print("-"*len("Welcome to the Number Guessing Game!") ,"\nWelcome to the Number Guessing Game! \n"+"-"*len("Welcome to the Number Guessing Game!"))

def start_game(num_tries):
	
	secret = random.randint(1,10)
	print(secret) #test
	number_pick = 0 
	
	while secret != number_pick: 
		try:
			number_pick = int(input("Pick a number between 1 and 10: "))
		except ValueError:
			print("Oops! your entry is not valid, please pick a number between 1 and 10")
		if number_pick < 1 or number_pick > 10:
			print("Oops! Your number is out of the range of this game, please pick a number between 1 and 10")
		elif number_pick < secret: 
			print("It is higher!")
			num_tries +=1
		elif number_pick > secret:
			print("It is lower!")
			num_tries +=1
		else:
			print(f"You got it!, it took you {num_tries} tries")
	return num_tries 

retry = 'yes' 
high_score = 10000 
while retry.lower()=='yes': 
	check_score = start_game(1)
	retry = input("Would you like to play again? [yes/no]\n") 
	if check_score<high_score and retry == 'yes': 
		high_score = check_score
		print (f"the Highscore is {high_score}")
	if check_score>high_score: 
		print (f"the Highscore is {high_score}")

print("Good Bye!, thank you for playing")