#!/bin/python

import pandas as pd
import random
import math

# First start with random selections. Make it smart later.


# Pick a cell at random and go there. This is a useful first step 
def random_move (current_board, player):
    #select a random column
    c = random.choice(list(current_board.columns.values))
    column = current_board[c]
    r = check_cell(column,0)
    if (r): #
	current_board.loc[r][c] = player    
	print "New board: \n %r" % print_board(current_board)
    else:
	random_move(current_board, player) # try again


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
	print row  
	# Check for four vertical
	# Check for four diagonal

    # If the board is a loss, score it at -100

    # If we place a piece next to another piece, it is a slightly higher value.
    

    # For minmax, we will need to make the score high for player 0, low for 1
    if player:
	return value*(-1)
    return value


# Check which cell (if any), we can drop to in a column.
def check_cell(column,index):
    # If we are at the last row and it is still empty, just return that
    if (index == len(column)-1):
	return index
    if (not math.isnan(column[0])): #if top cell full, column is full. 
	return False
    # If current cell is empty, but the next one down is full, return index.
    if (math.isnan(column[index]) and not math.isnan(column[index+1])):
	return index 
    #Otherwise, check the next cell down.
    return check_cell(column, index+1)
   
    

def print_board (board):
    board = board.fillna('_') # fill NaNs with something more appealing.
    return board


def main ():
    # Create initial game dataframe. We are using dataframes instead of a
    #   matrix as formatting can be applied  on a per-cell or colum basis, and 
    #   it prints better.

    board = pd.DataFrame(index=range(6), columns=['A','B','C','D','E','F','G'])

    # Pick who goes first. If player is false, then it is the computer's turn.
    player = random.randint(0,1)
    if (player):
     print "Player goes first."
    if (not player):
     print "Computer goes first."

    define_value(board, player)

    i=0
    #while (i<30): 
#	random_move(board, player)
#	i+=1
#	player = int(not player)

if __name__ == "__main__":
        main()
