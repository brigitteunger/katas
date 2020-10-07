import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 0 element linked list:
        if head is None:
            return None

        num_elem = self.countVals(head)
        # 1 element linked list:
        if num_elem == 1:
            return head

        # 2 element linked list:
        if num_elem == 2:
            if k % 2 == 1:
                val_head = head.val
                head.val = head.next.val
                head.next.val = val_head
            return head

        # else:
        steps = k % num_elem
        for _ in range(steps):
            node = head
            while 1:
                if node.next.next is None:
                    node.next.next = head
                    head = node.next
                    node.next = None
                    break
                node = node.next

        return head

    def countVals(self, head: ListNode) -> int:
        node = head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter


class TestRotateRight(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def createLinkedListFromList(self, vals: List[int]) -> ListNode:
        next = None
        for val in vals[::-1]:
            next = ListNode(val, next)
        return next

    def createListFromLinkedList(self, head: ListNode) -> List[int]:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals

    def testConvertions(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        head = self.createLinkedListFromList(vals)
        vals_of_ll = self.createListFromLinkedList(head)

        self.assertEqual(vals_of_ll, vals)

    def testRotateRight_1(self):
        vals = [1, 2, 3, 4, 5]
        k = 2
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [4, 5, 1, 2, 3])

    def testRotateRight_2(self):
        vals = [0, 1, 2]
        k = 4
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [2, 0, 1])

    def testRotateRight_3(self):
        vals = [0]
        k = 4
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [0])

    def testRotateRight_4(self):
        vals = [0, 1]
        k = 1
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [1, 0])

    def testRotateRight_5(self):
        vals = [0, 1]
        k = 2
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [0, 1])

    def testRotateRight_6(self):
        vals = [0, 1, 3]
        k = 20000
        head = self.createLinkedListFromList(vals)

        head_rotated = self.sol.rotateRight(head, k)
        vals_rotated = self.createListFromLinkedList(head_rotated)

        self.assertEqual(vals_rotated, [1, 3, 0])


if __name__ == "__main__":
    unittest.main()
