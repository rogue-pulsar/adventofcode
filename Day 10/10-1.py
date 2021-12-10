#Import input from file as a list
source = open('example_input.txt').readlines()

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
	#Ignore incomplete rows
	if len(subsystem[row])%2 == 0:
		index = 0
		current_opener = [subsystem[row][0]]
		while index <= len(subsystem[row]) - 1:
			if closing_character_of(subsystem[row][index]) == subsystem[row][index + 1]:
				index += 1
			elif subsystem[row][index + 1] in chunk_openers:
				current_opener.append(subsystem[row][index + 1])
				index += 1
			elif closing_character_of(current_opener[-1]) == subsystem[row][index + 1]:
				current_opener.pop(-1)
				index += 1
			elif subsystem[row][index + 1] in chunk_closers:
				corrupted_closers.append(subsystem[row][index + 1])
				break

print(corrupted_closers)


#Look for closing of current character, if next character is opening, look for closing of that character, if that is found, go back to looking for closing of previous character
