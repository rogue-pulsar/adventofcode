from collections import Counter
import copy

#Import instructions
instructions = open('input.txt').readlines()
#Strip linebreaks
for i in range(len(instructions)):
	instructions[i] = instructions[i].rstrip()
#Input template
current_polymer = list('VOKKVSKKPSBVOOKVCFOV')
steps = 0
count = {}
character_totals = {}
#Create empty count dictionary
for line in instructions:
	count[line[:2]] = [0, line[0] + line[-1], line[-1] + line[1]]
#Insert input into count
for pos in range(len(current_polymer) - 1):
	current_pair = current_polymer[pos] + current_polymer[pos + 1]
	if current_pair in count.keys():
		count[current_pair][0] += 1
#count dictionary = 'key' : [count of times key appears in input/current_ploymer, 'what keys it shifts to', 'what keys it shifts to']
next_count = copy.deepcopy(count)

#Create empty character total dictionary
for line in instructions:
	if line[-1] not in character_totals.keys():
		character_totals[line[-1]] = 0
#Count characters in input
for char in current_polymer:
	if char in character_totals.keys():
		character_totals[char] += 1

while steps < 40:
	for key in count.keys():
		#If pair exists
		if count[key][0] > 0:
			#Increase first and second pairs by number of initial pair
			next_count[count[key][1]][0] += count[key][0]
			next_count[count[key][2]][0] += count[key][0]
			#Decrease current pair by number of occurances
			next_count[key][0] -= count[key][0]
			#Increase character count by number of occurances
			character_totals[count[key][1][1]] += count[key][0]
	count = copy.deepcopy(next_count)
	steps += 1

final_result = []
for key in character_totals.keys():
	final_result.append(character_totals[key])
final_result.sort()

#Result = 3152788426516
print(final_result[-1] - final_result[0])