import numpy as np

#Load input as a numpy matrix of numpy integers
with open('example_input.txt','rt') as infile:
	dumbo_grid =  np.matrix([list(line.strip()) for line in infile.readlines()], dtype = np.int64)

flash_count = 0
steps = 0
#Array of 1s used for incrementing the grid
increment_by_1 = np.ones((10, 10), dtype = np.int64)
#Array of falses to track flashes
flash_grid = np.zeros((10, 10), dtype = bool)

def increment_neighbors(row, dumbo):
	for i in range(max(row-1, 0), min(row+2, 10)):
		for j in range(max(dumbo-1, 0), min(dumbo+2, 10)):
			dumbo_grid[i, j] += 1

def search_neighbors(row, dumbo):
	for i in range(max(row-1, 0), min(row+2, 10)):
		for j in range(max(dumbo-1, 0), min(dumbo+2, 10)):
			if dumbo_grid[i, j] > 9 and flash_grid[i, j] == False:
				increment_neighbors(row, dumbo)

#Increment all by 1, go item by item, if more than 9, set flash to true, increment all around by 1, once there are no more above 9 and false, set all true to zero, step ++
print(dumbo_grid[0, 0])
print(flash_grid[0][0]) # -> causing errors due to numpy, rewrite code without numpy
print(len(dumbo_grid[0]))
while steps < 100:
	#Increment all by 1
	dumbo_grid = dumbo_grid + increment_by_1 # needs to be rewritten to work without numpy
	#Number by number
	for row in range(len(dumbo_grid)):
		for dumbo in range(len(dumbo_grid[row])):
			#If number is more than 9
			if dumbo_grid[row][dumbo] > 9 and flash_grid[row][dumbo] == False:
					#Set flash to true
					flash_grid[row][dumbo] = True
					#Increment neighbors by 1
					increment_neighbors(row, dumbo)
					#Search neighbors for over 9 and not flashed
					search_neighbors(row, dumbo)
	steps += 1