import unittest
from src.slide import *

class SlideTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_row_slides_right(self):
        before_and_after_sliding = [
            [[2, None, None, None], [None, None, None, 2]],
            [[2, 2, None, 2], [None, 2, 2, 2]],
            [[4, None, 4, None], [None, None, 4, 4]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[None, None, None, None], [None, None, None, None]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide right for starting state', state=before):
                self.assertEqual(after, slide_right(before))

    def test_row_slides_left(self):
        before_and_after_sliding = [
            [[2, None, 2, None], [2, 2, None, None]],
            [[2, 2, None, 2], [2, 2, 2, None]],
            [[None, None, 4, 4], [4, 4, None, None]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[None, None, None, None], [None, None, None, None]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide left for starting state', state=before):
                self.assertEqual(after, slide_left(before))
                
    def test_col_slides_up(self):
        before_and_after_sliding = [
           [[[None], [None], [None], [2]], [[2], [None], [None], [None]]],
           [[[4], [None], [8], [2]], [[4], [8], [2], [None]]],
           [[[None], [4], [None], [2]], [[4], [2], [None], [None]]],
           [[[None], [None], [None], [None]], [[None], [None], [None], [None]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide up for starting state', state=before):
                self.assertEqual(after, slide_up(before))
    
    def test_col_slides_down(self):
        before_and_after_sliding = [
           [[[2], [None], [None], [None]], [[None], [None], [None], [2]]],
           [[[4], [None], [8], [2]], [[None], [4], [8], [2]]],
           [[[None], [4], [None], [2]], [[None], [None], [4], [2]]],
           [[[None], [None], [None], [None]], [[None], [None], [None], [None]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide down for starting state', state=before):
                self.assertEqual(after, slide_down(before))

if __name__ == '__main__':
    unittest.main()