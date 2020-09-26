import unittest
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        if not timeSeries:
            return 0
        poisend_time = duration
        last_slot = timeSeries[-1]
        for slot in range(len(timeSeries)-1,-1,-1):
            poisend_time += min(last_slot-timeSeries[slot], duration)
            last_slot = timeSeries[slot]

        return poisend_time


class TestFindPoisonedDuration(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindPoisonedDuration_1(self):
        time_series = [1, 4]
        duration = 2

        posionded_duration = self.sol.findPoisonedDuration(time_series, duration)

        self.assertEqual(posionded_duration, 4)

    def testFindPoisonedDuration_2(self):
        time_series = [1, 2]
        duration = 2

        posionded_duration = self.sol.findPoisonedDuration(time_series, duration)

        self.assertEqual(posionded_duration, 3)

    def testFindPoisonedDuration_3(self):
        time_series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duration = 0

        posionded_duration = self.sol.findPoisonedDuration(time_series, duration)

        self.assertEqual(posionded_duration, 0)

    def testFindPoisonedDuration_4(self):
        time_series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duration = 100000

        posionded_duration = self.sol.findPoisonedDuration(time_series, duration)

        self.assertEqual(posionded_duration, 100008)


if __name__ == "__main__":
    unittest.main()