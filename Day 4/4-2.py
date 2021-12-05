import csv

#Import draws as list
with open('input_draws.csv') as edf:
	csvReader = csv.reader(edf, delimiter = ',')
	for row in csvReader:
		draws = row
#Convert list from string to int
draws = list(map(int, draws))
#Change 0s into a and 1s into b
for i in range(len(draws)):
	if draws[i] == 0:
		draws[i] = 'a'
	if draws[i] == 1:
		draws[i] = 'b'

#Import boards into one big list
with open('input_tables.txt') as etf:
	boards = [int(x) for x in etf.read().split()]
#Change 0s into a and 1s into b
for i in range(len(boards)):
	if boards[i] == 0:
		boards[i] = 'a'
	if boards[i] == 1:
		boards[i] = 'b'

#Add tracker before each number
for i in range(len(boards)):
	boards.insert(i*2, False)
#Split big list into lists of 50, (25 numbers -> 1 board)
boards = [boards[i:i + 50] for i in range(0, len(boards), 50)]

#Global win tracker, used to break out of draw and checking loops
win = False

#Global winning board tracker
winning_boards = []

'''
Column positions
c1p = [0, 1, 10, 11, 20, 21, 30, 31, 40, 41]
c2p = [2, 3, 12, 13, 22, 23, 32, 33, 42, 43]
c3p = [4, 5, 14, 15, 24, 25, 34, 35, 44, 45]
c4p = [6, 7, 16, 17, 26, 27, 36, 37, 46, 47]
c5p = [8, 9, 18, 19, 28, 29, 38, 39, 48, 49]
'''

def scoring(board_number, draw):
	score = 0
	#Sum uncalled numbers
	for i in range(0, 50):
		if boards[board_number][i] == False:
			if boards[board_number][i + 1] == 'a':
				score += 0
			elif boards[board_number][i + 1] == 'b':
				score += 1
			else:
				score += boards[board_number][i + 1]
	#Calculate final score
	if draws[draw] == 'a':
		score = 0
	elif draws[draw] == 'b':
		score += 0
	else:
		score = score * draws[draw]
	#Track which boards have won
	global winning_boards
	if board_number not in winning_boards:
		winning_boards.append(board_number)
	#Only calculate final board score if all boards have won
	if len(winning_boards) == len(boards):
		global win
		win = True
		print("Final score is:", score, "The final draw was:", draws[draw], "The final winning board was number:", board_number + 1)
	return

#Loop through each row/column of a given board looking for a False - if none are found, call the scoring function
def victory_check(board_number, draw):
	#Rows
	row = []
	check = True
	for r1 in range(0, 10):
		row.append(boards[board_number][r1])
	for i in row:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	row = []
	check = True
	for r2 in range(10, 20):
		row.append(boards[board_number][r2])
	for i in row:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	row = []
	check = True
	for r3 in range(20, 30):
		row.append(boards[board_number][r3])
	for i in row:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	row = []
	check = True
	for r4 in range(30, 40):
		row.append(boards[board_number][r4])
	for i in row:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	row = []
	check = True
	for r5 in range(40, 50):
		row.append(boards[board_number][r5])
	for i in row:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	row = []
	#Columns
	column = []
	check = True
	for c1 in [0, 1, 10, 11, 20, 21, 30, 31, 40, 41]:
		column.append(boards[board_number][c1])
	for i in column:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	column = []
	check = True
	for c2 in [2, 3, 12, 13, 22, 23, 32, 33, 42, 43]:
		column.append(boards[board_number][c2])
	for i in column:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	column = []
	check = True
	for c3 in [4, 5, 14, 15, 24, 25, 34, 35, 44, 45]:
		column.append(boards[board_number][c3])
	for i in column:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	column = []
	check = True
	for c4 in [6, 7, 16, 17, 26, 27, 36, 37, 46, 47]:
		column.append(boards[board_number][c4])
	for i in column:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	column = []
	check = True
	for c5 in [8, 9, 18, 19, 28, 29, 38, 39, 48, 49]:
		column.append(boards[board_number][c5])
	for i in column:
		if bool(i) == False:
			check = False
	if check == True:
		scoring(board_number, draw)
		return
	column = []
	check = True

#Read draw
for draw in range(len(draws)):
	#Check for match
	for board_number in range(len(boards)):
		for i in range(len(boards[board_number])):
			if draws[draw] == boards[board_number][i]:
				if i > 0:
					boards[board_number][i - 1] = True
			#Check for victory
			victory_check(board_number, draw)
			if win == True:
				break
		if win == True:
			break
	if win == True:
		break

#Part 1 answer: Final score: 51776, final draw: 64, winning board: 37