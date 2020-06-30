import unittest
from typing import Dict, Optional, Any


class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        # Note that using a dictionary for children (as in this implementation)
        # would not by default lexicographically sort the children, which is
        # required by the lexicographic sorting mentioned in the next section
        # (Sorting).
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

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        for letter in word:
            if letter in self.children:
                self = self.children[letter]
            else:
                return False
        if self.end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts
        with the given prefix.
        """
        for letter in prefix:
            if letter in self.children:
                self = self.children[letter]
            else:
                return False
        return True


class TestImplementTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")

    def test_search_trie_true(self):
        self.assertTrue(self.trie.search("apple"))

    def test_search_trie_false(self):
        self.assertFalse(self.trie.search("app"))

    def test_starts_with(self):
        self.assertTrue(self.trie.startsWith("app"))

    def test_search_trie_true_app(self):
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))


if __name__ == "__main__":
    unittest.main()
