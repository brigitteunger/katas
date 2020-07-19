import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), '0b')

    def addBinaryBitByBit(self, a: str, b: str) -> str:
        list_a = list(a)
        list_b = list(b)
        len_a = len(list_a)
        len_b = len(list_b)
        diff = abs(len_a - len_b)
        if len_a > len_b:
            list_b = [0]*diff + list_b
        elif len_a < len_b:
            list_a = [0]*diff + list_a

        len_max = len(list_a)
        list_sum = [0]*len_max
        carry = 0

        for i in range(len_max-1, -1, -1):
            sum_bits = carry + int(list_a[i]) + int(list_b[i])
            if sum_bits == 0:
                list_sum[i] = '0'
                carry = 0
            elif sum_bits == 1:
                list_sum[i] = '1'
                carry = 0
            elif sum_bits == 2:
                list_sum[i] = '0'
                carry = 1
            else:  # sum_ == 3:
                list_sum[i] = '1'
                carry = 1

        if carry == 1:
            list_sum.insert(0, '1')

        sum_str = ''.join(list_sum)
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
