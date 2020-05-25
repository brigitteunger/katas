import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def merge_two_lists(self, L1: ListNode, L2: ListNode) -> ListNode:
        if not L1:
            return L2
        if not L2:
            return L1

        if L1.val < L2.val:
            node = L1
            L1 = L1.next
        else:
            node = L2
            L2 = L2.next
        head = node

        while 1:
            if L1 is None:
                node.next = L2
                break
            elif L2 is None:
                node.next = L1
                break
            elif L1.val < L2.val:
                node.next = L1
                L1 = L1.next
            else:
                node.next = L2
                L2 = L2.next
            node = node.next

        return head


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def convert_list_2_linked_list(self, vals: list) -> ListNode:
        node = None
        for val in reversed(vals):
            node = ListNode(val, node)
        return node

    def convert_linked_list_2_list(self, node: ListNode) -> list:
        vals = []
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals

    def test_merge_two_lists(self):
        list_1 = [1, 2, 4]
        list_2 = [1, 3, 4]
        L1 = self.convert_list_2_linked_list(list_1)
        L2 = self.convert_list_2_linked_list(list_2)

        merged_linked_list = self.sol.merge_two_lists(L1, L2)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, [1, 1, 2, 3, 4, 4])

    def test_merge_two_lists_one_empty(self):
        list_1 = []
        list_2 = [1, 3, 4]
        L1 = self.convert_list_2_linked_list(list_1)
        L2 = self.convert_list_2_linked_list(list_2)

        merged_linked_list = self.sol.merge_two_lists(L1, L2)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, [1, 3, 4])

    def test_merge_two_lists_two_empty(self):
        list_1 = []
        list_2 = []
        L1 = self.convert_list_2_linked_list(list_1)
        L2 = self.convert_list_2_linked_list(list_2)

        merged_linked_list = self.sol.merge_two_lists(L1, L2)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, [])

    def test_merge_two_lists_different_size(self):
        list_1 = [2]
        list_2 = [1, 3, 4]
        L1 = self.convert_list_2_linked_list(list_1)
        L2 = self.convert_list_2_linked_list(list_2)

        merged_linked_list = self.sol.merge_two_lists(L1, L2)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, [1, 2, 3, 4])


tests = TestMergeTwoLists()
tests.setUp()
tests.test_merge_two_lists()
