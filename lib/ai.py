class Ai:
  def __init__(self) -> None:
    pass

  def make_move(self, board):
    possible_moves = board.possible_moves()
    return possible_moves[0]