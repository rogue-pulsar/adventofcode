from statistics import mode

#Import input from file as a list
report = open("input.txt").readlines()

#Remove linebreaks from list
for i in range(len(report)):
	report[i] = report[i].rstrip()

#Create empty lists for each column (1-12)
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
c10 = []
c11 = []
c12 = []

#Split input into columns
for i in range(len(report)):
	c1.append(report[i][0])
	c2.append(report[i][1])
	c3.append(report[i][2])
	c4.append(report[i][3])
	c5.append(report[i][4])
	c6.append(report[i][5])
	c7.append(report[i][6])
	c8.append(report[i][7])
	c9.append(report[i][8])
	c10.append(report[i][9])
	c11.append(report[i][10])
	c12.append(report[i][11])

#Find mode for each column
g1 = mode(c1)
g2 = mode(c2)
g3 = mode(c3)
g4 = mode(c4)
g5 = mode(c5)
g6 = mode(c6)
g7 = mode(c7)
g8 = mode(c8)
g9 = mode(c9)
g10 = mode(c10)
g11 = mode(c11)
g12 = mode(c12)

gamma_rate = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12

#Result 000100011100 (284), therefore epsilon_rate = 111011100011 (3811)
print(gamma_rate)
print(284 * 3811)
