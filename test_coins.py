import unittest


class Solution:
    def find_combinations(self, amount: int, actual_coin: int = 50) -> int:
        if amount < 2:
            return amount

        coins = [1, 2, 5, 10, 20, 50]

        num_combination = 0
        index = coins.index(actual_coin)

        for coin in coins[:index+1]:
            rest = amount - coin
            if rest == 0:
                num_combination += 1
            elif rest > 0:
                num_combination += self.find_combinations(rest, coin)

        return num_combination


class TestCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_combination_0(self):
        amount = 0

        actual = self.sol.find_combinations(amount)

        self.assertEqual(0, actual)

    def test_combination_1_cent(self):
        amount = 1

        actual = self.sol.find_combinations(amount)

        self.assertEqual(1, actual)

    def test_combination_2_cents(self):
        amount = 2

        actual = self.sol.find_combinations(amount)

        self.assertEqual(2, actual)

    def test_combination_3_cents(self):
        amount = 3

        actual = self.sol.find_combinations(amount)

        self.assertEqual(2, actual)

    def test_combination_4_cents(self):
        amount = 4

        actual = self.sol.find_combinations(amount)

        self.assertEqual(3, actual)


if __name__ == "__main__":
    unittest.main()
