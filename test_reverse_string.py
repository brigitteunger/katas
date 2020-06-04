import unittest
from typing import List


class Solution():
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return []

        n = len(s)
        for i in range(int(n/2)):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp


class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_reverse_string_hello(self):
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]

        self.sol.reverseString(s)

        self.assertEqual(s, expected)

    def test_reverse_string_Hannah(self):
        s = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]

        self.sol.reverseString(s)

        self.assertEqual(s, expected)

    def test_reverse_string_empty(self):
        s = []
        expected = []

        self.sol.reverseString(s)

        self.assertEqual(s, expected)
