import pytest
from longest_substring_without_repeating_characters import Solution

class TestClass:
    
    def test_lengthOfLongestSubstring_aab(self):
        sol = Solution()
        assert  sol.lengthOfLongestSubstring("aab") == 2 

    def test_lengthOfLongestSubstring_abcabcbb(self):
        sol = Solution()
        assert  sol.lengthOfLongestSubstring("abcabcbb") == 3

    def test_lengthOfLongestSubstring_bbbbbb(self):
        sol = Solution()
        assert  sol.lengthOfLongestSubstring("bbbbbb") == 1

    def test_lengthOfLongestSubstrin_pwwkew(self): 
        sol = Solution()
        assert  sol.lengthOfLongestSubstring("pwwkew") == 3   
