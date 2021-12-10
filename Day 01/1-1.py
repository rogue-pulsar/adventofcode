#Import input from file as a list
report = open("input.txt").readlines()
#Convert list from string to int
report = list(map(int, report))
x = 0
#Loop comparing values
for i in range(len(report)):
	try:
		if report[i] < report[i+1]:
			x += 1
	except:
		pass
#Result = 1692
print(x)