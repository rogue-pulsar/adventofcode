test = '[({(<(())[]>[[{[]{<()<>>'

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
    if closing_character_of(test1[0][index]) == test1[0][index + 1]:
        index += 1
        print('option1')
    elif test1[0][index + 1] in chunk_openers:
        if index == 0:
            current_opener.append(test1[0][index])
        current_opener.append(test1[0][index + 1])
        index += 1
        print('option2')
    elif closing_character_of(current_opener[-1]) == test1[0][index + 1]:
        current_opener.pop(-1)
        index += 1
        print('option3')
    elif test1[0][index + 1] in chunk_closers:
        print(index) #possible issue due to not moving index to skip over already checked closers?
        print(current_opener)
        corrupted_closers.append(test1[0][index + 1])
        print(test1[0][index])
        print('option4')
        break

print(corrupted_closers)
