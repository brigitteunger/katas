import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        vals = self.linkedList2List(head)
        vals.sort()
        head = self.list2LinkedList(vals)
        return head

    def list2LinkedList(self, my_list: List[int]) -> ListNode:
        node = None
        for val in reversed(my_list):
            node = ListNode(val, node)
        return node

    def linkedList2List(self, head) -> List:
        my_list = []
        node = head
        while node:
            my_list.append(node.val)
            node = node.next
        return my_list


class TestSortList(unittest.TestCase):
    def list2LinkedList(self, my_list: List[int]) -> ListNode:
        node = None
        for val in reversed(my_list):
            node = ListNode(val, node)
        return node

    def linkedList2List(self, head) -> List:
        my_list = []
        node = head
        while node:
            my_list.append(node.val)
            node = node.next
        return my_list

    def setUp(self):
        self.sol = Solution()

    def testSort_1(self):
        head = self.list2LinkedList([4, 2, 1, 3])

        sorted_head = self.sol.sortList(head)
        sorted_list = self.linkedList2List(sorted_head)

        self.assertEqual(sorted_list, [1, 2, 3, 4])

    def testSort_2(self):
        head = self.list2LinkedList([-1, 5, 3, 4, 0])

        sorted_head = self.sol.sortList(head)
        sorted_list = self.linkedList2List(sorted_head)

        self.assertEqual(sorted_list, [-1, 0, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
