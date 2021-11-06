import sys
from lib.board import Board
from lib.config import Config
from lib.helpers import PLAYER_ONE, PLAYER_TWO, PASS_AND_PLAY, bcolors, clear
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

    # beginner = self.config.beginner
    # not_beginner = PLAYER_TWO if self.config.beginner == PLAYER_ONE else PLAYER_ONE

    # self.first_player = Player(PLAYER_ONE, True) if beginner == PLAYER_ONE else (Player(PLAYER_TWO, True) if self.config.mode == PASS_AND_PLAY else Ai(PLAYER_TWO, True))
    # self.second_player = Player(PLAYER_TWO) if beginner == PLAYER_ONE else (Player(PLAYER_ONE) if self.config.mode == PASS_AND_PLAY else Ai(PLAYER_ONE))
    #######################################################
    ###################### Fix This  ######################
    #######################################################

    # self.first_player =  Player(beginner, True) if self.config.mode == PASS_AND_PLAY else Ai(beginner, True)
    # self.second_player = Player(PLAYER_ONE, True) if self.beginner == PLAYER_ONE else (Player(PLAYER_TWO, True) if self.config.mode == PASS_AND_PLAY else Ai(PLAYER_TWO))
    # self.first_player = Player(PLAYER_ONE, True) if self.config.beginner == PLAYER_ONE else (Player(PLAYER_TWO, True) if self.config.mode == PASS_AND_PLAY else Ai(PLAYER_TWO, True))
    # self.second_player = Player(not_beginner) if self.config.mode == PASS_AND_PLAY else Ai(not_beginner)
    # if(self.config.mode == PASS_AND_PLAY):
    #   self.first_player = Player(self.config.beginner, True)
    #   self.second_player = Player(not_beginner)
    # else:
    #   self.first_player = 

    # Player(PLAYER_ONE, True) if self.beginner == PLAYER_ONE else (Player(PLAYER_TWO, True) if self.mode == PASS_AND_PLAY else Player(PLAYER_ONE, True))


    # self.first_player = Player(self.config.beginner, True) if self.config.mode == PASS_AND_PLAY else Ai(self.config.beginner, True)
    # not_beginner = PLAYER_TWO if self.config.beginner == PLAYER_ONE else PLAYER_ONE
    # self.second_player = Player(not_beginner) if self.config.mode == PASS_AND_PLAY else Ai(not_beginner)
    self.victory = None

  def game_info(self, winner):
    print(f"Player {self.first_player if winner == self.first_player else self.second_player} won!")
    pass

  def _check_restart_or_exit_input(self, value):
    value = value.rstrip("\n")
    if(value.isdigit() and int(value) == 1):
      return 1
    elif(value.isdigit() and int(value) == 2):
      return 2
    elif(value.isdigit() and int(value) == 3):
      return 3
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
      new_game(new_config)
    elif(tmp_restart_or_exit == 2):
      clear()
      new_game()
    elif(tmp_restart_or_exit == 3):
      return sys.exit()
    else:
      self.restart_or_exit()

  def _player_move_cycle(self, player):
    player_move = player.make_move(self.board)
    self.board.update(player_move, player.player)
    print(self.board)
    possible_victory = check_victory(self.board, player)

    if(possible_victory):
      self.victory = possible_victory
      self.game_info(self.victory[1])
      print(self.board.victory_str(self.victory[0])) # victory[0] is the position e. g. [1, 2, 3]
      self.restart_or_exit()

  def tie(self):
    print(f"{bcolors.WARNING}Tie!{bcolors.ENDC}\n")
    self.restart_or_exit()

  def loop(self):
    print(self.board)
    while(not self.victory): 
      self._player_move_cycle(self.first_player) if len(self.board.possible_moves()) > 1 else self.tie()
      self._player_move_cycle(self.second_player) if len(self.board.possible_moves()) > 1 else self.tie()

    
  def start(self):
    self.loop()

def new_game(args_config: Config = None, args_board: Board = None):
  config = args_config if args_config else Config().setup()
  board = args_board if args_board else Board()
  Game(config, board).start()