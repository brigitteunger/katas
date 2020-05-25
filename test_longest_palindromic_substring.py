import unittest


class Solution:
    def longest_palindrome(self, s: str) -> str:
        even_palindrome = ''
        odd_palindrome = ''
        s_list = list(s)

        if len(s_list) == 1:
            odd_palindrome = s_list[0]

        for index in range(1, len(s_list)):
            tmp_even_palindrome = self.find_even_palindrome(s_list, index)
            if len(tmp_even_palindrome) > len(even_palindrome):
                even_palindrome = tmp_even_palindrome

            tmp_odd_palindrome = self.find_odd_palindrome(s_list, index)
            if len(tmp_odd_palindrome) > len(odd_palindrome):
                odd_palindrome = tmp_odd_palindrome

        if len(even_palindrome) > len(odd_palindrome):
            longest_palindrome = even_palindrome
        else:
            longest_palindrome = odd_palindrome

        return longest_palindrome

    def find_odd_palindrome(self, s_list: list, index: int) -> str:
        elem_left = index
        elem_right_odd = len(s_list) - index-1
        palindrome = s_list[index]
        for offset in range(min(elem_left, elem_right_odd)):
            if s_list[index-1-offset] == s_list[index+offset+1]:
                palindrome = (s_list[index-1-offset] + palindrome +
                              s_list[index+offset+1])
            else:
                break
        return palindrome

    def find_even_palindrome(self, s_list: list, index: int) -> str:
        elem_left = index
        elem_right_even = len(s_list)-index
        palindrome = ''
        for offset in range(min(elem_left, elem_right_even)):
            if s_list[index-1-offset] == s_list[index+offset]:
                palindrome = (s_list[index-1-offset] + palindrome +
                              s_list[index+offset])
            else:
                break
        return palindrome


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestPalindrome_a(self):
        self.assertEqual(self.sol.longest_palindrome('a'), 'a')

    def test_longestPalindrome_abc(self):
        self.assertIn(self.sol.longest_palindrome('abc'), ['a', 'b', 'c'])

    def test_longestPalindrome_babad(self):
        self.assertIn(self.sol.longest_palindrome('babad'), ['bab', 'aba'])

    def test_longestPalindrome_acbabcx(self):
        self.assertEqual(self.sol.longest_palindrome('acbabcx'), 'cbabc')

    def test_longestPalindrome_cbbd(self):
        self.assertEqual(self.sol.longest_palindrome('cbbd'), 'bb')

    def test_longestPalindrome_cbbc(self):
        self.assertEqual(self.sol.longest_palindrome('cbbc'), 'cbbc')

    def test_longestPalindrome_acbbcx(self):
        self.assertEqual(self.sol.longest_palindrome('acbbcx'), 'cbbc')

    def test_longestPalindrome_abbacxdx(self):
        self.assertEqual(self.sol.longest_palindrome('abbacxdx'), 'abba')
