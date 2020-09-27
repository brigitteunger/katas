import unittest
from typing import List, Dict


class Solution:
    def calcEquation(self,
                     equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]]) -> List[float]:
        equa_2_val = self.create_dict_equa_2_val(equations, values)
        adjacent_equation = self.build_adjacency_list(equations)
        answers = []
        for query in queries:
            if query[0] == query[1]:
                if query[0] in adjacent_equation.keys():
                    answers.append(1.0)
                else:
                    answers.append(-1.0)
            else:
                path = self.dfs(adjacent_equation, query[0], query[1], [])
                if path is None:
                    answers.append(-1.0)
                else:
                    answer = 1
                    for entry in range(len(path)-1):
                        answer *= equa_2_val[self.create_key_from_equation(
                                  path[entry], path[entry+1])]
                    answers.append(answer)

        return answers

    def dfs(self,
            adjacent_equation: Dict[str, str],
            start: str,
            end: str,
            visited: List[str]) -> List[str]:
        if start not in adjacent_equation.keys():
            return None
        else:
            visited.append(start)
            neighbours = adjacent_equation[start]
            for neighbour in neighbours:
                if neighbour == end:
                    return [start, end]
                else:
                    if neighbour not in visited:
                        path = self.dfs(adjacent_equation,
                                        neighbour,
                                        end,
                                        visited[:])
                        if path:
                            return [start] + path
            return None

    def create_dict_equa_2_val(self,
                               equations: List[List[str]],
                               values: List[float]) -> Dict[str, float]:
        equa_2_val = {}
        for i in range(len(equations)):
            equa_2_val[self.create_key_from_equation(equations[i][0],
                       equations[i][1])] = values[i]
            equa_2_val[self.create_key_from_equation(equations[i][1],
                       equations[i][0])] = 1/values[i]
        return equa_2_val

    def create_key_from_equation(self, start: str, end: str) -> str:
        return start + "_" + end

    def build_adjacency_list(self,
                             equations: List[List[str]]) -> Dict[str, str]:
        dict_equation = {}
        for equation in equations:
            self.make_entry_in_dict(equation[0], equation[1], dict_equation)
            self.make_entry_in_dict(equation[1], equation[0], dict_equation)
        return dict_equation

    def make_entry_in_dict(self,
                           key: str,
                           entry: str,
                           dict_equation: Dict[str, List[str]]) -> None:
        if key in dict_equation:
            if entry not in dict_equation[key]:
                dict_equation[key].append(entry)
        else:
            dict_equation[key] = [entry]


class TestCalcEquation(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCalcEquation_1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

        answers = self.sol.calcEquation(equations, values, queries)

        self.assertEqual(answers, [6.0, 0.5, -1.0, 1.0, -1.0])

    def testCalcEquation_2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

        answers = self.sol.calcEquation(equations, values, queries)

        self.assertEqual(answers, [3.75000, 0.40000, 5.00000, 0.20000])

    def testCalcEquation_3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]

        answers = self.sol.calcEquation(equations, values, queries)

        self.assertEqual(answers, [0.50000, 2.00000, -1.00000, -1.00000])


if __name__ == "__main__":
    unittest.main()
