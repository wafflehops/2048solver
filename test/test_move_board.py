import unittest
from src.move_board import *

class CombineTests(unittest.TestCase):
    def test_board_moves_right(self):
        before_and_after_moving = [
           [[[None, None, None, 2], [2, None, None, None], [8, 8, 2, None], [2, 4, None, None]], [[None, None, None, 2], [None, None, None, 2], [None, None, 16, 2], [None, None, 2, 4]]],
           [[[4, None, None, None], [4, 2, None, 2], [16, 2, 4, None], [8, 4, 2, None]], [[None, None, None, 4], [None, None, 4, 4], [None, 16, 2, 4], [None, 8, 4, 2]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_right(before))

    def test_board_moves_left(self):
        before_and_after_moving = [
           [[[None, 2, 8, 4], [None, 4, 16, 8], [None, None, 2, 4], [None, None, None, 2]], [[2, 8, 4, None], [4, 16, 8, None], [2, 4, None, None], [2, None, None, None]]],
           [[[2, None, None, None], [None, None, None, 8], [None, 4, None, 16], [None, 2, 8, 2]], [[2, None, None, None], [8, None, None, None], [4, 16, None, None], [2, 8, 2, None]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_left(before))
                    
    def test_board_moves_up(self):
        before_and_after_moving = [
           [[[2, None, None, None], [2, 2, None, None], [8, 16, 4, None], [8, 8, 8, None]], [[4, 2, 4, None], [16, 16, 8, None], [None, 8, None, None], [None, None, None, None]]],
           [[[None, None, None, None], [2, 4, None, None], [4, 16, 2, None], [4, 4, 32, 2]], [[2, 4, 2, 2], [8, 16, 32, None], [None, 4, None, None], [None, None, None, None]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_up(before))
    
    def test_board_moves_down(self):
        before_and_after_moving = [
           [[[2, 4, 2, 2], [8, 16, 32, None], [None, 4, None, None], [None, 4, None, None]], [[None, None, None, None], [None, 4, None, None], [2, 16, 2, None], [8, 8, 32, 2]]],
           [[[2, 8, 4, 2], [8, 32, 16, None], [8, 2, None, None], [None, 2, None, None]], [[None, None, None, None], [None, 8, None, None], [2, 32, 4, None], [16, 4, 16, 2]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_down(before))

if __name__ == '__main__':
    unittest.main()
    
    
