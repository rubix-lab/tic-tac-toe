from sys import base_exec_prefix
from lib.board import Board
from lib.helpers import PLAYER_ONE, PLAYER_TWO
from lib.player import Player

def check_winner(arr, player):
  try:
    player_symbol = "X" if player.player == PLAYER_ONE else "O"
  except:
    player_symbol = "X" if player == PLAYER_ONE else "O"

  if(arr.count(player_symbol) == 3):
    return player
  else:
    return None
  

def check_victory(board: Board, player: Player):
  for row_pos in board.rows_pos():
    row = [board.board[pos - 1] for pos in row_pos]
    winner = check_winner(row, player)
    if winner:
      return (row_pos, winner) 

  for col_pos in board.cols_pos():
    col = [board.board[pos - 1] for pos in col_pos]
    winner = check_winner(col, player)
    if winner:
      return (col_pos, winner)

  for diagonal_pos in board.diagonals_pos():
    diagonal = [board.board[pos - 1] for pos in diagonal_pos]
    winner = check_winner(diagonal, player)
    if winner:
      return (diagonal_pos, winner) 
  
  return None

def game_over(board: Board):
  for row in board.rows():
    if(row.count("X") == 3):
      return PLAYER_ONE
    if(row.count("O") == 3):
      return PLAYER_TWO

  for col in board.cols():
    if(col.count("X") == 3):
      return PLAYER_ONE
    if(col.count("O") == 3):
      return PLAYER_TWO

  for diagonal in board.diagonals():
    if(diagonal.count("X") == 3):
      return PLAYER_ONE
    if(diagonal.count("O") == 3):
      return PLAYER_TWO
  
  return True if len(board.possible_moves()) == 0 else False