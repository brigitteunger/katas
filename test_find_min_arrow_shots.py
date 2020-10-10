import unittest
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        len_interval = len(points)
        if len_interval == 0:
            return 0
        elif len_interval == 1:
            return 1

        points.sort(key=lambda point: (point[1], point[1]-point[0]))
        arrow_pos = points[0][1]
        count = 1
        for i in range(len_interval):
            if arrow_pos >= points[i][0]:
                continue
            count += 1
            arrow_pos = points[i][1]
        return count


class TestFindMinArrowShots(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindMinArrowShots_1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]

        min_shots = self.sol.findMinArrowShots(points)

        self.assertEqual(2, min_shots)

    def testFindMinArrowShots_2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]

        min_shots = self.sol.findMinArrowShots(points)

        self.assertEqual(4, min_shots)

    def testFindMinArrowShots_3(self):
        points = [[1, 2]]

        min_shots = self.sol.findMinArrowShots(points)

        self.assertEqual(1, min_shots)

    def testFindMinArrowShots_4(self):
        points = [[2, 3], [2, 3]]

        min_shots = self.sol.findMinArrowShots(points)

        self.assertEqual(1, min_shots)

    def testFindMinArrowShots_5(self):
        points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]

        min_shots = self.sol.findMinArrowShots(points)

        self.assertEqual(2, min_shots)


if __name__ == "__main__":
    unittest.main()
