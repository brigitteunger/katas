import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        if q is None:
            return False

        nodes_to_visit_1 = [p]
        nodes_to_visit_2 = [q]

        while 1:
            if not nodes_to_visit_1 and not nodes_to_visit_2:
                return True
            if not nodes_to_visit_1:
                return False
            if not nodes_to_visit_2:
                return False
            # else:

            node_1 = nodes_to_visit_1.pop(0)
            node_2 = nodes_to_visit_2.pop(0)

            if node_1.val != node_2.val:
                return False
            else:
                left_1 = node_1.left
                left_2 = node_2.left
                if left_1 is None:
                    if left_2 is None:
                        pass
                    else:
                        return False
                elif left_2 is None:
                    return False
                else:
                    nodes_to_visit_1.append(left_1)
                    nodes_to_visit_2.append(left_2)

                right_1 = node_1.right
                right_2 = node_2.right
                if right_1 is None:
                    if right_2 is None:
                        pass
                    else:
                        return False
                elif right_2 is None:
                    return False
                else:
                    nodes_to_visit_1.append(right_1)
                    nodes_to_visit_2.append(right_2)

        return False


class TestIsSameTree(unittest.TestCase):
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

    def test_is_same_tree_123_True(self):
        vals_1 = [1, 2, 3]
        tree_1 = self.create_tree_from_list(vals_1)
        tree_2 = self.create_tree_from_list(vals_1)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertTrue(same_tree)

    def test_is_same_tree_12_False(self):
        vals_1 = [1, 2]
        vals_2 = [1, None, 2]
        tree_1 = self.create_tree_from_list(vals_1)
        tree_2 = self.create_tree_from_list(vals_2)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertFalse(same_tree)

    def test_is_same_tree_11_False(self):
        vals_1 = [1, 1, 2]
        vals_2 = [1, 2, 1]
        tree_1 = self.create_tree_from_list(vals_1)
        tree_2 = self.create_tree_from_list(vals_2)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertFalse(same_tree)

    def test_is_same_tree_6072_False(self):
        vals_1 = [1, None, -60]
        vals_2 = [1, None, 72]
        tree_1 = self.create_tree_from_list(vals_1)
        tree_2 = self.create_tree_from_list(vals_2)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertFalse(same_tree)

    def test_is_same_tree_1_True(self):
        tree_1 = TreeNode(1)
        tree_2 = TreeNode(1)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertTrue(same_tree)

    def test_is_same_tree_1_False(self):
        tree_1 = TreeNode(1)
        tree_2 = TreeNode(0)

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertFalse(same_tree)

    def test_is_same_tree_None_True(self):
        tree_1 = None
        tree_2 = None

        same_tree = self.sol.isSameTree(tree_1, tree_2)

        self.assertTrue(same_tree)


if __name__ == "__main__":
    unittest.main()
