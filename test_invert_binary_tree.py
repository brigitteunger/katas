import unittest
from typing import List


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root


class TestInvertTree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_list_from_tree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        list_ = []
        nodes = []
        nodes.append(root)
        i = 0
        while 1:
            if i > len(nodes)-1:
                break
            if nodes[i] is None:
                i += 1
                continue
            if nodes[i].left is not None:
                nodes.append(nodes[i].left)
            else:
                if nodes[i].right is not None:
                    nodes.append(None)
            if nodes[i].right is not None:
                nodes.append(nodes[i].right)
            else:
                if nodes[i].left is not None:
                    nodes.append(None)
            i += 1
        for node in nodes:
            if node is not None:
                list_.append(node.val)
            else:
                list_.append(None)
        return list_

    def build_tree_from_list(self, vals: List[int], i: int = 0) -> TreeNode:
        if i >= len(vals):
            return None
        return TreeNode(vals[i], self.build_tree_from_list(vals, 2*i+1),
                        self.build_tree_from_list(vals, 2*i+2))

    def test_build(self):
        list_ = [4, 2, 7, 1, 3, 6, 9]

        root = self.build_tree_from_list(list_)
        actual_list = self.build_list_from_tree(root)

        self.assertEqual(actual_list, list_)

    def test_build_none(self):
        list_ = [4, 2, 7, 1, None, 6, None]

        root = self.build_tree_from_list(list_)
        actual_list = self.build_list_from_tree(root)

        self.assertEqual(actual_list, list_)

    def test_build_last_two_none(self):
        list_ = [4, 2, 7, 1, 3, None, None]

        root = self.build_tree_from_list(list_)
        actual_list = self.build_list_from_tree(root)

        self.assertEqual(actual_list, list_)

    def assert_trees_equal(self, actual_root, expect_list):
        actual_list = self.build_list_from_tree(actual_root)
        self.assertEqual(actual_list, expect_list)

    def test_invert_tree(self):
        list_ = [4, 2, 7, 1, 3, 6, 9]
        expect_list = [4, 7, 2, 9, 6, 3, 1]

        root = self.build_tree_from_list(list_)
        inverted_tree = self.sol.invertTree(root)

        self.assert_trees_equal(inverted_tree, expect_list)

    def test_invert_tree_leaf_None(self):
        list_ = [4, 2, 7, 1, 3, 6]
        expect_list = [4, 7, 2, None, 6, 3, 1]

        root = self.build_tree_from_list(list_)
        inverted_tree = self.sol.invertTree(root)

        self.assert_trees_equal(inverted_tree, expect_list)

    def test_invert_tree_two_leafs_None(self):
        list_ = [4, 2, 7, 1, 3, None, None]
        expect_list = [4, 7, 2, None, None, 3, 1]

        root = self.build_tree_from_list(list_)
        inverted_tree = self.sol.invertTree(root)

        self.assert_trees_equal(inverted_tree, expect_list)

    def test_invert_tree_only_root(self):
        list_ = [4]
        expect_list = [4]

        root = self.build_tree_from_list(list_)
        inverted_tree = self.sol.invertTree(root)

        self.assert_trees_equal(inverted_tree, expect_list)

    def test_invert_tree_empty(self):
        list_ = []
        expect_list = []

        root = self.build_tree_from_list(list_)
        inverted_tree = self.sol.invertTree(root)

        self.assert_trees_equal(inverted_tree, expect_list)


test_ = TestInvertTree()
test_.test_build()
test_.test_build_none()
