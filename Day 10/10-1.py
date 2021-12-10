#Import input from file as a list
source = open('example_input.txt').readlines()

#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

