import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_sum = nums[0]
        actual_sum = 0
        for num in nums:
            actual_sum += num
            if actual_sum > max_sum:
                max_sum = actual_sum
            if actual_sum < 0:
                actual_sum = 0
        return max_sum


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_max_subarray(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, 6)

    def test_max_subarray_one_pus(self):
        nums = [-2, 1, -3, -1,  -5]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, 1)

    def test_max_subarray_empty_list(self):
        nums = []

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, None)

    def test_max_subarray_one_list(self):
        nums = [0]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, 0)

    def test_max_subarray_one_neg(self):
        nums = [-1]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, -1)

    def test_max_subarray_only_negs(self):
        nums = [-2, -1, -3, -4, -1, -2, -1, -5, -4]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, -1)

    def test_max_subarray_two_pos(self):
        nums = [1, 2]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, 3)

    def test_max_subarray_use_neg(self):
        nums = [-1, 2, -1, 3, -1]

        actual_sum = self.sol.maxSubArray(nums)

        self.assertEqual(actual_sum, 4)


if __name__ == '__main__':
    unittest.main()
