import unittest
from typing import List


class Solution:
    def minInsertions(self, s: str) -> int:
        if s == "" or s is None:
            return 0

        nums = 0
        expected = 0
        index = -1
        max_index_s = len(s) - 1
        while index < max_index_s:
            index += 1
            if s[index] == '(':
                expected += 1
            elif index < max_index_s and s[index+1] == ')':
                index += 1
                if expected == 0:
                    nums += 1
                else:
                    expected -= 1
            else:  # letter == )
                if expected == 0:
                    nums += 2
                else:
                    expected -= 1
                    nums += 1
        return nums + (2*expected)

    def minInsertions_long(self, s: str) -> int:
        if s == "" or s is None:
            return 0

        s = list(s)
        for i in range(len(s)-2, -1, -1):
            if s[i] == ")" and s[i+1] == ")":
                s[i] = "2"
                del s[i+1]
        print(s)

        nums = 0
        expected = 0

        for letter in s:
            if letter == '(':
                expected += 1
            elif letter == '2':
                if expected == 0:
                    nums += 1
                else:
                    expected -= 1
            else:  # letter == )
                if expected == 0:
                    nums += 2
                else:
                    expected -= 1
                    nums += 1
        return nums + (2*expected)


class TestMinInsertions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canConvertString_1(self):
        s = "(()))"
        self.assertEqual(self.sol.minInsertions(s), 1)

    def test_canConvertString_2(self):
        s = "())"
        self.assertEqual(self.sol.minInsertions(s), 0)

    def test_canConvertString_3(self):
        s = "))())("
        self.assertEqual(self.sol.minInsertions(s), 3)

    def test_canConvertString_4(self):
        s = "(((((("
        self.assertEqual(self.sol.minInsertions(s), 12)

    def test_canConvertString_5(self):
        s = ")))))))"
        self.assertEqual(self.sol.minInsertions(s), 5)

    def test_canConvertString_6(self):
        s = "()()()()()("
        self.assertEqual(self.sol.minInsertions(s), 7)


if __name__ == "__main__":
    unittest.main()
