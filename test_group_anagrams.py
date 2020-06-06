import unittest
from typing import List


class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        anagrams = []
        sorted_anagrams = {}
        i = 0
        for str_ in strs:
            sorted_str = str(sorted(str_))
            if sorted_str in sorted_anagrams:
                index = sorted_anagrams[sorted_str]
                anagrams[index].append(str_)
            else:
                anagrams.append([str_])
                sorted_anagrams[sorted_str] = i
                i = i+1

        return anagrams


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertElementsInListEqual(self, actual: List[List[str]],
                                  expected: List[List[str]]) -> None:
        actual_sorted = self.deep_sort(actual)
        expected_sorted = self.deep_sort(expected)

        self.assertEqual(actual_sorted, expected_sorted)

    def deep_sort(self, lists: List[List[str]]) -> List[List[str]]:
        if not lists:
            return [[]]

        sorted_lists = []
        for list_ in lists:
            sorted_lists.append(sorted(list_))

        return sorted(sorted_lists)

    def test_group_anagrams_empty(self):
        strs = []
        expected_anagrams = [[]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertEqual(actual_anagrams, expected_anagrams)

    def test_group_anagrams_standard(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat", "s"]
        expected_anagrams = [["ate", "eat", "tea"],
                             ["nat", "tan"],
                             ["bat"],
                             ["s"]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertElementsInListEqual(actual_anagrams, expected_anagrams)

    def test_group_anagrams_one_empty(self):
        strs = ["eat", "tea", "tan", "ate", "nat", ""]
        expected_anagrams = [["ate", "eat", "tea"],
                             ["nat", "tan"],
                             [""]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertElementsInListEqual(actual_anagrams, expected_anagrams)

    def test_group_anagrams_no_group(self):
        strs = ["eat", "tear", "tanc", "eats", "nat", "bat"]
        expected_anagrams = [["eat"],
                             ["tear"],
                             ["tanc"],
                             ["eats"],
                             ["nat"],
                             ["bat"]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertElementsInListEqual(actual_anagrams, expected_anagrams)

    def test_group_anagrams_all_in_one(self):
        strs = ["eat", "tea", "eta"]
        expected_anagrams = [["eat", "tea", "eta"]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertElementsInListEqual(actual_anagrams, expected_anagrams)

    def test_group_anagrams_all_in_one_same_elem(self):
        strs = ["eat", "tea", "eta", "eat"]
        expected_anagrams = [["eat", "tea", "eta", "eat"]]

        actual_anagrams = self.sol.groupAnagrams(strs)

        self.assertElementsInListEqual(actual_anagrams, expected_anagrams)


test_ = TestGroupAnagrams()
test_.setUp()
test_.test_group_anagrams_standard()
