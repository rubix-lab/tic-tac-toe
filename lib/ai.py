from lib.board import Board
from lib.helpers import POSITIVE_INFINITY, NEGATIVE_INFINITY, PLAYER_ONE, scores, bcolors
from lib.logic import check_victory
from lib.player import Player

class Ai:
  def __init__(self, player, enemy: Player, beginner = False) -> None:
    self.player = player
    self.enemy = enemy
    self.beginner = beginner
  
  def color_str(self, input_str) -> str:
    return f"{bcolors.FAIL if self.beginner else bcolors.OKGREEN}{input_str}{bcolors.ENDC}"

  def __str__(self) -> str:
      return self.color_str("One" if self.player == PLAYER_ONE else "Two")
  
  def symbol(self) -> str:
    return self.color_str("X" if self.beginner else "O")

  def make_move(self, board):
    a = self.best_move(board)
    print("Move", a)
    return a #self.best_move(board)
    # possible_moves = board.possible_moves()
    # return possible_moves[0]

  def best_move(self, board: Board):
    
    best_score = NEGATIVE_INFINITY
    best_move = None

    for move in board.possible_moves():
      minimax_board = Board(board.board.copy()).update(move, self.player)
      print(minimax_board, board.board)
      score = self.minimax(minimax_board, len(board.possible_moves()), True)
      if(score > best_score):
        print(score, best_move)
        best_score = score
        best_move = move
        print(score, best_move)
    
    return best_move
  
  # def minimax(self, board: Board):
  #   # print(board.possible_moves())
  #   # return board.possible_moves()[0]
  #   return 1

  def evaluate(self, board):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if check_victory(self.board, self.player):
        score = +1
    elif check_victory(self.board, self.enemy):
        score = -1
    else:
        score = 0

    return score

def minimax(self, board: Board, depth: int, isMaximizing: bool): 
  result = check_victory(board, self.player) or check_victory(board, self.enemy)
  if(result):
    if(result[1] == self.player):
      score = scores.X if self.beginner else scores.O
    else:
      score = scores.O if self.beginner else scores.X
    
    return score
  
  if(isMaximizing):
    best_score = NEGATIVE_INFINITY
    for move in board.possible_moves():
      minimax_board = Board(board.board.copy()).update(move, self.player)
      score = self.minimax(minimax_board, depth - 1, False)
      if(score > best_score):
        best_score = score
    return best_score
  else:
    best_score = POSITIVE_INFINITY
    for move in board.possible_moves():
      minimax_board = Board(board.board.copy()).update(move, self.player)
      score = self.minimax(minimax_board, depth - 1, True)
      if(score < best_score):
        best_score = score
    return best_score