from typing import List
from lib.helpers import DEFAULT_BOARD, bcolors, BOARD_SPACE, PLAYER_ONE

check_player_val = lambda val: val != "O" and val != "X"

class Board:
  def __init__(self, board_list = None) -> None:

    if board_list:
      check_board_list = [True for x in board_list if (isinstance(x, int) and 1 <= x <= 9) or (x == "X" or x == "O")]
      if(len(check_board_list) == 9):
        self.board = board_list
      else:
        raise ValueError(f"Board consists of 9 values consisting of intengers 1-9, 'X' and 'O', got: {board_list}")
    else:
      self.board = DEFAULT_BOARD.copy()

  def __str__(self) -> str:
    """
     1 | X | X 
    ---+---+---
     4 | 5 | O 
    ---+---+---
     O | 8 | 9 
    """
    board_str = "\n"
    for index, char in enumerate(self.board):
      if(char == "X"):
        char = f" {bcolors.FAIL}{char}{bcolors.ENDC} "
      elif(char == "O"):
        char = f" {bcolors.OKGREEN}{char}{bcolors.ENDC} "
      else:
        char = f" {char} "

      if((index + 1) % 3 == 0):
        board_str = f"{board_str}{char}\n"
        if(index != 8):
          board_str = f"{board_str}{BOARD_SPACE}"
      else:
        char = f"{char}|"
        board_str = f"{board_str}{char}"
  
    return board_str

  def possible_moves(self) -> List:
    return [val for val in self.board if check_player_val(val)]
  
  def update(self, pos, player) -> List:
    self.board[int(pos) - 1] = "X" if player == PLAYER_ONE else "O"
    return self.board

  def victory_str(self, pos):
    board_str = "\n"
    for index, char in enumerate(self.board):
      if(pos.count(index + 1) != True):
        char = f" {bcolors.OKBLUE}{char}{bcolors.ENDC} "
      else:
        if(char == "X"):
          char = f" {bcolors.FAIL}{char}{bcolors.ENDC} "
        elif(char == "O"):
          char = f" {bcolors.OKGREEN}{char}{bcolors.ENDC} "
        else:
          char = f" {char} "

      if((index + 1) % 3 == 0):
        board_str = f"{board_str}{char}\n"
        if(index != 8):
          board_str = f"{board_str}{BOARD_SPACE}"
      else:
        char = f"{char}|"
        board_str = f"{board_str}{char}"
  
    return board_str

  def rows(self):
    yield self.board[0:3]
    yield self.board[3:6]
    yield self.board[6:9]

  def cols(self):
    yield self.board[0:9:3]
    yield self.board[1:9:3]
    yield self.board[2:9:3]

  def diagonals(self):
    yield [self.board[0], self.board[4], self.board[8]]
    yield [self.board[2], self.board[4], self.board[6]]

  def rows_pos(self):
    yield DEFAULT_BOARD[0:3]
    yield DEFAULT_BOARD[3:6]
    yield DEFAULT_BOARD[6:9]

  def cols_pos(self):
    yield DEFAULT_BOARD[0:9:3]
    yield DEFAULT_BOARD[1:9:3]
    yield DEFAULT_BOARD[2:9:3]

  def diagonals_pos(self):
    yield [DEFAULT_BOARD[0], DEFAULT_BOARD[4], DEFAULT_BOARD[8]]
    yield [DEFAULT_BOARD[2], DEFAULT_BOARD[4], DEFAULT_BOARD[6]]

if __name__ == "__main__":
  board = Board()
  print(board)