import unittest
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxx = 0
        mask = 0
        for i in range(30, -1, -1):
            prefixes = set()
            mask |= (1 << i)
            maxx_candidate = maxx | (1 << i)
            for num in nums:
                prefixes.add(num & mask)
            for prefix in prefixes:
                if (maxx_candidate ^ prefix) in prefixes:
                    maxx = maxx_candidate
                    break
        return maxx


class TestFindMaximumXOR(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindMaximumXOR(self):
        nums = [3, 10, 5, 25, 2, 8]

        maximum = self.sol.findMaximumXOR(nums)

        self.assertEqual(maximum, 28)


if __name__ == "__main__":
    unittest.main()
