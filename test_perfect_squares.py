import unittest
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = self.generate_square_nums(n)
        if n == square_nums[-1]:
            return 1
        elif self.is_sum_of_two_squares(n, square_nums):
            return 2
        elif self.is_sum_of_three_squares(n, square_nums):
            return 3
        else:
            # according to Lagrange's four-square theorem:
            # every natural number can be represented as the sum of
            # four integer squares
            # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
            return 4

    def generate_square_nums(self, n: int) -> List[int]:
        last_square = 1
        odd_number = 1
        square_nums = [1]
        while last_square < n:
            odd_number += 2
            last_square += odd_number
            square_nums.append(last_square)
        return square_nums

    def is_sum_of_two_squares(self, n: int, squares: List[int]) -> bool:
        for num in squares:
            rest = n - num
            if rest in squares:
                return True
            elif rest < num:
                break
        return False

    def is_sum_of_three_squares(self, n: int, squares: List[int]) -> bool:
        for num in squares:
            rest = n - num
            if self.is_sum_of_two_squares(rest, squares):
                return True
        return False


class TestSumNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_num_squares_12(self):
        n = 12

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 3)

    def test_num_squares_13(self):
        n = 13

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 2)

    def test_num_squares_1(self):
        n = 1

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 1)

    def test_num_squares_16(self):
        n = 16

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 1)

    def test_num_squares_72(self):
        n = 72

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 2)

    def test_num_squares_98(self):
        n = 98

        num_summands = self.sol.numSquares(n)

        self.assertEqual(num_summands, 2)


if __name__ == "__main__":
    unittest.main()
