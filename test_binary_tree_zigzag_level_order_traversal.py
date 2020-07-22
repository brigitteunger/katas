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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        nodes_to_visit = [root]
        to_do_actual_level = 1
        to_do_next_level = 0
        zigzag_vals = []
        level_vals = []
        right_2_left = False
        while 1:
            if not nodes_to_visit:
                break

            node = nodes_to_visit.pop(0)
            level_vals.append(node.val)
            to_do_actual_level -= 1

            if node.left is not None:
                to_do_next_level += 1
                nodes_to_visit.append(node.left)
            if node.right is not None:
                to_do_next_level += 1
                nodes_to_visit.append(node.right)

            if to_do_actual_level == 0:
                to_do_actual_level = to_do_next_level
                to_do_next_level = 0
                if right_2_left:
                    level_vals.reverse()
                    right_2_left = False
                else:
                    right_2_left = True
                zigzag_vals.append(level_vals)
                level_vals = []

        return zigzag_vals


class TestzigZagLevelOrder(unittest.TestCase):
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

    def testZigZagLevelOrder_5(self):
        vals = [3, 9, 20, None, None, 15, 7]
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        zigzag_vals = self.sol.zigzagLevelOrder(root)

        self.assertEqual(zigzag_vals, [[3], [20, 9], [15, 7]])

    def testZigZagLevelOrder_7(self):
        vals = [3, 9, 20, 1, 2, 15, 7]
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        zigzag_vals = self.sol.zigzagLevelOrder(root)

        self.assertEqual(zigzag_vals, [[3], [20, 9], [1, 2, 15, 7]])

    def testZigZagLevelOrder_1(self):
        root = TreeNode(0)

        zigzag_vals = self.sol.zigzagLevelOrder(root)

        self.assertEqual(zigzag_vals, [[0]])


if __name__ == "__main__":
    unittest.main()
