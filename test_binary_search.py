import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        len_nums = len(nums)
        right = len_nums-1
        left = 0
        while 1:
            index = (right + left)//2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                if index == len_nums-1:
                    return -1
                elif nums[index+1] > target:
                    return -1
                left = index + 1
            else:
                if index == 0:
                    return -1
                elif nums[index-1] < target:
                    return -1
                right = index - 1


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testSearch_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9

        index = self.sol.search(nums, target)

        self.assertEqual(index, 4)

    def testSearch_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def testSearch_3(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = -1

        index = self.sol.search(nums, target)

        self.assertEqual(index, 0)

    def testSearch_4(self):
        nums = [5]
        target = -5

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def testSearch_5(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 13

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def testSearch_6(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = -2

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)


if __name__ == "__main__":
    unittest.main()
