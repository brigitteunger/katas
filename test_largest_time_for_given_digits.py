import unittest
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = ""
        for first_digit in range(2, -1, -1):
            temp = A[:]
            if self.removeIfExits(temp, first_digit):
                time = str(first_digit)
                if first_digit == 2:
                    limit = 3
                else:
                    limit = 9
                for second_digit in range(limit, -1, -1):
                    if self.removeIfExits(temp, second_digit):
                        time += str(second_digit) + ":"
                        for third_digit in range(5, -1, -1):
                            if self.removeIfExits(temp, third_digit):
                                time += str(third_digit) + str(temp[0])
                                return time

        return ""

    def removeIfExits(self, nums: List[int], num) -> bool:
        if num in nums:
            nums.remove(num)
            return True
        return False


class TestLargestTimeFromDigits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testlargestTimeFromDigits_1(self):
        A = [1, 2, 3, 4]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "23:41")

    def testlargestTimeFromDigits_2(self):
        A = [5, 5, 5, 5]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "")

    def testlargestTimeFromDigits_3(self):
        A = [1, 2, 5, 9]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "21:59")

    def testlargestTimeFromDigits_4(self):
        A = [1, 5, 7, 9]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "19:57")

    def testlargestTimeFromDigits_5(self):
        A = [0, 0, 0, 3]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "03:00")

    def testlargestTimeFromDigits_6(self):
        A = [0, 0, 0, 9]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "09:00")

    def testlargestTimeFromDigits_7(self):
        A = [0, 1, 2, 6]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "21:06")

    def testlargestTimeFromDigits_8(self):
        A = [2, 3, 9, 9]

        time = self.sol.largestTimeFromDigits(A)

        self.assertEqual(time, "")


if __name__ == "__main__":
    unittest.main()
