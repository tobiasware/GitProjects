import math

board = [
[1,0,0,6,0,7,0,8,0],
[0,4,0,0,1,3,0,5,2],
[7,2,0,0,0,4,3,0,6],
[2,0,9,0,5,0,0,0,0],
[0,0,0,7,3,0,0,2,4],
[0,0,0,0,8,0,1,6,0],
[0,1,2,0,6,0,5,0,7],
[0,0,4,1,7,0,0,0,8],
[3,5,0,2,4,8,0,0,0]
]

def print_board(board):

	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - -")

		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print("|", end = " ")

			if j == 8:
				print(board[i][j])
			else:
				print(board[i][j], end=" ")


def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j)	# row, column
	return None

def valid(board, num, pos):

	for i in range(len(board)):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	x = (pos[0] // math.sqrt(len(board))) * 3
	y = (pos[1] // math.sqrt(len(board))) * 3

	for i in range(int(math.sqrt(len(board)))):
		for j in range(int(math.sqrt(len(board)))):
			if board[int(x)+i][int(y)+j] == num and (i,j) != pos:
				return False
	return True

def solve(board):

 	f = find_empty(board)
 	if not f:
 		return True
 	else:
 		row, col = f

 	for i in range(1,10):
 		if valid(board, i, (row, col)):
 			board[row][col] = i

 			if solve(board):
 				return True
 			board[row][col] = 0
 	return False

print_board(board)
solve(board)
print()
print()
print()
print_board(board)
