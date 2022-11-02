import unittest
from src.combine import *

class CombineTests(unittest.TestCase):
    def test_combine_right(self):
        before_and_after_combining = [
            [[None, None, 2, 2], [None, None, None, 4]],
            [[2, 2, 2, 2], [None, 4, None, 4]],
            [[None, 4, 4, 2], [None, None, 8, 2]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[None, 2, 4, 4], [None, 2, None, 8]],
            [[None, 2, 2, 8], [None, None, 4, 8]],
            [[None, None, None, None], [None, None, None, None]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine right for starting state', state=before):
                self.assertEqual(after, combine_right(before))
        
    def test_combine_left(self):
        before_and_after_combining = [
            [[2, 2, None, None], [4, None, None, None]],
            [[2, 2, 2, 2], [4, None, 4, None]],
            [[2, 4, 4, None], [2, 8, None, None]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[4, 4, 2, None], [8, None, 2, None]],
            [[8, 2, 2, None], [8, 4, None, None]],
            [[None, None, None, None], [None, None, None, None]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine left for starting state', state=before):
                self.assertEqual(after, combine_left(before))
    
    def test_col_combines_up(self):
        before_and_after_combining = [
           [[[2], [2], [None], [None]], [[4], [None], [None], [None]]],
           [[[8], [8], [8], [2]], [[16], [None], [8], [2]]],
           [[[2], [2], [2], [2]], [[4], [None], [4], [None]]],
           [[[None], [None], [None], [None]], [[None], [None], [None], [None]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
           [[[2], [4], [4], [None]], [[2], [8], [None], [None]]],
           [[[4], [4], [2], [None]], [[8], [None], [2], [None]]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine up for starting state', state=before):
                self.assertEqual(after, combine_up(before))
                
    def test_col_combines_down(self):
        before_and_after_combining = [
           [[[None], [None], [2], [2]], [[None], [None], [None], [4]]],
           [[[2], [8], [8], [8]], [[2], [8], [None], [16]]],
           [[[2], [2], [2], [2]], [[None], [4], [None], [4]]],
           [[[None], [None], [None], [None]], [[None], [None], [None], [None]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
           [[[None], [4], [4], [2]], [[None], [None], [8], [2]]],
           [[[None], [2], [4], [4]], [[None], [2], [None], [8]]],
        ]
        
        for before, after in before_and_after_combining:
            with self.subTest(msg='combine down for starting state', state=before):
                self.assertEqual(after, combine_down(before))
                
if __name__ == '__main__':
    unittest.main()