import unittest
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if low > 123456789:
            return[]
        len_low = len(str(low))
        len_high = len(str(high))
        first_digit = low//(10**(len_low-1))
        sequence = []
        while 1:
            num = 0
            digit = first_digit
            for i in range(len_low-1, -1, -1):
                new_num = True
                num += digit * (10 ** i)
                digit += 1
                if digit > 10:
                    # One digit more?
                    if len_low < len_high:
                        len_low += 1
                        first_digit = 0
                    new_num = False
                    continue
            if new_num:
                if num <= high:
                    if num >= low:
                        sequence.append(num)
                        if num == 123456789:
                            break
                else:
                    break
            first_digit += 1
        return sequence


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
