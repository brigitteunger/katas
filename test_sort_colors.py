import unittest
from typing import List


class Solution():
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        nums_0 = nums.count(0)
        nums_1 = nums.count(1) + nums_0
        size_nums = len(nums)
        for i in range(size_nums):
            if i < nums_0:
                nums[i] = 0
            elif i < nums_1:
                nums[i] = 1
            else:
                nums[i] = 2


class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sort_colors_easy(self):
        input_ = [2, 0, 2, 1,  1, 0]
        expected_output = [0, 0, 1, 1, 2, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_empty(self):
        input_ = []

        self.sol.sortColors(input_)

        self.assertEqual(input_, [])

    def test_sort_colors_no_zeros(self):
        input_ = [2, 1, 2, 1,  1, 2]
        expected_output = [1, 1, 1, 2, 2, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_no_ones(self):
        input_ = [2, 0, 2, 0,  0, 0, 2]
        expected_output = [0,  0, 0, 0, 2, 2, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_no_twos(self):
        input_ = [1, 0, 1, 0,  0, 0, 1, 1, 1]
        expected_output = [0,  0, 0, 0, 1, 1, 1, 1, 1]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_one_elem(self):
        input_ = [1]
        expected_output = [1]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_two_elem(self):
        input_ = [2, 0]
        expected_output = [0, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_three_elem(self):
        input_ = [2, 0, 1]
        expected_output = [0, 1, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_all_twos(self):
        input_ = [2, 2, 2]
        expected_output = [2, 2, 2]

        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)

    def test_sort_colors_two_elem_0_1(self):
        input_ = [0, 1]
        expected_output = [0, 1]
        self.sol.sortColors(input_)

        self.assertEqual(input_, expected_output)


if __name__ == '__main__':
    unittest.main()
