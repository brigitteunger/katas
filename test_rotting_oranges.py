import unittest
from typing import List, Dict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        status = self.evaluation(grid)
        if status['rotten'] is False and status['fresh'] is True:
            return -1
        if status['fresh'] is False:
            return 0

        mins = self.rotting(grid)
        status = self.evaluation(grid)

        if status['fresh'] is True:
            return -1
        else:
            return mins

    def rotting(self, grid: List[List[int]], mins: int = 0) -> int:
        still_rotting = True
        mins = -1
        rows = len(grid)
        cols = len(grid[0])
        while still_rotting:
            still_rotting = False
            mins += 1
            # self.printGrid(grid)
            for index_row in range(rows):
                for index_col in range(cols):
                    if grid[index_row][index_col] == 2 + mins:
                        # right orange rots
                        if (index_col+1 < cols) and (
                           grid[index_row][index_col+1] == 1):
                            grid[index_row][index_col+1] = 3 + mins
                            still_rotting = True
                        # left orange rots
                        if (index_col-1 >= 0) and (
                           grid[index_row][index_col-1] == 1):
                            grid[index_row][index_col-1] = 3 + mins
                            still_rotting = True
                        # upper orange rots
                        if (index_row-1 >= 0) and (
                           grid[index_row-1][index_col] == 1):
                            grid[index_row-1][index_col] = 3 + mins
                            still_rotting = True
                        # bottom orange rots
                        if (index_row+1 < rows) and (
                           grid[index_row+1][index_col] == 1):
                            grid[index_row+1][index_col] = 3 + mins
                            still_rotting = True
        return mins

    def evaluation(self, grid: List[List[int]]) -> Dict[str, bool]:
        status = {}
        status['fresh'] = False
        status['rotten'] = False
        for row in grid:
            if 1 in row:
                status['fresh'] = True
                if status['rotten'] is True:
                    break
            if 2 in row:
                status['rotten'] = True
                if status['fresh'] is True:
                    break
        return status

    def printGrid(self, grid: List[List[int]]) -> None:
        for col in grid:
            print(col)
        print()


class TestOrangesRotting(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testOrangesRotting_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

        mins = self.sol.orangesRotting(grid)

        self.assertEqual(mins, 4)

    def testOrangesRotting_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

        mins = self.sol.orangesRotting(grid)

        self.assertEqual(mins, -1)

    def testOrangesRotting_3(self):
        grid = [[0, 2]]

        mins = self.sol.orangesRotting(grid)

        self.assertEqual(mins, 0)


if __name__ == "__main__":
    unittest.main()
