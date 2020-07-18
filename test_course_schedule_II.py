import unittest
from typing import Dict, List
from data_course_schedule import num_courses_2, prerequisites_2


class CircleFound(Exception):
    pass


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        courses_pre = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            courses_pre[pre[0]].append(pre[1])

        schedule = []
        try:
            while len(schedule) != numCourses:
                for course in range(numCourses):
                    if course not in schedule:
                        start = self.findStart(course, courses_pre, schedule)
                        schedule.append(start)
                        break
        except CircleFound:
            return []
        else:
            return schedule

    def findStart(self, course: int, courses_pre: Dict[int, List[int]],
                  schedule: List[int], visited: List[int] = []) -> int:
        pres = courses_pre[course]
        for pre in pres:
            if pre not in schedule:
                if pre in visited:
                    raise CircleFound
                x = visited[:]
                x.append(course)
                return self.findStart(pre, courses_pre, schedule, x)
        return course


class TestFindOrders(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindOrder10(self):
        num_courses = 2
        prerequisites = [[1, 0]]

        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [0, 1])

    def testFindOrder0123(self):
        num_courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [0, 1, 2, 3])

    def testFindOrder01234(self):
        num_courses = 5
        prerequisites = [[4, 1], [4, 2], [4, 3], [1, 0]]

        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [0, 1, 2, 3, 4])

    def testFindOrder1(self):
        num_courses = 1
        prerequisites = []
        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [0])

    def testFindOrder013(self):
        num_courses = 4
        prerequisites = [[3, 0], [0, 1]]
        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [1, 0, 2, 3])

    def testFindOrderCircle(self):
        num_courses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]

        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [])

    def testFindOrderCircle_3210(self):
        num_courses = 3
        prerequisites = [[0, 1], [0, 2], [1, 2]]

        schedule = self.sol.findOrder(num_courses, prerequisites)

        self.assertEqual(schedule, [2, 1, 0])

    def testFindOrderCircle_big(self):
        schedule = self.sol.findOrder(num_courses_2, prerequisites_2)

        self.assertEqual(schedule, [2, 1, 0])


if __name__ == "__main__":
    unittest.main()
