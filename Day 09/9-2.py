from skimage.morphology import flood
import numpy

#Import input from file as a list
source = open('input.txt').readlines()

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

basin_sizes = []
#Selects the first integer of each low point coordinate pair
for low_point in range(0, len(low_points), 2):
	#Sets the lowpoint to 0, to allow for flood filling
	heightmap[low_points[low_point]][low_points[low_point + 1]] = 0
	#Calculates size of basin and adds it to the list
	basin_sizes.append(numpy.sum((flood(heightmap, (low_points[low_point], low_points[low_point + 1]), connectivity=1, tolerance=8))))

#Sort the sizes
basin_sizes.sort()

#Result = 89, 90, 92 // 736920
print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])