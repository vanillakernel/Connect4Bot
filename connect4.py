#!/bin/python

import pandas as pd
import random

# First start with random selections. Make it smart later.

def random_move (current_board, player):
    print "Current board: %r" % current_board
    #select a random cell and see if we can go there
    c = random.choice(list(current_board.columns.values))
    r = random.randint(0,5)
    print current_board.loc[r][c]
    current_board.loc[r][c] = player
    print "New board %r" % current_board


# Create initial game dataframe and print it. We are using dataframes instead 
#   of a matrix as formatting can be applied  on a per-cell or colum basis, and 
#   it prints better.

board = pd.DataFrame(index=range(6), columns=['A','B','C','D','E','F','G'])
board = board.fillna('_') # with 0s rather than NaNs

print board

# Pick who goes first. If player is false, then it is the computer's turn.
player = random.randint(0,1)
if (player):
    print "Player goes first."
if (not player):
    print "Computer goes first."

random_move(board, player)

