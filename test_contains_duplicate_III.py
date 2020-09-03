import unittest
from typing import List
import numpy as np
from data_contains_duplicate_III import nums_2, t_2, k_2


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int],
                                      k: int, t: int) -> bool:
        if not nums:
            return False
        for i in range(1, len(nums)):
            slice_nums = np.array(nums[i:min(i+k, len(nums))])
            abs_slice = (abs(slice_nums-nums[i-1]) <= t)
            if True in abs_slice:
                return True
        return False

    def containsNearbyAlmostDuplicate_2(self, nums: List[int],
                                        k: int, t: int) -> bool:
        if not nums:
            return False
        len_nums = len(nums)
        for i in range(1, len_nums):
            slice_nums = nums[i:min(i+k, len_nums)]
            slice_nums.sort()
            if self.isWithinDistance(nums[i-1], slice_nums, t):
                return True
        return False

    def isWithinDistance(self, value: int, slice_nums: List[int],
                         t: int) -> bool:
        len_slice = len(slice_nums)
        left = 0
        right = len_slice
        while left < right:
            middle = int((left + right + 0.5) / 2)
            diff = slice_nums[middle] - value
            if abs(diff) <= t:
                return True
            elif diff < 0:
                left = middle + 1
            else:
                right = middle
        return False


class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testContainsNearbyAlmostDuplicate_1(self):
        nums = [1, 2, 3, 1]
        k = 3
        t = 0

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertTrue(solved)

    def testContainsNearbyAlmostDuplicate_2(self):
        nums = [1, 0, 1, 1]
        k = 1
        t = 2

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertTrue(solved)

    def testContainsNearbyAlmostDuplicate_3(self):
        nums = [1, 5, 9, 1, 5, 9]
        k = 2
        t = 3

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertFalse(solved)

    def testContainsNearbyAlmostDuplicate_4(self):
        nums = nums_2
        k = k_2
        t = t_2

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertFalse(solved)


if __name__ == "__main__":
    unittest.main()
