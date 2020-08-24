import unittest
from typing import List
import random


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.num_rects = len(rects)
        self.weights = [0]*self.num_rects
        self.__calc_weights_rect__()

    def __calc_weights_rect__(self) -> None:
        areas = [(abs(rect[2]-rect[0])+1)*(abs(rect[3]-rect[1])+1)
                 for rect in self.rects]
        sum_areas = sum(areas)
        self.weights = [area/sum_areas for area in areas]

    def pick(self) -> List[int]:
        # pick rectangle:
        if self.num_rects > 1:
            choices = random.choices(self.rects, self.weights)
            rect = choices[0]
        else:
            rect = self.rects[0]

        # find coordinates:
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]


class TestSortArraybyParity(unittest.TestCase):
    def is_in_rects(self,
                    rects: List[List[int]],
                    int_point: List[int]
                    ) -> bool:
        for rect in rects:
            if self.is_in_rect(rect, int_point):
                return True
        return False

    def is_in_rect(self,
                   rect: List[int],
                   point: List[int]
                   ) -> bool:
        if point[0] >= rect[0] and point[0] <= rect[2] and \
           point[1] >= rect[1] and point[1] <= rect[3]:
            return True
        else:
            return False

    def test_is_in_rects_1(self):
        rects = [[1, 1, 5, 5]]
        point = [4, 1]

        self.assertTrue(self.is_in_rects(rects, point))

    def test_is_in_rects_2(self):
        rects = [[1, 1, 5, 5]]
        point = [0, 1]

        self.assertFalse(self.is_in_rects(rects, point))

    def test_is_in_rects_3(self):
        rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
        point = [-1, -1]

        self.assertTrue(self.is_in_rects(rects, point))

    def test_is_in_rects_4(self):
        rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
        point = [2, 0]

        self.assertTrue(self.is_in_rects(rects, point))

    def testPick_1(self):
        rects = [[1, 1, 5, 5]]
        sol = Solution(rects)

        point = sol.pick()

        self.assertTrue(self.is_in_rects(rects, point))

    def testPick_2(self):
        rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
        sol = Solution(rects)

        point = sol.pick()

        self.assertTrue(self.is_in_rects(rects, point))

    def testPick_3(self):
        rects = [[82918473, -57180867, 82918476, -57180863],
                 [83793579, 18088559, 83793580, 18088560],
                 [66574245, 26243152, 66574246, 26243153],
                 [72983930, 11921716, 72983934, 11921720]]

        sol = Solution(rects)
        point = sol.pick()

        self.assertTrue(self.is_in_rects(rects, point))


if __name__ == "__main__":
    unittest.main()
