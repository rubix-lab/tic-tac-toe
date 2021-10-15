from lib.board import Board
from lib.game import Game
from lib.config import Config

def new_game(args_config: Config = None, args_board: Board = None):
  config = args_config if args_config else Config().setup()
  board = args_board if args_board else Board()
  Game(config, board).start()

if __name__ == "__main__":
  new_game()