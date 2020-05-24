import unittest
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        i = 0
        while i < n:
            node = node.next
            i += 1
        if node is None:
            return head.next
        else:
            node = node.next
        new_node = head
        while node is not None:
            node = node.next
            new_node = new_node.next
        new_node.next = new_node.next.next
        return head


class TestRemoveNthFromEnd(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def create_linked_list(self, values: List) -> ListNode:
        last_node = None
        for item in reversed(values):
            node = ListNode(item, last_node)
            last_node = node
        return last_node

    def create_list(self, head: ListNode) -> List:
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next
        return values

    def test_removeNthFromEnd(self):
        values = list(range(1, 6))
        head = self.create_linked_list(values)

        head_after_remove = self.sol.removeNthFromEnd(head, 2)

        list_after_remove = self.create_list(head_after_remove)
        self.assertEqual(list_after_remove, [1, 2, 3, 5])

    def test_removeNthFromEnd_remove_first_item(self):
        values = list(range(1, 6))
        head = self.create_linked_list(values)

        head_after_remove = self.sol.removeNthFromEnd(head, 5)

        list_after_remove = self.create_list(head_after_remove)
        self.assertEqual(list_after_remove, [2, 3, 4, 5])

    def test_removeNthFromEnd_remove_last_item(self):
        values = list(range(1, 6))
        head = self.create_linked_list(values)

        head_after_remove = self.sol.removeNthFromEnd(head, 1)

        list_after_remove = self.create_list(head_after_remove)
        self.assertEqual(list_after_remove, [1, 2, 3, 4])
