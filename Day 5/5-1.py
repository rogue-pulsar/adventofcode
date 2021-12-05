import numpy

#Import input
report = open('input.txt').readlines()
#Strip linebreaks
for i in range(len(report)):
	report[i] = report[i].rstrip()
#Split into Input>Path>Pair>Coord
for i in range(len(report)):
	report[i] = report[i].split(' -> ')
for path in range(len(report)):
	for pair in range(len(report[path])):
		report[path][pair] = report[path][pair].split(',')
#Flatten list via numpy
report = numpy.array(report).flatten()
#Return to list format
report = report.tolist()
#Change strings to integers
report = list(map(int, report))

#New list of horizontal paths
hreport = []
#New list of vertical paths
vreport = []
#Filter for just horizontal or vertical lines
for coord in range(0, len(report), 4):
	if report[coord] == report[coord + 2]:
		for i in range(0, 4):
			vreport.append(report[coord + i])
	elif report[coord + 1] == report[coord + 3]:
		for i in range(0, 4):
			hreport.append(report[coord + i])

#Swap coordinates so that they are always small to large
for coord in range(0, len(vreport), 4):
	if vreport[coord + 1] > vreport[coord + 3]:
		temp = vreport[coord + 1]
		vreport[coord + 1] = vreport[coord + 3]
		vreport[coord + 3] = temp

for coord in range(0, len(hreport), 4):
	if hreport[coord] > hreport[coord + 2]:
		temp = hreport[coord]
		hreport[coord] = hreport[coord + 2]
		hreport[coord + 2] = temp

#Create grid (numpy.ndarray)
grid = numpy.zeros((1000, 1000))

#Mark vertical lines
for coord in range(0, len(vreport), 4):
	path = grid[vreport[coord + 1]:vreport[coord + 3], vreport[coord]]
	for i in range(len(path)):
		grid[vreport[coord], vreport[coord + 1] + i] += 1
	grid[vreport[coord + 2], vreport[coord + 3]] += 1

#Mark horizontal lines
for coord in range(0, len(hreport), 4):
	path = grid[hreport[coord + 1], hreport[coord]:hreport[coord + 2]]
	for i in range(len(path)):
		grid[hreport[coord] + i, hreport[coord + 1]] += 1
	grid[hreport[coord + 2], hreport[coord + 3]] += 1

#Check for overlaps
overlap = 0
for row in grid:
	for i in row:
		if i > 1:
			overlap += 1

#Result = 6113
print(overlap)