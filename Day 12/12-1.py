import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
#For generating cave image
#from networkx.drawing.nx_pylab import draw_networkx

#Create empty graph where nodes = caves, edges = paths
map = nx.Graph()

#Import input from file as a list
source = open('example_input.txt').readlines()
#Remove linebreaks from list
for i in range(len(source)):
	source[i] = source[i].rstrip()

#Split into start and finish, adding nodes
for pair in range(len(source)):
	source[pair] = source[pair].split('-')
	map.add_nodes_from(source[pair])
#Add edges
for pair in range(len(source)):
	for node in range(0, len(source[pair]), 2):
		map.add_edge(source[pair][node], source[pair][node + 1])

found_paths = []
current_path = []

def find_paths(G, starting_node, current_path):
	global found_paths
	print('Current node is: ' + starting_node)
	#End condition
	if len(current_path) > 1:
		print('len check')
		if current_path[-1] == 'end':
			print('end check passed')
			if current_path[0] == 'start' and current_path[-1] == 'end':
				return current_path
			current_path.insert(0, 'start')
			return current_path
	neighbor_list = list(G.neighbors(starting_node))
	#For each neighbor of the current node
	for neighbor in neighbor_list:
		print(starting_node, ' neighbors are: ', neighbor)
		if len(current_path) > 1:
			print('len check')
			if current_path[-1] == 'end':
				print('end check passed')
				if current_path[0] == 'start' and current_path[-1] == 'end':
					return current_path
				current_path.insert(0, 'start')
				return current_path
		#If the neighbor is end, return this path
		if neighbor == 'end':
			current_path.append('end')
			print('A valid path is: ', current_path)
			return current_path
		#If the neighbor is start, skip this route
		elif neighbor == 'start':
			print('Start - invalid path')
			continue
		#If this lowercase neighbor already exists in the current path, skip this route
		elif neighbor.islower() and current_path.count(neighbor) > 0:
			print('Double small cave - invalid path')
			continue
		#Otherwise run the search for this neighbor's neighbors
		else:
			current_path.append(neighbor)
			print('Current path is: ', current_path)
			find_paths(G, neighbor, current_path)

find_paths(map, 'start', current_path)

#For generating cave image
#draw_networkx(map, with_labels = True)
#plt.show()

# def path_valid(path):
# 	#Check if path ends with end
# 	if path[-1] != 'end':
# 		return False
# 	#Check if path goes through start more than once
# 	if path.count('start') > 1:
# 		return False
# 	#Check if path has more than one instance of a given lowercase character
# 	for location in path:
# 		if location.islower() and path.count(location) > 1:
# 			return False
# 	return True

# def find_paths(G, starting_node, path_length):
# 	if path_length == 0:
# 		return [[starting_node]]
# 	paths = []
# 	for neighbor in G.neighbors(starting_node):
# 		if neighbor != 'start':
# 			#Check for paths of all lengths up to a given length
# 			for i in range(path_length):
# 				for path in find_paths(G, neighbor, i - 1):
# 					paths.append([starting_node] + path)
# 	return paths

# #Find all paths
# all_paths =  find_paths(map, 'start', 36)
# #Check for valid paths
# trimmed_paths = []
# for path in all_paths:
# 	if path_valid(path):
# 		trimmed_paths.append(path)
# #Remove duplicates
# valid_paths = []
# for path in trimmed_paths:
# 	if path not in valid_paths:
# 		valid_paths.append(path)

# print(len(valid_paths))