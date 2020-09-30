import unittest
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums.sort()
        if nums[-1] <= 0:
            return 1
        count = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                pass
            else:
                if nums[i] > count:
                    return count
                elif nums[i] == count:
                    count += 1
        return count


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFirstMissingPositive_1(self):
        nums = [1, 2, 0]

        missing_num = self.sol.firstMissingPositive(nums)

        self.assertEqual(3, missing_num)

    def testFirstMissingPositive_2(self):
        nums = [3, 4, -1, 1]

        missing_num = self.sol.firstMissingPositive(nums)

        self.assertEqual(2, missing_num)

    def testFirstMissingPositive_3(self):
        nums = [7, 8, 9, 11, 12]

        missing_num = self.sol.firstMissingPositive(nums)

        self.assertEqual(1, missing_num)

    def testFirstMissingPositive_4(self):
        nums = [0, 2, 2, 1, 1]

        missing_num = self.sol.firstMissingPositive(nums)

        self.assertEqual(3, missing_num)


if __name__ == "__main__":
    unittest.main()
