import unittest
from data_word_break_II import s_2, word_dict_2, expected_breaks_2
from typing import List, Set, Dict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []

        dict_words = {}
        set_words = set(wordDict)
        return self.find_words(s, set_words, dict_words)

    def find_words(self,
                   s: str,
                   set_words: Set[str],
                   dict_words: Dict[str, List[str]]):
        if not s:
            return ['']
        if s in dict_words:
            return dict_words[s]
        segments = []
        for i in range(1, len(s)+1):
            if s[:i] in set_words:
                set_word = self.find_words(s[i:], set_words, dict_words)
                for word in set_word:
                    segments.append((s[:i] + " " + word).strip())
        dict_words[s] = segments
        return dict_words[s]


class TestFindWords(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertDeepEqual(self,
                        actual_breaks: List[str],
                        expected_breaks: List[str]) -> None:
        actual_breaks.sort()
        expected_breaks.sort()

        self.assertEqual(actual_breaks, expected_breaks)

    def testWordBreak_1(self):
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        expected_breaks = [
                            "cats and dog",
                            "cat sand dog"
                           ]

        actual_breaks = self.sol.wordBreak(s, word_dict)

        self.assertDeepEqual(actual_breaks, expected_breaks)

    def testWordBreak_2(self):
        s = "pineapplepenapple"
        word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
        expected_breaks = [
                            "pine apple pen apple",
                            "pineapple pen apple",
                            "pine applepen apple"
                            ]

        actual_breaks = self.sol.wordBreak(s, word_dict)

        self.assertDeepEqual(actual_breaks, expected_breaks)

    def testWordBreak_3(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]

        actual_breaks = self.sol.wordBreak(s, word_dict)

        self.assertEqual(actual_breaks, [])

    def testWordBreak_4(self):
        s = "cbca"
        word_dict = ["bc", "ca"]

        actual_breaks = self.sol.wordBreak(s, word_dict)

        self.assertEqual(actual_breaks, [])

    def testWordBreak_5(self):
        s = s_2
        word_dict = word_dict_2
        expected_breaks = expected_breaks_2

        actual_breaks = self.sol.wordBreak(s, word_dict)

        self.assertDeepEqual(actual_breaks, expected_breaks)


if __name__ == "__main__":
    unittest.main()
