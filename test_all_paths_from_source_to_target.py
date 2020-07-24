import unittest
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        num_nodes = len(graph)
        all_pathes = []
        for edge in graph[0]:
            all_pathes.append([0, edge])

        for node in range(1, num_nodes-1):
            self.addNode(node, graph[node], all_pathes)

        for index_path in range(len(all_pathes)-1, -1, -1):
            if all_pathes[index_path][-1] != num_nodes-1:
                del all_pathes[index_path]

        return all_pathes

    def addNode(self, node: int, edges: List[int], all_pathes: List[List[int]]
                ) -> None:
        if not edges:
            return
        num_new_edges = len(edges)
        for path in all_pathes:
            if path[-1] == node:
                if num_new_edges > 1:
                    for index_edge in range(1, num_new_edges):
                        path_with_new_edge = path + [edges[index_edge]]
                        all_pathes.append(path_with_new_edge)
                path.append(edges[0])


class TestAllPathsSourceTarget(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testAllPathsSourceTarget_4_nodes(self):
        graph = [[1, 2], [3], [3], []]

        all_pathes = self.sol.allPathsSourceTarget(graph)
        all_pathes.sort()
        self.assertEqual(all_pathes, [[0, 1, 3], [0, 2, 3]])

    def testAllPathsSourceTarget_5_nodes(self):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        all_pathes_expected = [[0, 4],
                               [0, 1, 4],
                               [0, 3, 4],
                               [0, 1, 2, 3, 4],
                               [0, 1, 3, 4]
                               ]
        all_pathes_expected.sort()

        all_pathes = self.sol.allPathsSourceTarget(graph)
        all_pathes.sort()

        self.assertEqual(all_pathes, all_pathes_expected)


if __name__ == "__main__":
    unittest.main()
