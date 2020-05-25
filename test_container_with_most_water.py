import unittest
from typing import List
from data_test_container_with_most_water import long_list


class Solution:
    def max_area(self, height: List[int]) -> int:
        largest_area = 0
        index_left = 0
        index_right = len(height)-1

        while index_left < index_right:
            min_heigth = min(height[index_left], height[index_right])
            new_area = self.calculate_area(min_heigth, index_right-index_left)
            largest_area = max(largest_area, new_area)

            if height[index_left] < height[index_right]:
                index_left += 1
            else:
                index_right -= 1

            if index_left >= index_right:
                break

        return largest_area

    def calculate_area(self, height: int, width: int) -> int:
        return height*width


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_max_area(self):
        self.assertEqual(self.sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_max_area_long_list(self):
        self.assertEqual(self.sol.max_area(long_list), 18945816)
