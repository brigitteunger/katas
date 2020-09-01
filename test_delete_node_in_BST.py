import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            if root.left is not None:
                root.val = root.left.val
                root.right = self.addSubtree(root.right, root.left.right)
                root.left = root.left.left
            else:
                return root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def addSubtree(self, root: TreeNode, subtree: TreeNode,):
        if not subtree:
            return root
        if not root:
            return subtree
        head = root
        while head.left:
            head = head.left
        head.left = subtree
        return root


class TestDeleteode(unittest.TestCase):
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

    def testDeleteNode_0_children_1(self):
        vals = [5, 3, 6, 2, 4, None, 7]
        key = 4
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 3, 6, 2, None, None, 7])

    def testDeleteNode_0_children_2(self):
        vals = [5, 3, 6, 2, 4, None, 7]
        key = 7
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 3, 6, 2, 4])

    def testDeleteNode_1_child_right_right(self):
        vals = [5, 3, 6, 2, 4, None, 7]
        key = 6
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 3, 7, 2, 4])

    def testDeleteNode_1_child_right_left(self):
        vals = [5, 3, 6, 2, 4, 7, None]
        key = 6
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 3, 7, 2, 4])

    def testDeleteNode_1_child_left_left(self):
        vals = [5, 3, 6, 2, None, None, 7]
        key = 3
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 2, 6, None, None, None, 7])

    def testDeleteNode_1_child_left_right(self):
        vals = [5, 3, 6, None, 2, None, 7]
        key = 3
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 2, 6, None, None, None, 7])

    def testDeleteNode_2_children(self):
        vals = [5, 3, 6, 2, 4, None, 7]
        key = 3
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 2, 6, None, 4, None, 7])

    def testDeleteNode_root(self):
        vals = [5, 3, 6, 2, 4, None, 7]
        key = 5
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [3, 2, 6, None, None, 4, 7])

    def testDeleteNode_1(self):
        vals = [5, 3, 6, 1, 4, None, None, None, 2]
        key = 3
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, [5, 1, 6, None, 4, None, None, None,
                                       None, 2])

    def testDeleteNode_2(self):
        vals = [2, 0, 33, None, 1, 25, 40, None, None, 11, 31, 34, 45, 10,
                18, 29, 32, None, 36, 43, 46, 4, None, 12, 24, 26, 30, None,
                None, 35, 39, 42, 44, None, 48, 3, 9, None, 14, 22, None,
                None, 27, None, None, None, None, 38, None, 41, None, None,
                None, 47, 49, None, None, 5, None, 13, 15, 21, 23, None, 28,
                37, None, None, None, None, None, None, None, None, 8, None,
                None, None, 17, 19, None, None, None, None, None, None, None,
                7, None, 16, None, None, 20, 6]
        key = 33
        expected_vals = [2, 0, 25, None, 1, 34, 40, None, None, 11, 31, 12, 24,
                         10, 18, None, None, None, None, 43, 46, 4, None, 38,
                         None, 41, None, 45, None, 35, 39, None, None, None,
                         None, None, None, None, None, 22, None, None, 27,
                         None, None, None, None, None, None, None, None, None,
                         None, None, None, 26, 30, None, None, 13, 15, 21, 23,
                         None, None, None, None, None, None, None, None, None,
                         None, None, None, None, None, None, None, 19, None,
                         None, None, None, None, None, None, None, None, None,
                         None, None, None, None, None, None, None, None, None,
                         None, None, None, None, None, None, None, None, None,
                         None, None, None, None, None, 47, 49]
        root = self.create_tree_from_list(vals)
        # self.print_tree_from_list(vals)

        actual_root = self.sol.deleteNode(root, key)
        actual_vals = self.create_list_from_tree(actual_root)
        # self.print_tree_from_list(actual_vals)

        self.assertEqual(actual_vals, expected_vals)


if __name__ == "__main__":
    unittest.main()
