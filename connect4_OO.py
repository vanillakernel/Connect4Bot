#!/bin/python

import random
import math


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
   
###############################################################################
# The board makes sense as an object, however, memory footprint will be larger.
###############################################################################

class Game_Board (object):
  
  
  def __init__(self,rows,columns):
    self.board = []
    column = []
    for x in range(0,rows):
        for y in range(0,columns):
          column.append(None)
        self.board.append(column)


  # Random move.
  def random_move (self, player):
      moves = self.get_valid_moves(player)
      self.play_single_move(player,random.choice(moves))

  ### ONLY ONE TO CHOOSE SORRY  ###


  # Returns a virtual column from the array of arrays.
  def get_column(self, index):
      column = []
      for row in self.board:
        column.append(row[index])
      return column


  # This will play the game forward to D depth from the current board.
  def game_tree(self, player, depth):
     return "" 


  # This defines the value of a board given a few rules.
  def define_value(self, player):
      value = 0
      player_count = 0
      enemy_count = 0

  # TODO see if I can do the static evaluation once based on player.

    # If the board is a win, score it at 100, and abitrary number.
    # Check for four  horizontal.
      for row in self.iterrows():
       r = row.values
       print r
       if (not math.isnan(cell)): # cell is occupied.
        return
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
  def get_valid_moves(self,player):
    valid_moves =[] # this will store r/c where valid moves are.
     
    # For each column, try to drop a token, and return r/c if valid.
    for c in range (0,7):
      column = self.get_column(c);
      r = check_cell(column)
      if (r): #if the move is valid add it to the list of valid moves
        valid_moves.append((r,c))
    return valid_moves



  #This will play back all the moves passed to it. It is passed and array of
  # coordinate tuples, then flips between players as it runs them.
  def play_moves(self,player,move_array):
      for move in move_array:
        r, c = move
        print "{0} moves to row {1}, column {2}.".format( 
          "Player" if player == 1 else "Computer" , r+1 , c+1)
        self[r][c] = player
      player = not player


  # Test if a move is valid, then make it or return false.
  def play_single_move(self,player,move):
      valid_moves = self.get_valid_moves(player)
      if move in valid_moves:
        r, c = move
        self[r][c] = player
        print "{0} moves to row {1}, column {2}.".format( 
          "Player" if player == 1 else "Computer" , r+1 , c+1)
        player = not player
        print_board(self)
      else:
        return False
    
  def print_board (self):
    line = 1
    print ' '.join([' ','A','B','C','D','E','F','G'])
    for row in self:
       # Add column and row labels
       print '%r %s' % (line,' '.join(map(str,["_" if v is None else 
	       "X" if v == 1 else "O" if v==0 else v for v in row] )) )
       line+=1
    print "\n"



def main ():
    # Create the empty first board.
    board_object = Game_Board(6,7)
    # Pick who goes first. If player is false, then it is the computer's turn.
    player = random.randint(0,1)
    if (player):
     print "Player goes first."
    if (not player):
     print "Computer goes first."

    # Make the computer play against itself.
    i=0
    while (i<5): 
	board_object.random_move(player)
	i+=1
	player = int(not player)



if __name__ == "__main__":
        main()
