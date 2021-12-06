import csv
#Import input as list
with open('input.csv') as file:
	csvReader = csv.reader(file, delimiter = ',')
	for row in csvReader:
		fish_list = row
#Convert list from string to int
fish_list = list(map(int, fish_list))

#Time past
day = 0

#Fish states
f0 = 0
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0

#Assign initial fish states
for fish_state in range(len(fish_list)):
	if fish_list[fish_state] == 1:
		f1 += 1
	if fish_list[fish_state] == 2:
		f2 += 1
	if fish_list[fish_state] == 3:
		f3 += 1
	if fish_list[fish_state] == 4:
		f4 += 1
	if fish_list[fish_state] == 5:
		f5 += 1

#Loop for each day, moving the states down the line and adding new fish
while day < 256:
	temp = f0
	f0 = f1
	f1 = f2
	f2 = f3
	f3 = f4
	f4 = f5
	f5 = f6
	f6 = f7 + temp
	f7 = f8
	f8 = temp

	day += 1
	print('It is day:', day)
	print('There are:', f0 + f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8, 'fish.')

#Result = 1617359101538