from lib.board import Board
from lib.game import Game
from lib.config import Config

def start():
  config = Config().setup()
  board = Board()
  game = Game(config, board).start()

if __name__ == "__main__":
  start()