import unittest
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        for key in t_dict.keys():
            if key not in s_dict:
                return key
            elif t_dict[key] != s_dict[key]:
                return key
        return ""


class TestFindTheDifference(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindTheDifference_1(self):
        s = "abcd"
        t = "abcde"

        difference = self.sol.findTheDifference(s, t)

        self.assertEqual(difference, "e")

    def testFindTheDifference_2(self):
        s = "abcd"
        t = "aabcd"

        difference = self.sol.findTheDifference(s, t)

        self.assertEqual(difference, "a")


if __name__ == "__main__":
    unittest.main()
