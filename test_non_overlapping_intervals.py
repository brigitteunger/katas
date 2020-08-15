import unittest
from typing import List
from data_non_overlapping_intervals import intervals_2, intervals_3


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: (interval[1], interval[1]-interval[0]))
        min_erase = 0
        left_end = intervals[0][0]-1
        for interval in intervals:
            if left_end > interval[0]:
                min_erase += 1
            else:
                left_end = interval[1]
        return min_erase


class TestEraseOverlapIntervals(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testOverlap_1(self):
        intervals = [[1, 2], [3, 4],  [2, 3], [1, 3]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 1)

    def testOverlap_2(self):
        intervals = [[1, 2], [1, 2], [1, 2]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 2)

    def testOverlap_3(self):
        intervals = [[1, 2], [2, 3]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 0)

    def testOverlap_4(self):
        intervals = [[2, 5], [3, 4], [5, 6]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 1)

    def testOverlap_5(self):
        intervals = []

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 0)

    def testOverlap_6(self):
        intervals = [[1, 2], [2, 5], [3, 4], [5, 6]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 1)

    def testOverlap_7(self):
        intervals = [[3, 7], [4, 8]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 1)

    def testOverlap_8(self):
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 2)

    def testOverlap_9(self):
        intervals = [[1, 2], [1, 2], [1, 2], [1, 4], [1, 4], [1, 4]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 5)

    def testOverlap_10(self):
        intervals = intervals_2

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 187)

    def t_estOverlap_11(self):
        intervals = intervals_3

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 9273)

    def testOverlap_12(self):
        intervals = [[1, 2], [1, 5], [5, 6], [4, 8], [7, 8]]

        num_to_remove = self.sol.eraseOverlapIntervals(intervals)

        self.assertEqual(num_to_remove, 2)



if __name__ == "__main__":
    unittest.main()
