from core.helpers import bcolors, PLAYER_ONE

class Player:
  def __init__(self, player, beginner = False) -> None:
    self.player = player
    self.beginner = beginner
  
  def color_str(self, input_str) -> str:
    return f"{bcolors.FAIL if self.beginner else bcolors.OKGREEN}{input_str}{bcolors.ENDC}"

  def __str__(self) -> str:
      return self.color_str("One" if self.player == PLAYER_ONE else "Two")
  
  def symbol(self) -> str:
    return self.color_str("X" if self.beginner else "O")

  def _check_move_input(self, value, possible_moves):
    value = value.rstrip("\n")
    if(value.isdigit() and int(value) in possible_moves):
      return value
    else:
      return None

  def make_move(self, board):
    possible_moves = board.possible_moves()
    player_move_input = input(f"Player {self.__str__()} ({self.symbol()})\n"
                              f"Enter a position {possible_moves}: ")
    tmp_player_move_input = self._check_move_input(player_move_input, possible_moves)
    if(tmp_player_move_input == None):
      return self.make_move(board)
    else:
      return tmp_player_move_input

  