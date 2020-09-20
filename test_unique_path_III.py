import unittest
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    pos = [i, j]
                    break
        return self.findPath(grid, pos, rows, cols)

    def findPath(self,
                 grid: List[List[int]],
                 pos: List[int],
                 rows: int,
                 cols: int) -> int:
        original_val = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = -1
        num = 0
        # top
        if pos[0]-1 >= 0:
            if self.validPath(grid, [pos[0]-1, pos[1]], rows):
                grid[pos[0]][pos[1]] = original_val
                return 1
            if grid[pos[0]-1][pos[1]] == 0:
                num += self.findPath(grid, [pos[0]-1, pos[1]], rows, cols)
        # bottom
        if pos[0]+1 < rows:
            if self.validPath(grid, [pos[0]+1, pos[1]], rows):
                grid[pos[0]][pos[1]] = original_val
                return 1
            if grid[pos[0]+1][pos[1]] == 0:
                num += self.findPath(grid, [pos[0]+1, pos[1]], rows, cols)
        # right
        if pos[1]-1 >= 0:
            if self.validPath(grid, [pos[0], pos[1]-1], rows):
                grid[pos[0]][pos[1]] = original_val
                return 1
            if grid[pos[0]][pos[1]-1] == 0:
                num += self.findPath(grid, [pos[0], pos[1]-1], rows, cols)
        # left
        if pos[1]+1 < cols:
            if self.validPath(grid, [pos[0], pos[1]+1], rows):
                grid[pos[0]][pos[1]] = original_val
                return 1
            if grid[pos[0]][pos[1]+1] == 0:
                num += self.findPath(grid, [pos[0], pos[1]+1], rows, cols)

        grid[pos[0]][pos[1]] = original_val
        return num

    def validPath(self,
                  grid: List[List[int]],
                  pos: List[int],
                  rows: int) -> bool:

        if grid[pos[0]][pos[1]] == 2:
            for row in grid:
                if 0 in row:
                    return False
            return True
        else:
            return False


class TestUniquePathsIII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testUniquePathsIII_1(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

        num_unique_paths = self.sol.uniquePathsIII(grid)

        self.assertEqual(num_unique_paths, 2)

    def testUniquePathsIII_2(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]

        num_unique_paths = self.sol.uniquePathsIII(grid)

        self.assertEqual(num_unique_paths, 4)

    def testUniquePathsIII_3(self):
        grid = [[0, 1], [2, 0]]

        num_unique_paths = self.sol.uniquePathsIII(grid)

        self.assertEqual(num_unique_paths, 0)


if __name__ == "__main__":
    unittest.main()
