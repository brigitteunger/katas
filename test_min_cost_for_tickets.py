import unittest
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost_2_day = [0]*366
        j = 0
        for i in range(1, 366):
            cost_2_day[i] = costs[0] + cost_2_day[i-1]
            if i-7 >= 0:
                cost_2_day[i] = min(cost_2_day[i-7]+costs[1], cost_2_day[i])
            if i-30 >= 0:
                cost_2_day[i] = min(cost_2_day[i-30]+costs[2], cost_2_day[i])
            if j < len(days) and days[j] == i:
                j += 1
            else:
                cost_2_day[i] = min(cost_2_day[i], cost_2_day[i-1])
        return cost_2_day[365]


class TestMinCostTickets(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMincostTickets_1(self):
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 11)

    def testMincostTickets_2(self):
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 17)

    def testMincostTickets_3(self):
        days = [2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 15)

    def testMincostTickets_4(self):
        days = [100]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 2)

    def testMincostTickets_5(self):
        days = [100, 300]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 4)

    def testMincostTickets_6(self):
        days = [100, 101, 102, 103]
        costs = [2, 7, 15]

        overall_costs = self.sol.mincostTickets(days, costs)

        self.assertEqual(overall_costs, 7)


if __name__ == '__main__':
    unittest.main()
