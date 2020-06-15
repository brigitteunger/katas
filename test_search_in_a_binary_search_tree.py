import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        else:
            if root.left is not None:
                node = self.searchBST(root.left, val)
                if node is not None:
                    return node
            if root.right is not None:
                node = self.searchBST(root.right, val)
                if node is not None:
                    return node
        return None


class TestSearchBST(unittest.TestCase):
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

    def test_search_BST_easy(self):
        tree_list = [4, 2, 7, 1, 3]
        root = self.build_tree_from_list(tree_list)
        val = 2
        expected_list = [2, 1, 3]

        actual_node = self.sol.searchBST(root, val)
        actual_list = self.build_list_from_tree(actual_node)

        self.assertEqual(actual_list, expected_list)

    def test_search_BST_return_tree_no_child(self):
        tree_list = [4, 2, 7, 1, 3]
        root = self.build_tree_from_list(tree_list)
        val = 7
        expected_list = [7]

        actual_node = self.sol.searchBST(root, val)
        actual_list = self.build_list_from_tree(actual_node)

        self.assertEqual(actual_list, expected_list)

    def test_search_BST_val_not_in_tree(self):
        tree_list = [4, 2, 7, 1, 3]
        root = self.build_tree_from_list(tree_list)
        val = 5

        actual_node = self.sol.searchBST(root, val)

        self.assertEqual(actual_node, None)

    def test_search_BST_val_not_in_tree_one_node(self):
        tree_list = [1]
        root = self.build_tree_from_list(tree_list)
        val = 5

        actual_node = self.sol.searchBST(root, val)

        self.assertEqual(actual_node, None)


if __name__ == "__main__":
    unittest.main()
