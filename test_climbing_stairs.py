import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        first = 3
        second = 5
        actual = 4
        while actual < n:
            tmp = second
            second += first
            first = tmp
            actual += 1

        return second


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testClimbingStairs_2(self):
        n = 2

        num = self.sol.climbStairs(n)

        self.assertEqual(num, 2)

    def testClimbingStairs_3(self):
        n = 3

        num = self.sol.climbStairs(n)

        self.assertEqual(num, 3)

    def testClimbingStairs_4(self):
        n = 4

        num = self.sol.climbStairs(n)

        self.assertEqual(num, 5)

    def testClimbingStairs_5(self):
        n = 5

        num = self.sol.climbStairs(n)

        self.assertEqual(num, 8)

    def testClimbingStairs_6(self):
        n = 6

        num = self.sol.climbStairs(n)

        self.assertEqual(num, 13)


if __name__ == "__main__":
    unittest.main()
