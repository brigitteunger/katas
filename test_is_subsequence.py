import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if t == "":
            return False

        s_list = list(s)
        t_list = list(t)

        size_s = len(s_list)
        s_index = 0
        s_letter = s_list[s_index]
        for t_letter in t_list:
            if t_letter is s_letter:
                if s_index == size_s-1:
                    return True
                else:
                    s_index += 1
                    s_letter = s_list[s_index]

        return False


class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_subsequence_true(self):
        s = "abc"
        t = "ahbgdc"

        actual = self.sol.isSubsequence(s, t)

        self.assertTrue(actual)

    def test_is_subsequence_false(self):
        s = "axc"
        t = "ahbgdc"

        actual = self.sol.isSubsequence(s, t)

        self.assertFalse(actual)

    def test_is_subsequence_both_empty(self):
        s = ""
        t = ""

        actual = self.sol.isSubsequence(s, t)

        self.assertTrue(actual)

    def test_is_subsequence_empty(self):
        s = ""
        t = "ahbgdc"

        actual = self.sol.isSubsequence(s, t)

        self.assertTrue(actual)

    def test_is_subsequence_only_one(self):
        s = "g"
        t = "ahbgdc"

        actual = self.sol.isSubsequence(s, t)

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
