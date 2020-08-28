import unittest
from typing import List
import random


def rand7() -> int:
    return random.randint(1, 7)


class Solution:
    def rand10(self) -> int:
        num_1 = 7
        while num_1 > 5:
            num_1 = rand7()
        num_2 = 7
        while num_2 > 6:
            num_2 = rand7()

        return ((num_1 * 2) - (num_2 % 2))


class TestRand10(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_rand7(self):
        num = rand7()

        self.assertIn(num, range(1, 8))

    def test_rand10(self):
        num = self.sol.rand10()
        print(num)
        self.assertIn(num, range(1, 11))


if __name__ == "__main__":
    unittest.main()
