import unittest
from typing import List


class Solution():
    def reconstructQueue(self, people: List[List[int]], expected_queue
                         ) -> List[List[int]]:
        people.sort()
        slice_people_sorted = []
        people_reconstructed = []
        num_people = len(people)
        for i in range(num_people-1, -1, -1):
            peo = people[i]
            if not slice_people_sorted:
                slice_people_sorted.append(peo)
            elif peo[0] == slice_people_sorted[0][0]:
                slice_people_sorted.append(peo)
            else:
                slice_num_people = len(slice_people_sorted)
                for j in range(slice_num_people-1, -1, -1):
                    peo_ = slice_people_sorted[j]
                    people_reconstructed.insert(peo_[1], peo_)
                slice_people_sorted.clear()
                slice_people_sorted.append(peo)

        slice_num_people = len(slice_people_sorted)
        for j in range(slice_num_people-1, -1, -1):
            peo = slice_people_sorted[j]
            people_reconstructed.insert(peo[1], peo)
        return people_reconstructed


class TestReconstructQueue(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_reconstruct_queue_standard(self):
        input_queue = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected_queue = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

        actual_queue = self.sol.reconstructQueue(input_queue, expected_queue)

        self.assertEqual(actual_queue, expected_queue)

    def test_reconstruct_queue_standard_hard(self):
        input_queue = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2], [5, 1],
                       [7, 2]]
        expected_queue = [[5, 0],  [5, 1], [5, 2], [7, 0], [4, 4], [6, 1],
                          [7, 1], [7, 2]]

        actual_queue = self.sol.reconstructQueue(input_queue, expected_queue)

        self.assertEqual(actual_queue, expected_queue)

    def test_reconstruct_queue_standard_harder(self):
        input_queue = [[2, 4], [3, 4], [9, 0], [0, 6], [7, 1], [6, 0], [7, 3],
                       [2, 5], [1, 1], [8, 0]]
        expected_queue = [[6, 0], [1, 1], [8, 0], [7, 1], [9, 0], [2, 4],
                          [0, 6], [2, 5], [3, 4], [7, 3]]

        actual_queue = self.sol.reconstructQueue(input_queue, expected_queue)

        self.assertEqual(actual_queue, expected_queue)

    def test_reconstruct_queue_standard_on_elem(self):
        input_queue = [[1, 0]]
        expected_queue = [[1, 0]]

        actual_queue = self.sol.reconstructQueue(input_queue, expected_queue)

        self.assertEqual(actual_queue, expected_queue)


test_ = TestReconstructQueue()
test_.setUp()
test_.test_reconstruct_queue_standard()
#  test_.test_reconstruct_queue_standard_hard()
#  test_.test_reconstruct_queue_standard_harder()
