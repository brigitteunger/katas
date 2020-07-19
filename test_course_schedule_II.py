import unittest
from typing import Dict, List
from data_course_schedule import num_courses_2, prerequisites_2, schedule_2


class CircleFound(Exception):
    pass


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        courses_to_visit = self.collect_prerequisites_per_course(
            numCourses, prerequisites)

        try:
            schedule = []
            for course in range(numCourses):
                if course in courses_to_visit:
                    schedule = schedule + self.scheduleForCourse(
                        course, courses_to_visit)
            return schedule
        except CircleFound:
            return []

    def collect_prerequisites_per_course(self, numCourses: int,
                                         prerequisites: List[List[int]]
                                         ) -> Dict[int, List[int]]:
        courses_with_prerequisites = {i: [] for i in range(numCourses)}
        for prerequisite_pair in prerequisites:
            course = prerequisite_pair[0]
            prerequisite = prerequisite_pair[1]
            courses_with_prerequisites[course].append(prerequisite)
        return courses_with_prerequisites

    def scheduleForCourse(self, course: int, courses_to_visit: Dict[int, List[int]],
                          visited: List[int] = []) -> List[int]:
        schedule = []
        for pre in courses_to_visit[course]:
            if pre in courses_to_visit:
                if pre in visited:
                    raise CircleFound
                schedule = schedule + self.scheduleForCourse(
                    pre, courses_to_visit, visited + [course])
        schedule.append(course)
        del courses_to_visit[course]
        return schedule


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

        self.assertEqual(schedule, schedule_2)


if __name__ == "__main__":
    unittest.main()
