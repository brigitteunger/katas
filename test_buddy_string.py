import unittest
from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_A = len(A)
        len_B = len(B)

        if len_A != len_B:
            return False

        if A == B:
            dict_A = Counter(A)
            for val in dict_A.values():
                if val > 1:
                    return True
            return False

        diff_A_1 = ""
        diff_A_2 = ""
        diff_B_1 = ""
        diff_B_2 = ""
        count_diffs = 0
        for i in range(len_A):
            if A[i] != B[i]:
                if count_diffs >= 2:
                    return False
                else:
                    count_diffs += 1
                    if count_diffs == 1:
                        diff_A_1 = A[i]
                        diff_B_1 = B[i]
                    else:
                        diff_A_2 = A[i]
                        diff_B_2 = B[i]

        if diff_A_1 == diff_B_2 and diff_B_1 == diff_A_2:
            return True
        else:
            return False


class TestBuddyStrings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testBuddyStrings_1(self):
        A = "ab"
        B = "ba"

        are_buddies = self.sol.buddyStrings(A, B)

        self.assertTrue(are_buddies)

    def testBuddyStrings_2(self):
        A = "ab"
        B = "ab"

        are_buddies = self.sol.buddyStrings(A, B)

        self.assertFalse(are_buddies)

    def testBuddyStrings_3(self):
        A = "aa"
        B = "aa"

        are_buddies = self.sol.buddyStrings(A, B)

        self.assertTrue(are_buddies)

    def testBuddyStrings_4(self):
        A = "aaaaaaabc"
        B = "aaaaaaacb"

        are_buddies = self.sol.buddyStrings(A, B)

        self.assertTrue(are_buddies)

    def testBuddyStrings_5(self):
        A = ""
        B = "aa"

        are_buddies = self.sol.buddyStrings(A, B)

        self.assertFalse(are_buddies)


if __name__ == "__main__":
    unittest.main()
