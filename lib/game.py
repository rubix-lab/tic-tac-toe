import sys
from typing import TYPE_CHECKING
from lib import board
if TYPE_CHECKING:
  import start
from lib.board import Board
from lib.config import Config
from lib.helpers import PLAYER_ONE, PLAYER_TWO, PASS_AND_PLAY, clear
from lib.logic import check_victory
from lib.player import Player
from lib.ai import Ai

restart_or_exit_input = lambda: input(f"Restart or exit game: \n"
                                      f"- [1] Restart (keep config) \n"
                                      f"- [2] New game (new config) \n"
                                      f"- [3] Exit \n"
                                      f"Enter number[1/2/3]: ")

class Game:
  def __init__(self, config: Config, board: Board) -> None:
    self.config = config
    self.board = board
    self.first_player = Player(self.config.beginner) if self.config.mode == PASS_AND_PLAY else Ai(self.config.beginner)
    not_beginner = PLAYER_ONE if self.config.beginner == PLAYER_ONE else PLAYER_TWO
    self.second_player = Player(not_beginner) if self.config.mode == PASS_AND_PLAY else Ai(not_beginner)

  def game_info(self, winner):
    print(f"{winner.color_str()} won!\n")
    pass

  def _check_restart_or_exit_input(self, value):
    value = value.rstrip("\n")
    if(value.isdigit() and int(value) == 1):
      return value
    elif(value.isdigit() and int(value) == 2):
      return value
    else:
      return None

  def restart_or_exit(self):
    restart_or_exit_value = restart_or_exit_input()
    tmp_restart_or_exit = self._check_restart_or_exit_input(restart_or_exit_value)
    if(tmp_restart_or_exit == None):
      return self.restart_or_exit()
    elif(tmp_restart_or_exit == 1):
      new_config = self.config
      new_config.get_beginner()
      new_config.config_info()
      new_config.start()
      clear()
      start.new_game(new_config)
    elif(tmp_restart_or_exit == 2):
      start.new_game()
    else:
      return sys.exit()

  def _player_move_cycle(self, player):
    player_move = player.make_move(self.board)
    self.board.update(player_move, player)
    print(self.board)
    possible_victory = check_victory(self.board, player)

    if(possible_victory):
      self.victory = possible_victory
      self.game_info(self.victory[1])
      self.board.display_victory(self.victory[0]) # victory[0] is the position e. g. [1, 2, 3]
      self.restart_or_exit()

  def loop(self):
    if(self.board.possible_moves):
      self._player_move_cycle(self.first_player)
      self._player_move_cycle(self.second_player)
    else:
      print("No winner!\n")
      self.restart_or_exit()

    
  def start(self):
    self.loop()


