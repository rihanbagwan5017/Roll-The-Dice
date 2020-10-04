import random
import time
def game():
	chances=3
	human_score=0
	bot_score=0
	print("You have total 3 chances")
	print("Press yes or y to roll the dice:")
	a=str(input())
	while a=="yes" or a=="y" :
		print("Lets start the  game!")
		print("\tIf you got match then you are winner.")
		chances=chances-1
		print("Chance on going : ",chances+1)
		print("Dice is rolling....\n please wait..")
		time.sleep(1)
		dic1=random.randint(1,6)
		dic2=random.randint(1,6)
		print("Value of dice-1 is : ",dic1)
		print("Value of dice-2 is : ",dic2)
		if dic1==dic2:
			print("Your luck is awesome this time,you got match!")
			print("WINNER WINNER of this round.")
			human_score=human_score+1
			print("Your score is : ",human_score)
		elif dic1!=dic2:
				bot_score=bot_score+1
				print("Bot score is : ",bot_score)
				
		if chances<=0:
				print("Your chances are over .")
				print(f"Your total score : {human_score}.")
				print(f"bot total score : {bot_score}.")
				if human_score==bot_score:
					print("~Game tied~")
				elif human_score>bot_score:
					print("$¥~You won! :)¥$¢")
				else:
					print("\tBot won the match!\n Try Next time.")
				break

		else:
			print("Chances left  are : ",chances)
			user_1="Do you want to roll again?\n y/yes  for yes and no for No"
			print(user_1)
			user_1=str(input()).lower()
			if user_1=="no":
				break
game()
		
print("Game finished!")
print("~~~~~~~~~~~~~~~~~")
time.sleep(1)
def menu():
	print("Do you want to restart the Game?")
	print("Type r to restart or n for finish game.")
	v=str(input()).lower()
	if v=="r":
		game()
	elif v=="n":
		print("Game finished!")
		print("~~~~~~~~~~~~~~~~~~~")
	else:
			print("\t\tEnter correct key")
			menu()
menu()
game()