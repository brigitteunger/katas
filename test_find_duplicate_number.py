import unittest
from typing import List
import data_test_find_duplicate_number


class Solution():
    def findDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        seen = {}
        for num in nums:
            if num in seen:
                return num
            else:
                seen[num] = None

        return None

    def findDuplicates_set(self, nums: List[int]) -> int:
        if not nums:
            return None
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)

        return None


class TestFindDuplicates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_duplicates_empty(self):
        nums = []

        duplicate = self.sol.findDuplicates(nums)

        self.assertEqual(duplicate, None)

    def test_find_duplicates_5_2(self):
        nums = [1, 3, 4, 2, 2]

        duplicate = self.sol.findDuplicates(nums)

        self.assertEqual(duplicate, 2)

    def test_find_duplicates_5_3(self):
        nums = [3, 1, 3, 4, 2]

        duplicate = self.sol.findDuplicates(nums)

        self.assertEqual(duplicate, 3)

    def test_find_duplicates_7_2(self):
        nums = [3, 1, 7, 4, 2, 2]

        duplicate = self.sol.findDuplicates(nums)

        self.assertEqual(duplicate, 2)

    def test_find_duplicates_long(self):
        nums = data_test_find_duplicate_number.nums

        duplicate = self.sol.findDuplicates(nums)

        self.assertEqual(duplicate, 12983)


if __name__ == "__main__":
    unittest.main()
