from core.board import Board
from core.logic import game_over
from core.helpers import NEGATIVE_INFINITY, POSITIVE_INFINITY

class Minimax():
  def __init__(self,  player, enemy) -> None:
    self.player = player
    self.enemy = enemy
  
  def algo(self, board: Board, depth: int, isMaximizing: bool):
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
        score = self.algo(minimax_board, depth + 1, False)
        best_score = max(score, best_score)

      return best_score
    else:
      best_score = POSITIVE_INFINITY
      for move in board.possible_moves():
        minimax_board = Board(board.board.copy())
        minimax_board.update(move, self.enemy)
        score = self.algo(minimax_board, depth + 1, True)
        best_score = min(score, best_score)
      
      return best_score