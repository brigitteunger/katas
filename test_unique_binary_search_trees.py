import unittest
import math


class Solution:
    def numTrees(self, n: int) -> int:
        if n < 1:
            return 0
        total_num = (math.factorial(2*n) /
                     (math.factorial(n+1)*math.factorial(n)))
        return int(total_num)


class TestNumTrees(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_num_trees_1(self):
        n = 1

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 1)

    def test_num_trees_2(self):
        n = 2

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 2)

    def test_num_trees_3(self):
        n = 3

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 5)

    def test_num_trees_4(self):
        n = 4

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 14)

    def test_num_trees_5(self):
        n = 5

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 42)

    def test_num_trees_11(self):
        n = 11

        total_num = self.sol.numTrees(n)

        self.assertEqual(total_num, 58786)


if __name__ == "__main__":
    unittest.main()
