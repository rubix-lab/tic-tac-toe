class Player:
  def __init__(self, player) -> None:
    self.player = player
  
  def _check_move_input(self, value, possible_moves):
    value = value.rstrip("\n")
    if(value in possible_moves):
      return value
    else:
      return None

  def make_move(self, board):
    possible_moves = board.possible_moves()
    player_move_input = input(f"Enter a position {possible_moves}: ")
    tmp_player_move_input = self._check_move_input(player_move_input, possible_moves)
    if(tmp_player_move_input == None):
      return self.make_move()
    else:
      return tmp_player_move_input

  