import unittest
from typing import List, Tuple


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        counter = 0
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    A_shifted = A
                else:
                    A_shifted = self.matrixShift(A, rows, cols, row, col)
                actual_counter = self.countOverlappingOnes(A_shifted, B,
                                                           rows, cols)
                counter = max(counter, actual_counter)
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                B_shifted = self.matrixShift(B, rows, cols, row, col)
                actual_counter = self.countOverlappingOnes(A, B_shifted,
                                                           rows, cols)
                counter = max(counter, actual_counter)
        return counter

    def matrixShift(self,
                    mat:  List[List[int]],
                    rows: int,
                    cols: int,
                    row_shift: int,
                    col_shift: int) -> List[List[int]]:
        mat_shifted = [[0]*cols]*rows
        for row in range(rows-row_shift):
            mat_shifted[row+row_shift] = mat_shifted[row][0:col_shift] + \
                                        mat[row][0:cols-col_shift]
        return mat_shifted

    def countOverlappingOnes(self, A: List[List[int]],
                             B: List[List[int]],
                             rows: int,
                             cols: int) -> int:
        counter = 0
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1 and B[row][col] == 1:
                    counter += 1
        return counter


class TestLargesOverlap(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLargestOverlap1(self):
        A = [[1, 1, 0],
             [0, 1, 0],
             [0, 1, 0]]
        B = [[0, 0, 0],
             [0, 1, 1],
             [0, 0, 1]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 3)

    def testLargestOverlap2(self):
        A = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        B = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 1]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 1)

    def testLargestOverlap3(self):
        A = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        B = [[0, 0, 0],
             [0, 0, 0],
             [1, 0, 0]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 1)

    def testLargestOverlap4(self):
        A = [[1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
        B = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 1, 0]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 3)

    def testLargestOverlap5(self):
        A = [[0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1],
             [0, 1, 0, 0, 1]]
        B = [[1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 5)

    def testLargestOverlap6(self):
        A = [[0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 0, 1, 0]]
        B = [[0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 0, 1],
             [0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0]]

        overlaps = self.sol.largestOverlap(A, B)

        self.assertEqual(overlaps, 4)


if __name__ == "__main__":
    unittest.main()
