from typing import List
from helpers import bcolors, BOARD_SPACE, PLAYER_ONE

class Board:
  def __init__(self, board_list = None) -> None:
    if board_list:
      self.board = board_list
    else:
      self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

  
  def update(self, pos, player) -> List:
    self.board[pos - 1] = "X" if player == PLAYER_ONE else "O"
    return self.board

# b = Board([1, "X", "X", 4, 5, "O", "O", 8, 9])
# print(b)
# b.update(1, PLAYER_ONE)
# print(b)