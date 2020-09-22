import unittest
from typing import List, Dict, Tuple


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick_up_dict, min_pick, _ = self.create_passenger_dict(trips, 1)
        drop_off_dict, _, max_drop = self.create_passenger_dict(trips, 2)

        passengers = 0
        for i in range(min_pick, max_drop):
            if i in drop_off_dict:
                passengers -= drop_off_dict[i]
            if i in pick_up_dict:
                passengers += pick_up_dict[i]
            if passengers > capacity:
                return False
        return True

    def create_passenger_dict(self,
                              trips: List[List[int]],
                              pick_drop: int) -> Dict[int, int]:
        # pick_drop: 1: pick up dict, 2: drop off dict
        pick_up_dict = {}
        max_stop = 0
        min_stop = trips[0][pick_drop]
        for trip in trips:
            if trip[pick_drop] not in pick_up_dict:
                pick_up_dict[trip[pick_drop]] = trip[0]
                min_stop = min(min_stop, trip[pick_drop])
                max_stop = max(max_stop, trip[pick_drop])
            else:
                pick_up_dict[trip[pick_drop]] += trip[0]
        return pick_up_dict, min_stop, max_stop


class TestCarPooling(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCarPooling_1(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4

        actual = self.sol.carPooling(trips, capacity)

        self.assertFalse(actual)

    def testCarPooling_2(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5

        actual = self.sol.carPooling(trips, capacity)

        self.assertTrue(actual)

    def testCarPooling_3(self):
        trips = [[2, 1, 5], [3, 5, 7]]
        capacity = 3

        actual = self.sol.carPooling(trips, capacity)

        self.assertTrue(actual)

    def testCarPooling_4(self):
        trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
        capacity = 11

        actual = self.sol.carPooling(trips, capacity)

        self.assertTrue(actual)

    def testCarPooling_5(self):
        trips = [[3, 2, 5], [3, 2, 7], [3, 7, 9], [8, 3, 9]]
        capacity = 11

        actual = self.sol.carPooling(trips, capacity)

        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
