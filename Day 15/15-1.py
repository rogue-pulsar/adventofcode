import networkx as nx
import matplotlib.pyplot as plt

#Import instructions
input_map = open('input.txt').readlines()
print('Input loaded')
#Strip linebreaks
for i in range(len(input_map)):
	input_map[i] = input_map[i].rstrip()
#Break up each line
for line in range(len(input_map)):
	input_map[line] = list(input_map[line])
#Count number of rows in input
rows = (len(input_map))
print('Input formatted')
print('Row count: ', rows)
#Flatten list and convert to ints
input_list = [item for sublist in input_map for item in sublist]
input_list = [int(i) for i in input_list]
print('Input flattened')
print('Input length: ', len(input_list))
#Calculate number of numbers per row
shift = int(len(input_list)/rows)
print('Shift count: ', shift)
#Create graph of nodes: 0 to 99
map = nx.empty_graph(n = len(input_list), create_using = nx.Graph)
print('Graph created')
#Assign edge weights using input
for i in range(len(input_list)):
	#Starting position
	if i == 0:
		continue
	#First row
	elif i < shift - 1:
		map.add_edge(i, i + 1, weight = input_list[i])
		map.add_edge(i, i - 1, weight = input_list[i])
		map.add_edge(i, i + shift, weight = input_list[i])
	#First row, right side
	elif i == shift - 1:
		map.add_edge(i, i - 1, weight = input_list[i])
		map.add_edge(i, i + shift, weight = input_list[i])
	#Last row, left side
	elif i / shift == rows - 1:
		map.add_edge(i, i + 1, weight = input_list[i])
		map.add_edge(i, i - shift, weight = input_list[i])
	#Finish position
	elif i == len(input_list) - 1:
		map.add_edge(i, i - 1, weight = input_list[i])
		map.add_edge(i, i - shift, weight = input_list[i])
	#Last row
	elif i // (rows - 1) == rows:
		map.add_edge(i, i + 1, weight = input_list[i])
		map.add_edge(i, i - 1, weight = input_list[i])
		map.add_edge(i, i - shift, weight = input_list[i])
	#Other rows
	else:
		#Left side
		if i % shift == 0:
			map.add_edge(i, i + 1, weight = input_list[i])
			map.add_edge(i, i + shift, weight = input_list[i])
			map.add_edge(i, i - shift, weight = input_list[i])
		#Right side
		elif i % shift == shift - 1:
			map.add_edge(i, i - 1, weight = input_list[i])
			map.add_edge(i, i + shift, weight = input_list[i])
			map.add_edge(i, i - shift, weight = input_list[i])
		#Middle
		else:
			map.add_edge(i, i + 1, weight = input_list[i])
			map.add_edge(i, i - 1, weight = input_list[i])
			map.add_edge(i, i + shift, weight = input_list[i])
			map.add_edge(i, i - shift, weight = input_list[i])
print('Edges added')

#Find least expensive path
path = nx.dijkstra_path_length(map, source = 0, target = len(input_list) - 1, weight = 'weight')
print('Path found')

print('Total cost: ', path)
# #Display graph
# nx.draw(map)
# plt.show()