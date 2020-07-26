import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return self.binary_search(nums, 0, len(nums)-1)

    def binary_search(self, nums: List[int], left_index: int,
                      right_index: int) -> int:
        while left_index <= right_index:
            if left_index == right_index:
                return nums[left_index]
            middle_index = int((left_index + right_index) / 2+0.5)
            if nums[middle_index] < nums[middle_index-1]:
                return nums[middle_index]

            if nums[middle_index] == nums[left_index] and nums[middle_index] == nums[right_index]:
                left_index += 1
            elif nums[middle_index] <= nums[right_index]:
                right_index = middle_index - 1
            else:  # elif nums[middle_index] <= nums[left_index]:
                left_index = middle_index + 1


class TestFindMin(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindMin3(self):
        nums = [1, 3, 5]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 1)

    def testFindMin5(self):
        nums = [2, 2, 2, 0, 1]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 0)

    def testFindMin2(self):
        nums = [1, 1]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 1)

    def testFindMin3b(self):
        nums = [1, 1, 1]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 1)

    def testFindMin4(self):
        nums = [1, 1, 0, 1]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 0)

    def testFindMin5b(self):
        nums = [10, 10, 10, 1, 10]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 1)

    def testFindMin6b(self):
        nums = [1, 1, 2, 2, 0, 0]

        min_num = self.sol.findMin(nums)

        self.assertEqual(min_num, 0)


if __name__ == "__main__":
    unittest.main()
