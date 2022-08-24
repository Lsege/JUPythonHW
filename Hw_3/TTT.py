def create_row(width):
	row= []
	for i in range(width):
		row.append('-')
	return row

def first_player_move(position):
	if position >= 0 and position <= 2:
		row1[position] = 'X'
	elif position >= 3 and position <= 5:
		row2[position-3] = 'X'
	elif position >= 6 and position <= 8:
		row3[position-6] = 'X'
	else:
		print('select a valid position')

def second_player_move(position):
	if position >= 0 and position <= 2:
		row1[position] = 'O'
	elif position >= 3 and position <= 5:
		row2[position-3] = 'O'
	elif position >= 6 and position <= 8:
		row3[position-6] = 'O'
	else:
		print('select a valid position')

def coulumn_win(row1, row2, row3):
	for i in range(3):
		if row1[i] == row2[i]  and row1[i] == row3[i] and row1[i] != '-': return True


def row_win(row1, row2, row3):
	if row1[0] == row1[1] and row1[0] == row1[2] and row1[0] != '-': return True
	elif row2[0] == row2[1] and row2[0] == row2[2] and row2[0] != '-': return True
	elif row3[0] == row3[1] and row3[0] == row3[2] and row3[0] != '-': return True


def cross_win(row1, row2, row3):
	if row1[0] == row2[1] and row1[0] == row3[2] and row1[0] != '-': return True
	elif row3[0] == row2[1] and row3[0] == row1[2] and row3[0] != '-': return True
	

def end_game(row1, row2, row3):
	if row_win(row1, row2, row3): return True
	elif coulumn_win(row1, row2, row3): return True
	elif cross_win(row1, row2, row3): return True


def show_rows(row1, row2, row3):
	print(f'  {row1[0]} | {row1[1]} | {row1[2]}')
	print(f'  {row2[0]} | {row2[1]} | {row2[2]}')
	print(f'  {row3[0]} | {row3[1]} | {row3[2]}')


row1 = create_row(8)
row2 = create_row(8)
row3 = create_row(8)
count = 0
win = False

while not win:
	position = int(input('Insert the position you want to put your simbol: '))-1
	
	count +=1
	if count % 2 == 1:
		first_player_move(position)
	else:
		second_player_move(position)

	show_rows(row1, row2, row3)

	if count == 9:
		break

	win = end_game(row1, row2, row3)

if win: 
	print('You win')
else:
	print('Game tied')


