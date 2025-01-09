from math import inf as infinte 
from random import choice 

# game board 
board = [[0, 0, 0], 
         [0, 0, 0],
         [0, 0, 0]]

AI = +1
HUMAN = -1

def ai_move():
  print()

def minimax(state, depth, player):
  print

def empty_cells(state):
  cells = []
  for x, rows in enumerate(board):
    for y, cell in enumerate(rows):
      if cell == 0: 
        cells.append([x, y])
  return cells


'''
Checks to see if a specific player has won the game in the given state of the game
:param state: the given state of the game 
:param player: states whether the specified player is the human or AI
:return: True if the specified player wins the game; otherwise, false
'''
def check_win(state, player): 
  possible_wins = [[state[0][0], state[0][1], state[0][2]], 
                   [state[1][0], state[1][1], state[1][2]], 
                   [state[2][0], state[2][1], state[2][2]],
                   [state[0][0], state[1][0], state[2][0]],
                   [state[0][1], state[1][1], state[2][1]],
                   [state[0][2], state[1][2], state[2][2]],
                   [state[0][0], state[1][1], state[2][2]],
                   [state[0][2], state[1][1], state[2][0]]]
  if [player, player, player] in possible_wins:
    return True
  else: 
    return False 

'''
Determines whether the game is over or not
:param state: the given state of the game
:return: True if someone has wins the game; otherwise, false
'''
def game_over(state):
  return check_win(state, HUMAN) or check_win(state, AI) 

def player_move():
  print()

