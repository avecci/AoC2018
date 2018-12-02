import sys
sys.path.append('.')
import day2
from day2 import checksum
from day2 import findboxes
import unittest

class TestDay2(unittest.TestCase):
    def test_checksum(self):
        ids = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]
        self.assertEqual(12, day2.checksum(ids))

    def test_findboxes(self):
        ids2 = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]
        self.assertEqual('fgij', day2.findboxes(ids2))

if __name__ == '__main__':
    unittest.main()
