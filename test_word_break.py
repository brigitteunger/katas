import unittest
from typing import List, Set
from data_word_break import s_2, wordDict_2


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return []

        set_words = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in set_words:
                    dp[i] = True
                    break
        return dp[-1]


class TestFindWords(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testWordBreak_1(self):
        s = "leetcode"
        word_dict = ["leet", "code"]

        segmented = self.sol.wordBreak(s, word_dict)

        self.assertTrue(segmented)

    def testWordBreak_2(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]

        segmented = self.sol.wordBreak(s, word_dict)

        self.assertTrue(segmented)

    def testWordBreak_3(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]

        segmented = self.sol.wordBreak(s, word_dict)

        self.assertFalse(segmented)

    def testWordBreak_4(self):
        s = "goalspecial"
        word_dict = ["go", "goal", "goals", "special"]

        segmented = self.sol.wordBreak(s, word_dict)

        self.assertTrue(segmented)

    def testWordBreak_5(self):
        s = s_2
        word_dict = wordDict_2

        segmented = self.sol.wordBreak(s, word_dict)

        self.assertFalse(segmented)


if __name__ == "__main__":
    unittest.main()
