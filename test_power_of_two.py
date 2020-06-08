import unittest


class Solution():
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        number_format_bin = format(n, 'b')
        number_ones = number_format_bin.count('1')
        if number_ones == 1:
            return True
        else:
            return False


class TsetIsPowerOfTwO(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_power_of_Two_One(self):
        input_ = 1

        actual = self.sol.isPowerOfTwo(input_)

        self.assertTrue(actual)

    def test_is_power_of_Two_16(self):
        input_ = 16

        actual = self.sol.isPowerOfTwo(input_)

        self.assertTrue(actual)

    def test_is_power_of_Two_218(self):
        input_ = 218

        actual = self.sol.isPowerOfTwo(input_)

        self.assertFalse(actual)

    def test_is_power_of_Two_Zero(self):
        input_ = 0

        actual = self.sol.isPowerOfTwo(input_)

        self.assertFalse(actual)

    def test_is_power_of_Two_Neg(self):
        input_ = -16

        actual = self.sol.isPowerOfTwo(input_)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
