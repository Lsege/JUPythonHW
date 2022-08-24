def create_grid(height, width, by_default):
	grid =[]
	for _ in range(height):	
		row = []
		for _ in range(width):
			row.append(by_default)
		grid.append(row)
	return grid

def show_grid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print(f'|{grid[i][j]}|', end='')
		print('')

def total_length(grid):
	total_length = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			total_length +=1
	return total_length 


def replace_cell(grid, position, value):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			count += 1
			if position == count:
				grid[i][j] = value
				return grid

def replace_cell2(grid, position, value):
	aux = position -1
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if aux == j:
				grid[i][j] = value
				return grid 
		if aux > len(grid[i]):
			aux = aux - len(grid[i])

def is_occupied(grid, position, by_default):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			count += 1
			if position == count:
				if grid[i][j] != by_default:
					return True
				else:
					return False

tic_tac_toe = create_grid(3, 3, '_')
show_grid(tic_tac_toe)
print('-----')
tic_tac_toe = replace_cell(tic_tac_toe, 5, 'X')
show_grid(tic_tac_toe)

print(is_occupied(tic_tac_toe, 5, '_'))
print(is_occupied(tic_tac_toe, 6, '_'))
