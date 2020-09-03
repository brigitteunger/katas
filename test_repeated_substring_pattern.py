import unittest
from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        len_s = len(s)
        if len_s == 1:
            return False
        elif len_s == 2:
            return s[0] == s[1]
        elif len_s == 3:
            return s[0:1] == s[1:2]
        else:
            middle = len_s//2
            if len_s % 2 == 1:
                middle -= 1
            for i in range(1, middle+1):
                if s[0:len_s-i] == s[i:]:
                    return True
            return False


class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testRepeatedSubstringPattern_1(self):
        s = "abab"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)

    def testRepeatedSubstringPattern_2(self):
        s = "aba"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertFalse(valid)

    def testRepeatedSubstringPattern_3(self):
        s = "abcabcabcabc"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)

    def testRepeatedSubstringPattern_4(self):
        s = ""

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertFalse(valid)

    def testRepeatedSubstringPattern_5(self):
        s = "abcdefabcdef"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)

    def testRepeatedSubstringPattern_6(self):
        s = "abcabcdabcabcd"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)

    def testRepeatedSubstringPattern_7(self):
        s = "a"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertFalse(valid)

    def testRepeatedSubstringPattern_8(self):
        s = "aa"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)

    def testRepeatedSubstringPattern_9(self):
        s = "aaa"

        valid = self.sol.repeatedSubstringPattern(s)

        self.assertTrue(valid)


if __name__ == "__main__":
    unittest.main()
