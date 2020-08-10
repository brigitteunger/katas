import unittest
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        j = 0
        len_arr = len(arr)

        while k != 0:
            i += 1
            if len_arr == j:
                return arr[j-1] + k

            if i != arr[j]:
                k -= 1
            else:
                j += 1
        return i


class TestKthMissing_number(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findKthPositive_1(self):
        arr = [2, 3, 4, 7, 11]
        k = 5

        result = self.sol.findKthPositive(arr, k)

        self.assertEqual(result, 9)

    def test_findKthPositive_2(self):
        arr = [1, 2, 3, 4]
        k = 2

        result = self.sol.findKthPositive(arr, k)

        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
