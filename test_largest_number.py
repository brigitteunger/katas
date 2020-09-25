import unittest
from typing import List
from functools import cmp_to_key



class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        str_nums = [str(num) for num in nums]
        str_nums.sort(key=cmp_to_key(self.compare))
        if str_nums[0] == "0":
            return "0"
        else:
            return "".join(str_nums)

    def compare(self, x: str, y: str) -> int:
        if x == y:
            return 0
        elif x + y > y + x:
            return -1
        else:
            return 1



class TestPartitionLabels(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLargestNumber_1(self):
        nums = [10, 2]

        largest_num = self.sol.largestNumber(nums)

        self.assertEqual(largest_num, "210")

    def testLargestNumber_2(self):
        nums = [3, 30, 34, 5, 9]

        largest_num = self.sol.largestNumber(nums)

        self.assertEqual(largest_num, "9534330")

    def testLargestNumber_3(self):
        nums = []

        largest_num = self.sol.largestNumber(nums)

        self.assertEqual(largest_num, "")

    def testLargestNumber_4(self):
        nums = [0, 0]

        largest_num = self.sol.largestNumber(nums)

        self.assertEqual(largest_num, "0")

if __name__ == "__main__":
    unittest.main()
