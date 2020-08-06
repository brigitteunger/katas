import unittest
from typing import List
import data_test_find_duplicate_number


class Solution():
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        duplicates = []

        for i in range(len(nums)):
            abs_num = abs(nums[i])
            if nums[abs_num-1] > 0:
                nums[abs_num-1] *= -1
            else:
                if not duplicates:
                    duplicates = [abs_num]
                else:
                    duplicates.append(abs_num)

        return duplicates


class TestFindDuplicates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_duplicates_empty(self):
        nums = []

        duplicates = self.sol.findDuplicates(nums)

        self.assertEqual(duplicates, [])

    def test_find_duplicates_1(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]

        duplicates = self.sol.findDuplicates(nums)

        self.assertEqual(duplicates, [2, 3])


if __name__ == "__main__":
    unittest.main()
