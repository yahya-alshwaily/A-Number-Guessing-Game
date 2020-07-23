import random

print("------------------------------------ \nWelcome to the Number Guessing Game! \n------------------------------------")

def start_game(num_tries):
	
	secret = random.randint(1,10) # code adapted from https://www.tutorialspoint.com/generating-random-number-list-in-python
	#print(secret) was used here for testing
	number_pick = 0 
	
	while secret != number_pick: 
		
		try: 
			number_pick = int(input("\nPick a number between 1 and 10: "))
		except ValueError:
			print("\nOops! your entry is not valid, please pick a number between 1 and 10")
			continue 
			
		if number_pick < 1: 
			print("\nOops! Your number is out of the range of this game, please pick a number between 1 and 10")
			continue
		elif number_pick > 10:
			print("\nOops! Your number is out of the range of this game, please pick a number between 1 and 10")
			continue
				
		elif number_pick < secret: 
			print("\nIt is higher!")
			num_tries +=1
			continue
				
		elif number_pick > secret:
			print("\nIt is lower!")
			num_tries +=1
			continue
			
		elif number_pick == secret:
				
			print(f"\nYou got it!, it took you {num_tries} tries")
			break
				
	return num_tries 

retry = 'yes' 

high_score = 10000 

while retry.lower()=='yes':
	
	check_score = start_game(1)  
	
	retry = input("\nWould you like to play again? [yes/no]\n")
	
	while retry.lower() != 'yes' and retry.lower() != 'no':
		retry = input("\nWould you like to play again? [yes/no]\n")
	
	if check_score<high_score: 

		high_score = check_score
		print (f"\nthe Highscore is {high_score}")
		
	
	while check_score>high_score: 
		print (f"\nthe Highscore is {high_score}")
		break 

print("\nGood Bye!, thank you for playing") 
