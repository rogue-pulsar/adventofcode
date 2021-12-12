import numpy as np

#Load input as a numpy matrix of numpy integers
with open('input.txt','rt') as infile:
	dumbo_grid =  np.matrix([list(line.strip()) for line in infile.readlines()], dtype = np.int64)

#Array of falses to track flashes
flash_grid = np.zeros((10, 10), dtype = bool)
#Convert numpy arrays to python lists
dumbo_grid = dumbo_grid.tolist()
flash_grid = flash_grid.tolist()

def increment_neighbors(row, dumbo):
	for i in range(max(row-1, 0), min(row+2, 10)):
		for j in range(max(dumbo-1, 0), min(dumbo+2, 10)):
			if flash_grid[i][j] == False:
				dumbo_grid[i][j] += 1

def search_neighbors(row, dumbo):
	for i in range(max(row-1, 0), min(row+2, 10)):
		for j in range(max(dumbo-1, 0), min(dumbo+2, 10)):
			if dumbo_grid[i][j] > 9 and flash_grid[i][j] == False:
				if flash_grid[i][j] == False:
					dumbo_grid[i][j] += 1

def no_unflashed_dumbos():
	for row in range(len(dumbo_grid)):
		for char in range(len(dumbo_grid[row])):
			if dumbo_grid[row][char] > 9:
				if flash_grid[row][char] == False:
					return False
	return True

flash_count = 0
steps = 0

while steps < 300:
	#Increment all by 1
	for row in range(len(dumbo_grid)):
		for dumbo in range(len(dumbo_grid[row])):
			dumbo_grid[row][dumbo] = dumbo_grid[row][dumbo] + 1
	#Main logic
	while no_unflashed_dumbos() == False:
		#Number by number
		for row in range(len(dumbo_grid)):
			for dumbo in range(len(dumbo_grid[row])):
				#If number is more than 9  and it hasn't already been accounted for
				if dumbo_grid[row][dumbo] > 9 and flash_grid[row][dumbo] == False:
						#Set flash to true
						flash_grid[row][dumbo] = True
						#Increment neighbors by 1
						increment_neighbors(row, dumbo)
						#Search neighbors for over 9 and not flashed
						search_neighbors(row, dumbo)
	#Reset flashes
	for row in range(len(dumbo_grid)):
		for dumbo in range(len(dumbo_grid[row])):
			if dumbo_grid[row][dumbo] > 9:
				flash_count += 1
				dumbo_grid[row][dumbo] = 0
				flash_grid[row][dumbo] = False
	#Look for all zeroes
	if dumbo_grid == flash_grid:
		#Result = 276
		print(steps + 1)
	
	steps += 1
