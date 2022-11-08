import unittest
from src.combine import *

class CombineTests(unittest.TestCase):
    def test_combine_right(self):
        before_and_after_combining = [
            [[0, 0, 2, 2], [0, 0, 0, 4]],
            [[2, 2, 2, 2], [0, 4, 0, 4]],
            [[0, 4, 4, 2], [0, 0, 8, 2]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[0, 2, 4, 4], [0, 2, 0, 8]],
            [[0, 2, 2, 8], [0, 0, 4, 8]],
            [[0, 0, 0, 0], [0, 0, 0, 0]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine right for starting state', state=before):
                self.assertEqual(after, combine_right(before))
        
    def test_combine_left(self):
        before_and_after_combining = [
            [[2, 2, 0, 0], [4, 0, 0, 0]],
            [[2, 2, 2, 2], [4, 0, 4, 0]],
            [[2, 4, 4, 0], [2, 8, 0, 0]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[4, 4, 2, 0], [8, 0, 2, 0]],
            [[8, 2, 2, 0], [8, 4, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine left for starting state', state=before):
                self.assertEqual(after, combine_left(before))
    
    def test_col_combines_up(self):
        before_and_after_combining = [
           [[[2], [2], [0], [0]], [[4], [0], [0], [0]]],
           [[[8], [8], [8], [2]], [[16], [0], [8], [2]]],
           [[[2], [2], [2], [2]], [[4], [0], [4], [0]]],
           [[[0], [0], [0], [0]], [[0], [0], [0], [0]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
           [[[2], [4], [4], [0]], [[2], [8], [0], [0]]],
           [[[4], [4], [2], [0]], [[8], [0], [2], [0]]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine up for starting state', state=before):
                self.assertEqual(after, combine_up(before))
                
    def test_col_combines_down(self):
        before_and_after_combining = [
           [[[0], [0], [2], [2]], [[0], [0], [0], [4]]],
           [[[2], [8], [8], [8]], [[2], [8], [0], [16]]],
           [[[2], [2], [2], [2]], [[0], [4], [0], [4]]],
           [[[0], [0], [0], [0]], [[0], [0], [0], [0]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
           [[[0], [4], [4], [2]], [[0], [0], [8], [2]]],
           [[[0], [2], [4], [4]], [[0], [2], [0], [8]]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine down for starting state', state=before):
                self.assertEqual(after, combine_down(before))
                
if __name__ == '__main__':
    unittest.main()