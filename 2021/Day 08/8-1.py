#Import input from file as a list
source = open('input.txt').readlines()

#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

output_values = []

#Split signal patterns and output values
for line in range(len(source)):
	output_values.append(source[line].split('|'))

#Remove signal patterns
for line in range(len(output_values)):
	output_values[line].pop(0)

#Split into individual output values
for line in range(len(output_values)):
	for value in range(len(output_values[line])):
		output_values[line] = output_values[line][value].split()

count = 0

#Calculate how many 1, 4, 7, 8s there are
for output in range(len(output_values)):
	for value in range(len(output_values[output])):
		#If length of value is equal to what results in 1, 4, 7 or 8
		if len(output_values[output][value]) in [2, 4, 3, 7]:
			count += 1

#Result = 539
print(count)