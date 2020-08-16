import unittest
from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        buy_0 = prices[0]
        buy_1 = buy_0
        sell_0 = 0
        sell_1 = 0

        for price in prices:
            buy_0 = min(buy_0, price)
            sell_0 = max(sell_0, price-buy_0)
            buy_1 = min(buy_1, price - sell_0)
            sell_1 = max(sell_1, price - buy_1)

        return sell_1


class TestLeastInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaxProfit1(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 6)

    def testMaxProfit2(self):
        prices = [1, 2, 3, 4, 5]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 4)

    def testMaxProfit3(self):
        prices = [7, 6, 4, 3, 1]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 0)


if __name__ == '__main__':
    unittest.main()
