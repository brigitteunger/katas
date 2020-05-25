import unittest
from typing import List
from data_long_list_three_sum import long_list, long_list_sol


class Solution():
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        set_triplets = set()
        for index in range(len(nums)-2):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                sum_triplet = nums[index]+nums[left]+nums[right]
                if sum_triplet == 0:
                    set_triplets.add((nums[index], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum_triplet > 0:
                    right -= 1
                else:
                    left += 1
        list_triplets = []
        for item in set_triplets:
            list_triplets.append(list(item))
        return list_triplets


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_threeSum(self):
        self.assertEqual(sorted(self.sol.three_sum([-1, 0, 1, 2, -1, -4])),
                         [[-1, -1, 2], [-1, 0, 1]])

    def test_threeSum_000(self):
        self.assertEqual(self.sol.three_sum([0, 0, 0]), [[0, 0, 0]])

    def test_threeSum_long_list(self):
        self.assertEqual(sorted(self.sol.three_sum(long_list)), long_list_sol)
