import unittest
from typing import List
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        return self.get_permutation_list(nums, k)

    def get_permutation_list(self, nums: List[int], k: int) -> str:
        n = len(nums)
        if n == 1:
            number = nums[k-1]
            return str(number)
        n_min_1_fac = math.factorial(n-1)
        first_index = (k-1) // n_min_1_fac
        k_next = k % n_min_1_fac
        number = nums[first_index]
        nums.remove(number)

        tail = self.get_permutation_list(nums, k_next)
        return str(number) + tail


class TestGetPermutation(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_get_permutation_1(self):
        n = 1
        k = 1

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, '1')

    def test_get_permutation_21(self):
        n = 2
        k = 2

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, '21')

    def test_get_permutation_213(self):
        n = 3
        k = 3

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "213")

    def test_get_permutation_2314(self):
        n = 4
        k = 9

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "2314")

    def test_get_permutation_1234(self):
        n = 4
        k = 1

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "1234")

    def test_get_permutation_312(self):
        n = 3
        k = 5

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "312")

    def test_get_permutation_64731528(self):
        n = 8
        k = 27891

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "64731528")

    def test_get_permutation_132(self):
        n = 3
        k = 2

        actual = self.sol.getPermutation(n, k)

        self.assertEqual(actual, "132")


if __name__ == "__main__":
    unittest.main()
