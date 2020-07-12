import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            new_sets = []
            for subset in subsets:
                new_set = subset[:]
                new_set.append(num)
                new_sets.append(new_set)
            subsets = subsets + new_sets

        return subsets


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def deepSort(self, nums: List[List[int]]) -> List[List[int]]:
        if not nums:
            return []

        for i in range(len(nums)):
            nums[i] = sorted(nums[i])

        nums.sort()
        return nums

    def assertDeepEqual(self,
                        nums_1: List[List[int]],
                        nums_2: List[List[int]]
                        ) -> None:
        nums_1 = self.deepSort(nums_1)
        nums_2 = self.deepSort(nums_2)

        len_1 = len(nums_1)
        len_2 = len(nums_2)

        self.assertEqual(len_1, len_2, "Lists have different length")

        for num_1, num_2 in zip(nums_1, nums_2):
            self.assertEqual(num_1, num_2)

    def testSubsets123(self):
        nums = [1, 2, 3]
        expected_subsets = [
                            [3],
                            [1],
                            [2],
                            [1, 2, 3],
                            [1, 3],
                            [2, 3],
                            [1, 2],
                            []
                            ]

        actual_subsets = self.sol.subsets(nums)

        self.assertDeepEqual(actual_subsets, expected_subsets)

    def testSubsetsEmpty(self):
        nums = []

        actual_subsets = self.sol.subsets(nums)

        self.assertEqual(actual_subsets, [[]])

    def testSubsets1(self):
        nums = [1]

        actual_subsets = self.sol.subsets(nums)

        self.assertDeepEqual(actual_subsets, [[], [1]])


if __name__ == "__main__":
    unittest.main()
