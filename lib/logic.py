from lib.board import Board
from lib.helpers import PLAYER_ONE
from lib.player import Player

def check_winner(arr, player):
  player_symbol = "X" if player.player == PLAYER_ONE else "O"
  if(arr.count(player_symbol) == 3):
    return player.player
  else:
    return None
  

def check_victory(board: Board, player: Player):
  for row_pos in board.rows_pos():
    print(row_pos)# board.board[pos])
    row = [board.board[pos] for pos in row_pos]
    winner = check_winner(row, player)
    if winner:
      return (row_pos, winner) 

  for col_pos in board.cols_pos():
    col = [board.board[pos] for pos in col_pos]
    winner = check_winner(col, player)
    if winner:
      return (col_pos, winner)

  for diagonal_pos in board.diagonals_pos():
    diagonal = [board.board[pos] for pos in diagonal_pos]
    winner = check_winner(diagonal, player)
    if winner:
      return (diagonal_pos, winner) 
  
  return None