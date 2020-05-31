import unittest
from typing import List


class Solution():
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        if len(matrix[0]) == 1:
            return

        n = len(matrix)
        steps_to_inner = int(n/2)
        for step_in in range(steps_to_inner):
            for step_rows in range(n-1-step_in*2):
                temp = matrix[n-1 - step_rows-step_in][step_in]  # speichere 2,1
                matrix[n-1 - step_rows-step_in][step_in] = (
                    matrix[n-1-step_in][n-1-step_rows-step_in])  # 2,2->2,1
                matrix[n-1-step_in][n-1 - step_rows-step_in] = (
                    matrix[step_rows+step_in][n-1-step_in])  # 1,2->2,2
                matrix[step_rows+step_in][n-1-step_in] = (
                    matrix[step_in][step_rows+step_in])  # 1,1->1,2
                matrix[step_in][step_rows+step_in] = temp  # 2,1->1,1

    def print_matrix_nicely(self, matrix: List[List[int]], size_per_val=6):
        print()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(str(matrix[row][col]).center(size_per_val), end='')
        print()


class testRotate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_rotate_3_3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        self.sol.rotate(matrix)
        actual_result = matrix

        self.assertEqual(actual_result, expected_result)

    def test_rotate_4_4(self):
        matrix = [[5, 1, 9, 11],
                  [2, 4, 8, 10],
                  [13, 3, 6, 7],
                  [15, 14, 12, 16]]
        expected_result = [[15, 13, 2, 5],
                           [14, 3, 4, 1],
                           [12, 6, 8, 9],
                           [16, 7, 10, 11]]

        self.sol.rotate(matrix)
        actual_result = matrix

        self.assertEqual(actual_result, expected_result)

    def test_rotate_5_5(self):
        matrix = matrix = [[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20],
                           [21, 22, 23, 24, 25]]
        expected_result = [[21, 16, 11, 6, 1],
                           [22, 17, 12, 7, 2],
                           [23, 18, 13, 8, 3],
                           [24, 19, 14, 9, 4],
                           [25, 20, 15, 10, 5]]

        self.sol.rotate(matrix)
        actual_result = matrix

        self.assertEqual(actual_result, expected_result)

    def test_rotate_empty(self):
        matrix = []
        expected_result = []

        self.sol.rotate(matrix)
        actual_result = matrix

        self.assertEqual(actual_result, expected_result)

    def test_rotate_one_element(self):
        matrix = [[2]]
        expected_result = [[2]]

        self.sol.rotate(matrix)
        actual_result = matrix

        self.assertEqual(actual_result, expected_result)
