import unittest
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not A:
            return []
        moves = []
        for next_elem in range(len(A), 0, -1):
            index = A.index(next_elem)
            if index == next_elem:
                continue
            else:
                # bring biggest wrong located num to first pos in A
                if index > 0:
                    A[:index+1] = reversed(A[:index+1])
                    moves.append(index+1)
                # bring it to its right position
                A[:next_elem] = reversed(A[:next_elem])
                moves.append(next_elem)

        return moves


class TestPancakeSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def flips(self, A: List[int], moves: List[int]) -> None:
        for move in moves:
            A[:move] = reversed(A[:move])

    def test_flips(self):
        A = [3, 2, 4, 1]
        moves = [4, 2, 4, 3]

        self.flips(A, moves)

        self.assertEqual(A, list(range(1, 5)))

    def test_pankcakes_sort_1(self):
        A = [3, 2, 4, 1]

        moves = self.sol.pancakeSort(A[:])
        self.flips(A, moves)

        self.assertEqual(A, list(range(1, len(A)+1)))

    def test_pankcakes_sort_2(self):
        A = [1, 2, 3]

        moves = self.sol.pancakeSort(A[:])
        self.flips(A, moves)

        self.assertEqual(A, list(range(1, 4)))

    def test_pankcakes_sort_3(self):
        A = [1]

        moves = self.sol.pancakeSort(A[:])
        self.flips(A, moves)

        self.assertEqual(A, [1])


if __name__ == "__main__":
    unittest.main()
