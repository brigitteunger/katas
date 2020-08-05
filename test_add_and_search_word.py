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

    def search_with_dots(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        letter = word[0]
        if len(word) == 1:
            if letter == '.':
                for key in self.children.keys():
                    if self.children[key].end_of_word is True:
                        return True
                return False
            else:
                if letter in self.children:
                    return self.children[letter].end_of_word
                else:
                    return False
        else:
            if letter == '.':
                for key in self.children.keys():
                    if self.children[key].search_with_dots(word[1:]):
                        return True
                return False
            else:
                if letter in self.children:
                    return self.children[letter].search_with_dots(word[1:])
                else:
                    return False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' in word:
            return self.trie.search_with_dots(word)
        else:
            return self.trie.search(word)


class TestWordDictonary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def testAddWord_True(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("bad"))

    def testAddWord_False(self):
        self.word_dict.addWord("bad")
        self.assertFalse(self.word_dict.search("bat"))

    def testAddWord_False2(self):
        self.word_dict.addWord("bad")
        self.assertFalse(self.word_dict.search("badds"))

    def testAddWordDots_True(self):
        self.word_dict.addWord("ads")
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search(".ad"))

    def testAddWordDotsMiddle_True(self):
        self.word_dict.addWord("baad")
        self.assertTrue(self.word_dict.search("b.ad"))

    def testAddWordDots_False(self):
        self.word_dict.addWord("ads")
        self.assertFalse(self.word_dict.search(".ad"))

    def testAddWordDots_True_2(self):
        self.word_dict.addWord("ads")
        self.assertTrue(self.word_dict.search("..."))

    def testAddWordDots_False_2(self):
        self.word_dict.addWord("ads")
        self.assertFalse(self.word_dict.search("...."))

    def testAddWordChain_False(self):
        self.word_dict.addWord("bad")
        self.word_dict.addWord("dad")
        self.word_dict.addWord("mad")
        self.assertFalse(self.word_dict.search("pad"))
        self.assertTrue(self.word_dict.search("bad"))
        self.assertTrue(self.word_dict.search(".ad"))
        self.assertTrue(self.word_dict.search("b.."))


if __name__ == "__main__":
    unittest.main()
