import unittest
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        if k == len(nums):
            return nums

        dict_nums = Counter(nums)

        min_ = 0
        maxs = []
        for key, val in dict_nums.items():
            if min_ < val:
                if k > 1:
                    maxs.append([val, key])
                    k -= 1
                elif k == 1:
                    maxs.append([val, key])
                    maxs.sort()
                    min_ = maxs[0][0]
                    k -= 1
                else:
                    maxs.append([val, key])
                    maxs.sort()
                    del maxs[0]

        max_nums = []
        for max_ in maxs:
            max_nums.append(max_[1])

        return max_nums


class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testTopKFrequent_6_2(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1, 2])

    def testTopKFrequent_6_2_v2(self):
        nums = [-1, 1, 1, 2, 2, 3]
        k = 2

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1, 2])

    def testTopKFrequent_1_1(self):
        nums = [1]
        k = 1

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1])

    def testTopKFrequent_3_3(self):
        nums = [1, 2, 3]
        k = 3

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1, 2, 3])

    def testTopKFrequent_9_3(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        k = 3

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1, 2, 3])

    def testTopKFrequent_6_3(self):
        nums = [1, 2, 2, 3, 3, 3]
        k = 3

        frequents = self.sol.topKFrequent(nums, k)
        frequents.sort()

        self.assertEqual(frequents, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
