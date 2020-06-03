import unittest
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        weights = []
        n = len(costs)

        for i in range(n):
            weights.append([costs[i][0]-costs[i][1], i])

        weights.sort()
        sum_costs = 0
        middle = int(n/2)
        for i in range(middle):
            sum_costs = sum_costs + costs[weights[i][1]][0]
        for i in range(middle, n):
            sum_costs = sum_costs + costs[weights[i][1]][1]

        return sum_costs


class TestTwoCitySchedCost(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_two_city_sched_cost_easy(self):
        costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
        expected_total_min = 110

        actual_total_min = self.sol.twoCitySchedCost(costs)

        self.assertEqual(actual_total_min, expected_total_min)

    def test_two_city_sched_cost_two_equal(self):
        costs = [[10, 20], [30, 200], [400, 50], [30, 30]]
        expected_total_min = 120

        actual_total_min = self.sol.twoCitySchedCost(costs)

        self.assertEqual(actual_total_min, expected_total_min)

    def test_two_city_sched_cost_all_equal(self):
        costs = [[10, 20], [10, 20], [10, 20], [10, 20]]
        expected_total_min = 60

        actual_total_min = self.sol.twoCitySchedCost(costs)

        self.assertEqual(actual_total_min, expected_total_min)


test_ = TestTwoCitySchedCost()
test_.setUp()
test_.test_two_city_sched_cost_easy()
