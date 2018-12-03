import sys
sys.path.append('.')
import pandas as pd
import day3
from day3 import overlap
import unittest

class TestDay3(unittest.TestCase):
    def test_clotharea(self):
        testinput = {'index': ['#1','#2','#3'], 'atsign': ['@','@','@'], 'coordinates': ['1,3','3,1', '5,5'], 'area': ['4x4','4x4','2x2']}
        testinput = pd.DataFrame(testinput)

        area = 10
        testcloth = pd.DataFrame('.', index=[x for x in range(0,area)], columns=[x for x in range(0,area)])

        self.assertEqual(4, day3.overlap(testinput))


if __name__ == '__main__':
    unittest.main()
