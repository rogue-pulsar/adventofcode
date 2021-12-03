#from statistics import mode

#Import input from file as a list
report = open("input.txt").readlines()

# report = ["00100","11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

def omode(donkey):
	x = 0
	y = 0
	for i in range(len(donkey)):
		if donkey[i] == "1":
			x += 1
		else:
			y += 1
	if x >= y:
		return("1")
	else:
		return("0")

def cmode(donkey2):
	x = 0
	y = 0
	for i in range(len(donkey2)):
		if donkey2[i] == "1":
			x += 1
		else:
			y += 1
	if x > y:
		return("1")
	elif x == y:
		return("no")
	else:
		return("0")

#Remove linebreaks from list
for i in range(len(report)):
	report[i] = report[i].rstrip()

#Create empty list for first characters
c1 = []

#Create list of first characters
for i in range(len(report)):
	c1.append(report[i][0])

#Create empty lists for oxygen filtering, oX = full numbers, oXm = relevant character only
o1 = []
o2 = []
o3 = []
o4 = []
o5 = []
o6 = []
o7 = []
o8 = []
o9 = []
o10 = []
o11 = []
o12 = []
o1m = []
o2m = []
o3m = []
o4m = []
o5m = []
o6m = []
o7m = []
o8m = []
o9m = []
o10m = []
o11m = []
o12m = []

#Filter for first digit and populate lists
for i in range(len(c1)):
	if c1[i] == omode(c1):
		o1.append(report[i])
		o2m.append(report[i][1])
#Filter for second digit and create list
for i in range(len(o1)):
	#If the second character of the filtered numbers is equal to the most common character
	#of the filtered numbers, append the whole number and just the third character to new lists
	if o1[i][1] == omode(o2m):
		o2.append(o1[i])
		o3m.append(o1[i][2])

for i in range(len(o2)):
	if o2[i][2] == omode(o3m):
		o3.append(o2[i])
		o4m.append(o2[i][3])

for i in range(len(o3)):
	if o3[i][3] == omode(o4m):
		o4.append(o3[i])
		o5m.append(o3[i][4])

for i in range(len(o4)):
	if o4[i][4] == omode(o5m):
		o5.append(o4[i])
		o6m.append(o4[i][5])

for i in range(len(o5)):
	if o5[i][5] == omode(o6m):
		o6.append(o5[i])
		o7m.append(o5[i][6])

for i in range(len(o6)):
	if o6[i][6] == omode(o7m):
		o7.append(o6[i])
		o8m.append(o6[i][7])

for i in range(len(o7)):
	if o7[i][7] == omode(o8m):
		o8.append(o7[i])
		o9m.append(o7[i][8])

for i in range(len(o8)):
	if o8[i][8] == omode(o9m):
		o9.append(o8[i])
		o10m.append(o8[i][9])

for i in range(len(o9)):
	if o9[i][9] == omode(o10m):
		o10.append(o9[i])
		o11m.append(o9[i][10])

for i in range(len(o10)):
	if o10[i][10] == omode(o11m):
		o11.append(o10[i])
		o12m.append(o10[i][11])

#Result = 000111100110 (486)
print(o11)

#Create empty lists for carbon filtering, coX = full numbers, coXm = relevant character only
co1 = []
co2 = []
co3 = []
co4 = []
co5 = []
co6 = []
co7 = []
co8 = []
co9 = []
co10 = []
co11 = []
co12 = []
co1m = []
co2m = []
co3m = []
co4m = []
co5m = []
co6m = []
co7m = []
co8m = []
co9m = []
co10m = []
co11m = []
co12m = []

#Filter for first digit and populate lists
for i in range(len(c1)):
	if c1[i] != cmode(c1):
		co1.append(report[i])
		co2m.append(report[i][1])

#Filter for second digit and create list
for i in range(len(co1)):
	#If the second character of the filtered numbers is not equal to the most common character
	#of the filtered numbers, append the whole number and just the third character to new lists
	if co1[i][1] != cmode(co2m):
		co2.append(co1[i])
		co3m.append(co1[i][2])

for i in range(len(co2)):
	if co2[i][2] != cmode(co3m):
		co3.append(co2[i])
		co4m.append(co2[i][3])

for i in range(len(co3)):
	if co3[i][3] != cmode(co4m):
		co4.append(co3[i])
		co5m.append(co3[i][4])

for i in range(len(co4)):
	if co4[i][4] != cmode(co5m):
		co5.append(co4[i])
		co6m.append(co4[i][5])

for i in range(len(co5)):
	if co5[i][5] != cmode(co6m):
		co6.append(co5[i])
		co7m.append(co5[i][6])

for i in range(len(co6)):
	if co6[i][6] != cmode(co7m):
		co7.append(co6[i])
		co8m.append(co6[i][7])

for i in range(len(co7)):
	if co7[i][7] != cmode(co8m):
		co8.append(co7[i])
		co9m.append(co7[i][8])

for i in range(len(co8)):
	if co8[i][8] != cmode(co9m):
		co9.append(co8[i])
		co10m.append(co8[i][9])

for i in range(len(co9)):
	if co9[i][9] != cmode(co10m):
		co10.append(co9[i])
		co11m.append(co9[i][10])

for i in range(len(co10)):
	if co10[i][10] != cmode(co11m):
		co11.append(co10[i])
		co12m.append(co10[i][11])

for i in range(len(co11)):
	if co11[i][11] != cmode(co11m):
		co12.append(co11[i])

#Result = 101011100000 (2784)
print(co10)
print(486 * 2784)