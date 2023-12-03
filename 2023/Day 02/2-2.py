import re

#Import input from file as a list
#input = open("2023/Day 02/example.txt").readlines()
input = open("2023/Day 02/input.txt").readlines()

#Create framework for storing game information
class Game:
	def __init__(game, ID, redMin, greenMin, blueMin):
		pass
		game.ID = ID
		game.redMin = redMin
		game.greenMin = greenMin
		game.blueMin = blueMin
	def __str__(game):
		return f"{game.ID}({game.redMin}, {game.greenMin}, {game.blueMin})"

gameList = []

#Parse entire input
for i in range(0, len(input)):
	#Find all instances of red
	rered = re.findall(".{2} red", input[i])
	redMin = 0
	#Find highest instance of red
	for reddice in range(0, len(rered)):
		#Exception for double digit dice
		if rered[reddice][0] == " ":
			if int(rered[reddice][1]) > redMin:
				redMin = int(rered[reddice][1])
		elif int(rered[reddice][0:2]) > redMin:
			redMin = int(rered[reddice][0:2])
	#Find all instances of green
	regreen = re.findall(".{2} green", input[i])
	greenMin = 0
	#Find highest instance of green
	for greendice in range(0, len(regreen)):
		#Exception for double digit dice
		if regreen[greendice][0] == " ":
			if int(regreen[greendice][1]) > greenMin:
				greenMin = int(regreen[greendice][1])
		elif int(regreen[greendice][0:2]) > greenMin:
			greenMin = int(regreen[greendice][0:2])
	#Find all instances of blue
	reblue = re.findall(".{2} blue", input[i])
	blueMin = 0
	#Find highest instance of blue
	for bluedice in range(0, len(reblue)):
		#Exception for double digit dice
		if reblue[bluedice][0] == " ":
			if int(reblue[bluedice][1]) > blueMin:
				blueMin = int(reblue[bluedice][1])
		elif int(reblue[bluedice][0:2]) > blueMin:
			blueMin = int(reblue[bluedice][0:2])
	#Store data
	gameList.append(Game(int(i+1), redMin, greenMin, blueMin))

answer = 0
#Multiply dice
print(gameList[0])
for game in gameList:
	answer = answer + (game.redMin * game.greenMin * game.blueMin)
#Answer = 68638
print(answer)