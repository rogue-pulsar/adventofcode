#Import input from file as a list
report = open("input.txt").readlines()
#Convert list from string to int
report = list(map(int, report))
x = 0
#Loop adding and comparing values
for i in range(len(report)):
	try:
		y = report[i] + report[i+1] + report[i+2]
		z = report[i+1] + report[i+2] + report[i+3]
		if y < z:
			x += 1
	except:
		pass
#Result = 1724
print(x)