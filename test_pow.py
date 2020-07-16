import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        temp_x = self.myPow(x, int(n/2))

        if n % 2 == 0:
            return temp_x*temp_x
        else:
            if n > 0:
                return x*temp_x*temp_x
            else:
                return temp_x*temp_x/x


class TestMyPow(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMyPow_2_10(self):
        x = 2.
        n = 10

        result = self.sol.myPow(x, n)

        self.assertEqual(result, 1024.00000)

    def testMyPow_2_1_3(self):
        x = 2.1
        n = 3

        result = self.sol.myPow(x, n)

        self.assertAlmostEqual(result, 9.26100)

    def testMyPow_2_neg_2(self):
        x = 2
        n = -2

        result = self.sol.myPow(x, n)

        self.assertEqual(result, 0.25)

    def testMyPow_2_neg_1(self):
        x = 2
        n = -1

        result = self.sol.myPow(x, n)

        self.assertEqual(result, 0.5)

    def testMyPow_2_0(self):
        x = 2
        n = 0

        result = self.sol.myPow(x, n)

        self.assertEqual(result, 1)

    def testMyPow_very_small(self):
        x = 0.00001
        n = 2147483647

        result = self.sol.myPow(x, n)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
