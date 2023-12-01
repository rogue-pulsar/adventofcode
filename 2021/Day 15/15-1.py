import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

data = np.genfromtxt('input.txt', delimiter=1, dtype=int)
data = data.tolist()

grid = Grid(matrix = data)
start = grid.node(0,0)
end = grid.node(99,99)

finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print(grid.grid_str(path=path, start=start, end=end))

cost = -data[0][0]
for y,x in path:
	cost += data[x][y]

#Result = 487
print(cost)