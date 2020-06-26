import unittest
from typing import List


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def sumNumbers(self, root: TreeNode) -> int:
        nums = self.build_nums_from_tree(root)
        return sum(nums)

    def build_nums_from_tree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nodes = []
        nodes.append([root, str(root.val)])
        nums = []
        while 1:
            if not nodes:
                break
            node = nodes.pop(0)
            if node[0].left is not None:
                nodes.insert(
                    0,
                    [node[0].left, node[1] + str(node[0].left.val)]
                )
            if node[0].right is not None:
                nodes.insert(
                    0,
                    [node[0].right, node[1] + str(node[0].right.val)]
                )
            if node[0].right is None and node[0].left is None:
                nums.append(int(node[1]))

        return nums


class TestSumNumber(unittest.TestCase):
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

    def test_sum_number_123(self):
        vals = [1, 2, 3]
        root = self.build_tree_from_list(vals)

        sum = self.sol.sumNumbers(root)

        self.assertEqual(sum, 25)

    def test_sum_number_123456(self):
        vals = [1, 2, 3, 4, 5, 6]
        root = self.build_tree_from_list(vals)

        sum = self.sol.sumNumbers(root)

        self.assertEqual(sum, 385)

    def test_sum_number_49051(self):
        vals = [4, 9, 0, 5, 1]
        root = self.build_tree_from_list(vals)

        sum = self.sol.sumNumbers(root)

        self.assertEqual(sum, 1026)

    def test_sum_number_None(self):
        root = None

        sum = self.sol.sumNumbers(root)

        self.assertEqual(sum, 0)


if __name__ == "__main__":
    unittest.main()
