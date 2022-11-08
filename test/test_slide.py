import unittest
from src.slide import *

class SlideTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_row_slides_right(self):
        before_and_after_sliding = [
            [[2, 0, 0, 0], [0, 0, 0, 2]],
            [[2, 2, 0, 2], [0, 2, 2, 2]],
            [[4, 0, 4, 0], [0, 0, 4, 4]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[0, 0, 0, 0], [0, 0, 0, 0]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide right for starting state', state=before):
                self.assertEqual(after, slide_right(before))

    def test_row_slides_left(self):
        before_and_after_sliding = [
            [[2, 0, 2, 0], [2, 2, 0, 0]],
            [[2, 2, 0, 2], [2, 2, 2, 0]],
            [[0, 0, 4, 4], [4, 4, 0, 0]],
            [[8, 2, 4, 8], [8, 2, 4, 8]],
            [[0, 0, 0, 0], [0, 0, 0, 0]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide left for starting state', state=before):
                self.assertEqual(after, slide_left(before))
                
    def test_col_slides_up(self):
        before_and_after_sliding = [
           [[[0], [0], [0], [2]], [[2], [0], [0], [0]]],
           [[[4], [0], [8], [2]], [[4], [8], [2], [0]]],
           [[[0], [4], [0], [2]], [[4], [2], [0], [0]]],
           [[[0], [0], [0], [0]], [[0], [0], [0], [0]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide up for starting state', state=before):
                self.assertEqual(after, slide_up(before))
    
    def test_col_slides_down(self):
        before_and_after_sliding = [
           [[[2], [0], [0], [0]], [[0], [0], [0], [2]]],
           [[[4], [0], [8], [2]], [[0], [4], [8], [2]]],
           [[[0], [4], [0], [2]], [[0], [0], [4], [2]]],
           [[[0], [0], [0], [0]], [[0], [0], [0], [0]]],
           [[[2], [4], [8], [2]], [[2], [4], [8], [2]]],
        ]
        
        for before, after in before_and_after_sliding:
            with self.subTest(msg='slide down for starting state', state=before):
                self.assertEqual(after, slide_down(before))

if __name__ == '__main__':
    unittest.main()