import unittest


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        number_format_bin = format(num, 'b')
        number_ones = number_format_bin.count('1')
        if number_ones == 1:
            if (len(number_format_bin)-1) % 2 == 0:
                return True
        else:
            return False


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_power_of_four_16(self):
        num = 16

        validation = self.sol.isPowerOfFour(num)

        self.assertTrue(validation)

    def test_power_of_four_0(self):
        num = 0

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)

    def test_power_of_four_4(self):
        num = 4

        validation = self.sol.isPowerOfFour(num)

        self.assertTrue(validation)

    def test_power_of_four_2(self):
        num = 2

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)

    def test_power_of_four_1(self):
        num = 1

        validation = self.sol.isPowerOfFour(num)

        self.assertTrue(validation)

    def test_power_of_four_5(self):
        num = 5

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)

    def test_power_of_four_8(self):
        num = 8

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)

    def test_power_of_four_minus_2147483648(self):
        num = -2147483648

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)

    def test_power_of_four_81(self):
        num = 81

        validation = self.sol.isPowerOfFour(num)

        self.assertFalse(validation)


if __name__ == "__main__":
    unittest.main()
