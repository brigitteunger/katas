import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        if root.val is None:
            return []

        vals = []
        level_list = []
        nodes_to_visit = [root]
        nodes_per_level = 1

        while 1:
            if not nodes_to_visit:
                if level_list:
                    vals.insert(0, level_list)
                break

            node = nodes_to_visit.pop(0)

            if node.val is not None:
                level_list.append(node.val)
            nodes_per_level -= 1

            if node.left:
                nodes_to_visit.append(node.left)

            if node.right:
                nodes_to_visit.append(node.right)

            if nodes_per_level == 0:
                vals.insert(0, level_list)
                level_list = []
                nodes_per_level = len(nodes_to_visit)

        return vals


class TestLevelOrderBottom(unittest.TestCase):
    def build_tree_from_list(self, vals: List[int], i: int = 0) -> TreeNode:
        if i >= len(vals):
            return None
        return TreeNode(vals[i], self.build_tree_from_list(vals, 2*i+1),
                        self.build_tree_from_list(vals, 2*i+2))

    def setUp(self):
        self.sol = Solution()

    def test_level_order_bottom_5_nodes(self):
        vals = [3, 9, 20, None, None, 15, 7]
        root = self.build_tree_from_list(vals)

        bottom_up_level = self.sol.levelOrderBottom(root)

        self.assertEqual(bottom_up_level,
                         [[15, 7], [9, 20], [3]])

    def test_level_order_bottom_7_nodes(self):
        vals = [1, 2, 3, 4, 5, 6, 7]
        root = self.build_tree_from_list(vals)

        bottom_up_level = self.sol.levelOrderBottom(root)

        self.assertEqual(bottom_up_level,
                         [[4, 5, 6, 7], [2, 3], [1]])

    def test_level_order_bottom_1_node(self):
        vals = [1]
        root = self.build_tree_from_list(vals)

        bottom_up_level = self.sol.levelOrderBottom(root)

        self.assertEqual(bottom_up_level,
                         [[1]])

    def test_level_order_bottom_12_nodes(self):
        vals = [1, 2, 3, None, 5, 6, 7, None, None, 10, 11,
                12, 13, 14, 15]
        root = self.build_tree_from_list(vals)

        bottom_up_level = self.sol.levelOrderBottom(root)

        self.assertEqual(bottom_up_level,
                         [[10, 11, 12, 13, 14, 15],
                          [5, 6, 7], [2, 3], [1]])

    def test_level_order_bottom_5_nodes_holes(self):
        root = TreeNode(
                1,
                TreeNode(
                    2,
                    TreeNode(
                        3,
                        TreeNode(
                            4,
                            TreeNode(5)
                        )
                    )
                )
            )

        bottom_up_level = self.sol.levelOrderBottom(root)

        self.assertEqual(bottom_up_level,
                         [[5], [4], [3], [2], [1]])

    def test_level_order_bottom_empty(self):
        bottom_up_level = self.sol.levelOrderBottom(None)

        self.assertEqual(bottom_up_level, [])


if __name__ == "__main__":
    unittest.main()
