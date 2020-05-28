import unittest
from typing import List
from data_test_search_in_rotated_sorted_array import long_list


class Solution():
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        index_left = 0
        index_right = len(nums)-1

        if nums[index_left] < nums[index_right]:
            return self.binary_search(nums, target, index_left, index_right)

        while index_left <= index_right:
            index_middle = int((index_left + index_right) / 2)
            val_left = nums[index_left]
            val_middle = nums[index_middle]
            val_right = nums[index_right]

            if val_left == target:
                return index_left
            elif val_right == target:
                return index_right
            elif val_middle == target:
                return index_middle

            # linke seite stetig?
            if val_left < val_middle:
                # und target im stetigen Bereich?
                if val_left <= target and target < val_middle:
                    return self.binary_search(nums, target, index_left,
                                              index_middle)
                # Lösung in rechte Seite?
                elif ((val_middle > target and val_right > target) or
                      (val_middle < target and val_right < target)):
                    index_left = index_middle + 1
                    continue
                else:
                    return -1

            # rechte seite stetig?
            if val_middle < val_right:
                # und target im stetigen bereich?
                if val_middle < target and target <= val_right:
                    return self.binary_search(nums, target, index_middle,
                                              index_right)
                # Lösung in linker Seite?
                elif ((val_left > target and val_middle > target) or
                      (val_left < target and val_middle < target)):
                    index_right = index_middle - 1
                    continue
                else:
                    return -1
            else:
                return -1
        return -1

    def binary_search(self, nums: List[int], target: int, left_index: int,
                      right_index: int) -> int:
        if not nums:
            return -1

        while left_index <= right_index:
            middle_index = int((left_index + right_index) / 2)
            if nums[middle_index] < target:
                left_index = middle_index + 1
            elif nums[middle_index] > target:
                right_index = middle_index - 1
            elif nums[middle_index] == target:
                return middle_index
            else:
                return -1

        return -1

    def print_for_debugging(self, nums: List[int], index: int, size_per_int:
                            int = 6):
        str_per_int = '{:^' + str(size_per_int) + '}'
        for i in range(len(nums)):
            print(str_per_int.format(i), end='')
        print()
        for num in nums:
            print(str_per_int.format(num), end='')
        print()
        for _ in range(index):
            print(str_per_int.format('---'), end='')
        print(str_per_int.format('-/\\-'))
        print('index: ' + str(index))


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_search_nums(self):
        nums = [4, 5, 6, 7, 8, 0, 1, 2]
        target = 0

        index = self.sol.search(nums, target)

        self.assertEqual(index, 5)

    def test_search_nums_zero(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = -0

        index = self.sol.search(nums, target)

        self.assertEqual(index, 4)

    def test_search_target_not_in_nums(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 10

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def test_search_target_orderd_nums(self):
        nums = [-5, -4, -3, 5, 6, 7, 10, 200]
        target = 10

        index = self.sol.search(nums, target)

        self.assertEqual(index, 6)

    def test_search_nums_negative(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = -30

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def test_search_target_empty_list(self):
        nums = []
        target = 10

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def test_search_nums_first_num(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4

        index = self.sol.search(nums, target)

        self.assertEqual(index, 0)

    def test_search_nums_last_num(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2

        index = self.sol.search(nums, target)

        self.assertEqual(index, 6)

    def test_search_nums_last_middle(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 7

        index = self.sol.search(nums, target)

        self.assertEqual(index, 3)

    def test_search_nums_last_middle_left(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 6

        index = self.sol.search(nums, target)

        self.assertEqual(index, 2)

    def test_search_nums_last_middle_right(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0

        index = self.sol.search(nums, target)

        self.assertEqual(index, 4)

    def test_search_nums_long_list(self):
        nums = long_list
        target = 0

        index = self.sol.search(nums, target)

        self.assertEqual(index, 6667)

    def test_search_nums_long_list_last_elem(self):
        nums = long_list
        target = 3332

        index = self.sol.search(nums, target)

        self.assertEqual(index, 9999)

    def test_search_nums_two_elem_list(self):
        nums = [1, 3]
        target = 2

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)

    def test_search_nums_three_elem_list(self):
        nums = [5, 1, 3]
        target = 4

        index = self.sol.search(nums, target)

        self.assertEqual(index, -1)


test = TestSearch()
test.setUp()
test.test_search_nums_three_elem_list()
