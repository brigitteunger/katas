import unittest
from typing import Dict, List


class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.children: Dict[str, Trie] = {}  # mapping from character to Node
        self.end_of_word: bool = False

    def insert_backwards(self, word: str) -> None:
        """
        Inserts a word backwards into the trie.
        """
        for index in range(len(word)-1, -1, -1):
            if word[index] not in self.children:
                trie = Trie()
                self.children[word[index]] = trie
            self = self.children[word[index]]
        self.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        for letter in word:
            if letter in self.children:
                self = self.children[letter]
                if self.end_of_word:
                    return True
            else:
                return False
        return False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.my_query = ""
        self.len_longest_word = 0
        self.len_query = 0
        self.my_trie = Trie()
        for word in words:
            self.my_trie.insert_backwards(word)
            self.len_longest_word = max(self.len_longest_word, len(word))

    def query(self, letter: str) -> bool:
        if self.len_query == self.len_longest_word:
            self.my_query = letter + self.my_query[:self.len_query-1]
        else:
            self.my_query = letter + self.my_query

        return self.my_trie.search(self.my_query)


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.my_trie = Trie()
        self.my_trie.insert_backwards("home")
        self.my_trie.insert_backwards("house")
        self.my_trie.insert_backwards("ho")

    def testTrieTrue_1(self):
        self.assertTrue(self.my_trie.search("emoh"))

    def testTrieFalse_1(self):
        self.assertFalse(self.my_trie.search("emo"))

    def testTrieFalse_2(self):
        self.assertFalse(self.my_trie.search("home"))

    def testTrieTrue_2(self):
        self.assertTrue(self.my_trie.search("oh"))


class TestStreamChecker(unittest.TestCase):
    def testStreamChecker_1(self):
        self.sol = StreamChecker(["cd", "f", "kl"])

        self.assertFalse(self.sol.query('a'))
        self.assertFalse(self.sol.query('a'))
        self.assertFalse(self.sol.query('b'))
        self.assertFalse(self.sol.query('c'))
        self.assertTrue(self.sol.query('d'))
        self.assertFalse(self.sol.query('e'))
        self.assertTrue(self.sol.query('f'))
        self.assertFalse(self.sol.query('g'))
        self.assertFalse(self.sol.query('h'))
        self.assertFalse(self.sol.query('i'))
        self.assertFalse(self.sol.query('j'))
        self.assertFalse(self.sol.query('k'))
        self.assertTrue(self.sol.query('l'))


if __name__ == "__main__":
    unittest.main()
