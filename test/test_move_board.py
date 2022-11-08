import unittest
from src.move_board import *

class CombineTests(unittest.TestCase):
    def test_board_moves_right(self):
        before_and_after_moving = [
           [[[0, 0, 0, 2], [2, 0, 0, 0], [8, 8, 2, 0], [2, 4, 0, 0]], [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 16, 2], [0, 0, 2, 4]]],
           [[[4, 0, 0, 0], [4, 2, 0, 2], [16, 2, 4, 0], [8, 4, 2, 0]], [[0, 0, 0, 4], [0, 0, 4, 4], [0, 16, 2, 4], [0, 8, 4, 2]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_right(before))

    def test_board_moves_left(self):
        before_and_after_moving = [
           [[[0, 2, 8, 4], [0, 4, 16, 8], [0, 0, 2, 4], [0, 0, 0, 2]], [[2, 8, 4, 0], [4, 16, 8, 0], [2, 4, 0, 0], [2, 0, 0, 0]]],
           [[[2, 0, 0, 0], [0, 0, 0, 8], [0, 4, 0, 16], [0, 2, 8, 2]], [[2, 0, 0, 0], [8, 0, 0, 0], [4, 16, 0, 0], [2, 8, 2, 0]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_left(before))
                    
    def test_board_moves_up(self):
        before_and_after_moving = [
           [[[2, 0, 0, 0], [2, 2, 0, 0], [8, 16, 4, 0], [8, 8, 8, 0]], [[4, 2, 4, 0], [16, 16, 8, 0], [0, 8, 0, 0], [0, 0, 0, 0]]],
           [[[0, 0, 0, 0], [2, 4, 0, 0], [4, 16, 2, 0], [4, 4, 32, 2]], [[2, 4, 2, 2], [8, 16, 32, 0], [0, 4, 0, 0], [0, 0, 0, 0]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_up(before))
    
    def test_board_moves_down(self):
        before_and_after_moving = [
           [[[2, 4, 2, 2], [8, 16, 32, 0], [0, 4, 0, 0], [0, 4, 0, 0]], [[0, 0, 0, 0], [0, 4, 0, 0], [2, 16, 2, 0], [8, 8, 32, 2]]],
           [[[2, 8, 4, 2], [8, 32, 16, 0], [8, 2, 0, 0], [0, 2, 0, 0]], [[0, 0, 0, 0], [0, 8, 0, 0], [2, 32, 4, 0], [16, 4, 16, 2]]],
        ]

        for before, after in before_and_after_moving:
                with self.subTest(msg='slide up for starting state', state=before):
                    self.assertEqual(after, move_board_down(before))

if __name__ == '__main__':
    unittest.main()
    
    
