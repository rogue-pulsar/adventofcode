import numpy as np
### Import ###
#Import board
dots = open('input.txt').readlines()
#Strip linebreaks
for i in range(len(dots)):
	dots[i] = dots[i].rstrip()
#Split into y, x
for i in range(len(dots)):
	dots[i] = dots[i].split(',')
#Convert to integers
dots = [list(map(int, line)) for line in dots]

#Import instructions
instructions = open('instructions.txt').readlines()
#Strip linebreaks
for i in range(len(instructions)):
	instructions[i] = instructions[i].rstrip()
#Split into y/x and location
for i in range(len(instructions)):
	instructions[i] = instructions[i].split('=')
#Convert location to int
for line in range(len(instructions)):
	for i in range(0, len(instructions[line]), 2):
		instructions[line][i + 1] = int(instructions[line][i + 1])
#instructions = [line][fold along x/y (0) or int (1)][if x/y, [-1] to get x or y]

### Logic ###
#Find biggest y and x
maximum_y = 1
maximum_x = 1
for line in range(len(dots)):
	for i in range(0, len(dots[line]), 2):
		if dots[line][i] > maximum_y:
			maximum_y = dots[line][i]
		if dots[line][i + 1] > maximum_x:
			maximum_x = dots[line][i + 1]
#Add 1 to account for how range works
maximum_y += 1
maximum_x += 1

#Create matrix of false based on size provided by previously found maximums
t_paper = np.zeros((maximum_x, maximum_y), dtype = bool)
#Mark dots on grid
for line in range(len(dots)):
	for i in range(0, len(dots[line]), 2):
		t_paper[dots[line][i + 1], dots[line][i]] = True

for line in range(len(instructions)):
	for i in range(0, len(instructions[line]), 2):
		if instructions[line][0][-1] == 'y':
			#Slice the arrays along the given line
			to_be_folded = t_paper[instructions[line][1] + 1:, :]
			t_paper = t_paper[:instructions[line][1], :]
			#Vertically flip the folding array
			to_be_folded = np.flipud(to_be_folded)
			#Add the arrays together
			t_paper = t_paper + to_be_folded
		if instructions[line][0][-1] == 'x':
			#Slice the arrays along the given line
			to_be_folded = t_paper[:, instructions[line][1] + 1:]
			t_paper = t_paper[:, :instructions[line][1]]
			#Horizontally flip the folding array
			to_be_folded = np.fliplr(to_be_folded)
			#Add the arrays together
			t_paper = t_paper + to_be_folded

a = t_paper.tolist()
for line in a:
	print(''.join(['█' if char else ' ' for char in line]))
#Result = EFJKZLBL