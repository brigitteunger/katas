import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        even_longest_palindrome = ''
        odd_longest_palindrome = ''
        s_list = list(s)

        if len(s_list) == 1:
            odd_longest_palindrome = s_list[0]

        for index in range(1,len(s_list)):
            temp_even_longest_palindrome = self.find_longest_palindrome_even(s_list, index)
            if len(temp_even_longest_palindrome) > len(even_longest_palindrome):
                even_longest_palindrome = temp_even_longest_palindrome

            temp_odd_longest_palindrome = self.find_longest_palindrome_odd(s_list, index)
            if len(temp_odd_longest_palindrome) > len(odd_longest_palindrome):
                odd_longest_palindrome = temp_odd_longest_palindrome

         
        if len(even_longest_palindrome) > len(odd_longest_palindrome):
            longest_palindrome = even_longest_palindrome
        else:
            longest_palindrome = odd_longest_palindrome
        
        return longest_palindrome

    def find_longest_palindrome_odd(self,s_list: list,index: int) -> str:
        element_left = index
        element_right_odd = len(s_list)-index-1
        longest_palindrome = s_list[index]
        for offset in range(min(element_left,element_right_odd)):
                if s_list[index-1-offset] == s_list[index+offset+1]:
                    longest_palindrome = s_list[index-1-offset] + longest_palindrome + s_list[index+offset+1]
                else:                    
                    break 

        return longest_palindrome 

    def find_longest_palindrome_even(self,s_list: list,index: int) -> str:
        element_left = index
        element_right_even = len(s_list)-index
        longest_palindrome = ''
        for offset in range(min(element_left,element_right_even)):
                if s_list[index-1-offset] == s_list[index+offset]:
                    longest_palindrome = s_list[index-1-offset] + longest_palindrome + s_list[index+offset]
                else:                    
                    break 

        return longest_palindrome         


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestPalindrome_a(self):
        self.assertEqual(self.sol.longestPalindrome('a'), 'a')   

    def test_longestPalindrome_abc(self):
        self.assertIn(self.sol.longestPalindrome('abc'), ['a','b','c'])   

    def test_longestPalindrome_babad(self):
        self.assertIn(self.sol.longestPalindrome('babad'), ['bab','aba'])

    def test_longestPalindrome_acbabcx(self):
        self.assertEqual(self.sol.longestPalindrome('acbabcx'), 'cbabc')    

    def test_longestPalindrome_cbbd(self):
        self.assertEqual(self.sol.longestPalindrome('cbbd'), 'bb')

    def test_longestPalindrome_cbbc(self):
        self.assertEqual(self.sol.longestPalindrome('cbbc'), 'cbbc')
    
    def test_longestPalindrome_acbbcx(self):
        self.assertEqual(self.sol.longestPalindrome('acbbcx'), 'cbbc')

    def test_longestPalindrome_abbacxdx(self):
        self.assertEqual(self.sol.longestPalindrome('abbacxdx'), 'abba')    
