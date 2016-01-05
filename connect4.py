#!/bin/python

import pandas as pd
import random

# First start with random selections. Make it smart later.


# Pick a cell at random and go there. This is a useful first step 
def random_move (current_board, player):
    print "Current board: %r" % current_board
    #select a random column
    c = random.choice(list(current_board.columns.values))
    r = get_row(current_board, c)
    current_board.loc[r][c] = player    
    print "New board: \n %r" % print_board(current_board)


# As this game pieces are being 'dropped', find last empty cell in row.
def get_row(current_board, c):
    column = current_board[c]
    index = 0
    for cell in column:
	if (not cell):
	    return index
	index += 1
	if (index == len(column) and not cell): #column is full.
	    return False
    return index-1 #if none of the cells have a piece, return the last index.


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

    i=0
    while (i<20): 
	random_move(board, player)
	i+=1
	player = int(not player)

if __name__ == "__main__":
        main()
