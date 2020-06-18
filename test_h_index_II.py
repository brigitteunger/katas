import unittest
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        i = len(citations)-1
        while i >= 0:
            if citations[i] > h:
                h += 1
            else:
                return h
            i -= 1
        return h


class TesthIndex(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_hIndex_five_items(self):
        citations = [0, 1, 3, 5, 6]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 3)

    def test_hIndex_eleven_items(self):
        citations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 3)

    def test_hIndex_five_items_only_zeros(self):
        citations = [0, 0, 0, 0, 0]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 0)

    def test_hIndex_five_items_three_zeros(self):
        citations = [0, 0, 0, 2, 100]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 2)

    def test_hIndex_one_item_five(self):
        citations = [5]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 1)

    def test_hIndex_one_item_zero(self):
        citations = [0]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 0)

    def test_hIndex_one_item_one_hundred(self):
        citations = [100]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 1)

    def test_hIndex_one_item_one(self):
        citations = [1]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 1)

    def test_hIndex_two_items_high(self):
        citations = [11, 15]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 2)

    def test_hIndex_five_items_result_four(self):
        citations = [1, 40, 50, 60, 60]

        actual = self.sol.hIndex(citations)

        self.assertEqual(actual, 4)


if __name__ == "__main__":
    unittest.main()
