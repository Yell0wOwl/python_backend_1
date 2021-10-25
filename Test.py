import unittest
from unittest.mock import MagicMock
from main import TicTac


class Test(unittest.TestCase):
    def setUp(self):
        self.game = TicTac()
        self.game.SIZE = 3
        self.game.FIRST_NAME = 'Player1'
        self.game.SECOND_NAME = 'Player2'
        self.game.WIN_SIZE = 3
        self.game.board = [['X', '*', '*'], ['O', 'X', 'X'], ['*', '*', 'X']]

    def test_show_board(self):
        text_board = '''   1 2 3
        1 X * *
        2 O X X
        3 * * X'''
        self.assertEqual(self.game.show_board(), print(text_board))

    def test_check_winner(self):
        self.assertEqual(self.game.check_winner(0, [2, 2]), True)

    def test_turn(self):
        self.game.board = [['X', '*', '*'], ['*', '*', 'X'], ['*', '*', 'X']]
        true_board = [['X', '*', '*'], ['*', 'X', 'X'], ['*', '*', 'X']]
        self.game.get_coordinates = MagicMock(return_value=[1, 1])
        self.game.turn_counter = 3
        self.game.turn(0)
        self.assertEqual(self.game.board, true_board)


if __name__ == '__main__':
    unittest.main()
