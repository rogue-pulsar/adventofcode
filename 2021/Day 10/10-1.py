#Import input from file as a list
source = open('input.txt').readlines()

#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

chunk_openers = ['(', '[', '{', '<']
chunk_closers = [')', ']', '}', '>']
#Find the matching closing character
def closing_character_of(character):
	for i in range(4):
		if character == chunk_openers[i]:
			return chunk_closers[i]

subsystem = []
#Split into characters
for row in range(len(source)):
	subsystem.append(list(source[row]))

corrupted_closers = []
for row in range(len(subsystem)):
	index = 0
	current_opener = [subsystem[row][0]]
	while index < len(subsystem[row]) - 1:
		current_character = subsystem[row][index]
		next_character = subsystem[row][index + 1]
		if closing_character_of(current_character) == next_character:
			#Change the current opener since it has been closed
			if index != 0:
				current_opener.pop(-1)
			index += 1
		elif next_character in chunk_openers:
			if index == 0:
				current_opener.append(current_character)
			current_opener.append(next_character)
			index += 1
		elif closing_character_of(current_opener[-1]) == next_character:
			current_opener.pop(-1)
			index += 1
		elif next_character in chunk_closers:
			corrupted_closers.append(next_character)
			break

score = 0
for i in corrupted_closers:
	if i == ')':
		score += 3
	elif i == ']':
		score += 57
	elif i == '}':
		score += 1197
	else:
		score += 25137

#Result = 319233
print(score)
