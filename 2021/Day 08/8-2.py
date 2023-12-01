#Import input from file as a list
source = open('input.txt').readlines()

#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

#Split signal patterns and output values
for line in range(len(source)):
	source[line] = (source[line].split('|'))

#Split strings of values into values
for line in range(len(source)):
	for value in range(len(source[line])):
		source[line][value] = source[line][value].split()
#Source = [[[<signal pattern>], [<output values>]], [<signal pattern>], [<output values>]]
#Signal pattern and output values are split into individual strings

results = []

for line in range(len(source)):
	#Display values where the index of the element is what number it displays
	display_values = ['','','','','','','','','','']
	#Access each individual string on the signal pattern side
	for string in range(len(source[line][0])):
		#Whiles are required to find certain numbers first since they are used later to find other numbers
		while display_values[1] == '' or display_values[4] == '' or display_values[7] == '' or display_values[8] == '':
			for string_known in range(len(source[line][0])):
				signal_pattern = source[line][0][string_known]
				#Assign known signal pattern lengths to their display values
				if len(signal_pattern) == 2:
					display_values[1] = signal_pattern
				if len(signal_pattern) == 4:
					display_values[4] = signal_pattern
				if len(signal_pattern) == 3:
					display_values[7] = signal_pattern
				if len(signal_pattern) == 7:
					display_values[8] = signal_pattern
		while display_values[3] == '':
			for string_3 in range(len(source[line][0])):
				signal_pattern = source[line][0][string_3]
				if len(signal_pattern) == 5:
					#Assign 3 because it is the only five character string to contain all of 1
					#If set of pattern containing 5 characters is in the set of the pattern for 1
					if set(signal_pattern).intersection(set(display_values[1])) == set(display_values[1]):
						#Then the pattern is 3
						display_values[3] = signal_pattern
		while display_values[9] == '':
			for string_9 in range(len(source[line][0])):
				signal_pattern = source[line][0][string_9]
				if len(signal_pattern) == 6:
					#If the union of 3 and 4 is the same as the signal pattern
					if set(display_values[3]).union(set(display_values[4])) == set(signal_pattern):
						#Then the pattern is 9
						display_values[9] = signal_pattern
		while display_values[5] == '' or display_values[2] == '':
			for string_5_2 in range(len(source[line][0])):
				signal_pattern = source[line][0][string_5_2]
				#Pattern of 5 length that isn't an display value of 3 (already found)
				if len(signal_pattern) == 5 and signal_pattern != display_values[3]:
					#If it contains the difference of 9 and 3
					if (set(display_values[9]).difference(set(display_values[3]))).issubset(set(signal_pattern)):
						#Then the pattern is 5
						display_values[5] = signal_pattern
					else:
						#Otherwise it has to be 2 if it isn't 3
						display_values[2] = signal_pattern
		while display_values[0] == '' or display_values[6] == '':
			for string_0_6 in range(len(source[line][0])):
				signal_pattern = source[line][0][string_0_6]
				#Pattern of 6 length that isn't an display value of 9 (already found)
				if len(signal_pattern) == 6 and signal_pattern != display_values[9]:
					#If it contains the intersection of 2 and 1
					if (set(display_values[2]).intersection(set(display_values[1]))).issubset(set(signal_pattern)):
						#Then the pattern is 0
						display_values[0] = signal_pattern
					else:
						#Otherwise it has to be 6
						display_values[6] = signal_pattern

	#Sort display values alphabetically for comparison
	for value in range(len(display_values)):
		display_values[value] = ''.join(sorted(display_values[value]))

	#Access each individual string on the output value side
	for string in range(len(source[line][1])):
		#Sorting output value for comparison
		output_value = ''.join(sorted(source[line][1][string]))
		for value in range(len(display_values)):
			#Match output value to display value
			if output_value == display_values[value]:
				#Append index (the actual displayed value) to results
				results.append(value)
				break

#Since the results are currently individual integers, they need to be concatenated in groups of 4
results_final = []
for value in range(0, len(results), 4):
	results_final.append(int(str(results[value]) + str(results[value + 1]) + str(results[value + 2]) + str(results[value + 3])))

#Result = 1084606
print(sum(results_final))