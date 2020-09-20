import unittest
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        len_low = len(str(low))
        len_high = len(str(high))
        return sorted([
            number
            for number in self.sequentialNumbers(len_low, len_high)
            if number >= low and number <= high
        ])

    def sequentialNumbers(
        self,
        min_num_digits: int,
        max_num_digits: int
    ):
        for first_digit in range(1, 10):
            max_num_digits = min(max_num_digits, 10 - first_digit)
            if (max_num_digits >= min_num_digits):
                number = 0
                for i in range(0, max_num_digits):
                    number = number * 10 + first_digit + i
                    yield number


class TestSequentialDigits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testSequentialDigits_1(self):
        low = 100
        high = 300

        sequence = self.sol.sequentialDigits(low, high)

        self.assertEqual(sequence,
                         [123, 234])

    def testSequentialDigits_2(self):
        low = 1000
        high = 13000

        sequence = self.sol.sequentialDigits(low, high)

        self.assertEqual(sequence,
                         [1234, 2345, 3456, 4567, 5678, 6789, 12345])

    def testSequentialDigits_3(self):
        low = 10
        high = 1000000000

        sequence = self.sol.sequentialDigits(low, high)

        self.assertEqual(sequence,
                         [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345,
                          456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678,
                          6789, 12345, 23456, 34567, 45678, 56789, 123456,
                          234567, 345678, 456789, 1234567, 2345678,
                          3456789, 12345678, 23456789, 123456789])

    def testSequentialDigits_4(self):
        low = 58
        high = 155

        sequence = self.sol.sequentialDigits(low, high)
        print(sequence)

        self.assertEqual(sequence, [67, 78, 89, 123])

    def testSequentialDigits_5(self):
        low = 178546104
        high = 812704742

        sequence = self.sol.sequentialDigits(low, high)
        print(sequence)

        self.assertEqual(sequence, [])

    def testSequentialDigits_6(self):
        low = 31365477
        high = 514800930

        sequence = self.sol.sequentialDigits(low, high)
        print(sequence)

        self.assertEqual(sequence, [123456789])


if __name__ == "__main__":
    unittest.main()
