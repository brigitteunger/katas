import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                del nums_dict[num]
            else:
                nums_dict[num] = None

        single_nums = []
        for key in nums_dict.keys():
            single_nums.append(key)

        return single_nums


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testSingleNumber6(self):
        nums = [1, 2, 1, 3, 2, 5]

        single_nums = self.sol.singleNumber(nums)

        self.assertEqual(single_nums, [3, 5])

    def testSingleNumber2(self):
        nums = [1, 2]

        single_nums = self.sol.singleNumber(nums)

        self.assertEqual(single_nums, [1, 2])

    def testSingleNumberEmpty(self):
        nums = []

        single_nums = self.sol.singleNumber(nums)

        self.assertEqual(single_nums, [])


if __name__ == "__main__":
    unittest.main()
