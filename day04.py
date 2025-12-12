# --- Day 4: Printing Department ---

with open("input04.txt") as file:
    grid = [list(x) for x in file.read().splitlines()]
	
def neighbors(x, y, grid_array):
	"""Calculates the qty of occupied neighbours cells for one cell at grid."""
	neighs = [[x-1, y-1], [x, y-1], [x+1, y-1],
	          [x-1, y],              [x+1, y], 
	          [x-1, y+1], [x, y+1], [x+1, y+1]]
	paper_rolls = 0
	for n in neighs:
		new_x = n[0]
		new_y = n[1]
		if (0 <= new_x <= len(grid_array[0]) - 1) and (0 <= new_y <= len(grid_array) - 1):
			state = grid_array[new_y][new_x]
			if state == '@':
				paper_rolls += 1
	return paper_rolls

# Part one
accesible_spots = 0
cols = len(grid[1])
rows = len(grid)
for j in range(rows):
    for i in range(cols):
        result = neighbors(i,j,grid)
        spot = grid[j][i]
        if result < 4 and spot == "@":
            accesible_spots += 1
print(f"Part one answer --> {accesible_spots}")

# Part two
removed = 0
changes = [-1]
while changes:
    changes = [] 
    for j in range(rows):
        for i in range(cols):
            result = neighbors(i,j,grid)
            spot = grid[j][i]
            if result < 4 and spot == "@":
                accesible_spots += 1
                changes.append((j,i))
    removed += len(changes)
    for item in changes:
        y = item[0]
        x = item[1]
        grid[y][x] = "."

print(f"Part two answer --> {removed}")
