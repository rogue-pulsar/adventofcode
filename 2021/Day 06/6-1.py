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

#Loop for each day
while days < 80:
	for fish in range(len(fish_list)):
		if fish_list[fish] == 0:
			#Reset fish to 7 (not six since it gets processed today)
			fish_list[fish] = 7
			fish_list.append(8)
		fish_list[fish] -= 1
	day += 1

#Result = 356190
print(len(fish_list))