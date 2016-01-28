#!/bin/python

import random
import math
from itertools import groupby
import copy




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
      moves = board.valid_moves()
      move = random.choice(moves)
      self.play_single_move(board,move)
      print "The random move is: %r,%r" % move
      board.print_board()
      score = self.board_score(board, self.marker)
      #print "This move has a score of %r" % score
      #print ("Playing the RANDOM MOVE, as the {0} with {1} as my opponent, I score this board at {2} "
#	     ).format("Human" if self.marker else "Computer",
#		     "Human" if not self.marker else "Computer", score)
      if score == True:
	  print "{0} wins!" .format(
		  "Computer" if self.marker == 0 else "Human")
	  return True
      else:
	  return False


  # MinMax
  def minmax(self, board):
    moves = board.valid_moves()
    best_board = copy.deepcopy(board)
    best_move = random.choice(moves) #yolo
    if (self.marker): # Human wants the max.
	best_score=(-1)
    else: # Computer wants the min.
	best_score=(1)
    for move in moves:
	temp_board = copy.deepcopy(board)
	temp_board = self.play_single_move(temp_board, move)
	temp_board.score = self.board_score(temp_board,self.marker)
	if (temp_board.score == True):
	    best_score = temp_board.score
	    best_board = temp_board
	    best_move = move
	    print "The WINNING  move is: %r, %r:" % move
	    best_board.print_board()
	    return move
	if (self.marker and temp_board.score > best_score):#Maximize
	    print "Found a better score: {0} is better than {1} for the {2}".format(
		    temp_board.score, best_score, "Computer" if self.marker == 0 else "Human")
	    best_score = temp_board.score
	    best_board = temp_board
	    best_move = move
	if (not self.marker and temp_board.score < best_score): #minimize
	    print "Found a better score: {0} is better than {1} for the {2}".format(
		    temp_board.score, best_score, "Computer" if self.marker == 0 else "Human")
	    best_score = temp_board.score
	    best_board = temp_board
	    best_move = move
    print "The ideal move is: %r, %r:" % move
    best_board.print_board()
    return move 
  
  # MinMaxDeep
  def minmax_deep(self, board, depth, score):
    last_score = score
    # Turn one is always us.
    if depth%2==0:
	turn = not self.marker
    else:
	turn = self.marker
    print "depth %r , turn %r" % (depth,turn) 
    print "{0}'s turn.".format("Computer" if turn == 0 else "Human")
    moves = board.valid_moves()
    best_board = copy.deepcopy(board)
    best_move = random.choice(moves) #yolo
    
    if (turn): # Human wants the max.
	best_score=(-1)
    else: # Computer wants the min.
	best_score=(1)
	
    if (depth > 0):
	for move in moves:
	    temp_board = copy.deepcopy(board)
	    temp_board = self.play_single_move(temp_board, move)
	    temp_board.score = self.board_score(temp_board, turn)

	    if (temp_board.score == True):
		best_score = temp_board.score
	        best_board = temp_board
		best_move = move
		print "The WINNING  move is: %r, %r:" % move
		best_board.print_board()
		return move
	    if (turn and temp_board.score > best_score):#Maximize
		print "Found a better score: {0} is better than {1} for the {2}".format(
		temp_board.score, best_score, "Computer" if turn == 0 else "Human")
		best_score = temp_board.score
		best_board = temp_board
		best_move = move
	    if (not turn and temp_board.score < best_score): #minimize
		print "Found a better score: {0} is better than {1} for the {2}".format(
		temp_board.score, best_score, "Computer" if turn == 0 else "Human")
		best_score = temp_board.score
		best_board = temp_board
		best_move = move
	self.minmax_deep(temp_board, depth-1, best_score)

    print "The ideal move is: %r, %r:" % best_move
    best_board.print_board()
    return best_move 
  
  
  # Time to score.
  def board_score(self, board, turn):
     if turn == 0: # This is the computer
	 sign = -1
	 enemy = 1
     else:
	 sign = 1
	 enemy = 0
     score = 2*sign # reset the score for the board.
     # We can convert each column to a row and put it through here.
     def score_row(row, score):
	matches = [(key,len(list(group))) for key, group in groupby(row)]
	for match in matches:
	    key,count=match
	    if count>=4 and key is turn: # Board is a win for us.
		print "HNGGGGGG"
		#score += (20000*sign)
		return True
	    if count==3 and key is enemy: # Enemy will win
		#print "Our enemy, the {0}, has a triple!".format(
		#	"Human" if enemy else "Computer")
		score += (200* (-sign))
	    if count==3 and key is turn: # We may win!
		#print "We, the {0}, are so close!".format(
		#	"Human" if self.marker else "Computer")
		score += (200*sign)
	    if count==2 and key is enemy: # Enemy has a pair
		#print "Our enemy, the {0}, has a pair".format(
		#	"Human" if enemy else "Computer")
		score += (1* (-sign))
	    if count==2 and key is turn: # We have a pair
		#print "We, the {0}, have a pair".format(
		#	"Human" if self.marker else "Computer")
		score += (1*sign)
	return score
     def score_diagonal(self):
	return "ugh"
     # We score rows first because all things equal,rows are easier to complete.
     for row in board.board: 
	 row_score = score_row(row,score)
	 if row_score == True:
	     return True
	 else:
	     score += row_score
     for c in range (0,7):
	 column = board.get_column(c);
	 row_score =  score_row(column, score)
	 if row_score == True:
	     return True
	 else:
	    score += row_score
	     
     '''print ("Playing as the {0} with {1} as my opponent, I score this board at {2} "
	     ).format("Human" if self.marker else "Computer",
		     "Human" if enemy else "Computer", score)'''
     
     return score
     
  # Test if a move is valid, then make it or return false.
  def play_single_move(self,local_board,move):
      valid_moves = local_board.valid_moves() 
      if move in valid_moves:
        r, c = move
        local_board.board[r][c] = self.marker
        #print "{0} moves to row {1}, column {2}.".format( 
         # "Player" if self.marker == 1 else "Computer" , r+1 , c+1)
        #local_board.print_board()
	return local_board
      else:
        return False

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
  
   
###############################################################################
# The board makes sense as an object, however, memory footprint will be larger.
###############################################################################
class Game_Board (object):
  
  def __init__(self,rows,columns):
    self.board = []
    self.rows = rows
    self.columns=columns

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

    # Check which cell (if any), we can drop to in a column.
  def check_cell(self, column, index=0):
    # If we are at the last row and it is still empty, just return that
      if (index == len(column)-1):
  	  return index
      if (column[0] is not None): #if top cell full, column is full. 
	  return False
      # If current cell is empty, but the next one down is full, return index.
      if (column[index] is None and column[index+1] is not None):
 	  return index 
      #Otherwise, check the next cell down.
      return self.check_cell(column, index+1)

  # This will play the game forward to D depth from the current board.
  def game_tree(self, player, depth):
     return "" 

  # Get valid moves, and return an array of potential moves.
  def valid_moves(self):
    valid_moves =[] # this will store r/c where valid moves are.
    # For each column, try to drop a token, and return r/c if valid.
    for c in range (0,self.columns):
      column = self.get_column(c);
      r = self.check_cell(column)
      if (r): #if the move is valid add it to the list of valid moves
        valid_moves.append((r,c))
    return valid_moves



   

#TODO replace with a cross-product.
  def print_board (self):
    line = 1
    columns_label = [chr(32)]
    for char in range(ord('A'), (ord('A') + self.columns) ):
	columns_label.append(chr(char))
    print ' '.join(columns_label)
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
    while (i<2 and win==False): 
      if (current_player):
	print "Human's turn."
	#human.minmax(board)
	human.minmax_deep(board, 2, 0)
	score=human.random_move(board)
      else:
	print "Computer's turn."
	#computer.minmax(board)
	human.minmax_deep(board, 2, 0)
        score=computer.random_move(board)
      i+=1
      current_player = int(not current_player)
      if score == True:
	  print "Game Over"
	  win = True

if __name__ == "__main__":
        main()
