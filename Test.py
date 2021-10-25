import sys
import unittest
from main import TicTac

class Test(unittest.TestCase):
    def setUp(self):
        self.game = TicTac()
        self.game.SIZE = 3
        self.game.FIRST_NAME = 'Player1'
        self.game.SECOND_NAME = 'Player2'
        self.game.WIN_SIZE = 3
        self.game.board = [['X', '*', '*'], ['0', 'X', 'X'], ['*', '*', 'X']]

    def test_show_board(self):
        text_board = '''   1 2 3
        1 X * *
        2 O X X
        3 * * X'''
        self.assertEqual(self.game.show_board(), print(text_board))

    def test_check_winner(self):
        self.assertEqual(self.game.check_winner(1,[2,2]),sys.exit("Конец игры!"))
if __name__ == '__main__':
    unittest.main()