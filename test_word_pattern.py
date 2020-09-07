import unittest


class Solution:
    def wordPattern(self, pattern: str, str_: str) -> bool:
        words = str_.split(" ")
        len_pattern = len(pattern)
        if len_pattern != len(words):
            return False
        pattern_dict = {}
        for index in range(len_pattern):
            if pattern[index] not in pattern_dict:
                if words[index] in words[:index]:
                    return False
                else:
                    pattern_dict[pattern[index]] = words[index]
            elif pattern_dict[pattern[index]] != words[index]:
                return False

        return True


class TestWordPattern(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testWordPattern_1(self):
        pattern = "abba"
        str_ = "dog cat cat dog"

        full_match = self.sol.wordPattern(pattern, str_)

        self.assertTrue(full_match)

    def testWordPattern_2(self):
        pattern = "abba"
        str_ = "dog cat cat fish"

        full_match = self.sol.wordPattern(pattern, str_)

        self.assertFalse(full_match)

    def testWordPattern_3(self):
        pattern = "aaaa"
        str_ = "dog cat cat dog"

        full_match = self.sol.wordPattern(pattern, str_)

        self.assertFalse(full_match)

    def testWordPattern_4(self):
        pattern = "abba"
        str_ = "dog dog dog dog"

        full_match = self.sol.wordPattern(pattern, str_)

        self.assertFalse(full_match)

    def testWordPattern_5(self):
        pattern = "aaa"
        str_ = "aa aa aa aa"

        full_match = self.sol.wordPattern(pattern, str_)

        self.assertFalse(full_match)


if __name__ == "__main__":
    unittest.main()
