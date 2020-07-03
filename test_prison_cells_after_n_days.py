import unittest
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cells_after = [0, 0, 0, 0, 0, 0, 0, 0]
        cell_after_days = []

        for days in range(1, N+1):
            for m in range(1, 7):
                if cells[m-1] == cells[m+1]:
                    cells_after[m] = 1
                else:
                    cells_after[m] = 0
            cells = cells_after[:]

            if cells in cell_after_days:
                num = N % (days-1)  # days-1 = len(cell_after_days)
                if num == 0:
                    return cell_after_days[-1]
                else:
                    return cell_after_days[num-1]
            else:
                cell_after_days.append(cells)

        return cells


class TestPrisonAfterNDays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_prison_after_1_days(self):
        cells = [0, 1, 0, 1, 1, 0, 0, 1]
        N = 1

        cells_after = self.sol.prisonAfterNDays(cells, N)

        self.assertEqual(cells_after,
                         [0, 1, 1, 0, 0, 0, 0, 0])

    def test_prison_after_7_days(self):
        cells = [0, 1, 0, 1, 1, 0, 0, 1]
        N = 7

        cells_after = self.sol.prisonAfterNDays(cells, N)

        self.assertEqual(cells_after,
                         [0, 0, 1, 1, 0, 0, 0, 0])

    def test_prison_after_1000000000_days(self):
        cells = [1, 0, 0, 1, 0, 0, 1, 0]
        N = 1000000000

        cells_after = self.sol.prisonAfterNDays(cells, N)

        self.assertEqual(cells_after,
                         [0, 0, 1, 1, 1, 1, 1, 0])

    def test_prison_after_574_days(self):
        cells = [0, 0, 0, 1, 1, 0, 1, 0]
        N = 574

        cells_after = self.sol.prisonAfterNDays(cells, N)

        self.assertEqual(cells_after,
                         [0, 0, 0, 1, 1, 0, 1, 0])

if __name__ == "__main__":
    unittest.main()
