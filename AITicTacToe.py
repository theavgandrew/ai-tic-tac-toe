from math import inf as infinity 
from random import choice 

# game board 
board = [
  [0, 0, 0], 
  [0, 0, 0],
  [0, 0, 0],
] 

AI = +1
HUMAN = -1


'''
function sets the move on the board given the specifed x and y coordinates and player
:param x: x coordinate on the board
:param y: y coordinate on the board
:param player: specified player whose move the function is setting
:return: True if setting the move was successful; otherwise, False
'''
def set_move(x, y, player):
  if board[x][y] == 0: # if cell at [x, y] is empty
    board[x][y] = player
    return True
  else: 
    return False


'''
function used to determine the static value of the state
:param state: the given state of the game
:return: the static value of the state of the game 
'''
def evaluate(state):
  if check_win(state, AI):
    return +1
  elif check_win(state, HUMAN): 
    return -1
  else: 
    return 0

'''

'''
def minimax(state, depth, player):
  if depth == 0 or check_win(state, player) == True: 
    return [-1, -1, evaluate(state)]
  
  if player == AI: 
    best_val = [-1, -1, -infinity]
  else: 
    best_val = [-1, -1, infinity] 

  cells = empty_cells(state) 

  for cell in cells: # checking all children (aka possible moves) 
    x, y = cell[0], cell[1]
    state[x][y] = player
    curr_val = minimax(state, depth - 1, -player) 
    state[x][y] = 0
    curr_val[0], curr_val[1] = x, y

    if player == AI: 
      if curr_val[2] > best_val[2]: # ensures max value 
        best_val = curr_val
    elif player == HUMAN: 
      if curr_val[2] < best_val[2]: # ensures min value
        best_val = curr_val

  return best_val


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
:return: True if the specified player wins the game; otherwise, False
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
  
def ai_move(c_symb, h_symb):
  depth = len(empty_cells(board))
  if depth == 0 or game_over(board): 
    return 
  
  clear()
  print(f"It's the AI's turn [{c_symb}]") 
  print_board(board, c_symb, h_symb)

  if depth == 9:
    x = choice([0, 1, 2])
    y = choice([0, 1, 2]) 
  else:
    move = minimax(board, depth, AI)
    x, y = move[0], move[1]

  return set_move(x, y, AI)

def human_move(c_symb, h_symb): 
  depth = len(empty_cells(board))
  if depth == 0 or game_over(board): 
    return 
  
  # valid moves
  move = -1
  possible_moves = {
    1: [0, 0], 2: [0, 1], 3: [0, 2], 
    4: [1, 0], 5: [1, 1], 6: [1, 2], 
    7: [2, 0], 8: [2, 1], 9: [2, 2], 
  }

  clear()
  print(f"It's your turn [{h_symb}]")
  print_board(c_symb, h_symb)

  while not 1 > move > 9: 
    try:
      move = int(input("Input your move (1-9): "))
      coord = possible_moves[move] 
      can_move = set_move(coord[0], coord[1], HUMAN)

      if not can_move: 
        print("Invalid nove. Try again.") 
        move = -1
    except (EOFError, KeyboardInterrupt):
      # if user interrupts the program
      print("Good game! Bye")
      exit()
    except (KeyError, ValueError): 
      # if user inputs something that's not in dictionary
      # or not a number
      print("Horribly invalid move. Try again.")






def clear():
  print()
def print_board(state, c_symb, h_symb): 
  print()

'''
Determines whether the game is over or not
:param state: the given state of the game
:return: True if someone has wins the game; otherwise, False
'''
def game_over(state):
  return check_win(state, HUMAN) or check_win(state, AI) 

def player_move():
  print()

def play_game():
  print

if __name__ == '__main__': 
  play_game()

