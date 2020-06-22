import unittest
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return None

        rows = len(dungeon)
        cols = len(dungeon[0])

        hp_to_enter = [[None]*cols for row in dungeon]

        for row in range(rows-1, -1, -1):
            # self.print_dungon(hp_to_enter)
            for col in range(cols-1, -1, -1):

                if row + 1 == rows:
                    neigbor_bottom = None
                else:
                    neigbor_bottom = hp_to_enter[row+1][col]

                if col + 1 == cols:
                    neighbor_right = None
                else:
                    neighbor_right = hp_to_enter[row][col+1]

                hp_to_enter[row][col] = self.calc_min_HP(
                                            dungeon[row][col],
                                            neighbor_right,
                                            neigbor_bottom
                                            )
        # self.print_dungon(hp_to_enter)
        return hp_to_enter[0][0]

    def calc_min_HP(self, val_cell: int, neighbor_right: int,
                    neigbor_bottom: int) -> int:
        if neigbor_bottom is None and neighbor_right is None:
            min_neighbor = 1
        elif neigbor_bottom is None:
            min_neighbor = neighbor_right
        elif neighbor_right is None:
            min_neighbor = neigbor_bottom
        else:
            min_neighbor = min(neigbor_bottom, neighbor_right)

        if val_cell <= 0:
            min_HP = min_neighbor - val_cell
            return min_HP

        else:  # val_cell > 0:
            if min_neighbor <= val_cell:
                return 1
            else:  # if min_neighbor > val_cell:
                min_HP = min_neighbor - val_cell
                return min_HP

    def print_dungon(self,  dungeon: List[List[int]]) -> None:
        print()
        for row in dungeon:
            [print('{:^5}'.format(elem), end="") for elem in row]
            print()
        print()


class TestCalculateMinimumHP(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_calculate_minimum_hp_3_4(self):
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5], [0, 0, 0]]

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, 7)

    def test_calculate_minimum_hp_3_3(self):
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, 7)

    def test_calculate_minimum_hp_1_1_4(self):
        dungeon = [[-3]]

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, 4)

    def test_calculate_minimum_hp_1_1_1(self):
        dungeon = [[1]]

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, 1)

    def test_calculate_minimum_hp_none(self):
        dungeon = []

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, None)

    def test_calculate_minimum_hp_7_5(self):
        # Test mit HP min in der mitte sehr niedrig
        dungeon = [[-1, -1, 3, 1, -1, 1, -1],
                   [-10, -10, -10, -5, -10, -10, 1],
                   [-10, -10, -10, -10, 20, -1, 4],
                   [-10, -10, -10, -10, -10, -10, -5],
                   [-10, -10, -10, -10, -10, -10, 1]]

        min_hp = self.sol.calculateMinimumHP(dungeon)

        self.assertEqual(min_hp, 3)


if __name__ == "__main__":
    unittest.main()
    test_ = TestCalculateMinimumHP()
    test_.setUp()
    test_.test_calculate_minimum_hp_3_3()
