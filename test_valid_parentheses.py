import unittest


class Solution():
    def is_valid(self, s: str) -> bool:
        list_s = list(s)
        list_opening_brackets = []
        for bracket in list_s:
            if bracket in ['{', '[', '(']:
                if bracket == '{':
                    list_opening_brackets.append('}')
                elif bracket == '[':
                    list_opening_brackets.append(']')
                else:
                    list_opening_brackets.append(')')
            elif list_opening_brackets:
                if bracket == list_opening_brackets[-1]:
                    list_opening_brackets.pop()
                else:
                    return False
            else:
                return False
        if list_opening_brackets:
            return False
        return True


class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_valid_empty(self):
        self.assertTrue(self.sol.is_valid(""))

    def test_is_valid_only_closing_bracket(self):
        self.assertFalse(self.sol.is_valid(")"))

    def test_is_valid_only_opening_bracket(self):
        self.assertFalse(self.sol.is_valid("("))

    def test_is_valid_one_bracket(self):
        self.assertTrue(self.sol.is_valid("()"))

    def test_is_valid_two_brackets(self):
        self.assertTrue(self.sol.is_valid("()[]{}"))

    def test_is_valid_mixed_bracket(self):
        self.assertFalse(self.sol.is_valid("(]"))

    def test_is_valid_mixed_brackets(self):
        self.assertFalse(self.sol.is_valid("([)]"))

    def test_is_valid_enclosing_brackets(self):
        self.assertTrue(self.sol.is_valid("{[]}()"))

    def test_is_valid_enclosing_brackets_false(self):
        self.assertFalse(self.sol.is_valid("{[]"))
