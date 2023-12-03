import re

#Import input from file as a list
#input = open("2023/Day 02/example.txt").readlines()
input = open("2023/Day 02/input.txt").readlines()

#Create framework for storing game information
class Game:
	def __init__(game, ID, redMax, greenMax, blueMax):
		pass
		game.ID = ID
		game.redMax = redMax
		game.greenMax = greenMax
		game.blueMax = blueMax
	def __str__(game):
		return f"{game.ID}({game.redMax}, {game.greenMax}, {game.blueMax})"

gameList = []

#Parse entire input
for i in range(0, len(input)):
	#Find all instances of red
	rered = re.findall(".{2} red", input[i])
	redMax = 0
	#Find highest instance of red
	for reddice in range(0, len(rered)):
		#Exception for double digit dice
		if rered[reddice][0] == " ":
			if int(rered[reddice][1]) > redMax:
				redMax = int(rered[reddice][1])
		elif int(rered[reddice][0:2]) > redMax:
			redMax = int(rered[reddice][0:2])
	#Find all instances of green
	regreen = re.findall(".{2} green", input[i])
	greenMax = 0
	#Find highest instance of green
	for greendice in range(0, len(regreen)):
		#Exception for double digit dice
		if regreen[greendice][0] == " ":
			if int(regreen[greendice][1]) > greenMax:
				greenMax = int(regreen[greendice][1])
		elif int(regreen[greendice][0:2]) > greenMax:
			greenMax = int(regreen[greendice][0:2])
	#Find all instances of blue
	reblue = re.findall(".{2} blue", input[i])
	blueMax = 0
	#Find highest instance of blue
	for bluedice in range(0, len(reblue)):
		#Exception for double digit dice
		if reblue[bluedice][0] == " ":
			if int(reblue[bluedice][1]) > blueMax:
				blueMax = int(reblue[bluedice][1])
		elif int(reblue[bluedice][0:2]) > blueMax:
			blueMax = int(reblue[bluedice][0:2])
	#Store data
	gameList.append(Game(int(i+1), redMax, greenMax, blueMax))

condition = [12, 13, 14]
answer = 0

#Check each game against the condition
for game in gameList:
	print(game)
	if game.redMax <= condition[0]:
		if game.greenMax <= condition[1]:
			if game.blueMax <= condition[2]:
				answer = answer + game.ID

#Answer = 2776
print(answer)