import numpy

#Import input from file as a list
#draws = open("input.txt").readlines()
#Convert list from string to int
#draws = list(map(int, report))

#draw a number, loop through matrice make int into string

#Import boards as one big matrix
example = numpy.loadtxt("example_tables.txt", dtype = int)

#Split big matrix into separate boards
boards = numpy.vsplit(example, len(example)/5)

for array in range(len(boards)):
	boards[array] = tuple(map(tuple, boards[array]))
	boards[array] = dict.fromkeys(boards[array], False)

print(boards[0])


