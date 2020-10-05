import unittest


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binaries = list(format(N, 'b'))
        len_binaries = len(binaries)
        num = 0
        for i in range(len_binaries):
            if binaries[i] == "0":
                num += (2**(len_binaries-i-1))
        return num


class TestBitwiseComplement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testBitwiseComplement_1(self):
        N = 5

        complement = self.sol.bitwiseComplement(N)

        self.assertEqual(complement, 2)

    def testBitwiseComplement_2(self):
        N = 7

        complement = self.sol.bitwiseComplement(N)

        self.assertEqual(complement, 0)

    def testBitwiseComplement_3(self):
        N = 10

        complement = self.sol.bitwiseComplement(N)

        self.assertEqual(complement, 5)


if __name__ == "__main__":
    unittest.main()
