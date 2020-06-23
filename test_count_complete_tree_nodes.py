import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        else:
            if root.left is not None and root.right is not None:
                return (1 + self.countNodes(root.left)
                        + self.countNodes(root.right))
            elif root.left is not None and root.right is None:
                return self.countNodes(root.left) + 1
            else:
                return self.countNodes(root.right) + 1


class TestCountNodes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_tree_from_list(self, vals: List[int], i: int = 0) -> TreeNode:
        if i >= len(vals):
            return None
        return TreeNode(vals[i], self.build_tree_from_list(vals, 2*i+1),
                        self.build_tree_from_list(vals, 2*i+2))

    def test_count_nodes_6(self):
        nodes = [1, 2, 3, 4, 5, 6]
        root = self.build_tree_from_list(nodes)

        num_nodes = self.sol.countNodes(root)

        self.assertEqual(num_nodes, 6)

    def test_count_nodes_10(self):
        nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root = self.build_tree_from_list(nodes)

        num_nodes = self.sol.countNodes(root)

        self.assertEqual(num_nodes, 10)

    def test_count_nodes_1(self):
        nodes = [1]
        root = self.build_tree_from_list(nodes)

        num_nodes = self.sol.countNodes(root)

        self.assertEqual(num_nodes, 1)

    def test_count_nodes_5(self):
        nodes = [1, 2, 3, 1, 1]
        root = self.build_tree_from_list(nodes)

        num_nodes = self.sol.countNodes(root)

        self.assertEqual(num_nodes, 5)

    def test_count_nodes_0(self):
        nodes = []
        root = self.build_tree_from_list(nodes)

        num_nodes = self.sol.countNodes(root)

        self.assertEqual(num_nodes, 0)


if __name__ == "__main__":
    unittest.main()
