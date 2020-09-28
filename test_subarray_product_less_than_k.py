import unittest
from typing import List, Tuple
from data_subarray_product_less_than_k import nums_1


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        num_subarrays = 0
        start = -1
        end = - 1
        old_end = -1
        while 1:
            interval = self.findInterval(start, end, k, nums)
            if interval is None:
                break
            start = interval[0]
            end = interval[1]
            num_subarrays += self.calcNumCombinations(start, end)
            if end != old_end and start <= old_end:
                num_subarrays -= self.calcNumCombinations(start, old_end)
            old_end = end
        return num_subarrays

    def productInterval(self, start: int, end: int, nums: List[int]) -> int:
        product = 1
        for i in range(start, end+1, 1):
            product *= nums[i]
        return product

    def findInterval(self, start: int, end: int, k: int, nums: List[int]) -> Tuple[int, int]:
        len_nums = len(nums)
        new_start = start + 1
        new_end = end + 1
        if new_end == len_nums:
            return None

        product = self.productInterval(new_start, new_end, nums)
        while 1:  # abbruch?
            if new_start == new_end:
                while nums[new_start] >= k:
                    product /= nums[new_start]
                    new_start += 1
                    new_end += 1
                    if new_start == len_nums:
                        return None
                    product *= nums[new_end]

            if product < k:  # found new_start
                for i in range(new_end + 1, len_nums):
                    product *= nums[i]
                    if product >= k:
                        return (new_start, i - 1)
                return (new_start, len_nums - 1)

            else:  # search new start
                product /= nums[new_start]
                new_start += 1

    def calcNumCombinations(self, start: int, end: int) -> int:
        n = end - start + 1
        return (n*(n+1))//2


class TestCalcEquation(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testNumSubarrayProductLessThanK_1(self):
        nums = [10, 5, 2, 6]
        k = 100

        num_subarrays = self.sol.numSubarrayProductLessThanK(nums, k)

        self.assertEqual(num_subarrays, 8)

    def testNumSubarrayProductLessThanK_2(self):
        nums = nums_1
        k = 5

        num_subarrays = self.sol.numSubarrayProductLessThanK(nums, k)

        self.assertEqual(num_subarrays, 367968907)

    def testNumSubarrayProductLessThanK_3(self):
        nums = [1, 2, 3]
        k = 0

        num_subarrays = self.sol.numSubarrayProductLessThanK(nums, k)

        self.assertEqual(num_subarrays, 0)

    def testNumSubarrayProductLessThanK_4(self):
        nums = [1, 1, 1]
        k = 1

        num_subarrays = self.sol.numSubarrayProductLessThanK(nums, k)

        self.assertEqual(num_subarrays, 0)


if __name__ == "__main__":
    unittest.main()
