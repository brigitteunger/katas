import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class TestDeleteNode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def generate_linked_list(self, vals: List[int]) -> ListNode:
        if not vals:
            return None
        head = ListNode(vals[0])
        node = head
        for val in vals[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

    def generate_list(self, head: ListNode) -> List[int]:
        vals = []
        node = head
        while 1:
            if node is None:
                break
            vals.append(node.val)
            node = node.next
        return vals

    def test_delete_node_second_node(self):
        vals = [4, 5, 1, 9]
        # node = 5
        expected_list = [4, 1, 9]

        head = self.generate_linked_list(vals)
        self.sol.deleteNode(head.next)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_delete_node_third_node(self):
        vals = [4, 5, 1, 9]
        # node = 1
        expected_list = [4, 5, 9]

        head = self.generate_linked_list(vals)
        self.sol.deleteNode(head.next.next)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_delete_node_first_node(self):
        vals = [4, 5, 1, 9]
        # node = 4
        expected_list = [5, 1, 9]

        head = self.generate_linked_list(vals)
        self.sol.deleteNode(head)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)
