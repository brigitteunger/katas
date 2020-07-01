import unittest
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairs = int(math.sqrt(2*n+0.25)-0.5)
        return stairs


class TestArrangeCoins(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_arrange_coins_5(self):
        n = 5

        stairs = self.sol.arrangeCoins(n)

        self.assertEqual(stairs, 2)

    def test_arrange_coins_8(self):
        n = 8

        stairs = self.sol.arrangeCoins(n)

        self.assertEqual(stairs, 3)

    def test_arrange_coins_0(self):
        n = 0

        stairs = self.sol.arrangeCoins(n)

        self.assertEqual(stairs, 0)


if __name__ == "__main__":
    unittest.main()
