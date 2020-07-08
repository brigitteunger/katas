import unittest
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None

        spiral_order = []

        rows = len(matrix)
        cols = len(matrix[0])
        rows_to_do = rows
        cols_to_do = cols
        i = 0
        while 1:
            # go left
            if rows_to_do:
                for col in range(0+i, cols-i):
                    spiral_order.append(matrix[0+i][col])
                rows_to_do -= 1

            # go down
            if cols_to_do:
                for row in range(1+i, rows-i):
                    spiral_order.append(matrix[row][cols-1-i])
                cols_to_do -= 1

            # go right
            if rows_to_do:
                for col in range(cols-2-i, -1+i, -1):
                    spiral_order.append(matrix[rows-1-i][col])
                rows_to_do -= 1

            # go up
            if cols_to_do:
                for row in range(rows-2-i, 0+i, -1):
                    spiral_order.append(matrix[row][0+i])
                cols_to_do -= 1

            if not (rows_to_do or cols_to_do):
                break

            i += 1

        return spiral_order


class TestsSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_spiral_order_3x3(self):
        matrix = [
                  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]
                ]

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order,
                         [1, 2, 3, 6, 9, 8, 7, 4, 5]
                         )

    def test_spiral_order_3x4(self):
        matrix = [
                  [1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]
                ]

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order,
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
                         )

    def test_spiral_order_4x3(self):
        matrix = [
                  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]
                ]

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order,
                         [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
                         )

    def test_spiral_order_4x6(self):
        matrix = [
                  [1, 2, 3, 13, 14, 15],
                  [4, 5, 6, 16, 17, 18],
                  [7, 8, 9, 19, 20, 21],
                  [10, 11, 12, 22, 23, 24]
                ]

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order,
                         [1, 2, 3, 13, 14, 15, 18, 21, 24, 23, 22, 12, 11, 10,
                          7, 4, 5, 6, 16, 17, 20, 19, 9, 8]
                         )

    def test_spiral_order_empty(self):
        matrix = []

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order, None)

    def test_spiral_order_1x1(self):
        matrix = [[1]]

        spiral_order = self.sol.spiralOrder(matrix)

        self.assertEqual(spiral_order, [1])


if __name__ == "__main__":
    unittest.main()
