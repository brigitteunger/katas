import unittest
from typing import List
from sortedcontainers import SortedList
from data_contains_duplicate_III import nums_2, t_2, k_2


class Solution:
    def containsNearbyAlmostDuplicate(self, A: List[int], k: int,
                                      t: int) -> bool:
        bst = SortedList()
        for i in range(len(A)):
            if i > k:
                bst.remove(A[i-k-1])
            closest_left = bst.bisect_left(A[i] - t)
            closest_right = bst.bisect_right(A[i] + t)

            if closest_left != closest_right and closest_left != len(bst):
                return True

            bst.add(A[i])

        return False


class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testContainsNearbyAlmostDuplicate_1(self):
        nums = [1, 2, 3, 1]
        k = 3
        t = 0

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertTrue(solved)

    def testContainsNearbyAlmostDuplicate_2(self):
        nums = [1, 0, 1, 1]
        k = 1
        t = 2

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertTrue(solved)

    def testContainsNearbyAlmostDuplicate_3(self):
        nums = [1, 5, 9, 1, 5, 9]
        k = 2
        t = 3

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertFalse(solved)

    def testContainsNearbyAlmostDuplicate_4(self):
        nums = nums_2
        k = k_2
        t = t_2

        solved = self.sol.containsNearbyAlmostDuplicate(nums, k, t)

        self.assertFalse(solved)


if __name__ == "__main__":
    unittest.main()
