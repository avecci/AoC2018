import sys
sys.path.append('.')

import day1
from day1 import day1_part1
from day1 import day1_part2
import unittest

class TestDay1(unittest.TestCase):

    def testsum(self):
        cases = [
            ([1, -2, 3, 1], 3),
            ([+1, +1, 1], 3),
            ([-1, -2, -3], -6)
            ]

        for i in cases:
            self.assertEqual(i[1], day1.day1_part1(i[0]))

    def test_first_repeat(self):
        cases = [
                ([3, 3, 4, -2, -4], 10),
                ([-6, 3, 8, 5, -6], 5),
                ([7, 7, -2, -7, -4], 14)
                ]

        for i in cases:
            self.assertEqual(i[1], day1.day1_part2(i[0]))

if __name__ == '__main__':
    unittest.main()
