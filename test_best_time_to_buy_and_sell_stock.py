import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        sell = 0
        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)
        return sell


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaxProfit_1(self):
        prices = [7, 1, 5, 3, 6, 4]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 5)

    def testMaxProfit_2(self):
        prices =[7, 6, 4, 3, 1]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 0)

    def testMaxProfit_3(self):
        prices = [7]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 0)


if __name__ == "__main__":
    unittest.main()
