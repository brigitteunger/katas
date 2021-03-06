import unittest
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        if not candidates:
            return []
        candidates.sort()
        combinations = []
        for combination in self.generator_combination(candidates, target):
            combinations.append(combination)
        return combinations

    def generator_combination(self, candidates: List[int],
                              target: int) -> List[List[int]]:
        i = 0
        length_candiates = len(candidates)
        while i < length_candiates:
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                yield [candidates[i]]
                break
            else:
                new_target = target - candidates[i]
                part_combinations = self.generator_combination(
                                     candidates[i:], new_target)
                for part_combination in part_combinations:
                    part_combination.append(candidates[i])
                    yield part_combination
            i += 1


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def deep_sort(self, lists: List[List[int]]) -> List[List[int]]:
        sorted_list_ = [sorted(list_) for list_ in lists]
        return sorted(sorted_list_)

    def assertDeepEqual(self, actual: List[List[int]],
                        expected: List[List[int]]) -> None:
        actual_sorted = self.deep_sort(actual)
        expected_sorted = self.deep_sort(expected)
        self.assertEqual(actual_sorted, expected_sorted)

    def test_combination_sum_list_of_four(self):
        candiates = [2, 3, 6, 7]
        target = 7
        solution = [[7], [2, 2, 3]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_of_three(self):
        candiates = [2, 3, 5]
        target = 8
        solution = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_one_one(self):
        candiates = [2]
        target = 2
        solution = [[2]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_one_three(self):
        candiates = [2]
        target = 6
        solution = [[2, 2, 2]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_empty(self):
        candiates = []
        target = 6
        solution = []

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_of_mixed_three(self):
        candiates = [3, 5, 2]
        target = 8
        solution = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_of_three_no_solution(self):
        candiates = [3, 5, 2]
        target = 1
        solution = []

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_of_long_solution(self):
        candiates = [7, 3, 2]
        target = 18
        solution = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 3, 3],
                    [2, 2, 2, 2, 3, 7], [2, 2, 2, 3, 3, 3, 3], [2, 2, 7, 7],
                    [2, 3, 3, 3, 7], [3, 3, 3, 3, 3, 3]]

        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)

    def test_combination_sum_list_easy(self):
        candiates = [2, 3]
        target = 8
        solution = [[2, 2, 2, 2], [2, 3, 3]]
        combinations = self.sol.combinationSum(candiates, target)

        self.assertDeepEqual(combinations, solution)


test_ = TestCombinationSum()
test_.setUp()
test_.test_combination_sum_list_easy()
