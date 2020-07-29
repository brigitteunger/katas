import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        buy_0 = -prices[0]
        buy_1 = buy_0
        sell_0 = 0
        sell_1 = 0
        sell_2 = 0

        for price in prices:
            buy_0 = max(buy_1, sell_2 - price)
            sell_0 = max(sell_1, buy_1 + price)
            buy_1 = buy_0
            sell_2 = sell_1
            sell_1 = sell_0

        return sell_0


class TestLeastInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaxProfit1(self):
        prices = [1, 2, 3, 0, 2]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 3)

    def testMaxProfit2(self):
        prices = [0, 4, 1, 2]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 4)

    def testMaxProfit3(self):
        prices = [0, 3, 0, 1, 2]

        profit = self.sol.maxProfit(prices)

        self.assertEqual(profit, 4)


if __name__ == '__main__':
    unittest.main()
