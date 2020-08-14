import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s or s == '':
            return 0

        num_char = Counter(s)
        nums = 0
        odd = False
        for val in num_char.values():
            if val % 2 == 0:
                nums += val
            else:
                odd = True
                nums += (val-1)
        if odd:
            nums += 1

        return nums


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestPalindrome_7(self):
        self.assertEqual(self.sol.longestPalindrome('abccccdd'), 7)

    def test_longestPalindrome_0(self):
        self.assertEqual(self.sol.longestPalindrome(''), 0)


if __name__ == "__main__":
    unittest.main()
