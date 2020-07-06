import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        rest = 1
        for index in range(len(digits)-1, -1, -1):
            digit = digits[index] + rest

            rest = digit - 9
            if rest <= 0:
                digits[index] = digit
                return digits
            else:
                digits[index] = digit - 10

        digits.insert(0, rest)
        return digits


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_plus_one_123(self):
        digits = [1, 2, 3]

        actual_plus_one = self.sol.plusOne(digits)

        self.assertEqual(actual_plus_one, [1, 2, 4])

    def test_plus_one_4321(self):
        digits = [4, 3, 2, 1]

        actual_plus_one = self.sol.plusOne(digits)

        self.assertEqual(actual_plus_one,  [4, 3, 2, 2])

    def test_plus_one_999(self):
        digits = [9, 9, 9]

        actual_plus_one = self.sol.plusOne(digits)

        self.assertEqual(actual_plus_one,  [1, 0, 0, 0])



if __name__ == "__main__":
    unittest.main()
