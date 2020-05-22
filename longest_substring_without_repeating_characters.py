class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        length_longest_substring = 0
        index = 0
        for index in range(len(s)):
            if s[index] in substring:
                if length_longest_substring < len(substring):
                    length_longest_substring = len(substring) 
                kill = substring.index(s[index]) 
                substring = substring[kill+1 :]
                substring.append(s[index])                
            else:    
                substring.append (s[index])

        if length_longest_substring < len(substring):
            length_longest_substring = len(substring)        
        
        return length_longest_substring  

sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))