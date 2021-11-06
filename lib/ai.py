from lib.board import Board
from lib.helpers import POSITIVE_INFINITY, NEGATIVE_INFINITY, PLAYER_ONE, scores, bcolors

class Ai:
  def __init__(self, player, beginner = False) -> None:
    self.player = player
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
      score = self.minimax(minimax_board)
      if(score > best_score):
        print(score, best_move)
        best_score = score
        best_move = move
        print(score, best_move)
    
    return best_move
  
  def minimax(self, board: Board):
    # print(board.possible_moves())
    # return board.possible_moves()[0]
    return 1
