import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        new_s = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                new_s += char.lower()

        if not new_s:
            return True

        middle_index = int(len(new_s)/2)

        if len(new_s) % 2 == 0:
            left_s = new_s[0:middle_index]
            right_s = new_s[middle_index:]
        else:
            left_s = new_s[0:middle_index+1]
            right_s = new_s[middle_index:]

        if left_s == right_s[::-1]:
            return True
        else:
            return False


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_palindrome_1(self):
        s = "A man, a plan, a canal: Panama"

        evaluation = self.sol.isPalindrome(s)

        self.assertTrue(evaluation)

    def test_is_palindrome_2(self):
        s = "race a car"

        evaluation = self.sol.isPalindrome(s)

        self.assertFalse(evaluation)

    def test_is_palindrome_3(self):
        s = "A man, a plan, a anal: Panama"

        evaluation = self.sol.isPalindrome(s)

        self.assertTrue(evaluation)

    def test_is_palindrome_4(self):
        s = "aa"

        evaluation = self.sol.isPalindrome(s)

        self.assertTrue(evaluation)

    def test_is_palindrome_4(self):
        s = "aaa"

        evaluation = self.sol.isPalindrome(s)

        self.assertTrue(evaluation)


if __name__ == "__main__":
    unittest.main()
