import unittest
from typing import List
from data_non_overlapping_intervals import intervals_2, intervals_3


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        len_intervals = len(intervals)
        starts = []
        for i in range(len_intervals):
            starts.append([intervals[i][0], i])
        starts.sort()

        result = [-1]*len_intervals
        for i in range(len_intervals):
            end = intervals[i][1]
            left = 0
            right = len_intervals-1
            while left < right:
                middle = left + int((right-left)/2)
                start = starts[middle][0]
                if start >= end:
                    right = middle
                else:
                    left = middle+1
            if starts[left][0] >= end and i != starts[left][1]:
                result[i] = starts[left][1]
        return result


class TestFindRightInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindRightInterval_1(self):
        intervals = [[1, 2]]

        overlapping = self.sol.findRightInterval(intervals)

        self.assertEqual(overlapping, [-1])

    def testFindRightInterval_2(self):
        intervals = [[3, 4], [2, 3], [1, 2]]

        overlapping = self.sol.findRightInterval(intervals)

        self.assertEqual(overlapping, [-1, 0, 1])

    def testFindRightInterval_3(self):
        intervals = [[1, 4], [2, 3], [3, 4]]

        overlapping = self.sol.findRightInterval(intervals)

        self.assertEqual(overlapping, [-1, 2, -1])

    def testFindRightInterval_4(self):
        intervals = [[1, 2], [2, 3], [0, 1], [3, 4]]

        overlapping = self.sol.findRightInterval(intervals)

        self.assertEqual(overlapping, [1, 3, 0, -1])


if __name__ == "__main__":
    unittest.main()
