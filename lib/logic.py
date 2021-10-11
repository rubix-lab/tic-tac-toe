from lib.board import Board
from lib.helpers import PLAYER_ONE, PLAYER_TWO

def check_count(arr):
    if(arr.count("X") == 3):
      return PLAYER_ONE
    elif(arr.count("O") == 3):
      return PLAYER_TWO
    else:
      return None
  

def check_winner(board: Board):
  for row in board.rows():
    count_res = check_count(row)
    if count_res:
      return (count_res, row) 

  for col in board.cols():
    count_res = check_count(col)
    if count_res:
      return (count_res, col)

  for diagonal in board.diagonals():
    count_res = check_count(diagonal)
    if count_res:
      return (count_res, diagonal) 
  
  return None