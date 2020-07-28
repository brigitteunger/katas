import unittest
from typing import List
from collections import Counter
from data_task_scheduler import n2, tasks2, tasks3, tasks4


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)

        tasks_dict = Counter(tasks)
        max_num_task = 0
        for val in tasks_dict.values():
            max_num_task = max(max_num_task, val)
        count_max = 0
        for val in tasks_dict.values():
            if val == max_num_task:
                count_max += 1
        return(max(len(tasks), count_max + (max_num_task-1)*(n+1)))


class TestLeastInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLeastInterval62(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 8)

    def testLeastInterval60(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 6)

    def testLeastInterval122(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 16)

    def testLeastIntervalLong(self):
        tasks = tasks2
        n = n2

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 52651)

    def testLeastIntervallFillMany(self):
        tasks = tasks3
        n = 8

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 1000)

    def testLeastIntervallMany(self):
        tasks = tasks4
        n = 2

        least = self.sol.leastInterval(tasks, n)

        self.assertEqual(least, 52)


if __name__ == '__main__':
    unittest.main()
