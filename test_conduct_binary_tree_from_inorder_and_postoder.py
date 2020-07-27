import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        num_vals = len(inorder)
        if num_vals == 1:
            return TreeNode(inorder[0])

        root_val = postorder[-1]
        print("inorder:")
        print(inorder)
        print()
        print("postorder:")
        print(postorder)
        print()
        index_root_inorder = inorder.index(root_val)
        nums_nodes_left = index_root_inorder
        # left side of tree
        left = self.buildTree(inorder[: nums_nodes_left],
                              postorder[: nums_nodes_left])
        # right side of tree
        right = self.buildTree(inorder[index_root_inorder+1:],
                               postorder[nums_nodes_left: num_vals-1])
        return TreeNode(root_val, left, right)


class TestBuiltTree(unittest.TestCase):
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

    def test_build_tree_1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        expected_vals = [3, 9, 20, None, None, 15, 7]

        root = self.sol.buildTree(inorder, postorder)
        actual_vals = self.create_list_from_tree(root)

        self.assertEqual(actual_vals, expected_vals)

    def test_build_tree_2(self):
        inorder = [1, 2, 3, 4]
        postorder = [4, 3, 2, 1]
        expected_vals = [1, None, 2, None, None, None, 3, None, None, None,
                         None, None, None, None, 4]
        self.print_tree_from_list(expected_vals)

        root = self.sol.buildTree(inorder, postorder)
        actual_vals = self.create_list_from_tree(root)

        self.assertEqual(actual_vals, expected_vals)




if __name__ == "__main__":
    unittest.main()
