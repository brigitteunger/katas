import unittest


class Solution:
    def titleToNumber(self, s: str) -> int:
        if s == '':
            return 0

        num = 0
        len_s = len(s)
        for index, letter in enumerate(s):
            num += self.letterToNumber(letter)*(26**(len_s-index-1))
        return num

    def letterToNumber(self, s: str) -> int:
        return ord(s)-64


class TestTitleToNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testOrangesRotting_A(self):
        title = "A"

        num = self.sol.titleToNumber(title)

        self.assertEqual(num, 1)

    def testOrangesRotting_B(self):
        title = "B"

        num = self.sol.titleToNumber(title)

        self.assertEqual(num, 2)

    def testOrangesRotting_2(self):
        title = "AB"

        num = self.sol.titleToNumber(title)

        self.assertEqual(num, 28)

    def testOrangesRotting_3(self):
        title = "ZY"

        num = self.sol.titleToNumber(title)

        self.assertEqual(num, 701)


if __name__ == "__main__":
    unittest.main()
