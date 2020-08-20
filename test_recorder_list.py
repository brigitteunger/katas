import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        nodes_list = []
        node = head
        while 1:
            if node is None:
                break
            nodes_list.append(node)
            node = node.next

        num_nodes = len(nodes_list)
        node = head
        i = 1
        count = num_nodes
        while 1:
            if count == 0:
                break
            node.next = nodes_list[-(i)]
            node = node.next
            count -= 1
            if count == 0:
                break
            node.next = nodes_list[i]
            node = node.next
            count -= 1
            i += 1
        node.next = None


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

    def test_recorder_list_1(self):
        vals = [1, 2, 3, 4]
        expected_list = [1, 4, 2, 3]

        head = self.generate_linked_list(vals)
        self.sol.reorderList(head)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_recorder_list_2(self):
        vals = [1, 2, 3, 4, 5]
        expected_list = [1, 5, 2, 4, 3]

        head = self.generate_linked_list(vals)
        self.sol.reorderList(head)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_recorder_list_3(self):
        vals = [1, 2]
        expected_list = [1, 2]

        head = self.generate_linked_list(vals)
        self.sol.reorderList(head)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_recorder_list_4(self):
        vals = [1]
        expected_list = [1]

        head = self.generate_linked_list(vals)
        self.sol.reorderList(head)
        actual_list = self.generate_list(head)

        self.assertEqual(actual_list, expected_list)

    def test_recorder_list_5(self):
        head = None
        self.sol.reorderList(head)

        self.assertEqual(head, None)


if __name__ == "__main__":
    unittest.main()
