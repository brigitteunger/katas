import unittest
from typing import List, Dict


class Solution():
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        if not coins:
            return 0

        num_combinations = [0] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                num_combinations[coin] += 1
                partial_amount = coin + 1
                while partial_amount <= amount:
                    rest = partial_amount - coin
                    num_combinations[partial_amount] += num_combinations[rest]
                    partial_amount += 1

        return num_combinations[amount]


class TestChange(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_change_three_coins(self):
        amount = 5
        coins = [1, 2, 5]

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 4)

    def test_change_no_solution(self):
        amount = 3
        coins = [2]

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 0)

    def test_change_one_solution(self):
        amount = 10
        coins = [1]

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 1)

    def test_change_no_coins(self):
        amount = 10
        coins = []

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 0)

    def test_change_none_coins(self):
        amount = 10
        coins = None

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 0)

    def test_change_amount_zero(self):
        amount = 0
        coins = []

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 1)

    def test_change_amount_big_number(self):
        amount = 500
        coins = [3, 5, 7, 8, 9, 10, 11]

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 35502874)

    def test_coins_bigger_than_amount(self):
        amount = 10
        coins = [1, 11, 12, 13, 14]

        actual = self.sol.change(amount, coins)

        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()

""" test_ = TestChange()
test_.setUp()
test_.test_change_one_solution()
 """
