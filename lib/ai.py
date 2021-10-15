class Ai:
  def __init__(self) -> None:
    pass

  def make_move(self, board):
    possible_moves = board.possible_moves()
    return possible_moves[0]
    # player_move_input = input(f"Enter a position {possible_moves}: ")
    # tmp_player_move_input = self._check_move_input(player_move_input, possible_moves)
    # if(tmp_player_move_input == None):
    #   return self.make_move()
    # else:
    #   return tmp_player_move_input

  