import unittest
from data_word_search import board_1, words_1
from typing import List, Dict
from copy import deepcopy


class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.children: Dict[str, Trie] = {}  # mapping from character to Node
        self.end_of_word: bool = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for letter in word:
            if letter not in self.children:
                trie = Trie()
                self.children[letter] = trie
            self = self.children[letter]
        self.end_of_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        found_words = []
        trie_words = Trie()
        for word in words:
            trie_words.insert(word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.depth_first_search(board, row, col, trie_words,
                                        found_words)
        return found_words

    def depth_first_search(self,
                           board: List[List[str]],
                           row: int,
                           col: int,
                           trie_words: Trie,
                           found_words: List[str],
                           found_word: str = ""
                           ) -> None:
        letter = board[row][col]
        if letter in trie_words.children:
            found_word = found_word + letter
            trie_words = trie_words.children[letter]
            if trie_words.end_of_word:
                if found_word not in found_words:
                    found_words.append(found_word)

            board[row][col] = 'X'
            if col-1 >= 0:
                self.depth_first_search(board, row, col-1, trie_words,
                                        found_words, found_word)
            if col+1 < len(board[0]):
                self.depth_first_search(board, row, col+1, trie_words,
                                        found_words, found_word)
            if row-1 >= 0:
                self.depth_first_search(board, row-1, col, trie_words,
                                        found_words, found_word)
            if row+1 < len(board):
                self.depth_first_search(board, row+1, col, trie_words,
                                        found_words, found_word)
            board[row][col] = letter


class TestFindWords(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_words_4x4(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
            ]
        words = ["oath", "pea", "eat", "rain"]

        found_words = self.sol.findWords(board, words)

        self.assertEqual(sorted(found_words), ["eat", "oath"])

    def test_find_words_5x4(self):
        # test: do not use same letter twice
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['e', 'a', 't', 'r'],
            ['i', 'f', 'a', 'e']
            ]
        words = ["treat", "pea", "eat", "rain", ""]

        found_words = self.sol.findWords(board, words)

        self.assertEqual(found_words, ["eat"])

    def test_find_words_empty(self):
        board = []
        words = ["oath", "pea", "eat", "rain", ""]

        found_words = self.sol.findWords(board, words)

        self.assertEqual(found_words, [])

    def test_find_words_abc(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["ab", "cb", "ad", "bd", "ac", "ca", "da",
                 "bc", "db", "adcb", "dabc", "abb", "acb"]

        found_words = self.sol.findWords(board, words)

        self.assertEqual(found_words,
                         ["ab", "ac", "bd", "ca", "db"])

    def test_find_words_long(self):
        found_words = self.sol.findWords(board_1, words_1)

        self.assertEqual(found_words,
                         ['aaaaaaaaaaaaaaaa',
                          'aaaaaaaaaaaaaaac',
                          'aaaaaaaaaaaaaadc',
                          'aaaaaaaaaaaaaade',
                          'aaaaaaaaaaaaaadh',
                          'aaaaaaaaaaaaaabc',
                          'aaaaaaaaaaaaaabf',
                          'aaaaaaaaaaaaaaae',
                          'aaaaaaaaaaaaaaed',
                          'aaaaaaaaaaaaaaei',
                          'aaaaaaaaaaaaaacb',
                          'aaaaaaaaaaaaaacd',
                          'aaaaaaaaaaaaaacg',
                          'aaaaaaaaaaaaaaad',
                          'aaaaaaaaaaaaaaab'])


if __name__ == "__main__":
    unittest.main()
