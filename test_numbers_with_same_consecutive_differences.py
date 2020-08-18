import unittest
from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        if K == 0:
            nums = []
            for i in range(1, 10):
                num = ''
                for _ in range(N):
                    num += str(i)
                nums.append(int(num))
            return nums
        nums = []
        for i in range(1, 10):
            self.dfs(N-1, K, i, nums)
        return nums

    def dfs(self, N: int, K: int, num: int, nums: List[int]) -> None:
        if N == 0:
            nums.append(num)
        else:
            last_digit = num % 10
            if last_digit+K < 10:
                self.dfs(N-1, K, num*10+last_digit+K, nums)
            if last_digit >= K and K != 0:
                self.dfs(N-1, K, num*10+last_digit-K, nums)


class TestNumsSameConsecDiff(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testNumsSameConsecDiff_1(self):
        n = 3
        k = 7

        nums = self.sol.numsSameConsecDiff(n, k)
        nums.sort()

        self.assertEqual(nums, [181, 292, 707, 818, 929])

    def testNumsSameConsecDiff_2(self):
        n = 2
        k = 1

        nums = self.sol.numsSameConsecDiff(n, k)
        nums.sort()

        self.assertEqual(nums, [10, 12, 21, 23, 32, 34, 43,
                                45, 54, 56, 65, 67, 76, 78,
                                87, 89, 98])

    def testNumsSameConsecDiff_3(self):
        n = 3
        k = 0

        nums = self.sol.numsSameConsecDiff(n, k)

        self.assertEqual(nums, [111, 222, 333, 444, 555,
                                666, 777, 888, 999])

    def testNumsSameConsecDiff_4(self):
        n = 1
        k = 0

        nums = self.sol.numsSameConsecDiff(n, k)

        self.assertEqual(nums, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def testNumsSameConsecDiff_5(self):
        n = 3
        k = 3

        nums = self.sol.numsSameConsecDiff(n, k)
        nums.sort()

        self.assertEqual(nums, [141, 147, 252, 258, 303, 363,
                                369, 414, 474, 525, 585, 630,
                                636, 696, 741, 747, 852, 858,
                                963, 969])


if __name__ == "__main__":
    unittest.main()
