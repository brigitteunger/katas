import unittest
from typing import List


class RecentCounter:

    def __init__(self):
        self.recent_requests = []
        self.time_range = [-3000, 0]
        self.index_in_time = 0

    def __count_recent_calls__(self):
        for i in range(self.index_in_time, len(self.recent_requests)):
            if self.recent_requests[i] >= self.time_range[0]:
                return len(self.recent_requests)-i

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        self.time_range[1] = t
        self.time_range[0] = self.time_range[1] - 3000
        counts = self.__count_recent_calls__()
        if counts < len(self.recent_requests):
            self.index_in_time = len(self.recent_requests)-counts
        return counts


class TestRecentCounter(unittest.TestCase):
    def setUp(self):
        self.obj = RecentCounter()

    def testRecentCounter_1(self):
        self.assertEqual(1, self.obj.ping(1))
        self.assertEqual(2, self.obj.ping(100))
        self.assertEqual(3, self.obj.ping(3001))
        self.assertEqual(3, self.obj.ping(3002))


if __name__ == "__main__":
    unittest.main()
