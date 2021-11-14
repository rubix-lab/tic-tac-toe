from lib import player
from lib.board import Board
from lib.helpers import POSITIVE_INFINITY, NEGATIVE_INFINITY, PLAYER_ONE, scores, bcolors
from lib.logic import game_over

class Ai:
  def __init__(self, player, enemy, beginner = False) -> None:
    self.player = player
    self.enemy = enemy
    self.beginner = beginner
  
  def color_str(self, input_str) -> str:
    return f"{bcolors.FAIL if self.beginner else bcolors.OKGREEN}{input_str}{bcolors.ENDC}"

  def __str__(self) -> str:
      return self.color_str("One" if self.player == PLAYER_ONE else "Two")
  
  def symbol(self) -> str:
    return self.color_str("X" if self.beginner else "O")

  def make_move(self, board: Board):
    return self.best_move(board)

  def best_move(self, board: Board):
    best_score = NEGATIVE_INFINITY
    best_move = None
    for move in board.possible_moves():
      new_board = Board(board.board.copy())
      new_board.update(move, self.player)
      score = self.minimax(new_board, 0, False)
      if(score > best_score):
        best_score = score
        best_move = move
    
    return best_move

  
  def minimax(self, board: Board, depth: int, isMaximizing: bool):
    result = game_over(board)
    if(result):
      if(result == self.player):
        return 1
      elif(result == self.enemy):
        return -1
      else:
        return 0

    if(isMaximizing):
      best_score = NEGATIVE_INFINITY
      for move in board.possible_moves():
        minimax_board = Board(board.board.copy())
        minimax_board.update(move, self.player)
        score = self.minimax(minimax_board, depth + 1, False)
        best_score = max(score, best_score)

      return best_score
    else:
      best_score = POSITIVE_INFINITY
      for move in board.possible_moves():
        minimax_board = Board(board.board.copy())
        minimax_board.update(move, self.enemy)
        score = self.minimax(minimax_board, depth + 1, True)
        best_score = min(score, best_score)

      return best_score