import unittest
from typing import Tuple
from data_test_longest_duplicate_substring import data, data_2, data_3, data_4
from collections import defaultdict


class Solution():
    def longestDupSubstring(self, S: str) -> str:
        size_S = len(S)
        left_index = 0
        right_index = size_S
        ex_duplicate = ""
        while left_index < right_index:
            size = int((right_index-left_index)/2) + left_index
            duplicate = self.find_duplicate(S, size, size_S)
            if duplicate != "":
                ex_duplicate = duplicate
                left_index = size + 1
            else:
                right_index = size
        return ex_duplicate  # self.find_duplicate(S, left_index-1, size_S)

    def find_duplicate(self, S: str, size: int, size_S: int) -> str:
        dict_S = {}
        base = 26
        modulus = 10 ** 9 + 7
        max_base = pow(base, size - 1, modulus)
        actual_hash = 0

        for i in range(0, size):
            actual_hash = (actual_hash * base + ord(S[i])) % modulus
        dict_S = defaultdict(list)
        dict_S[actual_hash].append(size-1)

        for j, i in enumerate(S[size:]):
            actual_hash -= ord(S[j]) * max_base
            actual_hash = (actual_hash * base + ord(i)) % modulus
            if actual_hash in dict_S:
                substring = S[j + 1:j + size + 1]
                for v in dict_S[actual_hash]:
                    if substring == S[v-size+1:v+1]:
                        return substring
            dict_S[actual_hash].append(j+size)
        return ""

    def longestDupSubstring_easy_long_sol(self, S: str) -> str:
        equal_sub = []
        size_equal_sub = 0

        list_s = list(S)
        size_s = len(list_s)
        min_size = 1
        for i in range(size_s-1):
            for j in range(i+1, size_s):
                min_size = size_equal_sub
                for size in range(min_size, size_s-i):
                    found_one = False
                    sub_1 = list_s[i:size+i]
                    sub_2 = list_s[j:size+j]
                    if sub_1 == sub_2:
                        found_one = True
                        if size > size_equal_sub:
                            equal_sub = sub_1
                            size_equal_sub = size
                    if not found_one:
                        break

        longest_substring = ''.join(equal_sub)
        return longest_substring


class TestLongestDupSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestDupSubstring_akyjakyj(self):
        S = "moakyjakyjmo"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "akyj")

    def test_longestDupSubstring_banana(self):
        S = "banana"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "ana")

    def test_longestDupSubstring_abcd(self):
        S = "abcd"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "")

    def test_longestDupSubstring_aa(self):
        S = "aa"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "a")

    def test_longestDupSubstring_anadfasasdfana(self):
        S = "anadfsasdfana"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "ana")

    def test_longestDupSubstring_aaa(self):
        S = "aaa"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "aa")

    def test_longestDupSubstring_a(self):
        S = "a"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "")

    def test_longestDupSubstring_alkientad(self):
        S = "alkientad"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "a")

    def test_longestDupSubstring_nananananan(self):
        S = "nananananan"

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "nanananan")

    def test_longestDupSubstring_data(self):
        S = data

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "akyj")

    def test_longestDupSubstring_data_2(self):
        S = data_2

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "maoli")

    def test_longestDupSubstring_data_3(self):
        S = data_3
        pass_test = False

        actual = self.sol.longestDupSubstring(S)
        if actual == "rbruh" or actual == "luqvg":
            pass_test = True

        self.assertTrue(pass_test)

    def test_longestDupSubstring_data_4(self):
        S = data_4

        actual = self.sol.longestDupSubstring(S)

        self.assertEqual(actual, "bbaababaabbbbaabaaaababbbabbbb")


if __name__ == "__main__":
    unittest.main()
