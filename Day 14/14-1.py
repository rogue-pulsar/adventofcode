import copy
from collections import Counter

#Import instructions
instructions = open('input.txt').readlines()
#Strip linebreaks
for i in range(len(instructions)):
	instructions[i] = instructions[i].rstrip()
#Input template
current_polymer = list('VOKKVSKKPSBVOOKVCFOV')
fabricated_polymer = list('VOKKVSKKPSBVOOKVCFOV')
insertions = 0
steps = 0

while steps < 10:
	for char in range(len(current_polymer) - 1):
		for pair in instructions:
			#If the instructions match the current two characters
			if pair[:2] == current_polymer[char] + current_polymer[char + 1]:
				#Insert it into the (other) list (to avoid reindexing errors)
				fabricated_polymer.insert(char + 1 + insertions, pair[-1])
				insertions += 1
	current_polymer = copy.deepcopy(fabricated_polymer)
	insertions = 0
	steps += 1

#Result = 'C': 4015, 'N': 3527, 'F': 2859, 'S': 1837, 'B': 1718, 'H': 1293, 'O': 1195, 'K': 1137, 'V': 956, 'P': 920
print(Counter(current_polymer))
# 4015 - 920 = 3095