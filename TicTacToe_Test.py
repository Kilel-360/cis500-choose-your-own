
import unittest
from TicTacToe import TicTacToe

class TestTicTacToeStudentTest(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_make_move_valid(self):
        self.tic_tac_toe.make_move(0, 0)
        self.assertEqual(self.tic_tac_toe.board[0][0], 'X')
        self.assertEqual(self.tic_tac_toe.current_player, 'O')

    def test_make_move_invalid(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(0, 0)  # Attempting to make a move in the same position
        self.assertEqual(self.tic_tac_toe.board[0][0], 'X')
        self.assertEqual(self.tic_tac_toe.current_player, 'O')

    def test_check_winner_row(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(0, 1)
        self.tic_tac_toe.make_move(0, 2)
        self.assertFalse(self.tic_tac_toe.is_game_over())
        self.assertEqual(self.tic_tac_toe.winner, None)

    def test_check_winner_column(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(1, 0)
        self.tic_tac_toe.make_move(2, 0)
        self.assertFalse(self.tic_tac_toe.is_game_over())
        self.assertEqual(self.tic_tac_toe.winner, None)

    def test_check_winner_diagonal(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(1, 1)
        self.tic_tac_toe.make_move(2, 2)
        self.assertFalse(self.tic_tac_toe.is_game_over())
        self.assertEqual(self.tic_tac_toe.winner, None)

    def test_check_winner_tie(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(0, 1)
        self.tic_tac_toe.make_move(0, 2)
        self.tic_tac_toe.make_move(1, 0)
        self.tic_tac_toe.make_move(1, 1)
        self.tic_tac_toe.make_move(1, 2)
        self.tic_tac_toe.make_move(2, 0)
        self.tic_tac_toe.make_move(2, 1)
        self.tic_tac_toe.make_move(2, 2)
        self.assertTrue(self.tic_tac_toe.is_game_over())
        self.assertEqual(self.tic_tac_toe.winner, 'X')
        self.assertFalse(self.tic_tac_toe.is_tie())

    def test_reset_game(self):
        self.tic_tac_toe.make_move(0, 0)
        self.tic_tac_toe.make_move(0, 1)
        self.tic_tac_toe.reset_game()
        self.assertEqual(self.tic_tac_toe.board, [[' ' for _ in range(3)] for _ in range(3)])
        self.assertEqual(self.tic_tac_toe.current_player, 'X')
        self.assertIsNone(self.tic_tac_toe.winner)
        self.assertFalse(self.tic_tac_toe.is_game_over())

if __name__ == '__main__':
    unittest.main()