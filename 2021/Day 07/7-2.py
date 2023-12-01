import csv

#Import input as list
with open('input.csv') as file:
	csvReader = csv.reader(file, delimiter = ',')
	for row in csvReader:
		crab_positions = row
#Convert list from string to int
crab_positions = list(map(int, crab_positions))
#Sort list
crab_positions.sort()

#Min and max values are used to calculate all possible positions the crabs can converge to
min_value = crab_positions[0]
max_value = crab_positions[-1]
fuel_used = 0
fuel_used_list = []

#Range of all possible positions
for position in range(max_value - min_value):
	#Calculate fuel used to move to a given position
	for i in range(len(crab_positions)):
		#Distance to a given position
		x = abs(crab_positions[i] - position)
		#Formula for new fuel useage ax = 1/2 x (x + 1)
		fuel_used += (0.5 * x * (x + 1))
	#Add fuel cost to list of all fuel costs
	fuel_used_list.append(fuel_used)
	fuel_used = 0

#Sort all fuel costs, lowest value is the answer
fuel_used_list.sort()

#Result = 99266250
print(fuel_used_list[0])
