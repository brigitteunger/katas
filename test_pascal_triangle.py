import unittest
from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = []

        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                val = 1
            else:
                val = int(factorial(rowIndex)/(
                          factorial(i)*factorial(rowIndex-i)))
            row.append(val)
        return row


class TestGetRow(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testGetRow3(self):
        rowIndex = 3

        row = self.sol.getRow(rowIndex)

        self.assertEqual(row, [1, 3, 3, 1])

    def testGetRow0(self):
        rowIndex = 0

        row = self.sol.getRow(rowIndex)

        self.assertEqual(row, [1])

    def testGetRow1(self):
        rowIndex = 1

        row = self.sol.getRow(rowIndex)

        self.assertEqual(row, [1, 1])

    def testGetRow2(self):
        rowIndex = 2

        row = self.sol.getRow(rowIndex)

        self.assertEqual(row, [1, 2, 1])


if __name__ == "__main__":
    unittest.main()
