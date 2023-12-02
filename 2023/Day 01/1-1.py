#Import input from file as a list
#report = open("2023/Day 01/example.txt").readlines()
report = open("2023/Day 01/input.txt").readlines()

#New lists for extracting integers from report and final answers
report_integers = []
report_answers = []

#Remove all letters, leaving just digits
for line in report:
    report_integers.append(''.join(character for character in line if character.isdigit()))

#Reduce to just first and last digits
for line in report_integers:
    report_answers.append(line[0] + line[-1])

#Convert from string to integers
for i in range(0, len(report_answers)):
    report_answers[i] = int(report_answers[i])

#Final answer = 56506
print(sum(report_answers))