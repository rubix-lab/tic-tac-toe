import unittest
from core.board import Board

class TestBoardMethods(unittest.TestCase):
  def test_init_default_board(self):
    board = Board()
    self.assertIs(type(board), Board)

  def test_init_custom_board(self):
    board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9])
    self.assertIs(type(board), Board)
  
  def test_init_invalid_board(self):
    invalid_board = [1, "a", 10, "g", (1, 2)]
    self.assertRaises(ValueError, lambda: Board(invalid_board))

  def test_print_board(self):
    board = Board()
    self.assertEqual("\n 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n", board.__str__())

  def test_possible_moves(self):
    pass
  
  def test_update(self):
    pass

  def test_print_victory(self):
    pass

  def test_rows(self):
    pass

  def test_cols(self):
    pass

  def test_diagonals(self):
    pass

  def test_rows_pos(self):
    pass

  def test_cols_pos(self):
    pass

  def test_diagonals_pos(self):
    pass

if __name__ == '__main__':
    unittest.main()