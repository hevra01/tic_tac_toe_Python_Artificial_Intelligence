# Tic Tac Toe game build with Artificial Intelligence

# Creating an array that will represent the board of the game.
# range(10) starts with 0 and ends at 9. The first index is zero which acts as a dummy place.
board = [' ' for x in range(10)]


# This function will insert either 'X' or 'O' to the specified place.
def insertLetter(letter, pos):
	board[pos] = letter


# Before we insert a letter to the board, we need to check if that place is free. In other words, there are no 'X's or 'O's there. 
def spaceIsFree(pos):
	return board[pos] == ' '


# Used to print the board.
def printBoard(board):
	print('    |      |')
	print('  ' + board[1] + ' |   ' + board[2] + '  | ' + board[3])
	print('    |      |')
	print('----------------')
	print('    |      |')
	print('  ' + board[4] + ' |   ' + board[5] + '  | ' + board[6])
	print('    |      |')
	print('----------------')
	print('    |      |') 
	print('  ' + board[7] + ' |   ' + board[8] + '  | ' + board[9])
	print('    |      |') 


# This function will check if there will be a winning case with the given board and letter.
# It will do this by checking all the possible winning combinations: horizontally, vertically, diagonally.
def isWinner(bo, le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or
	(bo[4] == le and bo[5] == le and bo[6] == le) or
	(bo[1] == le and bo[2] == le and bo[3] == le) or
	(bo[1] == le and bo[5] == le and bo[9] == le) or
	(bo[3] == le and bo[5] == le and bo[7] == le) or
	(bo[1] == le and bo[4] == le and bo[7] == le) or
	(bo[2] == le and bo[5] == le and bo[8] == le) or
	(bo[3] == le and bo[6] == le and bo[9] == le))



# This function belongs to the player (not the computer) to play their turn.
def playerMove():
	run = True
	while run:
		# Input a position from the user to insert 'X'
		move = input('Please select a position to place an \'X\' (1-9): ')

		# This will catch any error that may arise.
		try:
			# int() function will return a typeError if the argument is not a number
			move = int(move)
			if move > 0  and move < 10:
				if spaceIsFree(move):
					run = False
					insertLetter('X', move)
				else:
					print("Sorry, this place is occupied!")
			else:
				print('Please type a number within the range!')
		except:
			print("Please enter an integer")


# This function is the artificial intelligence part of the project.
# It will try to make a move that would either result in a win for 'O' if not possible it will prevent 'X' from winning.
def compMove():
	# First make a list of all the possible moves.
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

	move = 0 # We initialize the move with 0 and if it stays as zero throughout the function, iit implies that there is no possible place left.

	# The for loop will start the iteration with 'O' => meaning first it will look for a place that will result in its winning.
	# If there is no possible place for 'O' to be added to result in victory, then it will make sure to place 'O' in a place that will
	# prevent 'X' from winning.
	for let in ['O', 'X']:
		for i in possibleMoves:
			boardCopy = board[:]  # Create a copy of the board rather than a reference that will cause the original board to change.
			boardCopy[i] = let
			if isWinner(boardCopy, let):
				move = i
				return move
	
	# If there is no place that can result in either 'O' winning or 'X' winning than it will look for the corners.
	cornersOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornersOpen.append(i) 
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move

	# Check if the center is free.
	if 5 in possibleMoves:
		move = 5
		return move

	# Check for the edges.
	edgesOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i) 
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
	
	return move

def selectRandom(list):
	import random
	ln = len(list)
	r = random.randrange(0,ln)
	return list[r]


# This function will check if the board is full. 
def isBoardFull(board):
	if board.count(' ') > 1: # This is because index 0 has empty space.
		return False
	else:
		return True


def main():
	print('Welcome to Tic Tac Toe')
	printBoard(board)

	# Continue the game until the board is full.
	while not(isBoardFull(board)):

		# The game starts with the 'X'.
		# 'X' plays its turn unless 'O' has won.
		if not(isWinner(board, 'O')):
			playerMove()
			printBoard(board)
		else:
			print('Sorry, O\'s won this time!')
			break

		# It is 'O's turn if 'X' has not already won.
		if not(isWinner(board, 'X')):
			# If computer move returns 0, it implies that the board is full.
			move = compMove()
			if move == 0:
				print('Tie Game!')
			else:
				insertLetter('O', move)
				print('Computer placed an \'O\' in position', move, ':')
				printBoard(board)
		else:
			print('X\'s won this time!')
			break

main()