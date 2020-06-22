import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
                if nums_dict[num] == 3:
                    del nums_dict[num]
            else:
                nums_dict[num] = 1
        for num in nums_dict.keys():
            single_num = num
        return single_num


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_number_4_3(self):
        nums = [2, 2, 3, 2]

        single_num = self.sol.singleNumber(nums)

        self.assertEqual(single_num, 3)

    def test_single_number_5_99(self):
        nums = [0, 1, 0, 1, 0, 1, 99]

        single_num = self.sol.singleNumber(nums)

        self.assertEqual(single_num, 99)


if __name__ == "__main__":
    unittest.main()
