from core import player
from core.board import Board
from core.helpers import NEGATIVE_INFINITY, PLAYER_ONE, bcolors
from core.minimax import Minimax

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
    minimax = Minimax(self.player, self.enemy)
    best_score = NEGATIVE_INFINITY
    best_move = None
    for move in board.possible_moves():
      new_board = Board(board.board.copy())
      new_board.update(move, self.player)
      score = minimax.algo(new_board, 0, False)
      if(score > best_score):
        best_score = score
        best_move = move
    
    return best_move

  
