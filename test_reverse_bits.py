import unittest
from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = format(n, '032b')
        list_bin = list(bin_str)
        list_bin.reverse()
        reversed_str_bin = ''.join(list_bin)
        reversed_int = int(reversed_str_bin, 2)
        return reversed_int


class TestReverseBist(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testReverseBists43261596(self):
        n = 43261596

        reversed_n = self.sol.reverseBits(n)

        self.assertEqual(reversed_n, 964176192)

    def testReverseBists4294967293(self):
        n = 4294967293

        reversed_n = self.sol.reverseBits(n)

        self.assertEqual(reversed_n, 3221225471)


if __name__ == "__main__":
    unittest.main()
