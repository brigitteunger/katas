import unittest
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasDiff = self.calculateGasDiff(gas, cost)
        for start in range(len(gas)):
            if self.roundTrip(gasDiff, start):
                return start
        return -1

    def calculateGasDiff(self, gas: List[int], cost: List[int]) -> List[int]:
        diff = []
        for station in range(len(gas)):
            diff.append(gas[station] - cost[station])
        return diff

    def roundTrip(self, gasDiff: List[int], start: int) -> bool:
        fuel = 0
        for station in range(start, len(gasDiff)):
            fuel += gasDiff[station]
            if fuel < 0:
                return False

        for station in range(0, start):
            fuel += gasDiff[station]
            if fuel < 0:
                return False
        return True


class TestCanCompleteCircuit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCanCompleteCircuit_1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]

        index_start = self.sol.canCompleteCircuit(gas, cost)

        self.assertEqual(index_start, 3)

    def testCanCompleteCircuit_2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]

        index_start = self.sol.canCompleteCircuit(gas, cost)

        self.assertEqual(index_start, -1)


if __name__ == "__main__":
    unittest.main()
