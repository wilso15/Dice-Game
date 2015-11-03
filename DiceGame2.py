import random
import os
import sys
print("Russian Dice Roulette")
print("""Rules: The person to last drink vodka, is Player Two and rolls second. Round 1: First roller rolls the 6 sided 
die, then the 4 sided die. If you roll a 1, you lose. Then Player Two rolls the 6 sided die, and 4 sided die, and 
rotate turns with Player One.  Round 2: Both players still alternating turns. If you roll a 1 or a 2, you lose. 
Round 3: Rolling a 1,2, or 3 loses.  Round 4: You now only roll the 6 sided die, rolling a 1,2,3, or 4 loses. 
Round 5: Rolling a 1,2,3,4, or 5 loses.  If you roll a 6, Player One wins.""")

print("ROUND 1: 1's LOSE")

player1 = input("So, who will begin? Name: ")
player2 = input("Great, and who will go second? Name: ")

print("Press enter to roll")

#def quit(stop):
	#if "q" == stop:
		#sys.exit(0)
	#elif "Q" == stop:
		#sys.exit(0)

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0} your turn with 6 sided die".format(player2))
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player2))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player2))
		break

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player1))
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player1))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player1))
		break
		
	print("ROUND 2: 1's & 2's LOSE")
		
while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player2))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player2))
		break

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player1))
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player1))
		break
		
	print("ROUND 3: 1's,2's, & 3's LOSE")
		
while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player1))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with 6 sided die".format(player2))
		break

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, 4 sided die roll next".format(player2))
		break

while True:
	input()
	number = random.randint(1,4)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, your turn with only 6 sided die".format(player1))
		break
		
	print("ROUND 4: 1's,2's,3's, and 4's LOSE. No Longer Use 4 Sided Die")

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, your turn with only 6 sided die".format(player2))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, your turn with only 6 sided die".format(player2))
		break
		
while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player2))
		quit()
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, your turn with only 6 sided die".format(player1))
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, your turn with only 6 sided die".format(player1))
		break

	print("ROUND 5: 1's,2's,3's,4's, and 5's LOSE. Roll a 6, and {0} WINS")

while True:
	input()
	number = random.randint(1,6)
	if number == 1:
		print("[-----]")
		print("[  1  ]")
		print("[-----]")
		print("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 2:
		print("[-----]")
		print("[  2  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 3:
		print("[-----]")
		print("[  3  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 4:
		print("[-----]")
		print("[  4  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 5:
		print("[-----]")
		print("[  5  ]")
		print("[-----]")
		print ("{0}, YOU LOSE! Weak Sauce, Bro/Broette.".format(player1))
		quit()
		break
	if number == 6:
		print("[-----]")
		print("[  6  ]")
		print("[-----]")
		print ("{0}, YOU WIN! You are very, very lucky.".format(player1))
		break


