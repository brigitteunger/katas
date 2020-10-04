import unittest
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        len_interval = len(intervals)
        intervals.sort(reverse=True, key=self.sortKey)
        if len_interval == 1:
            return 1
        count = len_interval
        for i in range(len_interval):
            for j in range(i+1, len_interval):
                if self.isOverlapping(intervals[i], intervals[j]):
                    count -= 1
                    break
        return count

    def isOverlapping(self,
                      interval_1: List[int],
                      interval_2: List[int]) -> bool:
        if interval_2[0] <= interval_1[0] and interval_1[1] <= interval_2[1]:
            return True
        else:
            return False

    def sortKey(self, interval: List[int]) -> int:
        return interval[0]*1000000+100000-interval[1]


class TestRemoveCoveredIntervals(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testRemoveCoveredIntervals_1(self):
        intervals = [[1, 4], [3, 6], [2, 8]]

        counts = self.sol.removeCoveredIntervals(intervals)

        self.assertEqual(counts, 2)

    def testRemoveCoveredIntervals_2(self):
        intervals = [[1, 4], [2, 3]]

        counts = self.sol.removeCoveredIntervals(intervals)

        self.assertEqual(counts, 1)

    def testRemoveCoveredIntervals_3(self):
        intervals = [[0, 10], [5, 12]]

        counts = self.sol.removeCoveredIntervals(intervals)

        self.assertEqual(counts, 2)

    def testRemoveCoveredIntervals_4(self):
        intervals = [[3, 10], [4, 10], [5, 11]]

        counts = self.sol.removeCoveredIntervals(intervals)

        self.assertEqual(counts, 2)

    def testRemoveCoveredIntervals_5(self):
        intervals = [[1, 2], [1, 4], [3, 4]]

        counts = self.sol.removeCoveredIntervals(intervals)

        self.assertEqual(counts, 1)


if __name__ == "__main__":
    unittest.main()
