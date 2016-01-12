#!/bin/python

import random
import math


# Pick a cell at random and go there. This is a useful first step 
def random_move (current_board, player):
    c = random.randint(0,6) # pick a random column
    column =  get_column(current_board, c);
    #Figure out which row we drop to.
    r = check_cell(column)
    if (r): 
	current_board[r][c] = player   
	#print_board(current_board)
    else:
	random_move(current_board, player) # try again




# Returns a virtual column from the array of arrays.
def get_column(current_board, index):
    column = []
    for row in current_board:
	column.append(row[index])
    return column



# This will play the game forward to D depth from the current board.
def game_tree(current_board, player, depth):
   return "" 





# This defines the value of a board given a few rules.
def define_value(board, player):
    value = 0
    player_count = 0
    enemy_count = 0

# TODO see if I can do the static evaluation once based on player.

    # If the board is a win, score it at 100, and abitrary number.
	# Check for four  horizontal.
    for row in board.iterrows():
	r = row.values
	print r
	if (not math.isnan(cell)): # cell is occupied.
	    if (cell == player):
		return
	# Check for four vertical
	# Check for four diagonal

    # If the board is a loss, score it at -100

    # If we place a piece next to another piece, it is a slightly higher value.
    

    # For minmax, we will need to make the score high for player 0, low for 1
    if player:
	return value*(-1)
    return value



# Get valid moves, and return an array of potential moves.
def get_valid_moves(current_board,player):
  valid_moves =[] # this will store r/c where valid moves are.
   
  # For each column, try to drop a token, and return r/c if valid.
  for c in range (0,7):
    column = get_column(current_board, c);
    r = check_cell(column)
    if (r): #if the move is valid add it to the list of valid moves
      valid_moves.append((r,c))
  return valid_moves



#This will play back all the moves passed to it. It is passed and array of
# coordinate tuples, then flips between players as it runs them.
def play_moves(board,player,move_array):
    for move in move_array:
	print "Move is %r,%r" % move
	r, c = move
	board[r][c] = player
	player = not player


# Test if a move is valid, then make it or return false.
def play_single_move(board,player,move_tuple):
    print "Player %r 's move is %r,%r" % player, move
    valid_moves = get_valid_moves(board, player)
    if move in valid_moves:
	r, c = move
	board[r][c] = player
	player = not player
    else:
	return False


# Check which cell (if any), we can drop to in a column.
def check_cell(column, index=0):
    # If we are at the last row and it is still empty, just return that
    if (index == len(column)-1):
	return index
    if (column[0] is not None): #if top cell full, column is full. 
	return False
    # If current cell is empty, but the next one down is full, return index.
    if (column[index] is None and column[index+1] is not None):
	return index 
    #Otherwise, check the next cell down.
    return check_cell(column, index+1)
   
    

def print_board (board):
    line = 1
    print ' '.join([' ','A','B','C','D','E','F','G'])
    for row in board:
        # Add column and row labels
        print '%r %s' % (line,' '.join(map(str,["_" if v is None else  "X" if v == 1 else "O" if v==0 else v for v in row] )) )
        line+=1   
    


def main ():
    # Create the empty first board.
    board = [[None,None,None,None,None,None,None],
	     [None,None,None,None,None,None,None],
	     [None,None,None,None,None,None,None],
	     [None,None,None,None,None,None,None],
	     [None,None,None,None,None,None,None],
	     [None,None,None,None,None,None,None]]
   
    # Pick who goes first. If player is false, then it is the computer's turn.
    player = random.randint(0,1)
    if (player):
     print "Player goes first."
    if (not player):
     print "Computer goes first."
    print "Valid moves:"
    moves = get_moves(board, player)
    play_moves(board,player,moves)
    print_board(board)  

    # Make the computer play against itself.
'''    i=0
    while (i<30): 
	random_move(board, player)
	i+=1
	player = int(not player)
'''


if __name__ == "__main__":
        main()
