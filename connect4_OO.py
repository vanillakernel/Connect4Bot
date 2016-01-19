#!/bin/python

import random
import math
import itertools

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
# The player will contain anything that makes decisions or takes actions.     #
###############################################################################
class Player (object):
  marker=None
  
  def __init__(self,marker):
    self.marker = marker
    if marker == 0:
      print "I am a computer player."
    if marker == 1:
      print "I am a human player."

    
  # Make a random move.
  def random_move (self, board):
      moves = board.get_valid_moves()
      board.play_single_move(self.marker,random.choice(moves))

  
  # This defines the value of a board given a few rules.
  def define_value(self, board):
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
        return
       if (cell == self.marker):
        return
    # Check for four vertical
    # Check for four diagonal

      # If the board is a loss, score it at -100

      # If we place a piece next to another piece, it is a slightly higher value.
      


      # For minmax, we will need to make the score high for player 0, low for 1
      if self.marker:
        return value*(-1)
      return value

  
   
###############################################################################
# The board makes sense as an object, however, memory footprint will be larger.
###############################################################################
class Game_Board (object):
  
  def __init__(self,rows,columns):
    self.board = []
    for x in range(0,rows):
      column = []
      for y in range(0,columns):
        column.append(None)
      self.board.append(column)

  # Returns a virtual column from the array of arrays.
  def get_column(self, index):
      column = []
      for row in self.board:
        column.append(row[index])
      return column


  # This will play the game forward to D depth from the current board.
  def game_tree(self, player, depth):
     return "" 

  # Get valid moves, and return an array of potential moves.
  def get_valid_moves(self):
    valid_moves =[] # this will store r/c where valid moves are.
    # For each column, try to drop a token, and return r/c if valid.
    for c in range (0,7):
      column = self.get_column(c);
      r = check_cell(column)
      if (r): #if the move is valid add it to the list of valid moves
        valid_moves.append((r,c))
    return valid_moves

  def board_score(self, player):
    #check a list for consecutive values
     if player == 0:
	 sign = -1
	 enemy = 1
     else:
	 sign = 1
	 enemy = 0
     score = 1000*(-sign)
     # We can convert each column to a row and put it through here.
     def score_row(row):
	temp_row = list (row)
	for x, y in itertools.groupby(temp_row):
	    length = len(list(y)) # y is changed in place. SIGHthon.
	    if length>=4 and x is not None: # Board is a win.
    		return True
    	    if length==3 and x is enemy: # Enemy will win
		return (100* (-sign))
	    if length==3 and x is not None: # We may win!
		return (100*sign)
	    if length==2 and x is enemy: # Enemy has a pair
		return (25* (-sign))
	    if length==2 and x is not None: # We have a pair
		return (25*sign)
	    return (10*sign)
     def score_diagonal(self):
	return "ugh"
     for c in range (0,7):
	 column = self.get_column(c);
	 row_score =  score_row(column)
	 if row_score == True:
	     return True
	 else:
	    print ("{0} is the player, {1} is the enemy. Row score is {2} "
		    ).format(player, enemy, row_score)
	    score += row_score
     for row in self.board:
	 row_score = score_row(row)
	 if row_score == True:
	     return True
	 else:
	     score += row_score
     return score
     

  #This will play back all the moves passed to it. It is passed and array of
  # coordinate tuples, then flips between players as it runs them.
  def play_moves(self,first_player,move_array):
    player = first_player # this is just for code clarity.
    for move in move_array:
      r, c = move
      print "{0} moves to row {1}, column {2}.".format( 
          "Player" if player == 1 else "Computer" , r+1 , c+1)
      self.board[r][c] = player
      player = not player


  # Test if a move is valid, then make it or return false.
  def play_single_move(self,player_marker,move):
      valid_moves = self.get_valid_moves() 
      if move in valid_moves:
        r, c = move
        self.board[r][c] = player_marker
        print "{0} moves to row {1}, column {2}.".format( 
          "Player" if player_marker == 1 else "Computer" , r+1 , c+1)
        self.print_board()
      else:
        return False
    
  def print_board (self):
    line = 1
    print ' '.join([' ','A','B','C','D','E','F','G'])
    for row in self.board:
       # Add column and row labels
       print '%r %s' % (line,' '.join(map(str,["_" if v is None else 
	       "X" if v == 1 else "O" if v==0 else v for v in row] )) )
       line+=1
    print "\n"

############################
#           MAIN           #
############################

def main ():
    # Create the empty first board.
    board = Game_Board(6,7)
    
    # Create players
    computer = Player(0)
    human = Player(1)

    # Pick who goes first. If current_player is 0, then it is the computer's turn.
    current_player = random.randint(0,1)

    if (current_player):
      print "The human goes first! \n"
    else:
      print "The computer goes first \n"

    # Make the computer play against itself.
    i=0
    win = False
    while (i<30 and win==False): 
      if (current_player):
	human.random_move(board)
      else:
        computer.random_move(board)
      i+=1
      score = board.board_score(current_player)
      print "This move has a score of %r" % score
      if score == True:
	  win = True
	  print "{0} wins!" .format(
		  "Computer" if current_player == 0 else "Human")
      current_player = int(not current_player)


if __name__ == "__main__":
        main()
