test = '{([(<{}[<>[]}>{[]{[(<()>'

test1 = []

test1.append(list(test))

chunk_openers = ['(', '[', '{', '<']
chunk_closers = [')', ']', '}', '>']
#Find the matching closing character
def closing_character_of(character):
	for i in range(4):
		if character == chunk_openers[i]:
			return chunk_closers[i]

corrupted_closers = []
index = 0
current_opener = []
while index < len(test1[0]) - 1:
    current_character = test1[0][index]
    next_character = test1[0][index + 1]
    if closing_character_of(current_character) == next_character:
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

print(corrupted_closers)
