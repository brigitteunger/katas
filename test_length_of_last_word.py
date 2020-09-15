import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.rstrip()
        words = s.split(' ')
        return len(words[-1])


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLengthOfLastWord_1(self):
        s = "Hello World"

        length = self.sol.lengthOfLastWord(s)

        self.assertEqual(length, 5)

    def testLengthOfLastWord_2(self):
        s = "a "

        length = self.sol.lengthOfLastWord(s)

        self.assertEqual(length, 1)


if __name__ == "__main__":
    unittest.main()
