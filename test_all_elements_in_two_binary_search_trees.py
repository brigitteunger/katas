import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals_1 = self.getValsOfTree(root1)
        vals_2 = self.getValsOfTree(root2)
        vals = vals_1 + vals_2
        return sorted(vals)

    def getValsOfTree(self, root: TreeNode) -> List[int]:
        if not root or root.val is None:
            return []
        else:
            vals = []
            nodes = [root]
            while nodes:
                node = nodes.pop(0)
                vals.append(node.val)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            return vals


class TestGetAllElements(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def create_tree_from_list(self, vals: List[int], i: int = 0) -> TreeNode:
        if i >= len(vals):
            return None
        if vals[i] is None:
            return None
        return TreeNode(vals[i], self.create_tree_from_list(vals, 2*i+1),
                        self.create_tree_from_list(vals, 2*i+2))

    def create_list_from_tree(self, root: TreeNode) -> List[int]:
        nodes = []
        nodes_to_visit = [root]

        nodes_per_level = 1
        visited_nodes = 0
        count_nodes_None = 0

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node is None:
                count_nodes_None += 1
                nodes_to_visit.append(None)
                nodes_to_visit.append(None)
                nodes.append(None)
            else:
                nodes.append(node.val)
                nodes_to_visit.append(node.left)
                nodes_to_visit.append(node.right)

            visited_nodes += 1

            # one level completed?
            if nodes_per_level == visited_nodes:
                if count_nodes_None == nodes_per_level:
                    nodes = nodes[:len(nodes)-nodes_per_level]
                    while 1:
                        if nodes[-1] is None:
                            del nodes[-1]
                        else:
                            break
                    break
                else:
                    nodes_per_level *= 2
                    count_nodes_None = 0
                    visited_nodes = 0

        return nodes

    def print_tree_from_list(self, nodes: List[int]):
        # find number of levels
        num_nodes = len(nodes)
        level = 1
        bigger_level = 2
        while 1:
            if num_nodes <= bigger_level-1:
                break
            else:
                bigger_level *= 2
                level += 1

        printed_nodes = 0
        space = int(bigger_level)*5
        string = "{:^" + str(space) + "}"
        nodes_per_level = 1

        for node in nodes:
            print(string.format(str(node)), end="")
            printed_nodes += 1
            if nodes_per_level == printed_nodes:
                print()
                print()
                nodes_per_level *= 2
                printed_nodes = 0
                bigger_level /= 2
                space = int(bigger_level) * 5
                string = "{:^"+str(space)+"}"
        print()

    def testGetAllElements_1(self):
        vals_1 = [2, 1, 4]
        vals_2 = [1, 0, 3]
        root_1 = self.create_tree_from_list(vals_1)
        root_2 = self.create_tree_from_list(vals_2)

        elements = self.sol.getAllElements(root_1, root_2)

        self.assertEqual(elements, [0, 1, 1, 2, 3, 4])

    def testGetAllElements_2(self):
        vals_1 = [0, -10, 10]
        vals_2 = [5, 1, 7, 0, 2]
        root_1 = self.create_tree_from_list(vals_1)
        root_2 = self.create_tree_from_list(vals_2)

        elements = self.sol.getAllElements(root_1, root_2)

        self.assertEqual(elements, [-10, 0, 0, 1, 2, 5, 7, 10])

    def testGetAllElements_3(self):
        vals_1 = [0, -10, 10]
        root_1 = self.create_tree_from_list(vals_1)
        root_2 = TreeNode(None)

        elements = self.sol.getAllElements(root_1, root_2)

        self.assertEqual(elements, [-10, 0, 10])

    def testGetAllElements_4(self):
        root_1 = TreeNode(None)
        root_2 = TreeNode(None)

        elements = self.sol.getAllElements(root_1, root_2)

        self.assertEqual(elements, [])


if __name__ == "__main__":
    unittest.main()
