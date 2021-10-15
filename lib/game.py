import random
from lib.board import Board
from lib.config import Config
from lib.helpers import PLAYER_ONE, PLAYER_TWO, PASS_AND_PLAY
from lib.logic import check_winner
from lib.player import Player
from lib.ai import Ai

class Game:
  def __init__(self, config: Config, board: Board) -> None:
    self.config = config
    self.board = board
    self.first_player = Player(self.config.beginner) if self.config.mode == PASS_AND_PLAY else Ai(self.config.beginner)
    not_beginner = PLAYER_ONE if self.config.beginner == PLAYER_ONE else PLAYER_TWO
    self.second_player = Player(not_beginner) if self.config.mode == PASS_AND_PLAY else Ai(not_beginner)

  def game_info(self):
    print(f"")
    pass

  def restart_or_exit(self):
    pass

  def _player_move_cycle(self, player):
    player_move = player.make_move(self.board)
    board.update(player_move)
    possible_victory = board.check_victory(player)

    if(possible_victory):
      self.victory = possible_victory
      self.board.display_victory(self.victory)
      self.game_info()
      self.restart_or_exit()

  def loop(self):
    self._player_move_cycle(self.first_player)
    self._player_move_cycle(self.second_player)
    
  def start(self):
    self.loop()


