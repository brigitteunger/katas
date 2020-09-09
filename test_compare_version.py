import unittest
from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        len_1 = len(version1_list)
        len_2 = len(version2_list)

        for i in range(max(len_1, len_2)):
            num1 = self.getNum(version1_list, i, len_1)
            num2 = self.getNum(version2_list, i, len_2)
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0

    def getNum(self, version_list: List[str], index: int, len_list: int
               ) -> int:
        if index >= len_list:
            return 0
        else:
            return int(version_list[index])


class TestCompareVersion(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCompareVersion1(self):
        version1 = "0.1"
        version2 = "1.1"

        result = self.sol.compareVersion(version1, version2)

        self.assertEqual(result, -1)

    def testCompareVersion2(self):
        version1 = "1.0.1"
        version2 = "1"

        result = self.sol.compareVersion(version1, version2)

        self.assertEqual(result, 1)

    def testCompareVersion3(self):
        version1 = "7.5.2.4"
        version2 = "7.5.3"

        result = self.sol.compareVersion(version1, version2)

        self.assertEqual(result, -1)

    def testCompareVersion4(self):
        version1 = "1.01"
        version2 = "1.001"

        result = self.sol.compareVersion(version1, version2)

        self.assertEqual(result, 0)

    def testCompareVersion5(self):
        version1 = "1.0"
        version2 = "1.0.0"

        result = self.sol.compareVersion(version1, version2)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
