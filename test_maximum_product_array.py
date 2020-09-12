import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.maxProduct2(nums),
            self.maxProduct2(nums[::-1])
        )

    def maxProduct2(self, nums: List[int]) -> int:
        max_product = 0
        actual_product = 0
        neg_val = 0

        for num in nums:
            if num == 0:
                max_product = max(actual_product, max_product)
                actual_product = 0
                neg_val = 0
            elif num < 0:
                if neg_val == 0:
                    if actual_product == 0:
                        neg_val = num
                    else:
                        neg_val = num * actual_product
                        max_product = max(max_product, actual_product)
                        actual_product = 0
                else:  # merge:
                    if actual_product == 0:
                        actual_product = neg_val * num
                        neg_val = 0
                    else:
                        actual_product = actual_product * neg_val * num
                        neg_val = 0
            else:
                if actual_product == 0:
                    actual_product = num
                else:
                    actual_product *= num

        return max(max_product, actual_product)


class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaxProduct1(self):
        nums = [2, 3, -2, 4]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 6)

    def testMaxProduct2(self):
        nums = [2, 3, -2, -4]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 48)

    def testMaxProduct3(self):
        nums = [2, 3, -2, 2, -4]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 96)

    def testMaxProduct4(self):
        nums = [2, 3, -2, 2, 0, -4]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 6)

    def testMaxProduct5(self):
        nums = [-2, 0, -1]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 0)

    def testMaxProduct6(self):
        nums = [-2]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, -2)

    def testMaxProduct7(self):
        nums = [-3, -1, -1]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 3)

    def testMaxProduct8(self):
        nums = [2, -5, -2, -4, 3]

        max_product = self.sol.maxProduct(nums)

        self.assertEqual(max_product, 24)

if __name__ == "__main__":
    unittest.main()
