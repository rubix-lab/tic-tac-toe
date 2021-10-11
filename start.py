# from lib.board import Board
# from lib.game import Game
from lib.config import Config

def start():
  config = Config().setup()
  # game = Game(config)
  # board = Board()
  # print(board)
  # game = Game()
  # print(game.first_player())
  pass


# b = Board([1, "X", "X", 4, 5, "O", "O", 8, 9])
# print(b)
# b.update(1, PLAYER_ONE)
# print(b)
# b.update(9, PLAYER_TWO)
# print(b)


if __name__ == "__main__":
  start()