import unittest
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = (math.factorial(m+n-2)) / (
            math.factorial(n-1)*math.factorial(m-1))
        return num


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_unique_path_7_3(self):
        m = 7
        n = 3

        num_unique_paths = self.sol.uniquePaths(m, n)

        self.assertEqual(num_unique_paths, 28)

    def test_unique_path_3_2(self):
        m = 3
        n = 2

        num_unique_paths = self.sol.uniquePaths(m, n)

        self.assertEqual(num_unique_paths, 3)


if __name__ == "__main__":
    unittest.main()
