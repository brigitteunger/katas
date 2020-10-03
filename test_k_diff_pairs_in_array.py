import unittest
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        counts = 0
        nums.sort()
        used = set()
        j = 0
        for i in range(len(nums)-1):
            j += 1
            wanted = k + nums[i]
            if wanted in used:
                pass
            elif wanted in nums[j:]:
                counts += 1
                used.add(wanted)
        return counts


class TestFindPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindPairs_1(self):
        nums = [3, 1, 4, 1, 5]
        k = 2

        combinations = self.sol.findPairs(nums, k)

        self.assertEqual(combinations, 2)

    def testFindPairs_2(self):
        nums = [1, 2, 3, 4, 5]
        k = 1

        combinations = self.sol.findPairs(nums, k)

        self.assertEqual(combinations, 4)

    def testFindPairs_3(self):
        nums = [3, 1, 4, 1, 5]
        k = 0

        combinations = self.sol.findPairs(nums, k)

        self.assertEqual(combinations, 1)

    def testFindPairs_4(self):
        nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
        k = 3

        combinations = self.sol.findPairs(nums, k)

        self.assertEqual(combinations, 2)

    def testFindPairs_5(self):
        nums = [-1, -2, -3]
        k = 1

        combinations = self.sol.findPairs(nums, k)

        self.assertEqual(combinations, 2)


if __name__ == "__main__":
    unittest.main()
