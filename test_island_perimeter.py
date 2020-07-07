import unittest
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return None

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    # north
                    if row == 0:
                        perimeter += 1
                    else:
                        if grid[row-1][col] == 0:
                            perimeter += 1
                    # south
                    if row == rows-1:
                        perimeter += 1
                    else:
                        if grid[row+1][col] == 0:
                            perimeter += 1

                    # west
                    if col == 0:
                        perimeter += 1
                    else:
                        if grid[row][col-1] == 0:
                            perimeter += 1
                    # east
                    if col == cols-1:
                        perimeter += 1
                    else:
                        if grid[row][col+1] == 0:
                            perimeter += 1
        return perimeter


class TestIslandPerimeter(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_island_perimeter_16(self):
        grid = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]

        perimeter = self.sol.islandPerimeter(grid)

        self.assertEqual(perimeter, 16)

    def test_island_perimeter_12(self):
        grid = [[1, 1, 1, 0],
                [1, 1, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]]

        perimeter = self.sol.islandPerimeter(grid)

        self.assertEqual(perimeter, 12)

    def test_island_perimeter_4(self):
        grid = [[1]]

        perimeter = self.sol.islandPerimeter(grid)

        self.assertEqual(perimeter, 4)

    def test_island_perimeter_0(self):
        grid = [[0]]

        perimeter = self.sol.islandPerimeter(grid)

        self.assertEqual(perimeter, 0)


if __name__ == "__main__":
    unittest.main()
