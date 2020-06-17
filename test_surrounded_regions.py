import unittest
from typing import List, Dict


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        label_coordinates = {}
        self.find_areas(board, label_coordinates)
        self.close_areas(board, label_coordinates)

    def find_areas(self,  board: List[List[str]],
                   label_coordinates: Dict[int, List[List[int]]]) -> None:
        label = 1

        # first row
        for col in range(0, len(board[0])):
            if board[0][col] != 'X':
                if col == 0:
                    board[0][0] = label
                    label_coordinates[label] = [[0, 0]]
                    label += 1
                    continue
                if board[0][col-1] != 'X':
                    board[0][col] = board[0][col-1]
                    label_coordinates[board[0][col-1]].append([0, col])
                else:
                    board[0][col] = label
                    label_coordinates[label] = [[0, col]]
                    label += 1

        # first col:
        for row in range(1, len(board)):
            if board[row][0] != 'X':
                if board[row-1][0] != 'X':
                    board[row][0] = board[row-1][0]
                    label_coordinates[board[row-1][0]].append([row, 0])
                else:
                    board[row][0] = label
                    label_coordinates[label] = [[row, 0]]
                    label += 1

        for row in range(1, len(board)):
            for col in range(1, len(board[row])):
                if board[row][col] != 'X':
                    # above
                    if board[row-1][col] != 'X':
                        board[row][col] = board[row-1][col]
                        label_coordinates[board[row-1][col]].append([row, col])
                        if board[row][col-1] != 'X' and col > 0:
                            if board[row-1][col] != board[row][col-1]:
                                self.merge_area(board, label_coordinates,
                                                board[row][col-1],
                                                board[row-1][col])
                    # left
                    elif board[row][col-1] != 'X':
                        board[row][col] = board[row][col-1]
                        label_coordinates[board[row][col-1]].append([row, col])
                    else:
                        board[row][col] = label
                        label_coordinates[label] = [[row, col]]
                        label += 1

    def merge_area(self, board: List[List[str]],
                   label_coordinates: Dict[int, List[List[int]]],
                   key_1: int,
                   key_2: int) -> None:
        for coordinates in label_coordinates[key_2]:
            row = coordinates[0]
            col = coordinates[1]
            board[row][col] = key_1
            label_coordinates[key_1].append([row, col])

        del label_coordinates[key_2]

    def close_areas(self, board: List[List[str]],
                    label_coordinates: Dict[int, List[List[int]]]) -> None:
        boarder_left = 0
        boarder_right = len(board[0]) - 1
        boarder_top = 0
        boarder_bottom = len(board) - 1

        for key in label_coordinates.keys():
            no_boarder = True
            for coordinate in label_coordinates[key]:
                row = coordinate[0]
                col = coordinate[1]
                if col == boarder_left or col == boarder_right:
                    self.close_area(board, label_coordinates[key], 'O')
                    no_boarder = False
                    break
                elif row == boarder_top or row == boarder_bottom:
                    self.close_area(board, label_coordinates[key], 'O')
                    no_boarder = False
                    break

            if no_boarder is True:
                self.close_area(board, label_coordinates[key], 'X')

    def close_area(self, board: List[List[str]],
                   coordinates: List[List[int]], val: str) -> None:
        for coordinate in coordinates:
            row = coordinate[0]
            col = coordinate[1]
            board[row][col] = val

    def print_board(self, board: List[List[str]]) -> None:
        print()
        for row in board:
            [print('{:^5}'.format(elem), end="") for elem in row]
            print()
        print()


class TestSolve(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solve_three_times_three(self):
        board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        expected = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_only_zeros(self):
        board = [["O", "O"], ["O", "O"]]
        expected = [["O", "O"], ["O", "O"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_not_connected_not_sym(self):
        board = [["X", "X", "X", "X",  "X"], ["X", "O", "O", "X",  "X"],
                 ["X", "X", "O", "X",  "X"], ["X", "O", "X", "X",  "X"]]
        expected = [["X", "X", "X", "X",  "X"], ["X", "X", "X", "X",  "X"],
                    ["X", "X", "X", "X",  "X"], ["X", "O", "X", "X",  "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_not_connected_tests(self):
        board = [["O", "O", "X", "O"],
                 ["X", "O", "O", "X"],
                 ["X", "O", "O", "X"],
                 ["O", "O", "X", "X"]]
        expected = [["O", "O", "X", "O"],
                    ["X", "O", "O", "X"],
                    ["X", "O", "O", "X"],
                    ["O", "O", "X", "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_not_connected(self):
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_not_connected_easy(self):
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
                 ["X", "O", "O", "X"], ["X", "X", "X", "X"]]
        expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"], ["X", "X", "X", "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_not_connected_hard(self):
        board = [['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'X', 'O', 'X'],
                 ['X', 'O', 'X', 'O', 'O', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'O']]
        expected = [['X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'O']]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_connected_hard(self):
        board = [['X', 'X', 'X', 'X', 'O'],
                 ['X', 'O', 'O', 'O', 'O'],
                 ['X', 'X', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'X', 'X']]
        expected = [['X', 'X', 'X', 'X', 'O'],
                    ['X', 'O', 'O', 'O', 'O'],
                    ['X', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'X', 'X', 'X'],
                    ['X', 'O', 'X', 'X', 'X']]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_border_connected(self):
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"], ["X", "O", "O", "X"]]
        expected = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"], ["X", "O", "O", "X"]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_empty_list(self):
        board = []
        expected = []

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_empty_list_in_list(self):
        board = [[]]
        expected = [[]]

        self.sol.solve(board)

        self.assertEqual(board, expected)

    def test_solve_one_element(self):
        board = [['O']]
        expected = [['O']]

        self.sol.solve(board)

        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
