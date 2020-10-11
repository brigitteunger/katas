import unittest
import string
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        visited = {key: False for key in counter.keys()}

        for letter in s:
            counter[letter] -= 1
            if visited[letter]:
                continue
            while stack and letter < stack[-1] and counter[stack[-1]] > 0:
                visited[stack[-1]] = False
                stack.pop()
            stack.append(letter)
            visited[letter] = True
        return "".join(stack)


class TestRemoveDuplicateLetters(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testRemoveDuplicateLetters_1(self):
        s = "bcabc"

        word = self.sol.removeDuplicateLetters(s)

        self.assertEqual(word, "abc")

    def testRemoveDuplicateLetters_2(self):
        s = "cbacdcbc"

        word = self.sol.removeDuplicateLetters(s)

        self.assertEqual(word, "acdb")


if __name__ == "__main__":
    unittest.main()
