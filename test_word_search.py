import unittest
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if word == "":
            return True

        letters = list(word)
        len_letters = len(letters)
        for row in range(len(board)):
            for col in range(len(board[0])):
                exists = self.depth_first_search(board, row, col,
                                                 len_letters, letters)
                if exists:
                    return True
        return False

    def depth_first_search(self,
                           board: List[List[str]],
                           row: int,
                           col: int,
                           len_letters: int,
                           letters: List[str],
                           index: int = 0
                           ) -> bool:
        letter = board[row][col]
        letter_word = letters[index]
        if letter == letter_word:
            if len_letters-1 == index:
                return True
            else:
                board[row][col] = '-'
                if col-1 >= 0:
                    if self.depth_first_search(board, row, col-1,
                                               len_letters, letters, index+1):
                        return True
                if col+1 < len(board[0]):
                    if self.depth_first_search(board, row, col+1,
                                               len_letters, letters, index+1):
                        return True
                if row-1 >= 0:
                    if self.depth_first_search(board, row-1, col,
                                               len_letters, letters, index+1):
                        return True
                if row+1 < len(board):
                    if self.depth_first_search(board, row+1, col,
                                               len_letters, letters, index+1):
                        return True
                board[row][col] = letter
        else:
            return False


class TestFindWord(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_words_4x4_True(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
            ]
        word = "oath"

        exists = self.sol.exist(board, word)

        self.assertTrue(exists)

    def test_find_words_3x4_True(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
            ]
        word = "ABCCED"

        exists = self.sol.exist(board, word)

        self.assertTrue(exists)

    def test_find_words_3x4_False(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
            ]
        word = "ABCB"

        exists = self.sol.exist(board, word)

        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()
