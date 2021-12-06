import csv
import numpy
import itertools

#Import input as list
with open('example_input.csv') as file:
	csvReader = csv.reader(file, delimiter = ',')
	for row in csvReader:
		fish_list = row
#Convert list from string to int
fish_list = list(map(int, fish_list))
#Convert to numpy array
fish_list = numpy.array(fish_list)

#Time past
day = 0

#Loop for each day
while day < 18:
	for fish in itertools.chain.from_iterable(fish_list):
	#for fish in range(fish_list.size):
		if fish_list[fish] == 0:
			#Reset fish to 7 (not six since it gets processed today)
			fish_list[fish] = 7
			print(fish_list)
			fish_list = numpy.append(fish_list, [8])
		fish_list[fish] -= 1
	day += 1
	print('It is day:', day)
	print('There are:', len(fish_list), 'fish.')


#Result = 
#print(len(fish_list))

#Started at 1:42am