import unittest
from typing import List


class Solution():
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        len_nums = len(nums)
        divisors = {}
        pre_divisor = {}
        for i in range(len_nums):
            dividend = nums[i]
            divisors[dividend] = []
            nogo = []
            for j in range(i-1, -1, -1):
                divisor = nums[j]
                if dividend % divisor == 0:
                    if divisor not in nogo:
                        divisors[dividend].append(divisor)
                        nogo_elem_list = divisors[divisor][:]
                        nogo_elem_list.append(divisor)
                        nogo = nogo + nogo_elem_list

        for num in nums:
            list_divs = divisors[num]
            if not list_divs:
                pre_divisor[num] = [num]
            else:
                longest = []
                for div in list_divs:
                    x = pre_divisor[div][:]
                    if len(x) > len(longest):
                        longest = x
                pre_divisor[num] = longest + [num]

        longest = []
        for x in pre_divisor.values():
            if len(x) > len(longest):
                longest = x
        return longest


class TestLargestDivisibleSubset(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertIn(self, actual:  List[int], expecteds:  List[List[int]]):
        equal = False
        actual.sort()
        len_actual = len(actual)
        len_exp = len(expecteds[0])

        self.assertEqual(len_actual, len_exp)

        for expected in expecteds:
            expected.sort()
            for i in range(len_exp):
                if actual[i] != expected[i]:
                    break
                if i == len_exp-1:
                    equal = True
                    break
            if equal is True:
                break
        message = "actual: " + str(actual) + "expecteds: " + str(expecteds)
        self.assertTrue(equal, msg=message)

    def test_largest_divisible_subset_list_three(self):
        nums = [1, 2, 3]
        expecteds = [[1, 2], [1, 3]]

        actual = self.sol.largestDivisibleSubset(nums)

        self.assertIn(actual, expecteds)

    def test_largest_divisible_subset_list_four(self):
        nums = [1, 2, 4, 8]
        expected = [1, 2, 4, 8]

        actual = self.sol.largestDivisibleSubset(nums)

        self.assertEqual(actual, expected)

    def test_largest_divisible_subset_list_eight(self):
        nums = [1, 2, 4, 8]
        expected = [1, 2, 4, 8]

        actual = self.sol.largestDivisibleSubset(nums)

        self.assertEqual(actual, expected)

    def test_largest_divisible_subset_list_seven(self):
        nums = [2, 5, 6, 9, 12, 15, 30]
        expected = [[5, 15, 30], [2, 6, 12]]

        actual = self.sol.largestDivisibleSubset(nums)

        self.assertIn(actual, expected)


if __name__ == "__main__":
    unittest.main()
