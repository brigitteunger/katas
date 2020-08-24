import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        sum_ = 0
        nodes = [[root, False]]
        while nodes:
            node = nodes.pop(0)
            if node[1]:
                if node[0].left is None and node[0].right is None:
                    sum_ += node[0].val
            if node[0].left is not None:
                nodes.append([node[0].left, True])
            if node[0].right is not None:
                nodes.append([node[0].right, False])
        return sum_


class TestSumOfLeftLeaves(unittest.TestCase):
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

    def test_list_2_tree_2_list_7_1(self):
        nodes = [1, 3, 2, 5, 3, None, 9]

        root = self.create_tree_from_list(nodes)
        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def test_list_2_tree_7_1(self):
        nodes = [1, 3, 2, 5, 3, None, 9]

        root = self.create_tree_from_list(nodes)
        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def test_tree_2_list_15_8(self):
        nodes = [1, 3, 2, 5, None, None, 9, 6, None, None, None, None, None,
                 None, 7]
        root = TreeNode(1,
                        TreeNode(3, TreeNode(5, TreeNode(6))),
                        TreeNode(2, None, TreeNode(9, None, TreeNode(7)))
                        )

        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def test_tree_2_list_3_0(self):
        nodes = [1, 3, 2]
        root = TreeNode(1,
                        TreeNode(3),
                        TreeNode(2)
                        )

        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def test_tree_2_list_3_1(self):
        nodes = [1, None, 2]
        root = TreeNode(1,
                        None,
                        TreeNode(2)
                        )

        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def test_tree_2_list_7_1(self):
        nodes = [1, None, 2, None, None, None, 4]
        root = TreeNode(1,
                        None,
                        TreeNode(2, None, TreeNode(4))
                        )

        actual_nodes = self.create_list_from_tree(root)

        self.assertEqual(actual_nodes, nodes)

    def testSumOfLeftLeaves_1(self):
        nodes = [3, 9, 20, None, None, 15, 7]
        root = self.create_tree_from_list(nodes)

        sum_ = self.sol.sumOfLeftLeaves(root)

        self. assertEqual(sum_, 24)

    def testSumOfLeftLeaves_2(self):
        nodes = [0]

        root = self.create_tree_from_list(nodes)

        sum_ = self.sol.sumOfLeftLeaves(root)

        self. assertEqual(sum_, 0)

    def testSumOfLeftLeaves_3(self):
        root = None

        sum_ = self.sol.sumOfLeftLeaves(root)

        self. assertEqual(sum_, 0)


if __name__ == "__main__":
    unittest.main()
