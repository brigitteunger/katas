import unittest
from typing import Dict, List
from data_test_width_of_binary_tree import nodes_1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        range_per_level = {}
        self.updateRanges(root, range_per_level, 0, 0)
        return self.findMaxWidth(range_per_level)

    def updateRanges(self, node: TreeNode, range_per_level: Dict, level: int,
                     pos: int) -> None:
        if level in range_per_level:
            current_range = range_per_level[level]
            if pos < current_range[0]:
                current_range[0] = pos
            if pos > current_range[1]:
                current_range[1] = pos
        else:
            range_per_level[level] = [pos, pos]

        if node.left:
            self.updateRanges(
                node.left, range_per_level, level + 1, 2 * pos)
        if node.right:
            self.updateRanges(
                node.right, range_per_level, level + 1, (2 * pos) + 1)

    def findMaxWidth(self, range_per_level: Dict) -> int:
        max_width = 0
        for current_range in range_per_level.values():
            width = current_range[1] - current_range[0] + 1
            if width > max_width:
                max_width = width
        return max_width


class TestWidthOfBinaryTree(unittest.TestCase):
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

    def test_width_of_bin_tree_6_4(self):
        nodes = [1, 3, 2, 5, 3, None, 9]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 4)

    def test_width_of_bin_tree_4_2(self):
        nodes = [1, 3, None, 5, 3]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 2)

    def test_width_of_bin_tree_4_2_2(self):
        nodes = [1, 3, 2, 5]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 2)

    def test_width_of_bin_tree_15_8(self):
        nodes = [1, 3, 2, 5, None, None, 9, 6, None, None, None, None, None,
                 None, 7]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 8)

    def test_width_of_bin_tree_14_2_left_gap(self):
        nodes = [1, None, 2, None, None, 3, 4]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 2)

    def tesst_width_of_bin_tree_long(self):
        root = self.create_tree_from_list(nodes_1)

        width = self.sol.widthOfBinaryTree(root)

        self. assertEqual(width, 1018)

    def test_width_of_bin_tree_7_5(self):
        nodes = [1, 3, None, 5, 3]
        # self.print_tree_from_list(nodes)
        root = self.create_tree_from_list(nodes)
        nodes_processed = self.create_list_from_tree(root)
        self.assertEqual(nodes, nodes_processed)

        width = self.sol.widthOfBinaryTree(root)

        self.assertEqual(width, 2)


if __name__ == "__main__":
    # nodes = [1, 3, None, 5, 3]
    # test_ = TestWidthOfBinaryTree()
    # test_.print_tree_from_list(nodes)
    # test_.create_tree_from_list(nodes)
    # test_.setUp()
    # test_.test_width_of_bin_tree_14_2_left_gap()
    unittest.main()
