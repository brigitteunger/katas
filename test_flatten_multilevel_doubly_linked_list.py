import unittest
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next_=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next_
        self.child = child

    def printNode(self):
        print(str(self.val), end="")
        if self.child is not None:
            children = [self.child]
        else:
            children = []

        node = self.next
        print_child = False
        while 1:
            if print_child:
                if children:
                    node = children.pop()
                if node is not None:
                    print_child = False
                    print()
                    print()
                else:
                    break

            else:
                if node:
                    print("--" + str(node.val), end="")
                    if node.child is not None:
                        children.append(node.child)
                    node = node.next
                else:
                    print_child = True


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        flattened = []
        heads_of_loose_lists = [head]
        while heads_of_loose_lists:
            node = heads_of_loose_lists[-1]
            del heads_of_loose_lists[-1]
            while node is not None:
                flattened.append(node.val)
                if node.child is None:
                    node = node.next
                else:
                    if node.next is not None:
                        heads_of_loose_lists.append(node.next)
                    node = node.child

        return self.to_linked_list(flattened)

    def to_linked_list(self, list: List) -> 'Node':
        head = None
        predecessor = None
        for item in list:
            if predecessor is None:
                head = Node(item, None, None, None)
                predecessor = head
            else:
                node = Node(item, predecessor, None, None)
                predecessor.next = node
                predecessor = node
        return head


class TestFlatten(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def to_list(self, head: 'Node') -> List[int]:
        values = []
        node = head
        while node is not None:
            self.assertIsNone(
                node.child,
                "Node with value " + str(node.val) + " has a child.")
            values.append(node.val)
            node = node.next
        return values

    def test_empty_list(self):
        headFlattened = self.sol.flatten(None)

        self.assertIsNone(headFlattened)

    def test_list_without_child(self):
        head = self.sol.to_linked_list([1, 2, 3, 4])

        headFlattened = self.sol.flatten(head)

        self.assertEquals(
            self.to_list(headFlattened),
            [1, 2, 3, 4])

    def test_list_with_1_child(self):
        head = self.sol.to_linked_list([1, 2, 3])
        head.next.child = self.sol.to_linked_list([4, 5])

        headFlattened = self.sol.flatten(head)

        self.assertEquals(
            self.to_list(headFlattened),
            [1, 2, 4, 5, 3])

    def test_list_with_last_element_has_child(self):
        head = self.sol.to_linked_list([1, 2])
        head.next.child = self.sol.to_linked_list([3, 4])

        headFlattened = self.sol.flatten(head)

        self.assertEquals(
            self.to_list(headFlattened),
            [1, 2, 3, 4])

    def test_list_with_2_children(self):
        head = self.sol.to_linked_list([1, 2, 3])
        head.next.child = self.sol.to_linked_list([4, 5, 6])
        head.next.child.next.child = self.sol.to_linked_list([7, 8, 9])

        headFlattened = self.sol.flatten(head)

        self.assertEquals(
            self.to_list(headFlattened),
            [1, 2, 4, 5, 7, 8, 9, 6, 3])

    def tesst_print_node(self):
        node_1 = Node(1)
        node_2 = Node(2, node_1)
        node_3 = Node(3)
        node_1.next = node_2
        node_1.child = node_3
        node_1.printNode()


if __name__ == "__main__":
    unittest.main()
