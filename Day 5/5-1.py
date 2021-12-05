import numpy
#import scipy

#Import input
report = open('example_input.txt').readlines()
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
		vreport.append(report[coord])
		vreport.append(report[coord + 1])
		vreport.append(report[coord + 2])
		vreport.append(report[coord + 3])
	elif report[coord + 1] == report[coord + 3]:
		hreport.append(report[coord])
		hreport.append(report[coord + 1])
		hreport.append(report[coord + 2])
		hreport.append(report[coord + 3])

#Swap coordinates so that they are always small to large
for coord in range(0, len(vreport), 4):
	if vreport[coord + 1] > vreport[coord + 3]:
		temp = vreport[coord + 1]
		vreport[coord + 1] = vreport[coord + 3]
		vreport[coord + 3] = temp

for coord in range(0, len(hreport), 4):
	if vreport[coord] > vreport[coord + 2]:
		temp = vreport[coord]
		vreport[coord] = vreport[coord + 2]
		vreport[coord + 2] = temp


#Create grid
grid = numpy.zeros((1000, 1000))

print(vreport)
for coord in range(0, len(vreport), 4):
	temp = grid[vreport[coord + 1]:vreport[coord + 3], coord]
	for i in range(len(temp)):
		grid[vreport[coord + 1]]


#print(hreport)
#print(vreport)

#for coord in range(0, len(hvreport), 4):

	#grid[hvreport[coord], hvreport[coord + 1]] =+ 1
	#grid[hvreport[coord + 2], hvreport[coord + 3]] =+ 1
	
	