#Import input from file as a list
#report = open("2023/Day 01/example2.txt").readlines()
report = open("2023/Day 01/input.txt").readlines()
#report = ["one7one"]

#Check lists
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#New lists for switching words to numbers, reducing to integers and answers
report_translated = report
report_integers = []
report_answers = []

for report_index in range(0, len(report)):
	index_list = [] #List of indexes where words are found
	word_list = [] #List of words found, translated into numbers (in string form), same order as list of indexes

	#Find words and list their indexes and the digit version of the words
	for word in words:
		for report_line_length_index in range(0, len(report[report_index])):
			if report[report_index].find(word, report_line_length_index) != -1:
				index_list.append(report[report_index].find(word, report_line_length_index))
				word_list.append(numbers[words.index(word)])

	#Insert the first and last numbers found as a digit, skipping if no numbers are found
	if index_list:
		report_translated[report_index] = report_translated[report_index][:min(index_list)] + word_list[index_list.index(min(index_list))] + report_translated[report_index][min(index_list):]
		report_translated[report_index] = report_translated[report_index][:max(index_list)+1] + word_list[index_list.index(max(index_list))] + report_translated[report_index][max(index_list)+1:]

#Remove all letters, leaving just digits
for line in report_translated:
	report_integers.append(''.join(character for character in line if character.isdigit()))

#Reduce to just first and last digits
for line in report_integers:
	report_answers.append(line[0] + line[-1])

#Convert from string to integers
for i in range(0, len(report_answers)):
	report_answers[i] = int(report_answers[i])

#Final answer = 56017
print(sum(report_answers))