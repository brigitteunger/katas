import unittest
from typing import List
from data_convert_string_in_k_moves import s_2, t_2, k_2, s_3, t_3, k_3


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        num_distance = [0] * 26
        for i in range(len(s)):
            shifts = self.num_shifts(s[i], t[i])
            if shifts != 0:
                num_distance[shifts] += 1
        maxx = 0
        for j in range(26):
            num = num_distance[j]
            if num >= 1:
                s = j + 26 * (num - 1)
                if s > maxx:
                    maxx = s
        if maxx <= k:
            return True
        else:
            return False

    def num_shifts(self, first: str, second: str) -> int:
        ord_1 = ord(first)
        ord_2 = ord(second)
        if ord_1 <= ord_2:
            return ord_2 - ord_1
        else:
            return 26 - (ord_1 - ord_2)


class TestcanConvertString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canConvertString_1(self):
        s = "input"
        t = "ouput"
        k = 9

        result = self.sol.canConvertString(s, t, k)

        self.assertTrue(result)

    def test_canConvertString_2(self):
        s = "abc"
        t = "bcd"
        k = 10

        result = self.sol.canConvertString(s, t, k)

        self.assertFalse(result)

    def test_canConvertString_3(self):
        s = "aab"
        t = "bbb"
        k = 27

        result = self.sol.canConvertString(s, t, k)

        self.assertTrue(result)

    def test_canConvertString_4(self):
        s = "leetcode"
        t = "leetcode"
        k = 0

        result = self.sol.canConvertString(s, t, k)

        self.assertTrue(result)

    def test_canConvertString_5(self):
        s = "abc"
        t = "abcd"
        k = 1000

        result = self.sol.canConvertString(s, t, k)

        self.assertFalse(result)

    def test_canConvertString_6(self):
        s = s_2
        t = t_2
        k = k_2

        result = self.sol.canConvertString(s, t, k)

        self.assertTrue(result)

    def test_canConvertString_7(self):
        s = s_3
        t = t_3
        k = k_3

        result = self.sol.canConvertString(s, t, k)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
