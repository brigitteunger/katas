import unittest
from typing import List


class Solution():
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        size_nums = len(nums)
        right_index = size_nums - 1
        left_index = 0

        while left_index <= right_index:
            middle_index = int(((left_index+right_index)/2) + 0.5)
            if nums[middle_index] < target:  # go right
                left_index = middle_index + 1
                if left_index == size_nums:
                    return size_nums
                elif nums[left_index] >= target:
                    return left_index
                elif left_index == right_index:
                    if nums[left_index] == target:
                        return left_index
                    else:
                        return size_nums
            elif nums[middle_index] > target:  # go left
                right_index = middle_index - 1
                if right_index < 0:
                    return 0
                elif nums[right_index] < target:
                    return right_index+1
                elif left_index == right_index:
                    return 0
            else:
                return middle_index


class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_search_insert_elem_in_list(self):
        nums = [1, 3, 5, 6]
        target = 5

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 2)

    def test_search_insert_empty_list(self):
        nums = []
        target = 5

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 0)

    def test_search_insert_elem_not_list(self):
        nums = [1, 3, 5, 6]
        target = 2

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 1)

    def test_search_insert_elem_biggest_val(self):
        nums = [1, 3, 5, 6]
        target = 7

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 4)

    def test_search_insert_elem_smallest_val(self):
        nums = [1, 3, 5, 6]
        target = 0

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 0)

    def test_search_insert_neg_nums_list(self):
        nums = [-5, -3, 0, 1, 3, 5, 6]
        target = -2

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 2)

    def test_search_insert_short_list(self):
        nums = [1, 3, 5]
        target = 5

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 2)

    def test_search_insert_short_list_end(self):
        nums = [1, 3]
        target = 4

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 2)

    def test_search_insert_short_list_front(self):
        nums = [1, 3]
        target = 0

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 0)

    def test_search_insert_seven_elem_list(self):
        nums = [1, 2, 4, 6, 8, 9, 10]
        target = 10

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 6)

    def test_search_insert_six_elem_list(self):
        nums = [2, 4, 5, 6, 7, 8]
        target = 7

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 4)

    def test_search_insert_one_elem_in_one_list(self):
        nums = [1]
        target = 0

        actual_index = self.sol.searchInsert(nums, target)

        self.assertEqual(actual_index, 0)


if __name__ == '__main__':
    unittest.main()
