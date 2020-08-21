import unittest
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return list(sorted(A, key=lambda a: (a & 1)))


class TestSortArraybyParity(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testSortArrayByParity_1(self):
        A = [3, 1, 2, 4]

        B = self.sol.sortArrayByParity(A)

        self.assertEqual(B, [2, 4, 3, 1])

    def testSortArrayByParity_2(self):
        A = [3, 2]

        B = self.sol.sortArrayByParity(A)

        self.assertEqual(B, [2, 3])


if __name__ == "__main__":
    unittest.main()
