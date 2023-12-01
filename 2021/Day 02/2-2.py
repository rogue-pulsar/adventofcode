#Import input from file as a list
course = open("input.txt").readlines()

#Remove linebreaks from list
for i in range(len(course)):
	course[i] = course[i].rstrip()

#Set starting position
depth = 0
horizontal = 0
aim = 0

#Loop through checking for first character and adding/subtracting the appropriate amount
for i in range(len(course)):
	if course[i][0] == "f":
		horizontal = horizontal + int(course[i][-1])
		depth = depth + (aim * int(course[i][-1]))
	elif course[i][0] == "d":
		aim = aim + int(course[i][-1])
	else:
		aim = aim - int(course[i][-1])

#Calcuate solution
answer = depth * horizontal

#Result = 1813664422
print(answer)