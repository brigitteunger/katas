import unittest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = [int(x_) for x_ in list('{0:0b}'.format(x))]
        bin_y = [int(y_) for y_ in list('{0:0b}'.format(y))]

        size_x = len(bin_x)
        size_y = len(bin_y)

        if size_x < size_y:
            rest = [0] * (size_y-size_x)
            bin_x = rest + bin_x
        elif size_x > size_y:
            rest = [0] * (size_x-size_y)
            bin_y = rest + bin_y

        hamming_dist = 0
        for bit_x, bit_y in zip(bin_x, bin_y):
            if bit_x != bit_y:
                hamming_dist += 1

        return hamming_dist


class TestHammingDistance(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_hamming_distance_short_2(self):
        x = 1
        y = 4

        hammming_distance = self.sol.hammingDistance(x, y)

        self.assertEqual(hammming_distance, 2)

    def test_hamming_distance_0(self):
        x = 20
        y = 20

        hammming_distance = self.sol.hammingDistance(x, y)

        self.assertEqual(hammming_distance, 0)

    def test_hamming_distance_max(self):
        x = 0
        y = 2147483647

        hammming_distance = self.sol.hammingDistance(x, y)

        self.assertEqual(hammming_distance, 31)

    def test_hamming_distance_long_2(self):
        x = 14
        y = 2

        hammming_distance = self.sol.hammingDistance(x, y)

        self.assertEqual(hammming_distance, 2)


if __name__ == "__main__":
    unittest.main()
