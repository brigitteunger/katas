import unittest


class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        nums = list(str_num)
        result = 0
        for num in nums:
            result += int(num)
            if result >= 10:
                result -= 9
        return result


class TestAddDigitst(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_add_digits_38(self):
        num = 38

        one_digit = self.sol.addDigits(num)

        self.assertEqual(one_digit, 2)

    def test_add_digits_1(self):
        num = 1

        one_digit = self.sol.addDigits(num)

        self.assertEqual(one_digit, 1)

    def test_add_digits_999(self):
        num = 999

        one_digit = self.sol.addDigits(num)

        self.assertEqual(one_digit, 9)


if __name__ == "__main__":
    unittest.main()
