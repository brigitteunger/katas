import unittest
from typing import List


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_nums = [1] * n
        multi_2 = 2
        multi_3 = 3
        multi_5 = 5
        index_multi_2 = 0
        index_multi_3 = 0
        index_multi_5 = 0

        for i_th in range(1, n):
            next_ugly_num = min(multi_2, multi_3, multi_5)
            ugly_nums[i_th] = next_ugly_num

            if next_ugly_num == multi_2:
                index_multi_2 += 1
                multi_2 = 2 * ugly_nums[index_multi_2]
            if next_ugly_num == multi_3:
                index_multi_3 += 1
                multi_3 = 3 * ugly_nums[index_multi_3]
            if next_ugly_num == multi_5:
                index_multi_5 += 1
                multi_5 = 5 * ugly_nums[index_multi_5]

        return ugly_nums[n-1]


class TestNthUglyNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_nth_ugly_number_10(self):
        n = 10

        ugly_number = self.sol.nthUglyNumber(n)

        self.assertEqual(ugly_number, 12)

    def test_nth_ugly_number_5(self):
        n = 5

        ugly_number = self.sol.nthUglyNumber(n)

        self.assertEqual(ugly_number, 5)

    def test_nth_ugly_number_1(self):
        n = 1

        ugly_number = self.sol.nthUglyNumber(n)

        self.assertEqual(ugly_number, 1)

    def test_nth_ugly_number_1690(self):
        n = 1690

        ugly_number = self.sol.nthUglyNumber(n)

        self.assertEqual(ugly_number, 2123366400)


if __name__ == "__main__":
    unittest.main()