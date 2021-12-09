#Import input from file as a list
source = open('example_input.txt').readlines()

#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

heightmap = []

#Split into individual numbers
for i in range(len(source)):
	heightmap.append(list(source[i]))

#Convert to integers
heightmap = [[int(x) for x in row] for row in heightmap]

low_points = []

#Find low points
for row in range(len(heightmap)):
	for value in range(len(heightmap[row])):
		low = True
		position = heightmap[row][value]
		#Vertical Checks
		#Check below only for first row
		if row == 0:
			if position >= heightmap[row + 1][value]:
				low = False
		#Check above only for last row
		elif row == len(heightmap) - 1:
			if position >= heightmap[row - 1][value]:
				low = False
		#Else check above and below
		else:
			if position >= heightmap[row - 1][value] or position >= heightmap[row + 1][value]:
				low = False
		#Horizontal Checks
		#Check right only for first element
		if value == 0:
			if position >= heightmap[row][value + 1]:
				low = False
		#Check left only for last element
		elif value == len(heightmap[row]) - 1:
			if position >= heightmap[row][value - 1]:
				low = False
		#Else check both sides
		else:
			if position >= heightmap[row][value - 1] or position >= heightmap[row][value + 1]:
				low = False
		#Check if it is a low point
		if low == True:
			low_points.append(row)
			low_points.append(value)
#low_points is now a list of integers that form the coordinates of all the low points

for low_point in range(0, len(low_points), 2):
	

#Check a cell, if there is no 9, check that cell, keep going until you have no cells to check
