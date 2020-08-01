import unittest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return False

        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word.istitle():
            return True
        else:
            return False


class TestDdetectCapitalUse(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testDetectCapitalUseAllCapitals(self):
        word = "USA"

        result = self.sol.detectCapitalUse(word)

        self.assertTrue(result)

    def testDetectCapitalUseNoCapitals(self):
        word = "leetcode"

        result = self.sol.detectCapitalUse(word)

        self.assertTrue(result)

    def testDetectCapitalUseFirstCapitals(self):
        word = "Google"

        result = self.sol.detectCapitalUse(word)

        self.assertTrue(result)

    def testDetectCapitalUseOneCapitalFalse(self):
        word = "gooGle"

        result = self.sol.detectCapitalUse(word)

        self.assertFalse(result)

    def testDetectCapitalUseTwoCapitalFalse(self):
        word = "GooGle"

        result = self.sol.detectCapitalUse(word)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
