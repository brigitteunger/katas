import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), '0b')

    def addBinaryBitByBit(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(a)
        diff = abs(len_a - len_b)
        if len_a > len_b:
            b = [0]*diff + b
        elif len_a < len_b:
            b = [0]*diff + a

        len_max = len(a)
        sum = [0]*len_max
        carry = 0

        for i in range(len_max-1, -1, -1):
            sum_bits = carry + int(a[i]) + int(b[i])
            if sum_bits == 0:
                sum[i] = '0'
                carry = 0
            elif sum_bits == 1:
                sum[i] = '1'
                carry = 0
            elif sum_bits == 2:
                sum[i] = '0'
                carry = 1
            else:  # sum_ == 3:
                sum[i] = '1'
                carry = 1

        first_letter = ''
        if carry == 1:
            first_letter = '1'

        sum_str = first_letter.join(sum)
        return sum_str


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testAddBinary11_1(self):
        a = "11"
        b = "1"

        sum_ = self.sol.addBinary(a, b)

        self.assertEqual(sum_, "100")

    def testAddBinary1010_1011(self):
        a = "1010"
        b = "1011"

        sum_ = self.sol.addBinary(a, b)

        self.assertEqual(sum_, "10101")

    def testAddBinary1111_1111(self):
        a = "1111"
        b = "1111"

        sum_ = self.sol.addBinary(a, b)

        self.assertEqual(sum_, "11110")


if __name__ == "__main__":
    unittest.main()
