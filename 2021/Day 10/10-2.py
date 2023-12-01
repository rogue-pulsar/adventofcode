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

corrupted_rows = []
#Find corrupted rows
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
			corrupted_rows.append(row)
			break

#Discard corrupted rows
for i in sorted(corrupted_rows, reverse = True):
    del subsystem[i]

completion_strings = []
#Complete incomplete rows
for row in range(len(subsystem)):
	index = 0
	current_opener = [subsystem[row][0]]
	row_completion_strings = []
	row_length = len(subsystem[row])
	while index < row_length:
		current_character = subsystem[row][index]
		if index < row_length - 1:
			next_character = subsystem[row][index + 1]
		if index == row_length - 1:
			if len(current_opener) == 0:
				break
			subsystem[row].append(closing_character_of(current_opener[-1]))
			row_completion_strings.append(closing_character_of(current_opener[-1]))
			current_opener.pop(-1)
			index += 1
			row_length += 1
		elif closing_character_of(current_character) == next_character:
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
		else:
			break
	completion_strings.append(row_completion_strings)

#Remove last element in each row of completion_strings because I somehow have an extra on each row??
for row in range(len(completion_strings)):
	del completion_strings[row][-1]


def score_of(character):
	for i in range(len(chunk_closers)):
		if character == chunk_closers[i]:
			return i + 1
	

score = []
#Calculate scores
for row in range(len(completion_strings)):
	row_score = 0
	for character in range(len(completion_strings[row])):
		row_score = row_score * 5 + score_of(completion_strings[row][character])
	score.append(row_score)

score.sort()
print(score[int((len(score) - 1)/2)])