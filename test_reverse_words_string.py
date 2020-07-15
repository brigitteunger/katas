import unittest
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        words = s.split(' ')

        words = [word.strip(" ") for word in words if word.strip(" ") != ""]
        words.reverse()

        return " ".join(words)


class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testReverseWords_1(self):
        s = "the sky is blue"

        reversed_s = self.sol.reverseWords(s)

        self.assertEqual(reversed_s, "blue is sky the")

    def testReverseWords_2(self):
        s = "  hello world!  "

        reversed_s = self.sol.reverseWords(s)

        self.assertEqual(reversed_s, "world! hello")

    def testReverseWords_3(self):
        s = "a good   example"

        reversed_s = self.sol.reverseWords(s)

        self.assertEqual(reversed_s, "example good a")


if __name__ == "__main__":
    unittest.main()
